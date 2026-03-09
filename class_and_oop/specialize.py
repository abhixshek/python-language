## class interface techniques


class Super:
    def method(self):
        print('in Super.method') # default behaviour
    def delegate(self):
        self.action() # expected to be defined

class Inheritor(Super): # inherit method verbatim
    pass

class Replacer(Super): # replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super): # extend method behaviour
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Entender.method')

class Provider(Super): # fill in a required method
    def action(self):
        print('in Provider.action')


if __name__ == "__main__":
    i = Inheritor()
    # i.delegate() this will lead to an AttributeError as action is not defined any where in the inheritance tree of `i`

    for kclass in (Inheritor, Replacer, Extender):
        print('\n' + kclass.__name__ + '...')
        kclass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

    class Super:
        def delegate(self):
            self.action()
        def action(self):
            raise NotImplementedError('action must be defined!')

    x = Super()
    # x.delegate() # raises NotImplementedError

