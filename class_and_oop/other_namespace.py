import namespace_concepts as nc

X = 66
print(X) # 66
print(nc.X) # 5. module globals become module attributes after import

nc.f() # 5. f has access to its module's X only. 

nc.g() # 22. local variable

print(nc.C.X) # 33
I = nc.C()
print(I.X) # 33 # still clas satttribute
I.m()
print(I.X) # 55. instance attribute



