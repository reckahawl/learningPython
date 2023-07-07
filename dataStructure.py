import enum, collections
import threading, time
import heapq , random
import bisect , queue
import functools, struct
import copy

"""
card_A = {'Ad':('A dice', 50),'Af':('A flower', 50),'As':('A spade', 50),'Ah':('A heart', 50)}

import enum

class card_A(enum.Enum):
    A_Dice = ('A dice', 50)
    A_Flower = ('A flower', 50)
    A_Spade = ('A spade', 50)
    A_Heart = ('A heart', 50)

print('\nMember name: {}'.format(card_A.A_Dice.name))
print('\nMember value: {}'.format(card_A.A_Dice.value[0]))

class BugStatus(enum.Enum):
    new = (7, ['incomplete','invalid','wont_fix','in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transition):
        self.num = num
        self.transition = transition
    
    def can_transition(self, new_state):
        return new_state.name in self.transition

print('Name:', BugStatus.in_progress)
print('Value:', BugStatus.in_progress.value)
print('Custom attribute:', BugStatus.in_progress.transition)
print('Using attribute:',BugStatus.in_progress.can_transition(BugStatus.new))   


a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))



c = collections.Counter()
print('Initial :', c)
c.update('abcdaab')
print('Sequence:', c)



c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')


print('\nCombined counts:')
print(c1 + c2)
print('\nSubtraction:')
print(c1 - c2)
print('\nIntersection (taking positive minimums):')
print(c1 & c2)
print('\nUnion (taking maximums):')
print(c1 | c2)


def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

print()

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

print()

# Add to the right.
d1 = collections.deque()
d1.extend('abcdefg')
print('extend:', d1)
d1.append('h')
print('append:', d1)
# Add to the left.
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)


candle = collections.deque(range(10))

def burn(direction, nextSource):
    while True:
        try:next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

c = collections.deque(range(10))
c.rotate(2)
#print(c)


print()


data = [i for i in range(10)]

print('\n')


import math
from io import StringIO


def show_tree(tree, total_width=36, fill=' '):
    Pretty-print a tre
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)


#Efficiently Merging Sorted Sequence
#list(sorted(itertools.chain(*data)))


random.seed(2016)
data = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

for i, d in enumerate(data):
    print('{}: {}'.format(i, d))

print('\nMerged')
for i in heapq.merge(*data):
    print(i, end=' ')
print()

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos   Contents')
print('---  ----  --------')
l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3} {:3}'.format(i, position), l)

for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)



q = queue.Queue()
lq = queue.LifoQueue()
for i in range(5):
    lq.put(i)
while not q.empty():
    print(lq.get(), end=' ')
print()
"""

@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return
    
    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented
        
    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()

workers = [
    threading.Thread(target=process_job, args = (q,)),
    threading.Thread(target=process_job, args = (q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()
q.join()  


@functools.total_ordering
class MyClass:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __gt__(self, other):
       return self.name>other.name

    def __copy__(self):
        print('__copy__()')
        return MyClass(self.name)
    def __deepcopy__(self, memo):
        print('__deepcopy__({})'.format(memo))
        return MyClass(copy.deepcopy(self.name, memo))

a = MyClass('a')
sc = copy.copy(a)
dc = copy.deepcopy(a)
my_list = [a]
dup = copy.copy(my_list)

print('     my_list:', my_list)


class Graph:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
    
    def add_connection(self, other):
        self.connections.append(other)
    
    def __repr__(self):
        return 'Graph(name={}, id={})'.format(self.name, id(self))
    
    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing=memo.get(self)
            print(' Already copied to {!r}'.format(existing))
            return existing
        print('   Memo dictionary')
        if memo:
            for k, v in memo.items():
                print('  {}: {}'.format(k,v))
        else:
            print('    (empty)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print(' Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup

root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.add_connection(a)
root.add_connection(b)
dup = copy.deepcopy(root)

