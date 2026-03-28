"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam__doc__"
    def method(self, arg):
        """I am: spam.method.__doc__ or self.method.__doc__"""
        pass

"""
in an interpreter run the following commands to explore the __doc__ attribute at runtime
>>> import docstr
>>> docstr.__doc__
'I am: docstr.__doc__'
>>> docstr.func.__doc__
'I am: docstr.func.__doc__'
>>> docstr.spam.__doc__
'I am: spam.__doc__ or docstr.spam.__doc__'
>>> docstr.spam.method.__doc__
'I am: spam.method.__doc__ or self.method.__doc__'
"""

# As a best-practice rule of thumb, use docstrings for functional documentation (what your
# objects do) and hash-mark comments for more micro-level documentation (how arcane expressions work).
