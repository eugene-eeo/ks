Prudent: Lazy Datastructures
----------------------------

**Prudent:** careful in providing for the future; provident.

Prudent is a library containing small and simple lazy datastructures,
including a Stream, Mapping, and Sequence. Prudent aims to have a very
simple and flexible core that developers can build heavier abstractions
around. Because of that the API is exteremely tiny and only contains a
few methods. The other methods are often handled by the mixins found in
the **collections** library. Example code:

.. code-block:: python

    from prudent import Mapping
    d = Mapping((k, k+1) for k in range(100))

    assert d[15] == 16
    assert d[20] == 21

Prudent is aimed at functional programs as well as situations
where datasets are either too large to fit into memory all at
once or where you need to lazily cache sequential operations
(a typical example is the recursive fibonacci implementation).
