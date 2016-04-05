from twisted.web import proxy
from twisted.internet import reactor
from twisted.internet import protocol
from twisted.python import log
import sys
log.startLogging(open('/home/calsoft/Desktop/code/cherrypytestapp/src/proto.log', 'w'))
log.startLogging(sys.stdout)