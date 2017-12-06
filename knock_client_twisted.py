from twisted.internet import reactor, protocol
import time
class KnockClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Knock knock")

    def dataReceived(self, data):
        if data.startswith("Who's there?"):
            response = "Disappearing client"
            time.sleep(5)
            self.transport.write(response)
        else:
            self.transport.loseConnection()
            reactor.stop()
class KnockFactory(protocol.ClientFactory):
    protocol = KnockClient

def main():
    f = KnockFactory()
    reactor.connectTCP('localhost', 8000, f)
    reactor.run()
if __name__ == '__main__':
    main()
