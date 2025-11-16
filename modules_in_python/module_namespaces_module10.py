import module1 as m

print(dir(m))

# print(module1.__dict__)

print(m.__dict__.keys())


print(m.sys)

print(m.__dict__['__file__'])
print(m.__dict__['__name__']) # even though module1 was imported with an alias as m, its __name__ attribute inside __dict__ is still module1

