names = ['alex','jack',2,'rain','mack',2,'racheal','shanshan',2,'longting']
for index,i in enumerate(names):
    if index % 2 == 0:
        names[index] = -1
print (names)
