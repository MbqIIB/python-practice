i = 0
age =23
client = 'y'
while client == 'y':
    while i < 3:
        _age = int(input("Age:"))
        if age == _age:
            print "you are right"
            break
        else:
            print "again"
        i += 1
    client = raw_input("Client(y):")
    if client == 'y' or client == 'Y':
        i = 0