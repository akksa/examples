import gevent

def mul(x):
    return x*x

my_list = [5,10,2]
jobs = [gevent.spawn(mul, x) for x in my_list]
gevent.joinall(jobs,timeout=2)
print [x.value for x in jobs]