from twisted.application import internet, service
from twisted.python import log
#if we have psyco, lets use it
try:
    import psyco
    psyco.full()
    print "imported and initialized psyco compiler"
except:
    log.warn('psyco is not available, will not optimize.')

from palomino import initStore 
initStore.makeAPoolAndStuff()


ms = service.MultiService()
#ms.addService(internet.TCPServer(54321, PBFactory))
ms.setServiceParent(application)
