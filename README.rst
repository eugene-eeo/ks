Prudent
=======

**Prudent** is a library of small, elegant, and composable
lazy data structures. The aim is to have a very small, fast,
focused, and flexible core that developers can build heavier
abstractions around. Usage example::

    from prudent import Mapping

    mapping = Mapping((n, n+1) for n in xrange(1000))
    assert mapping[99] == 100
    assert len(mapping) == 99
