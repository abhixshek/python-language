var = 99 # global variable == module attribute
def local():
    var = 0 # change local var

def glob1():
    global var # declare global (normal)
    var += 1 # change global var

def glob2():
    var = 0 # change local var
    import functions3 # import myself
    functions3.var += 1 # change global var

def glob3():
    var = 0 # change local var
    import sys # import system table
    glob = sys.modules['functions3'] # get module object (or use __name__)
    glob.var += 1

def test():
    print(var) # 99
    local(); glob1(); glob2(); glob3()
    print(var) # 102 (when run through another module)

if __name__ == "__main__":
    test() # prints 99 and then 100
    """when running this file directly, this file is known to the interpreter as __main__
    glob2() imports this same file but as an imported module object named functions3 and that functions3 's var is getting updated.
    so when this file is run directly, changes made by glob2() are not reflected in the run.

    also note that glob3() is able to run in test() because of running glob2() before it. otherwise if you run glob3() it will give KeyError as 'functions3'
    is not known to sys.
    also note that glob2() imported sys and therefore `sys` name is only available in the local scope. but the sys module knows about all the imported modules
    so while outside glob2() you cannot use the name functions3 (will get NameError) you can access functions3 through sys.modules dictionary (system table)

    """
    


