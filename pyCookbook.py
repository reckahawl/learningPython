import collections, re
from operator import *
from itertools import *
import  unicodedata, threading
import os, fnmatch
import bz2, gzip
from functools import *
import socket
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))


class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(99)]   

sorted(users, key=attrgetter('user_id'))




cards = [
    ('A', 'Dice', 50),
    ('7', 'Dice'),
    ('3', 'Dice', 'Special'),]

for card, *args in cards:
    if card == 'A':print(*args)

s2 = "'Spicy Jalapen\u0303o' s1 = 'Spicy Jalape\u00f1o'"
t1 = unicodedata.normalize('NFC', s2)
print(ascii(t1))

s2.strip()
s2.rstrip('')
s2.lstrip('=')


'%-20s' % text
'%20s' % text

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
','.join(parts)
','.join(str(d) for d in data)

item = [i for i in range(5)]
t = iter(item)
next(t)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
    

class depthFirstIterator(object):
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self
    
    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        #if processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild=next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        
        #Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

class countdown:
    def __init__(self,start):
        self.start = start
    
    #Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    
    #Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    
    def clear(self):
        self.history.clear()



# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)


##############
def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, ffilepat):
            yield os.path.join(path, name)

def gen_opener(filenames):

    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt') 
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt') 
        else:
            f = open(filename, 'rt')
        yield f
        f.close

def gen_concatenate(iterators):
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
##################

def flatten(items, ignore_types=(str, bytes)):
    # Reading from nested sequence
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def reader(s):
    for chunk in iter(lambda: s.recv(8192), b''):
        process_data(data)


####
print('ACME', 50, 91.5, sep=',', end='!!\n')


class Countdown:
    def __init__(self, n):
        self.n =n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()
    
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
    
    def __getstate__(self):
        return self.n
    
    def __setstate__(self):
        self.__init__(n)
    
t = Countdown(30)
print(t)

## name = lambda (Arguments): expression
def spam(a, b, c, d):
    return (a, b, c, c, d)

s1 = partial(spam, 1)
s1(2,3,4)

############3
class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)
    ####
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)

    

serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECIEVED'))
serv.serve_forever()


####'
class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))
def apply_async(func, args, *,callback):
    result = func(*args)

    callback(result)

def print_result(result):
    print('Got:',result)

def add(x,y):
    return x + y



apply_async(add, (3,5), callback=print_result)



class LazyConn:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already Connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

conn = LazyConn((www.python.org))
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
"""
class Integer:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]

    
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r
    return wrapper

class Span:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n >0:
            n -= 1
    
    @classmethod
    @timethis
    def class_method(cls, n):
        print(self, n)
        while n >0:
            n -= 1
    @staticmethod
    @timethis
    def static_method(cls, n):
        print(self, n)
        while n >0:
            n -= 1
            
