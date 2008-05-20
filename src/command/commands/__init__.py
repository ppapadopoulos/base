# $Id: __init__.py,v 1.55 2008/03/06 23:41:33 mjk Exp $
# 
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		            version 5.0 (V)
# 
# Copyright (c) 2000 - 2008 The Regents of the University of California.
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
# $Log: __init__.py,v $
# Revision 1.55  2008/03/06 23:41:33  mjk
# copyright storm on
#
# Revision 1.54  2008/03/06 23:12:55  mjk
# Added column level filtering of output for list commands.
#
# New params
#   output-header=BOOL
#   output-col=NAME,NAME,...
#
# Now can turn off the header line with output-header=no and can select
# which columns get printed with output-col.  For example:
#
# rocks list roll output-col=arch output-header=no
#
# Will just print the arch (not even roll name) for all the rolls on the
# cluster.
#
# TODO: Where to document, not going to touch every list command!
#
# Revision 1.53  2007/11/09 22:08:42  anoop
# Remove annoyance with duplicating multiple roll names
#
# Revision 1.52  2007/07/05 19:09:50  mjk
# - ArgumentProcessors work on empty tables
#
# Revision 1.51  2007/07/05 18:11:36  mjk
# - self.abort() prints command usage (w/o command name)
# - HostArgumentProcessor accepts % again
#
# Revision 1.50  2007/07/04 01:47:37  mjk
# embrace the anger
#
# Revision 1.48  2007/06/29 06:24:49  phil
# escape any XML characters in descriptions when creating docbook format.
#
# Revision 1.47  2007/06/27 21:30:34  bruno
# cleanup distribution commands
#
# Revision 1.46  2007/06/26 20:21:15  bruno
# touch ups
#
# added 'fillParameters' -- now, every command will have fillParameters,
# fillPositionalArgs or neither.
#
# Revision 1.45  2007/06/25 19:25:35  bruno
# need a list, not a list of tuples
#
# Revision 1.44  2007/06/25 18:36:00  bruno
# get the variables in the correct order (reverse the 'vars')
#
# Revision 1.43  2007/06/23 03:54:51  mjk
# - first pass at consistency
# - still needs some docstrings
# - argument processors take SQL wildcards
# - add cannot run twice (must use set)
# - dump does sets not just adds
#
# Revision 1.41  2007/06/19 16:42:40  mjk
# - fix add host interface docstring xml
# - update copyright
#
# Revision 1.40  2007/06/17 00:08:47  phil
# Fix naming of networks.
#
# Revision 1.39  2007/06/16 23:49:20  phil
# Add some helper functions for parameter,argument processing when wanting to
# support named arguments.   Cleaned up set host interface mac
#
# Revision 1.38  2007/06/16 02:39:50  mjk
# - added list roll commands (used for docbook)
# - docstrings should now be XML
# - added parser for docstring to ASCII or DocBook
# - ditched Phil's Network regex stuff (will come back later)
# - updated several docstrings
#
# Revision 1.36  2007/06/12 18:01:17  bruno
# kats spels gud
#
# Revision 1.35  2007/06/12 01:33:40  mjk
# - added NetworkArgumentProcessor
# - updated rocks list network
#
# Revision 1.34  2007/06/11 19:26:56  mjk
# - apache counts as root
# - alphabetized some help flags
# - rocks dump error on arguments
#
# Revision 1.33  2007/06/08 03:26:24  mjk
# - plugins call self.owner.addText()
# - non-existant bug was real, fix plugin graph stuff
# - add set host cpus|membership|rack|rank
# - add list host (not /etc/hosts, rather the nodes table)
# - fix --- padding for only None fields not 0 fields
# - list host interfaces is cool works for incomplete hosts
#
# Revision 1.32  2007/06/07 21:23:03  mjk
# - command derive from verb.command class
# - default is MustBeRoot
# - list.command / dump.command set MustBeRoot = 0
# - removed plugin non-bugfix
#
# Revision 1.31  2007/06/07 18:20:02  bruno
# make sure the first plugin get put in the 'dict' dictionary. otherwise, it
# will never be run.
#
# Revision 1.30  2007/06/07 17:21:50  mjk
# - added RollArgumentProcessor
# - added trimOwner option to the endOutput method
# - roll based commands are uniform
#
# Revision 1.29  2007/06/07 16:43:02  mjk
# - moved host(s) argument processing into a top level class
# - list/dump/set host commands now use this
#
# Revision 1.28  2007/06/07 16:19:10  mjk
# - add "rocks add host"
# - add "rocks dump host"
# - add "rocks dump host interface"
# - remove "rocks add host new"
# - add mysql db init script to foundation-mysql
# - more flexible hostname lookup for the command line
#
# Revision 1.27  2007/06/01 23:43:10  mjk
# fix extra space at end of line for endOutput
#
# Revision 1.26  2007/05/25 03:12:30  mjk
# - help takes a flag instead of an argument
# - added bash/readline completion
#
# Revision 1.25  2007/05/10 20:37:00  mjk
# - massive rocks-command changes
# -- list host is standardized
# -- usage simpler
# -- help is the docstring
# -- host groups and select statements
# - added viz commands
#
# Revision 1.23  2007/04/19 23:01:09  bruno
# pretty print rocks command line output with addOutput() and endOutput()
#
# Revision 1.22  2007/03/29 00:16:30  mjk
# - added self.os to base command
# - list.host.profile ready for solaris code
#
# Revision 1.21  2007/03/28 22:33:49  mjk
# - add getHostname() method to base command class
# - fix bad try block for default args in list.node.xml
# - list.node.xml works as standalone
#
# Revision 1.20  2007/03/02 01:14:37  mjk
# fix node specific app_globals
#
# Revision 1.19  2007/02/28 03:06:28  mjk
# - "rocks list host xml" replaces kpp
# - kickstart.cgi uses "rocks list host xml"
# - indirects in node xml now works
#
# Revision 1.18  2007/02/27 21:23:53  mjk
# checkpoint
#
# Revision 1.17  2007/02/27 01:53:57  mjk
# - run(self, args) => run(self, flags, args)
# - replaced rocks list host xml with more complete code
# - replaced rocks lust node xml with kpp shell (not a command now)
#
# Revision 1.16  2007/02/20 18:51:41  mjk
# Added getGlobalVars() method
#
# Revision 1.15  2007/02/13 19:17:39  mjk
# recursive xml for app_global vars
#
# Revision 1.14  2007/02/12 22:55:33  mjk
# start of indirects
#
# Revision 1.13  2007/02/08 17:48:48  mjk
# - single syslog open/close
# - log plug-ins
#
# Revision 1.12  2007/02/08 17:31:25  mjk
# Added root check for root-only commands
# Added syslog tracking to record changes to the cluster
#
# Revision 1.11  2007/02/05 23:29:19  mjk
# added 'rocks add roll'
# added plugin_* facility
# added 'rocks sync user' (plugin-able)
#
# Revision 1.10  2007/02/05 18:55:09  mjk
# fix to 80-col
#
# Revision 1.9  2007/01/17 02:11:39  anoop
# createEntitiesFromDB now replaced by getEntities()
# Minor correction for code that uses the database
#
# Revision 1.8  2007/01/10 17:32:05  mjk
# added list node interfaces|memberships
# minor tweaks
#
# Revision 1.7  2006/12/07 00:29:48  mjk
# might work this time
#
# Revision 1.6  2006/12/07 00:28:14  mjk
# might work this time
#
# Revision 1.5  2006/12/07 00:20:57  mjk
# might work
#
# Revision 1.4  2006/12/06 23:45:11  mjk
# added xxxText methods
#
# Revision 1.3  2006/12/01 22:25:43  bruno
# one world, one cursor
#
# Revision 1.2  2006/11/22 02:15:46  mjk
# working version
#
# Revision 1.1  2006/11/02 21:49:46  mjk
# prototype
#

import os
import socket
import string
import re
import syslog
import pwd
import types
import sys
import rocks
import rocks.graph
import xml
from xml.sax import saxutils
from xml.sax import handler
from xml.sax import make_parser
from xml.sax._exceptions import SAXParseException


def Abort(message, doExit=1):
	"""Print a standard error message and abort the program"""
	syslog.syslog(syslog.LOG_ERR, message)
	print 'error - %s' % message
	if doExit:
		sys.exit(-1)


class MembershipArgumentProcessor:
	"""An Interface class to add the ability to process membership
	arguments."""
	
	def getMembershipNames(self, args=None):
		"""Returns a list of membership names from the database.
		For each arg in the ARGS list find all the membership
		names that match the arg (assume SQL regexp).  If an
		arg does not match anything in the database we Abort.  If the
		ARGS list is empty return all membership names.
		"""
		list = []
		if not args:
			args = [ '%' ] # find all memberships
		for arg in args:
			rows = self.db.execute("""select name from memberships 
				where name like '%s'""" % arg)
			if rows == 0 and arg == '%': # empty table is OK
				continue
			if rows < 1:
				Abort('unknown membership "%s"' % arg)
			for name, in self.db.fetchall():
				list.append(name)
		return list

		
	
class ApplianceArgumentProcessor:
	"""An Interface class to add the ability to process appliance
	arguments."""
		
	def getApplianceNames(self, args=None):
		"""Returns a list of appliance names from the database.
		For each arg in the ARGS list find all the appliance
		names that match the arg (assume SQL regexp).  If an
		arg does not match anything in the database we Abort.  If the
		ARGS list is empty return all appliance names.
		"""	
		list = []
		if not args:
			args = [ '%' ] # find all appliances
		for arg in args:
			rows = self.db.execute("""select name from appliances 
				where name like '%s'""" % arg)
			if rows == 0 and arg == '%': # empty table is OK
				continue
			if rows < 1:
				Abort('unknown appliance "%s"' % arg)
			for name, in self.db.fetchall():
				list.append(name)
		return list


class DistributionArgumentProcessor:
	"""An Interface class to add the ability to process distribution
	arguments."""
		
	def getDistributionNames(self, args=None):
		"""Returns a list of distribution names from the database.
		For each arg in the ARGS list find all the distribution
		names that match the arg (assume SQL regexp).  If an
		arg does not match anything in the database we Abort.  If the
		ARGS list is empty return all distribution names.
		"""	
		list = []
		if not args:
			args = [ '%' ] # find all distributions

		for arg in args:
			rows = self.db.execute("""select name from
				distributions where name like '%s'""" % arg)
			if rows == 0 and arg == '%': # empty table is OK
				continue
			if rows < 1:
				if arg == '%':
					# special processing for when the table
					# is empty
					continue
				else:
					Abort('unknown distribution "%s"' % arg)

			for name, in self.db.fetchall():
				list.append(name)

		return list
		

class NetworkArgumentProcessor:
	"""An Interface class to add the ability to process network (subnet)
	argument."""
	
	def getNetworkNames(self, args=None):
		"""Returns a list of network (subnet) names from the database.
		For each arg in the ARGS list find all the network
		names that match the arg (assume SQL regexp).  If an
		arg does not match anything in the database we Abort.  If the
		ARGS list is empty return all network names.
		"""
		list = []
		if not args:
			args = [ '%' ] # find all networks
		for arg in args:
			rows = self.db.execute("""select name from subnets
				where name like '%s'""" % arg)
			if rows == 0 and arg == '%': # empty table is OK
				continue
			if rows < 1:
				Abort('unknown network "%s"' % arg)
			for name, in self.db.fetchall():
				list.append(name)
		return list
	
	
class RollArgumentProcessor:
	"""An Interface class to add the ability to process roll arguments."""
	
	def getRollNames(self, args, params):
		"""Returns a list of (name, version) tuples from the roll
		table in the database.  If the PARAMS['version'] is provided
		only Rolls of that version are included otherwise no filtering
		on version number is performed.  If the ARGS list is empty then
		all Roll names are returned.  SQL regexps acan be used in 
		both the version parameter and arg list, but must expand to 
		something.
		"""

		if params.has_key('version'):
			version = params['version']
		else:
			version = '%' # SQL wildcard
	
		list = []
		if not args:
			args = [ '%' ] # find all roll names
		for arg in args:
			rows = self.db.execute("""select distinct name,version from rolls
				where name like '%s' and 
				version like '%s'""" % (arg, version))
			if rows == 0 and arg == '%': # empty table is OK
				continue
			if rows < 1:
				Abort('unknown roll name "%s"' % arg)
			for (name, ver) in self.db.fetchall():
				list.append((name, ver))
				
		return list
		

class HostArgumentProcessor:
	"""An Interface class to add the ability to process host arguments."""
	
	def getHostnames(self, names=None):
		"""Expands the given list of names to valid cluster 
		hostnames.  A name can be a hostname, IP address, our
		group (membership name).  Any combination of these is valid.
		If the names list is empty a list of all hosts in the cluster
		is returned.
		
		The following groups are recognized:
		
		rackN - All non-frontend host in rack N
		appliancename - All appliances of a given type (e.g. compute)
		select ... - an SQL statement that returns a list of hosts
		"""
		
		# Handle the simple case first and just return a complete
		# list of hosts in the cluster if no list of names was
		# provided
		
		list = []
		if not names:
			self.db.execute('select name from nodes')
			for host, in self.db.fetchall():
				list.append(host)
			return list

	
		# The names list was not empty so we now need to build
		# a list of acceptable group names based on the rack numbers
		# and appliance names (not membership names).  This 
		# convention follows the original idea (but not code) for
		# "dbreport tentakel".
		
		groups = {}
		self.db.execute('select min(rack), max(rack) from nodes')
		min,max = self.db.fetchone()
		for i in range(min, max+1): # racks
			self.db.execute("""select n.name from 
				nodes n, memberships m, appliances a where
				n.membership=m.id and m.appliance=a.id and
				a.name!="frontend" and n.rack=%d""" % i)
			l = []
			for node, in self.db.fetchall():
				l.append(node)
			groups['rack%d' % i] = l
		self.db.execute('select name from appliances')
		for name, in self.db.fetchall(): # appliances
			self.db.execute("""select n.name from 
				nodes n, memberships m, appliances a where
				n.membership=m.id and m.appliance=a.id and
				a.name="%s" """ % name)
			l = []
			for node, in self.db.fetchall():
				l.append(node)
			groups[name] = l
		
		# Iterate through the list and expand all names to a list of
		# host names.  Also handle any names that start with 'select'
		# and expand them as an SQL queury.  Populate a dictionary 
		# to make sure we only have one entry for each host.  
		# Then return a sorted list of keys.
		#
		# We may want to add other expansion rules like the old 
		# FDS style %d stuff here.
		
		dict = {}
		for name in names:
			if name.find('select') == 0:	# SQL select
				self.db.execute(name)
				for host, in self.db.fetchall():
					dict[host] = 1
			elif name.find('%') >= 0:	# SQL % pattern
				self.db.execute("""select name from nodes where
					name like '%s'""" % name)
				for h in self.db.fetchall():
					dict[h] = 1
			elif groups.has_key(name):	# group name
				for host in groups[name]:
					dict[host] = 1
			else:				# host name
				dict[self.db.getHostname(name)] = 1
		list = dict.keys()
		list.sort()
		return list

class AppGlobalsHandler(handler.ContentHandler,
	handler.DTDHandler,
	handler.EntityResolver,
	handler.ErrorHandler):
	
	def __init__(self, db, host, site):
		handler.ContentHandler.__init__(self)
		self.db		= db
		self.host	= host
		self.site	= site
		self.parser = make_parser()
		self.parser.setContentHandler(self)

	def lookup(self, service, component):
		nodespec = 'select app_globals.value from ' \
			'nodes,app_globals where ' \
			'app_globals.service="%s" and ' \
			'app_globals.component="%s" and ' \
			'app_globals.site=%d and ' \
			'nodes.name="%s" and ' \
			'nodes.membership=app_globals.membership' \
			% (service, component, self.site, self.host)
			
		default = 'select value from app_globals where ' \
			'service="%s" and component="%s" and ' \
			'membership=0 and site=%d' \
			% (service, component, self.site)
				
		rows = self.db.execute(nodespec)
		if not rows:
			rows = self.db.execute(default)
		if rows:
			val = self.db.fetchone()[0]
			if self.hasXML(val):
				return self.parse(self.val2XML(val))
			else:
				return val
		return None
		

	def hasXML(self, s):
		"""Returns TRUE if the provided string has any XML tags."""
		
		if re.search('<[a-zA-Z_=" ]*/>', s):
			return 1
		else:
			return 0
		
	def val2XML(self, text):
		"""Converts an app_globals value field to well formed XML."""
		
		xml 	 = ''
		curr	 = 0	
		for i,m in enumerate(re.finditer('<[a-zA-Z_=" ]*/>', text)):
			xml += saxutils.escape(text[curr:m.start()])
			xml += text[m.start():m.end()]
			curr = m.end()
		xml += saxutils.escape(text[curr:len(text)])
		return '<xml>%s</xml>' % xml
			
	def parse(self, xml):
		self.text      = ''
		self.foundTags = 0
		self.parser.reset()
		self.parser.feed(xml)
		return self.text
	
	def startElement(self, name, attrs):
		self.foundTags += 1
		if name == 'indirect':
			self.nextService   = attrs.get('service')
			self.nextComponent = attrs.get('component')
			self.text += self.lookup(self.nextService,
				self.nextComponent)
			
	def endElement(self, name):
		if name == 'indirect':
			pass
			
		
	def characters(self, s):
		self.text += s
		
		
class DocStringHandler(handler.ContentHandler,
	handler.DTDHandler,
	handler.EntityResolver,
	handler.ErrorHandler):
	
	def __init__(self, name='', users=[]):
		handler.ContentHandler.__init__(self)
		self.text			= ''
		self.name			= name
		self.users			= users
		self.section			= {}
		self.section['description']	= ''
		self.section['arg']		= []
		self.section['param']		= []
		self.section['example']		= []
		self.section['related']		= []
		self.parser = make_parser()
		self.parser.setContentHandler(self)

	def getDocbookText(self):
		s  = ''
		s += '<section id="rocks-%s" xreflabel="%s">\n' % \
			(string.join(self.name.split(' '), '-'), self.name)
		s += '<title>%s</title>\n' % self.name
		s += '<cmdsynopsis>\n'
		s += '\t<command>rocks %s</command>\n' % self.name
		for ((name, type, opt, rep), txt) in self.section['arg']:
			if opt:
				choice = 'opt'
			else:
				choice = 'req'
			if rep:
				repeat = 'repeat'
			else:
				repeat = 'norepeat'
			s += '\t<arg rep="%s" choice="%s">%s</arg>\n' % \
				(repeat, choice, name)
		for ((name, type, opt, rep), txt) in self.section['param']:
			if opt:
				choice = 'opt'
			else:
				choice = 'req'
			if rep:
				repeat = 'repeat'
			else:
				repeat = 'norepeat'
			s += '\t<arg rep="%s" choice="%s">' % (repeat, choice)
			s += '%s=<replaceable>%s</replaceable>' % (name, type)
			s += '</arg>\n'
		s += '</cmdsynopsis>\n'
		s += '<para>\n'
		s += saxutils.escape(self.section['description'])
		s += '\n</para>\n'
		if self.section['arg']:
			s += '<variablelist><title>arguments</title>\n'
			for ((name, type, opt, rep), txt) in \
				self.section['arg']:
				s += '\t<varlistentry>\n'
				if opt:
					term = '<optional>%s</optional>' % name
				else:
					term = name
				s += '\t<term>%s</term>\n' % term
				s += '\t<listitem>\n'
				s += '\t<para>\n'
				s += saxutils.escape(txt)
				s += '\n\t</para>\n'
				s += '\t</listitem>\n'
				s += '\t</varlistentry>\n'
			s += '</variablelist>\n'
		if self.section['param']:
			s += '<variablelist><title>parameters</title>\n'
			for ((name, type, opt, rep), txt) in \
				self.section['param']:
				s += '\t<varlistentry>\n'
				if opt:
					optStart = '<optional>'
					optEnd   = '</optional>'
				else:
					optStart = ''
					optEnd   = ''
				key = '%s=' % name
				val = '<replaceable>%s</replaceable>' % type
				s += '\t<term>%s%s%s%s</term>\n' % \
					(optStart, key, val, optEnd)
				s += '\t<listitem>\n'
				s += '\t<para>\n'
				s += saxutils.escape(txt)
				s += '\n\t</para>\n'
				s += '\t</listitem>\n'
				s += '\t</varlistentry>\n'
			s += '</variablelist>\n'
		if self.section['example']:
			s += '<variablelist><title>examples</title>\n'
			for (cmd, txt) in self.section['example']:
				s += '\t<varlistentry>\n'
				s += '\t<term>\n'
				if 'root' in self.users:
					s += '# '
				else:
					s += '$ '
				s += 'rocks %s' % cmd
				s += '\n\t</term>\n'
				s += '\t<listitem>\n'
				s += '\t<para>\n'
				s += saxutils.escape(txt)
				s += '\n\t</para>\n'
				s += '\t</listitem>\n'
				s += '\t</varlistentry>\n'
			s += '</variablelist>\n'
		if self.section['related']:
			s += '<variablelist><title>related commands</title>\n'
			for related in self.section['related']:
				s += '\t<varlistentry>\n'
				s += '\t<term>'
				s += '<xref linkend="rocks-%s">' % \
					string.join(related.split(' '), '-')
				s += '</term>\n'
				s += '\t<listitem>\n'
				s += '\t<para>\n'
				s += '\n\t</para>\n'
				s += '\t</listitem>\n'
				s += '\t</varlistentry>\n'
			s += '</variablelist>\n'
		s += '</section>'
		return s

	
	def getUsageText(self):
		s = ''
		for ((name, type, opt, rep), txt) in self.section['arg']:
			if opt:
				s += '[%s]' % name
			else:
				s += '{%s}' % name
			if rep:
				s += '...'
			s += ' '
		for ((name, type, opt, rep), txt) in self.section['param']:
			if opt:
				s += '[%s=%s]' % (name, type)
			else:
				s += '{%s=%s}' % (name, type)
			if rep:
				s += '...'
			s += ' '
		if s and s[-1] == ' ':
			return s[:-1]
		else:
			return s
	
	def getPlainText(self):
		if 'root' in self.users:
			prompt = '#'
		else:
			prompt = '$'
		s  = ''
		s += 'rocks %s %s' % (self.name, self.getUsageText())
		s += '\n\nDescription:\n'
		s += self.section['description']
		if self.section['arg']:
			s += '\nArguments:\n\n'
			for ((name, type, opt, rep), txt) in \
				self.section['arg']:
				if opt:
					s += '\t[%s]' % name
				else:
					s += '\t{%s}' % name
				s += '\n%s\n' % txt
		if self.section['param']:
			s += '\nParameters:\n\n'
			for ((name, type, opt, rep), txt) in \
				self.section['param']:
				if opt:
					s += '\t[%s=%s]' % (name, type)
				else:
					s += '\t{%s=%s}' % (name, type)
				s += '\n%s\n' % txt
		if self.section['example']:
			s += '\nExamples:\n\n'
			for (cmd, txt) in self.section['example']:
				s += '\t%s rocks %s\n' % (prompt, cmd)
				s += '%s\n' % txt
		if self.section['related']:
			s += '\nRelated Commands:\n\n'
			for related in self.section['related']:
				s += '\trocks %s\n' % related
		return s
		
	def getParsedText(self):
		return '%s' % self.section
		
	def startElement(self, name, attrs):
		if not self.section['description']:
			self.section['description'] = self.text
		self.key  = None
		self.text = ''
		if name in [ 'arg', 'param' ]:
			try:
				type = attrs.get('type')
			except:
				type = 'string'
			try:
				optional = int(attrs.get('optional'))
			except:
				if name == 'arg':
					optional = 0
				if name == 'param':
					optional = 1
			try:
				repeat = int(attrs.get('repeat'))
			except:
				repeat = 0
			name = attrs.get('name')
			self.key = (name, type, optional, repeat)
		elif name == 'example':
			self.key = attrs.get('cmd')
		
	def endElement(self, name):
		if name == 'docstring':
			# we are done so sort the param and related lists
			self.section['param'].sort()
			self.section['related'].sort()
		elif name in [ 'arg', 'param', 'example' ]:
			self.section[name].append((self.key, self.text))
		else:
			if self.section.has_key(name):
				self.section[name].append(self.text)
		
	def characters(self, s):
		self.text += s
			
			

class DatabaseConnection:

	"""Wrapper class for all database access.  The methods are based on
	those provided from the MySQLdb library and some other Rocks
	specific methods are added.  All RocksCommands own an instance of
	this object (self.db).
	
	Special Environment Variables:
	
	ROCKS_VARS_HOSTNAME	- If defined specified the Rocks host
				that all app_globals lookups are 
				relative to.  If unspecified the localhost
				is assumed.  All methods that use this
				also also the value to be passed as an
				argument.
	"""
	
	def __init__(self, db):
		# self.database : object returned from orginal connect call
		# self.link	: database cursor used by everyone else
		self.database	= db
		self.link	= db.cursor()
		
	def execute(self, command):
		if self.link:
			return self.link.execute(command)
		return None

	def fetchone(self):
		if self.link:
			return self.link.fetchone()
		return None

	def fetchall(self):
		if self.link:
			return self.link.fetchall()
		return None

	def getGlobalVars(self, service, hostname='', site=0):
		"""Returns a dictionary of COMPONENT x VALUES for all
		component of the provided service.  This is useful to
		resolve entire service without having to know all the
		component keys."""
		
		# For every component of the service lookup the values.
		# Don't worry about duplicates on the select, the
		# loop ignores dups.
		
		self.link.execute('select component from app_globals '
			'where service="%s"' % service)
		dict = {}
		for component, in self.link.fetchall():
			if not dict.has_key(component):
				dict[component] = self.getGlobalVar(service,
					component, hostname, site)
		return dict
	
	def getGlobalVar(self, service, component, hostname='', site=0):
		"""Returns the value of the SERVICE x COMPONENT in from the
		app_globals tables.  If a hostname is provided the membership
		specific value will be found (if it exists), otherwise the
		default value will be returned.  If no value exists None is
		returned."""

		if not hostname:
			hostname = os.getenv('ROCKS_VARS_HOSTNAME')
		if not hostname:
			hostname = socket.gethostname()	

		if self.link:
			handler = AppGlobalsHandler(self.link, hostname, site)
			return handler.lookup(service, component)
		else:
			return None
	

	def getHostname(self, hostname=None):
		"""Returns the name of the given host as referred to in
		the database.  This is used to normalize a hostname before
		using it for any database queries."""
		
		# Look for the hostname in the database before trying
		# to reverse lookup the IP address and map that to the
		# name in the nodes table.  This should speed up the
		# installer w/ the restore roll
		
		if hostname and self.link:
			rows = self.link.execute("""select * from nodes where
				name='%s'""" % hostname)
			if rows:
				return hostname
		
		if not hostname:					
			hostname = socket.gethostname()
		try:
			addr = socket.gethostbyname(hostname)
		except:
			addr = None

		if not addr:
			if self.link:
				self.link.execute("""select name from nodes
					where name="%s" """ % hostname)
				if self.link.fetchone():
					return hostname
			Abort('cannot resolve host "%s"' % hostname)
		
		if addr == '127.0.0.1': # allow localhost to be valid
			return self.getHostname()
			
		if self.link:
			self.link.execute('select nodes.name from '
				'networks,nodes where '
				'nodes.id=networks.node and ip="%s"' % (addr))
			try:
				hostname, = self.link.fetchone()
			except TypeError:
				pass

		return hostname


		

class Command:
	"""Base class for all Rocks commands the general command line form
	is as follows:

		rocks ACTION COMPONENT OBJECT [ <ARGNAME ARGS> ... ]
		
		ACTION(s):
			add
			create
			list
			load
			sync
	"""

	MustBeRoot = 1

	def __init__(self, database):
		"""Creates a DatabaseConnection for the RocksCommand to use.
		This is called for all commands, including those that do not
		require a database connection."""
		if database:
			self.db = DatabaseConnection(database)
		else:
			self.db = None
		self.text = ''
		
		self.output = []
        
		self.arch = os.uname()[4]
		if self.arch in [ 'i386', 'i486', 'i586', 'i686' ]:
			self.arch = 'i386'
		self.os = os.uname()[0].lower()
		
		self._args = None
		self._params = None
		
	def abort(self, msg):
		rocks.commands.Abort(msg, 0)
		print self.usage()
		sys.exit(-1)
	
	def fillPositionalArgs(self, names, params=None, args=None):
		# The helper function will allow named parameters
		# to be used in lieu of positional arguments
		# Example:  
		#   Suppose command is of the form: 
                #            command <arg1> <arg2> <arg3>
		#   Usually called as:
		#            command foo bar baz
                #   However if you name the arguments as parameters, say
		#           arg1, arg2, arg3
		#   Then, equivalent calls of the command are
		#	    command arg1=foo arg2=bar arg3=baz 
		#           command foo arg2=bar arg3=baz
                #           command foo bar arg3=baz
		#           command foo bar baz
		#           command foo arg2=bar baz
		#
		#   Arguments:
		#           paramlist = list of parameter names in the order
		#                       that their unnamed argument counterparts		#			 appear eg. paramlist=('iface','mac')
		#	    params    = list of parameters (e.g param=value) 
		#           args      = args
		#
		#  Returns:
		#           remaining args, Filled parameters
		#  Example:
		#           hostlist,iface,mac=self.fillPositionalArgs( \
	        #			('iface','mac'),params,args)
	
		if not type(names) in [ types.ListType, types.TupleType ]:
			names = [ names ]
			 
		if not params:
			params = self._params
		if not args:
			args = self._args
			
		list = []
		for name in names:
			if params.has_key(name):
				list.append(params[name])
			else:
				list.append(None)

		# now walk backwards through the args and pull off
		# positional arguments that have not already been set
		# as a param=<parameter>

		trimmedArgs = args
		vars = []
		list.reverse()
		for e in list:
			if not e and len(trimmedArgs):
				vars.append(trimmedArgs[-1])
				trimmedArgs = trimmedArgs[:-1]
			else:
				vars.append(e)
		
		# need to reverse the 'vars' to get them in the correct order
		# since we processed them above in reverse order
		vars.reverse()

		rlist=[]
		rlist.append(trimmedArgs)
		rlist.extend(vars)
		return rlist 

	def fillParams(self, names, params=None):
		"""Returns a list of variables with either default
		values of the values in the PARAMS dictionary.
		
		NAMES - list of (KEY, DEFAULT) tuples.
			KEY - key name of PARAMS dictionary
			DEFAULT - default value if key in not in dict
		PARAMS - optional dictionary
		
		For example:
		
		(svc, comp) = self.fillParams(
			('service', None),
			('component', None))
			
		Can also be written as:
		
		(svc, comp) = self.fillParams(('service',), ('component', ))
		"""

		# make sure names is a list or tuple
		
		if not type(names) in [ types.ListType, types.TupleType ]:
			names = [ names ]

		# for each element in the names list make sure it is also
		# a tuple.  If the second element (default value) is missing
		# use None.  The resulting PDLIST is a list of (key, default) 
		# tuples.
		
		pdlist = []
		for e in names:
			if type(e) in [ types.ListType, types.TupleType] \
				and len(e) == 2:
				tuple = ( e[0], e[1] )
			else:
				tuple = ( e[0], None )
			pdlist.append(tuple)
				
		if not params:
			params = self._params

		list = []
		for (key, default) in pdlist:
			if params.has_key(key):
				list.append(params[key])
			else:
				list.append(default)
		return list


	def command(self, command, args=[]):
		"""Import and run a Rocks command.
		Returns and output string."""

		modpath = 'rocks.commands.%s' % command
		__import__(modpath)
		mod = eval(modpath)

		try:
			o = getattr(mod, 'Command')(self.db.database)
			name = string.join(string.split(command, '.'), ' ')
		except AttributeError:
			return ''
		o.runWrapper(name, args)
		return o.getText()


	def loadPlugins(self):
		dict	= {}
		graph	= rocks.graph.Graph()
		
		dir = eval('%s.__path__[0]' % self.__module__)
		for file in os.listdir(dir):
			if file.split('_')[0] != 'plugin':
				continue
			if os.path.splitext(file)[1] != '.py':
				continue
			module = '%s.%s' % (self.__module__,
				os.path.splitext(file)[0])
			__import__(module)
			module = eval(module)
			try:
				o = getattr(module, 'Plugin')(self)
			except AttributeError:
				continue
			
			# All nodes point to TAIL.  This insures a fully
			# connected graph, otherwise partial ordering
			# will fail

			if graph.hasNode(o.provides()):
				plugin = graph.getNode(o.provides())
			else:
				plugin = rocks.graph.Node(o.provides())
			dict[plugin] = o

			if graph.hasNode('TAIL'):
				tail = graph.getNode('TAIL')
			else:
				tail = rocks.graph.Node('TAIL')
			graph.addEdge(rocks.graph.Edge(plugin, tail))			
			for req in o.requires():
				if graph.hasNode(req):
					head = graph.getNode(req)
				else:
					head = rocks.graph.Node(req)
				edge = rocks.graph.Edge(head, plugin)
				graph.addEdge(rocks.graph.Edge(head, plugin))
			
		list = []
		for node in PluginOrderIterator(graph).run():
			if dict.has_key(node):
				list.append(dict[node])
		return list

		
	def runPlugins(self, args='', plugins=None):
		if not plugins:
			plugins = self.loadPlugins()
		for plugin in plugins:
                        syslog.syslog(syslog.LOG_INFO, 'run %s' % plugin)
			plugin.run(args)


	def isRootUser(self):
		"""Returns TRUE if running as the root account."""
		if os.geteuid() == 0:
			return 1
		else:
			return 0
			
	def isApacheUser(self):
		"""Returns TRUE if running as the apache account."""
		try:
			if os.geteuid() == pwd.getpwnam('apache')[3]:
				return 1
		except:
			pass
		return 0
		
	
	def str2bool(self, s):
		"""Converts an on/off, yes/no, true/false string to 1/0."""
		if s.upper() in [ 'ON', 'YES', 'Y', 'TRUE', '1' ]:
			return 1
		else:
			return 0

	def bool2str(self, b):
		"""Converts an 1/0 to a yes/no"""
		if b:
			return 'yes'
		else:
			return 'no'

	
	def strWordWrap(self, line, indent=''):
		if os.environ.has_key('COLUMNS'):
			cols = os.environ['COLUMNS']
		else:
			cols = 80
		l = 0
		s = ''
		for word in line.split(' '):
			if l + len(word) < cols:
				s += '%s ' % word
				l += len(word) + 1 # space
			else:
				s += '\n%s%s ' % (indent, word)
				l += len(indent) + len(word) + 1 # space
		return s
			
	def clearText(self):
		"""Reset the output text buffer."""
		self.text = ''
		
	def addText(self, s):
		"""Append a string to the output text buffer."""
		if s:
			self.text += s
		
	def getText(self):
		"""Returns the output text buffer."""
		return self.text	

	def beginOutput(self):
		"""Reset the output list buffer."""
		self.output = []
		
	def addOutput(self, owner, vals):
		"""Append a list to the output list buffer."""

		# VALS can be a list, tuple, or primitive type.
				
		list = [ '%s:' % owner ]
		if type(vals) == types.ListType:
			list.extend(vals)
		if type(vals) == types.TupleType:
			for e in vals:
				list.append(e)
		else:
			list.append(vals)
			
		self.output.append(list)
		
		
	def endOutput(self, header=[], padChar='-', trimOwner=1):
		"""Pretty prints the output list buffer."""

		# Handle the simple case of no output, and bail out
		# early.  We do this to avoid printing out nothing
		# but a header w/o any rows.
		
		if not self.output:
			return
			
		# Loop over the output and check if there is more than
		# one owner (usually a hostname).  We have only one owner
		# there is no reason to display it.  The caller can use
		# trimOwner=0 to disable this optimization.

		if trimOwner:
			owner = ''
			startOfLine = 1
			for line in self.output:
				if not owner:
					owner = line[0]
				if not owner == line[0]:
					startOfLine = 0
		else:
			startOfLine = 0
				
		# Add the header to the output and start formatting.  We
		# keep the header optional and separate from the output
		# so the above decision (startOfLine) can be made.
		
		if header:
			list = []
			for field in header:
				list.append(field.upper())
			output = [ list ]
			output.extend(self.output)
		else:
			output = self.output
			
		colwidth = []
		for line in output:
			for i in range(0, len(line)):
				if len(colwidth) <= i:
					colwidth.append(0)
				if type(line[i]) != types.StringType:
					if line[i] == None:
						itemlen = 0
					else:
						itemlen = len(repr(line[i]))
				else:
					itemlen = len(line[i])

				if itemlen > colwidth[i]:
					colwidth[i] = itemlen
				
		o = ''
		for line in output:
			list = []
			for i in range(startOfLine, len(line)):
				if line[i] == None:
					s = ''
				else:
					s = str(line[i])
				if padChar != '':
					if s:
						o = s.ljust(colwidth[i])
					else:
						o = ''.ljust(colwidth[i],
							padChar)
				else:
					o = s
				list.append(o)
			self.addText('%s\n' % self.outputRow(list))

	def outputRow(self, list):
		return string.join(list, ' ')
		
	def usage(self):
		if self.__doc__:
			handler = DocStringHandler()
			parser = make_parser()
			parser.setContentHandler(handler)
			try:
				parser.feed('<docstring>%s</docstring>' %
					self.__doc__)
			except:
				return '-- invalid doc string --'
			return handler.getUsageText()
		else:
			return '-- missing doc string --'

		
	def help(self, command, flags={}):
		if not self.__doc__:
			return

		if self.MustBeRoot:
			users = [ 'root', 'apache' ]
		else:
			users = []
			
		if flags.has_key('format'):
			format = flags['format'].lower()
		else:
			format = 'plain'
		
		if format == 'raw':
			i = 1
			for line in self.__doc__.split('\n'):
				self.addText('%d:%s\n' % (i, line))
				i += 1
		else:
			handler = DocStringHandler(command, users)
			parser = make_parser()
			parser.setContentHandler(handler)
			parser.feed('<docstring>%s</docstring>' % self.__doc__)
			if format == 'docbook':
				self.addText(handler.getDocbookText())
			elif format == 'parsed':
				self.addText(handler.getParsedText())
			else:
				self.addText(handler.getPlainText())

	
	def runWrapper(self, name, args):
		"""Performs various checks and logging on the command before 
		the run() method is called.  Derived classes should NOT
		need to override this."""

		username = pwd.getpwuid(os.geteuid())[0]
		if args:
			command = '%s %s' % (name, string.join(args,' '))
		else:
			command = name

		syslog.syslog(syslog.LOG_INFO,
			'user %s called "%s"' % (username, command))
			
		# Split the args and flags apart.  Args have no '='
		# with the exception of select statements (special case), and
		# flags have one or more '='.
		
		dict = {} # flags
		list = [] # arguments
		
		for arg in args:
			tokens = arg.split()
			if tokens[0] == 'select':
				list.append(arg)
			elif len(arg.split('=',1)) == 2:
				(key, val) = arg.split('=', 1)
				dict[key] = val
			else:
				list.append(arg)

		if list and list[0] == 'help':
			self.help(name, dict)
		else:
			if self.MustBeRoot and not \
				(self.isRootUser() or self.isApacheUser()):
				Abort('command "%s" requires root' % name)
			else:
				self._args   = list
				self._params = dict
				self.run(self._params, self._args)


	def run(self, flags, args):
		"""All derived classes should override this method.
		This method is called by the rocks command line as the
		entry point into the Command object.
		
		flags: dictionary of key=value flags
		args: list of string arguments"""
		
		pass

		
class Plugin:
	"""Base class for all Rocks command plug-ins."""
	
	def __init__(self, command):
		self.owner = command
		self.db    = command.db
		
	def provides(self):
		"""Returns a unique string to identify the plug-in.  All
		Plugins must override this method."""

		return None
		
	def requires(self):
		"""Returns a list of plug-in identifiers that must be
		run before this Plugin.  This is optional for all 
		derived classes."""

		return []
		
	def run(self, args):
		"""All derived classes should override this method. This
		is the entry point into the Plugin object."""
		
		pass


class PluginOrderIterator(rocks.graph.GraphIterator):
	"""Iterator for Partial Ordering of Plugins"""

	def __init__(self, graph):
		rocks.graph.GraphIterator.__init__(self, graph)
		self.nodes = []
		self.time  = 0

	def run(self):
		rocks.graph.GraphIterator.run(self)
		list = []
		self.nodes.sort()
		for time, node in self.nodes:
			list.append(node)
		list.reverse()
		return list

	def visitHandler(self, node, edge):
		rocks.graph.GraphIterator.visitHandler(self, node, edge)
		self.time = self.time + 1

	def finishHandler(self, node, edge):
		rocks.graph.GraphIterator.finishHandler(self, node, edge)
		self.time = self.time + 1
		self.nodes.append((self.time, node))
		

