/*
 * Gmetricmodule.c - Python extension module for publishing gmetrics.
 * Works with Ganglia versions 2.5.x.
 *
 * @Copyright@
 * 
 * 				Rocks(r)
 * 		         www.rocksclusters.org
 * 		            version 5.0 (V)
 * 
 * Copyright (c) 2000 - 2008 The Regents of the University of California.
 * All rights reserved.	
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 * 
 * 1. Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * 
 * 2. Redistributions in binary form must reproduce the above copyright
 * notice unmodified and in its entirety, this list of conditions and the
 * following disclaimer in the documentation and/or other materials provided 
 * with the distribution.
 * 
 * 3. All advertising and press materials, printed or electronic, mentioning
 * features or use of this software must display the following acknowledgement: 
 * 
 * 	"This product includes software developed by the Rocks(r)
 * 	Cluster Group at the San Diego Supercomputer Center at the
 * 	University of California, San Diego and its contributors."
 * 
 * 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
 * neither the name or logo of this software nor the names of its
 * authors may be used to endorse or promote products derived from this
 * software without specific prior written permission.  The name of the
 * software includes the following terms, and any derivatives thereof:
 * "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
 * the associated name, interested parties should contact Technology 
 * Transfer & Intellectual Property Services, University of California, 
 * San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
 * Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
 * 
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
 * BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
 * IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * 
 * @Copyright@
 *
 * These functions are based on code by Matt Massie for the Ganglia
 * project, and David Helder, Andrew Lanoix for the GNet networking
 * library.
 *
 * ChangeLog:
 *      7mar2003 Federico Sacerdoti <fds@sdsc.edu>
 *          Original Version.
 *
 * Compile like this:
 * gcc -fPIC -I/usr/include/python2.2 -c Gmetricmodule.c
 * gcc -shared -Wl -o Gmetricmodule.so Gmetricmodule.o
 */
 
#include <Python.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <rpc/xdr.h>
#include <string.h>
#include <limits.h>
#include "metrics.h"

static PyObject *ErrorObject;

/* For funtions returning a pointer. */
#define myerror(message) \
    { PyErr_SetString(ErrorObject, message); return NULL; }

/* For funtions returning an integer. */
#define Myerror(message) \
    { PyErr_SetString(ErrorObject, message); return -1; }


static int
out_socket (const char* channel, unsigned short port, int mcast_ttl)
{
	int rval, sockfd;
	struct sockaddr_in channel_addr;
	const int on = 1;
	unsigned char ttl;
	char s[128];
	char *syserr;

	channel_addr.sin_family = AF_INET;
	channel_addr.sin_port = htons(port);

	rval = inet_pton(AF_INET, channel, &channel_addr.sin_addr);
	if (rval<0) return -1;

	/* Create the UDP socket */
	sockfd = socket(PF_INET, SOCK_DGRAM, 0);
	if (sockfd<0) Myerror("Cannot create socket");

	/* Allow channel to be reused. */
	rval = setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR,
		(void*) &on, sizeof(on));
	if (rval<0) Myerror("Cannot share our new socket");

	if (IN_MULTICAST(ntohl(channel_addr.sin_addr.s_addr)))
	{
		/* Let the kernel decide the interface to send on.
		* We do not set the IP_MULTICAST_IF socket option. */

		/* Set the mcast time-to-live. */
		ttl = (unsigned char) mcast_ttl;
		rval = setsockopt(sockfd, IPPROTO_IP, IP_MULTICAST_TTL,
			(void*) &ttl, sizeof(ttl));
		if (rval<0) Myerror("Cannot set mcast ttl");
	}
	else if (ntohl(channel_addr.sin_addr.s_addr)==INADDR_BROADCAST)
	{
		/* Only recognize the limited broadcast address since we dont
		 * know the subnet mask. */
		rval = setsockopt(sockfd, SOL_SOCKET, SO_BROADCAST,
			(void*) &on, sizeof(on));
		if (rval<0) Myerror("Cannot setup socket for broadcast");
	}

	/* Connect the socket. */
	rval = connect(sockfd, (struct sockaddr*) &channel_addr, sizeof(channel_addr));
	if (rval<0)
	{
		sprintf(s, "Could not connect to multicast channel: %s:%d",
			channel, port);
		Myerror(s)
	}

	return sockfd;
 }

 
int
writen (int fd, const void *buf, int n)
{
   size_t bytesleft;
   ssize_t byteswritten;
   const char *ptr;

   ptr = buf;
   bytesleft = n;
   while (bytesleft > 0)
     {
        byteswritten = write (fd, ptr, bytesleft);
        if (byteswritten <= 0)
          {
             if (errno == EINTR)
                byteswritten = 0;   /* and call write() again */
             else
                return -1;
          }
        bytesleft -= byteswritten;
        ptr += byteswritten;
     }
   return 1;
}


/*
 * Publish a complete user-level ganglia metric. Supports
 * any python object (with a __repr__ method) as a value.
 */
static PyObject *
publish_gmetric (PyObject *self, PyObject *args)
{
	int rval, len;
	int valsize, namesize, typesize, unitsize;
	const char *name;
	PyObject *val;
	PyObject *p;
	const char *Value;
	uint32_t tmax = 3600;
	uint32_t dmax = 0;
	int Slope = 0;
	char *units = "";
	char *slope = "";
	char *type = "";
	int mcast_ttl = 1;
	short int port = 0;
	char *channel = "";
	char s[128];
	char gmetric_msg[BUFSIZ];
	int udp_socket;
	uint32_t key = 0; /* user-defined */
	XDR xhandle;

	rval = PyArg_ParseTuple(args, "s#O|ssiihss:publish",
				&name, &namesize,
				&val,
				&units,
				&slope,
				&tmax,
				&dmax,
				&port,
				&channel,
				&type);
	if (!rval) return NULL;

	if (!strcspn(name, " \t"))
		myerror("Name cannot be blank or empty");
	if (namesize > FRAMESIZE)
		{
			sprintf(s, "Name is too long (%d)", namesize);
			myerror(s);
		}

	/* We generally want to automatically detect type. */
	if (!strlen(type))
		{
			if (PyInt_Check(val))
					type = "int32";
			else if (PyFloat_Check(val))
					type = "float";
			else  /* Assume string for all other objects. */
				{
					type = "string";
					slope = "zero";
				}
		}

	/* Get python string representation of value. */
	p = PyObject_Str(val);
	valsize = PyString_Size(p);
	Value = PyString_AsString(p);

	if (valsize + namesize > MAX_MCAST_MSG)
		{
			sprintf(s, "Metric name + value strings too long (%d + %d > %d)",
				namesize, valsize, MAX_MCAST_MSG);
			myerror(s);
		}

	unitsize = strlen(units);
	typesize = strlen(type);

	if (unitsize > MAX_FIELD_LEN)
		myerror("Unit string too long");
	if (typesize > MAX_FIELD_LEN)
		myerror("Type string too long");

	if (!strcmp(slope,"zero"))
			Slope = 0;
	else if (!strcmp(slope,"positive"))
			Slope = 1;
	else if (!strcmp(slope,"negative"))
			Slope = 2;
	else 
			/* Default slope is both. */
			Slope = 3;

	if (tmax <= 0)
		myerror("Tmax must be greater than zero.");
	if (dmax < 0)
		myerror("Dmax must be greater than zero");
		
	/* Choose Ganglia multicast channels by default. */
	if (!strlen(channel))
		channel = "239.2.11.71";
	if (!port)
		port = 8649;

	udp_socket = out_socket (channel, port, mcast_ttl);
	if (!udp_socket) return NULL;

	/*
		* Alright. We have checked our inputs. Now encode the XDR message.
		*/
	xdrmem_create(&xhandle, gmetric_msg, MAX_MCAST_MSG, XDR_ENCODE);

	rval = xdr_u_int(&xhandle, &key);
	if (!rval) myerror("could not encode key");

	/* Include the trailing \0 character in field string. */
	len = typesize+1;
	rval = xdr_bytes(&xhandle, (char **)&type, &len, MAX_FIELD_LEN);
	if (!rval) myerror("could not encode type");

	len = namesize+1;
	rval = xdr_bytes(&xhandle, (char **)&name, &len, FRAMESIZE);
	if (!rval) myerror("could not encode name");

	len = valsize+1;
	rval = xdr_bytes(&xhandle, (char **)&Value, &len, FRAMESIZE);
	if (!rval) myerror("could not encode value");

	len = unitsize+1;
	rval = xdr_bytes(&xhandle, (char **)&units, &len, MAX_FIELD_LEN);
	if (!rval) myerror("could not encode type");

	rval = xdr_u_int(&xhandle, &Slope);
	if (!rval) myerror("could not encode slope");

	rval = xdr_u_int(&xhandle, (uint32_t*) &tmax);
	if (!rval) myerror("could not encode tmax");

	rval = xdr_u_int(&xhandle, (uint32_t*) &dmax);
	if (!rval) myerror("could not encode dmax");

	len = xdr_getpos(&xhandle);

	rval = writen( udp_socket, gmetric_msg, len );
	if (rval<0)
		myerror("Unable to write msg to multicast channel");

	close(udp_socket);

	xdr_destroy(&xhandle);

	Py_DECREF(p);

	return Py_BuildValue("isOsssii", len, name, val, type, units, slope, tmax, dmax);
}


static char*
findslope(const int code)
{
	switch (code)
	{
		case -1:
		case 0:
			return "zero";
			break;
		case 1:
			return "positive";
			break;
		case 2:
			return "negative";
			break;
		default:
			return "both";
	}
}


/* 
 * The next two functions are from my (Sacerdoti) code in Ganglia
 * Gmetad version 2.5.4. 
 * The string fields in Metric_t are actually offsets into the value buffer field.
 * This function returns a regular char* pointer. Tricky, but efficient.
 */
char *
getfield(char* buf, short int index)
{
   if (index<0) return "unspecified";

   return (char*) buf+index;
}


static int
addstring(char *strings, int *edge, char *s)
{
	int e = *edge;
	int end = e + strlen(s) + 1;

	/* I wish C had real exceptions. */
	if (e > FRAMESIZE || end > FRAMESIZE)
	{
		fprintf(stderr, "Field is too big!!");
		return -1;
	}

	strcpy(strings + e, s);
	*edge = end;

	return e;
}


/*
 * Parses a ganglia XDR message. Assumes a Ganglia version 2.5.x
 * message format. Message truncated to 1500 bytes.
 */
static PyObject *
parse_gmetric (PyObject *self, PyObject *args)
{
	int rval, datalen;
	uint32_t key;
	char *msg;
	int msglen;
	g_val_t mcast_val;
	uint32_t slope;
	char *source;
	char *type;
	Metric_t metric;
	int edge = 0;
	char s[FRAMESIZE];
	char *p = s;
	XDR xhandle;


	rval = PyArg_ParseTuple(args, "s#:parse",
				&msg, &msglen);
	if (!rval) return NULL;

	/*printf("Got a %d-byte XDR message\n", msglen);*/

	xdrmem_create(&xhandle, msg, MAX_MCAST_MSG - 1, XDR_DECODE);

   rval = xdr_u_int(&xhandle, &key);
   if (!rval) myerror("could not decode key");

	if (key)
	{
		source = "gmond";

		/*printf("Got a built-in metric %d\n", key);*/
		metric.name = addstring(metric.strings, &edge, metrics[key].name);

		/* Parse value field */
		switch( metrics[key].type )
		{
			case g_string:
				rval = xdr_string(&xhandle, &p,  MAX_G_STRING_SIZE);
				type = "string";
				break;
			case g_int8:
				rval = xdr_char(&xhandle, &mcast_val.int8);
				type = "int8";
				snprintf(s, FRAMESIZE, metrics[key].fmt, mcast_val.int8);
				break;
			case g_uint8:
				rval = xdr_u_char(&xhandle, &mcast_val.uint8);
				type = "uint8";
				snprintf(s, FRAMESIZE, metrics[key].fmt, mcast_val.uint8);
				break;
			case g_int16:
				rval = xdr_short(&xhandle, &mcast_val.int16);
				if (!rval) myerror("could not decode string value");
				type = "int16";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.int16);
				break;
			case g_uint16:
				rval = xdr_u_short(&xhandle, &mcast_val.uint16);
				type = "uint16";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.uint16);
				break;
			case g_int32:
				rval = xdr_int(&xhandle, &mcast_val.int32);
				if (!rval) myerror("could not decode string value");
				type = "int32";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.int32);
				break;
			case g_uint32:
				rval = xdr_u_int(&xhandle, &mcast_val.uint32);
				type = "uint32";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.uint32);
				break;
			/* A timestamp type is always a uint32 (32-bit unsigned int) */
			case g_timestamp:
				rval = xdr_u_int(&xhandle, &mcast_val.uint32);
				type = "timestamp";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.uint32);
				break;
			case g_float:
				rval = xdr_float(&xhandle, &mcast_val.f);
				type = "float";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.f);
				break;
			case g_double:
				rval = xdr_double(&xhandle, &mcast_val.d);
				type = "double";
				snprintf(s,  FRAMESIZE, metrics[key].fmt, mcast_val.d);
				break;
			default:
				sprintf(s, "got a metric with a strange type (%d)", metrics[key].type);
				myerror(s);
		}
		if (!rval) myerror("could not decode builtin metric value");
		metric.value = addstring(metric.strings, &edge, s);

		/* Not strictly necessary to do a strcopy here. Done to make
			building the Python Dictionary easier and more symmetrical
			to user metrics. */
		metric.type = addstring(metric.strings, &edge, type);

		metric.units = addstring(metric.strings, &edge, metrics[key].units);

		metric.slope = addstring(metric.strings, &edge,
				metrics[key].check_min < 0 ? "zero" : "both");

		metric.tmax = metrics[key].mcast_max;
		metric.dmax = 0;
	}
	else
	{
		/* Not a builtin metric - a user-defined gmetric. */
		source = "gmetric";

		/* Type */
		rval = xdr_bytes(&xhandle, &p, &datalen, FRAMESIZE);
		if (!rval) myerror("could not decode user metric type");
		metric.type = addstring(metric.strings, &edge, s);

		/* Name */
		rval = xdr_bytes(&xhandle, &p, &datalen, FRAMESIZE);
		if (!rval) myerror("could not decode user metric name");
		metric.name = addstring(metric.strings, &edge, s);

		/* Value */
		rval = xdr_bytes(&xhandle, &p, &datalen, FRAMESIZE);
		if (!rval) myerror("could not decode user metric value");
		metric.value = addstring(metric.strings, &edge, s);

		/* Units */
		rval = xdr_bytes(&xhandle, &p, &datalen, FRAMESIZE);
		if (!rval) myerror("could not decode user metric units");
		metric.units = addstring(metric.strings, &edge, s);

		/* Slope */
		rval = xdr_u_int(&xhandle, &slope);
		if (!rval) myerror("could not decode user metric slope");
		metric.slope = addstring(metric.strings, &edge, findslope(slope));

		/* TMAX */
		rval = xdr_u_int(&xhandle, &metric.tmax);
		if (!rval) myerror("could not decode user metric tmax");
		if (metric.tmax > INT_MAX)
			metric.tmax = INT_MAX;

		/* DMAX */
		rval = xdr_u_int(&xhandle, &metric.dmax);
		if (!rval) myerror("could not decode user metric dmax");
		if (metric.dmax > INT_MAX)
			metric.dmax = INT_MAX;
	}

	return Py_BuildValue("{s:s, s:s, s:s, s:s, s:s, s:i, s:i, s:s, s:s}",
		"NAME", getfield(metric.strings, metric.name),
		"VAL", getfield(metric.strings, metric.value),
		"TYPE", getfield(metric.strings, metric.type),
		"UNITS", getfield(metric.strings, metric.units),
		"TN", "0",
		"TMAX", metric.tmax,
		"DMAX", metric.dmax,
		"SLOPE", getfield(metric.strings, metric.slope),
		"SOURCE", source
		);
}


static PyObject *
hi (PyObject *self, PyObject *args)
{
    return Py_BuildValue("s", "hi mom");
}

/* Python Method Registration Table. */
static struct PyMethodDef Gmetric_methods[] = {
   { "publish",  publish_gmetric,  METH_VARARGS },
   { "parse",  parse_gmetric,  METH_VARARGS },
   { "hi", hi, METH_VARARGS },
   { NULL, NULL }
};

void
initGmetric()
{
   PyObject *m, *d;
   
   m = Py_InitModule("Gmetric", Gmetric_methods);
   
   /* Add "error" as a symbolic constant to this module. */
   d = PyModule_GetDict(m);
   ErrorObject = PyErr_NewException("Gmetric.error", NULL, NULL);
   PyDict_SetItemString(d, "error", ErrorObject);
}




