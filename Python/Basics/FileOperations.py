f = open("/home/umamaheswaran/Code/Sample-Codes/Python/Basics/HelloWorld.py")
print(f.read())
f = open("/home/umamaheswaran/Code/Sample-Codes/Python/Basics/HelloWorld.py", "a")
f.writelines("\n")
f.write("test")
f = open("/home/umamaheswaran/Code/Sample-Codes/Python/Basics/HelloWorld.py")
print(f.read())
