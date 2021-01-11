def help():
    print('$ ./todo help')
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todo')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')
    print('```')


def add():
    L = list()
    Zero=input(' todo add'"")
    f = open('new.txt', 'r')
    for line in f.readlines():
        L.append(line)
    L.insert(0,'\n')
    L.insert(0,Zero)
    
    f.close()

    fi = open('new.txt', 'w')
    for line in range(len(L)):
        fi.write(L[line])

    fi.close()
    print('todo added ')


def ls():
    count=0
    fh=open('new.txt')
    for j in fh:
        count=count+1
    #    print(count)
    fh.close()
    fl=open('new.txt') 
    for  i in fl:
        print({count},i)   
        count=count-1
help()
while 1:

   
    z=input()
    if z=="add":
        add()
    if z=='help':
        help()
    if z=='ls':
        ls()
    elif z=='exit':
       break