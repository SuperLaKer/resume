import gevent, time

a = []

def eat(name):
    print('%s eat 1' %name)
    gevent.sleep(2)
    print('%s eat 2' %name)

    a.append(1)

def play(name):
    print('%s play 1' %name)
    gevent.sleep(1)
    print('%s play 2' %name)
    a.append(2)


g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,name='egon')
# g1.join()
# g2.join()
#或者gevent.joinall([g1,g2])

time.sleep(5)
print(a)
print('主')
