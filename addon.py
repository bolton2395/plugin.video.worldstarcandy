#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from future import standard_library
standard_library.install_aliases()
from builtins import str
import os
import sys
import urllib.parse
import xbmc
import xbmcaddon


LIB_DIR = xbmc.translatePath(
    os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'lib'))
sys.path.append(LIB_DIR)

from worldstarcandy_const import ADDON, DATE, VERSION, BASEURL

# Parse parameters...
if len(sys.argv[2]) == 0:
    #
    # Main menu
    #
    #
    xbmc.log("[ADDON] %s, Python Version %s" % (ADDON, str(sys.version)), xbmc.LOGDEBUG)
    xbmc.log("[ADDON] %s v%s (%s) is starting, ARGV = %s" % (ADDON, VERSION, DATE, repr(sys.argv)), xbmc.LOGDEBUG)
    import worldstarcandy_list as plugin
else:
    action = urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query)['action'][0]
    #
    # List
    #
    if action == 'list':
        import worldstarcandy_list as plugin
    #
    # Play
    #
    elif action == 'play':
        import worldstarcandy_play as plugin
    #
    # Search
    #
    elif action == 'search':
        import worldstarcandy_search as plugin

plugin.Main()
