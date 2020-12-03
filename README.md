

# AOC 2020

https://pypi.org/project/aocpy/



## Snippets 

### Regex

```
import re
pattern = re.compile(r'^(?P<v1>\d*)-(?P<v2>\d*) (?P<leter>.):(?P<pw>.*)$')

line = '1-66 b: sgdandausdiasbnfd'
match = pattern.search(line)

print(match.groupdict())
print('v1:', match.group('v1'))
```