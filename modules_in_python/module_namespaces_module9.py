import module1

print(dir(module1))

# gives Module namespaces can be accessed via the attribute module1.__dict__ or dir(module1)
print(module1.__dict__.keys())


print(module1.sys)

print(module1.__dict__['__file__']) # the full path of module1.py
print(module1.__dict__['__name__']) # module1
