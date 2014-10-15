ks
==

**ks** is a minimal library that implements lazy
data structures, mainly meant for functional
styled programs. Performance is a secondary
concern, elegance is the first concern and as
such sometimes we sacrifice performance for an
easier way/more elegant way.

```python
from ks.stream import Stream

s = (Stream(1, 2, 3) << 'abc').use(str)
assert ''.join(s) == '123abc'
```
