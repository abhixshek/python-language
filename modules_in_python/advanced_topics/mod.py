# __name__ attribute of modules

def func():
    print("tester function")

# when this module file is run directly as a program then this block of run will also be run since __name__ == "__main__" in that case.
# otherwise when this module is imported into other modules there the below block will not be executed as __name__ takes the value of the module_name, in this case 'mod'
if __name__ == "__main__":
    print("__name__ is __main__")
    func()
    print("program run complete.")

