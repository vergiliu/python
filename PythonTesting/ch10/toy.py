__author__ = 'vergiliu'

def global_function(x):
    r"""
    >>> global_function(5)
    6
    """
    return x+1

class ExampleClass:
    def __init__(self, a_param):
        self.a_param = a_param

    def times_two(self,):
        return self.a_param * 2

    def __repr__(self):
        return '<example param="%d">' % self.a_param

if __name__ == "__main__":
    import doctest
    doctest.testmod()