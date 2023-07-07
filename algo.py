import functools ,itertools
from itertools import *
import operator, pprint
import contextlib

"""

def myfunc(a, b=2):
    print( ' called myfunc wiyh: ', (a, b))

def show_details(name, f, is_partial=False):
    print('{}:'.format(name))
    print(' object:', f)
    print(' __doc__', repr(f.__doc__))
    if not is_partial:
        print(' __name__:', f.__name__)
    if is_partial:
        print(' func:', f.func)
        print(' args:', f.args)
        print(' keywords:', f.keywords)
    return


# Set a different default value for 'b', but require
# the caller to provide 'a'.

p1 = functools.partial(myfunc, b=4)
#show_details('partial with default',p2,True)
#p2()
#p2(b='overide b')
print()

#print('Insufient arguments:')
#p1()

def standalone(self, a=1, b=2):
    "Standalone function"
    print(' called standalone with:', (self, a, b))
    if self is not None:
        print(' self.attr =', self.attr)



def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults:', (a, b)):
        print(' decorated:', (a, b))
        print(' ', end=' ')
        return f(a, b=b)
    return decorated


@functools.lru_cache(maxsize=2)
def expensive(a, b):
    print('called expensive({}, {})'.format(a, b))
    return a * b

def make_call(a, b):
    print('({}, {})'.format(a, b), end=' ')
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print('cache hit')
print('Establish the cache')
make_call(1, 2)
make_call(2, 3)
class MyClass:
    "Demonstration class for functools"
    def __call__(self, e, f=6):
        "Docstring for MyClass.__call__"
        print(' called object with:', (self, e, f))
 
    def __init__(self):
        self.attr = 'instance attribute'
    
    method1 = functools.partialmethod(standalone)
    method2= functools.partial(standalone)


o = MyClass()

@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))

@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print(' {}'.format(item))


myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()

r = islice(count(), 5)
i1, i2 = tee(r)

print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()
print('i1:', list(i1))
print('i2:', list(i2))

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)

for i in zip(range(7),  cycle(['a','b','c','d'])):
    print(i)

for i in repeat('over-and-over', 5):
    print(i)

for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))

@functools.total_ordering
class Point:
    def __init__(self, x, y):
       self.x = x
       self.y = y
    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)

data = list(map(Point,
    cycle(islice(count(), 3)),
    islice(count(), 7)))

print('Data:')
pprint.pprint(data, width=35)
print()
# Try to group the unsorted data based on X values.
print('Grouped, unsorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()
# Sort the data.
data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Group the sorted data based on X values.
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()


FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')


SUITS = ('H', 'D', 'C', 'S')
DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,))
for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        print()

for card in DECK:
    print('{:>2}{}'.format(card[1], card[0]), end=' ')
    if card[1] == FACE_CARDS[-1]:
        print()  


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()

print('All permutations:\n')
show(permutations('abcd'))
print('\nPairs:\n')
show(permutations('abcd', r=2))

class WithinContext:
    def __init__(self, context):
        print('WithinContext.__init__({})'.format(context))
    def do_something(self):
        print('WithinContext.do_something()')
    def __del__(self):
        print('WithinContext.__del__')


class Context:
    def __init__(self):
        print('Context.__init__()')
    def __enter__(self):
        print('Context.__enter__()')
        return WithinContext(self)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')

with Context() as c:
    c.do_something()


class Context(contextlib.ContextDecorator):
    def __init__(self, how_used):
        self.how_used = how_used
        print('__init__({})'.format(how_used))

    def __enter__(self):
        print('__enter__({})'.format(self.how_used))
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({})'.format(self.how_used))

@Context('as decorator')
def func(message):
    print(message)

print()
with Context('as context manager'):
    print('Doing work in the context')

print()
func('Doing work in the wrapped function')

@contextlib.contextmanager
def make_context():
    print(' entering')
    try:
        yield {}
    except RuntimeError as err:
        print(' ERROR:', err)
    finally:
        print(' exiting')

def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)
print('Normal:')
variable_stack(2, 'inside context')


with make_context() as value:
    print(' inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling an error')
print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')

"""








