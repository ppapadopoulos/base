# --------------------------------------------------- -*- Makefile -*- --
# $Id: Makefile,v 1.9 2012/11/27 00:48:37 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
# 
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.9  2012/11/27 00:48:37  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.8  2012/05/06 05:48:44  phil
# Copyright Storm for Mamba
#
# Revision 1.7  2011/07/23 02:30:46  phil
# Viper Copyright
#
# Revision 1.6  2010/09/07 23:53:07  bruno
# star power for gb
#
# Revision 1.5  2009/05/15 00:34:24  anoop
# Added some solaris support to ganglia-pylib
#
# Revision 1.4  2009/05/01 19:07:07  mjk
# chimi con queso
#
# Revision 1.3  2008/10/18 00:56:00  mjk
# copyright 5.1
#
# Revision 1.2  2008/03/06 23:41:43  mjk
# copyright storm on
#
# Revision 1.1  2008/01/04 23:04:43  bruno
# moved ganglia-pylib and receptor from hpc to base roll
#
# Revision 1.7  2007/06/23 04:03:39  mjk
# mars hill copyright
#
# Revision 1.6  2006/09/11 22:48:51  mjk
# monkey face copyright
#
# Revision 1.5  2006/08/10 00:10:56  mjk
# 4.2 copyright
#
# Revision 1.4  2005/10/12 18:09:45  mjk
# final copyright for 4.1
#
# Revision 1.3  2005/09/16 01:03:23  mjk
# updated copyright
#
# Revision 1.2  2005/05/24 21:22:48  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/12 00:30:44  fds
# Split ganglia-python into ganglia-pylib and ganglia-python. This pylib
# is not really ganglia specific, includes our Python modules coded in C.
#
# Revision 1.4  2004/03/25 03:15:03  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.3  2003/10/21 23:17:21  fds
# Compiles on Opteron
#
# Revision 1.2  2003/09/16 00:35:05  fds
# Made python version handling cleaner.
#
# Revision 1.1  2003/09/14 16:46:35  fds
# First Design. See License in Networkmodule.c
#
# Revision 1.3  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.2  2003/07/14 23:41:31  fds
# Python versioning is hard.
#
# Revision 1.1  2003/03/10 18:14:30  fds
# Makefile for python extension modules
#

RELEASE = 1
MODULES = $(wildcard *module.c)
HEADERS = $(wildcard *.h)

# Some extra source files for this module.
SRCS = intf.c addr.c addr-util.c strlcpy.c
OBJS = $(SRCS:.c=.o)

# Our parent makefile provides PY_INCLUDE.
include $(OS).mk

modules: $(MODULES:.c=.so)
	cp *.so ../

%.o: %.c
	$(CC) $(CCOPTS) -o $@ -c $<

%.so: %.c $(HEADERS) $(OBJS)
	$(CC) $(CCOPTS) -g -I$(PY_INCLUDE) -c $<
	$(CC) -shared -o $@ $(<:.c=.o) $(OBJS) -L/opt/rocks/lib -ldnet

clean::
	rm -f *.o *.so
