Prudent
=======

**Prudent** is a library of small, elegant, and composable
lazy data structures. The aim is to have a very small and
flexible core that developers can build heavier abstractions
around. Usage example::

    from prudent import Mapping

    def fibo(n):
        return (n if n == 0 or n == 1 else
                cache[n-1] + cache[n-2])

    cache = Mapping((n, fibo(n)) for n in range(1000))
    assert fibo(10) == 55
