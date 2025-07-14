import sys

m = sys.modules
r = list(m.keys())
print(r)
print('functions4' in r) # False

def glob2():
    import functions4

glob2()
m = sys.modules
r = list(m.keys())
print(r)
print('functions4' in r) # False

# this code when run does not get into an infinite loop because once glob2() is called and it imports functions4 once, and while it is getting imported it runs
# glob2() again but this time the import statement does not do anything. because recall import statements are not reloaded automatically. 
# to explicitly reload we use reload() function - `from imp import reload`
# if you do this and then run then you will probably get into an inf loop
    
