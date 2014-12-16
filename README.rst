Prudent: Lazy Datastructures
============================

Prudent is a library containing small and simple implementations
of lazy datastructures. Prudent aims to have a very simple and
flexible core that developers can build more heavy abstractions
around. Example code:

.. code-block:: python

    from prudent import Mapping
    d = Mapping((k, k+1) for k in range(100))

    assert d[15] == 16
    assert d[20] == 21

Prudent is aimed at situations where datasets are either too
large to fit into memory, all at once or where you need to lazily
cache sequential operations.
