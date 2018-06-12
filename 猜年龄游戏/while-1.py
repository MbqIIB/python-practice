i = 0
age =23
client = 'y'
while i < 3:
    _age = int(input("Age:"))
    if age == _age:
        print ("you are right")
        break
    else:
        print ("again")
    i += 1
    if i ==3:
        choice = input('>:')
        if choice == 'y' or choice == 'Y':
            i = 0
