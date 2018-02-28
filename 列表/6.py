names = ['alex','jack',2,'rain','mack',2,'racheal','shanshan',2,'longting']
print (names.index(2))
first_index = names.index(2) #第一个2的索引值
new_list = names[first_index + 1 :] #切割第一个2之后的列表
print (new_list) #打印新生成的列表
second_index = new_list.index(2) #新列表的第一个2的索引值（就是原来列表的第二个2的索引值）
print (second_index) #打印第二个2的索引值
second_val = names[first_index + second_index + 1] #因为second_index是从新列表里面统计出来的，所以要统计原来列表的第二个2的索引，必须结合first_index
print (second_val)
print (first_index + second_index + 1)