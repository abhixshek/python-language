1. start a python interactive session
2. import the module changer.py
3. call changer.printer()
3. in another window, change the code of changer.py by editing the message or the body of printer() function.
4. from imp import reload
5. reload(changer)
6. call changer.printer() and it should reflect the updated code

