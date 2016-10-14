import ssl
import threading
import logging

import irc.client
import irc.connection
import irc.bot

from Legobot.Message import *
from Legobot.Lego import Lego

logger = logging.getLogger(__name__)

class IRCBot(threading.Thread, irc.client):
    def __init__(
            self,
            baseplate,
            channels,
            nickname,
            server,
            port=6667,
            use_ssl=False,
            password=None,
            username=None,
            ircname=None,
    ):
       return
