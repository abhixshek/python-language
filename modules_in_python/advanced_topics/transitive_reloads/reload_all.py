"""
reloadall.py: transitively reload nested modules
"""
import types
from importlib import reload


def status(mod):
    print("reloading", mod.__name__)


def transitive_reload(mod, visited):
    for key in mod.__dict__:
        if type(mod.__dict__[key]) == types.ModuleType and mod.__dict__[key].__name__ not in visited:
            transitive_reload(mod.__dict__[key], visited) # call function recursively

    status(mod)
    reload(mod)
    visited[mod] = None # the value does not have significance in this program. we are about the keys only. So you could have used set in place of dictionaries to do the same
    # NOTE, as key we have given a module object, mod. It is not a string, meaning modules can be given as keys of a dictionary.

    for key in mod.__dict__:
        if type(mod.__dict__[key]) == types.ModuleType and mod.__dict__[key] not in visited:
            ireload_all(mod.__dict__[key], visited) # call function recursively


def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)




if __name__ == "__main__":
    import a

    reload_all(a)



