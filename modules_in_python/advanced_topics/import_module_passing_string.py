# import "data_module" # this statement raises SyntaxError


mod = "data_module"

import mod # NOTE, this does not mean import data_module
# what happens here is 'mod.py' will be read and then that read module will be assigned to the variable by the same name, in this case mod
print(mod) # notice the module path in the output

# how do we read a module name as a string. The solution is to use exec() built-in function

mod = "data_module"
exec("import " + mod)
print(data_module) # notice how so far this variable name did not even exist in our current namespace
# notice the output path, pointing to data_module.py

print(data_module.age)
data_module.age = 9

exec("import " + mod) # does running exec() again reload the module?

print(data_module.age) # 9. so no it does not reload already loaded module as expected.

# another alternative to exec() is __import__() which takes as input module name as string and returns a module object

form = __import__("formats")
print(form) # module object pointing to formats.py
print(form.commas(89423835))

