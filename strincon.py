import inspect, string
import textwrap


"""
def is_str(value):
    return isinstance(value, str)

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):continue
    print('%s=%r'%(name, value))
"""
sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''
#print(textwrap.fill(sample_text, width=50))
d_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns: \n'.format(width))
    print(textwrap.fill(d_text, width=width))
    print()

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')
print('Quoted block:\n')
print(final)
#print(d_text)

def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ',predicate=should_indent)
print('\nQuoted block:\n')
print(final)
print('\n')


dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
initial_indent='',
subsequent_indent=' ' * 4,
width=50,
))



dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)
print('Original:\n')
print(original)


shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)
print('\nShortened:\n')
print(shortened_wrapped)


