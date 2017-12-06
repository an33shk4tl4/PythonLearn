from twisted.internet import protocol, reactor
import time

class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print 'client: ', data
        if data.startswith("Knock knock"):
            response = "Who's there?"
            time.sleep(5)
        else:
            response = data + " who?"
            time.sleep(5)
        print 'Server: ', response
        self.transport.write(response)

class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()
reactor.listenTCP(8000, KnockFactory())
reactor.run()

