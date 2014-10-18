ks
==

**ks** is a minimal library that implements lazy
data structures, mainly meant for functional styled
programs. Performance and elegance are the concerns
of the library. **ks** aims to provide a suite of
fast and easy-to-use datastructures.

## Why?

When designing systems in Python that require large
sets of data to be processed, the builtins are not
an option and there doesn't seem to be a viable third
party package available. **ks** aims to fill that gap
in a sane and Pythonic way.

## Usage example

```python
from ks.stream import Stream
from ks.mapping import Mapping

s = (Stream([1,2,3]) << [4,5,6]).use(str)
assert ''.join(s) == '123456'

m = Mapping([(1,2), (2,3), (3,4)])
assert m[2] == 3
assert m[3] == 4
```
