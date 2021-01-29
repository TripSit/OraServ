###
# Copyright (c) 2021, mogad0n
# All rights reserved.
#
#
###

from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('OraServ')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class OraServ(callbacks.Plugin):
    """An oragonoIRCd specific toolkit for IRCops"""
    threaded = True


Class = OraServ


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
