import re

pattern = 'this'
text = 'Does this text match the pattern which is given?'


regexes = [re.compile(p)for p in ['this', 'that']]

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')
    if regex.search(text):print('match!')
    else: print('no match')



p = 'ab'
t = 'abbaaabbbbaaaaa'

for match in re.findall(p, t):
    print('Found {!r}'.format(match))

for match in re.finditer(p, t):
    s =match.start()
    e =match.end()
    print('Found {!r} at {:d}:{:d}'.format(t[s:e], s, e))
#print('Found "{}"\nin"{}"\nfrom {} to {} ("{}")'.format(match.re.pattern,match.string, s, e, text[s:e]))



def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
# Look for each pattern in the text and print the results.
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print(" '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(" {}'{}'".format(prefix, substr))
        print()
        return
if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',[('ab', "'a' followed by 'b'"),])


test_patterns(
    'abbaabbba',
    [('ab*', 'a followed by zero or more b'),
    ('ab+', 'a followed by one or more b'),
    ('ab?', 'a followed by zero or one b'),
    ('ab{3}', 'a followed by three b'),
    ('ab{2,3}', 'a followed by two to three b')],)


test_patterns(
    'abbaabbba',
    [('ab*?', 'a followed by zero or more b'),
    ('ab+?', 'a followed by one or more b'),
    ('ab??', 'a followed by zero or one b'),
    ('ab{3}?', 'a followed by three b'),
    ('ab{2,3}?', 'a followed by two to three b')],)

test_patterns(
    'abbaabbba',
    [('[ab]', 'either a or b'),
    ('a[ab]+', 'a followed by 1 or more a or b'),
    ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],)

test_patterns(
    'This is some text -- with punctuation.',
    [('[^-. ]+', 'sequences without -, ., or space')],)

test_patterns(
    'abbaabbba',
    [('a.', 'a followed by any one character'),
    ('b.', 'b followed by any one character'),
    ('a.*b', 'a followed by anything, ending in b'),
    ('a.*?b', 'a followed by anything, ending in b')],)



test_patterns(
    'A prime #1 example!',
    [(r'\d+', 'sequence of digits'),
    (r'\D+', 'sequence of non-digits'),
    (r'\s+', 'sequence of whitespace'),
    (r'\S+', 'sequence of non-whitespace'),
    (r'\w+', 'alphanumeric characters'),
    (r'\W+', 'non-alphanumeric')],)


test_patterns(
    'This is some text -- with punctuation.',
    [(r'^\w+', 'word at start of string'),
    (r'\A\w+', 'word at start of string'),
    (r'\w+\S*$', 'word near end of string'),
    (r'\w+\S*\Z', 'word near end of string'),
    (r'\w*t\w*', 'word containing t'),
    (r'\bt\w+', 't at start of word'),
    (r'\w+t\b', 't at end of word'),
    (r'\Bt\B', 't, not start or end of word')],)



print('\n\n')
pattern = re.compile(r'\b\w*is\w*\b')

pos=0
while True:
    match = pattern.search(text, pos)
    if not match:break
    s = match.start()
    e = match.end()
    print(' {:>2d} : {:>2d} = "{}"'.format(s, e -1, text[s:e]))
    pos = e


test_patterns(
    'abbaaabbbbaaaaa',
    [('a(ab)', 'a followed by literal ab'),
    ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
    ('a(ab)*', 'a followed by 0-n ab'),
    ('a(ab)+', 'a followed by 1-n ab')],)



pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

dotall = re.compile(pattern, re.DOTALL)

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Case-sensitive:')
for match in with_case.findall(text):
    print(' {!r}'.format(match))
print('Casw-insensitive:')
for match in without_case.findall(text):
    print(' {!r}'.format(match))




address = re.compile(
    '''
    [\w\d.+-]+      # Username
    @
    ([\w\d.]+\.)+   # Domain name prefix
    (com|org|edu)   # TODO: support more top-level domains
    ''',
re.VERBOSE)
candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]
candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]
for candidate in candidates:
    match = address.search(candidate)
    print('{:<30} {}'.format(candidate, 'Matches' if match else 'No match'))



