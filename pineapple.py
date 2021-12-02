from sys import platform

if platform == "linux" or platform == "linux2":
    from linux import main
    
elif platform == "darwin":
    from mac import main
    
elif platform == "win32":
    from windows import main