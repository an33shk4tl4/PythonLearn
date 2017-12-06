import gevent
from gevent import socket
hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.antique-taxidermy.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# jobs1 = [gevent.spawn(gevent.socket.gethostbyaddr, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
# gevent.joinall(jobs1, timeout=10)

# for job in jobs1:
#     print(job.value)
for job in jobs:
    print(job.value)

