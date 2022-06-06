import os

l = [83,22,41,13,24,100]

def demo():
    
    child = os.fork()

    if child>0:
        print("Parent Process is : " , os.getpid())
        print(sorted(l))
    else:
        print("Child Process is : " , os.getpid())
        print(sorted(l , reverse=True))

demo()