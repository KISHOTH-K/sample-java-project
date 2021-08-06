dictionary={1:'January',2:'February',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
print(dictionary)
print(dictionary[1])
print(dictionary[12])
print(dictionary[4])
print(dictionary[8])
print(dictionary[9])
# keys
print(dictionary.keys())
# values
print(dictionary.values())
# copy the contents to other dictionary
copy_dict=dictionary.copy()
print(copy_dict)
# displaying the values of copied dictionary
print(copy_dict.values())
# clear the dictionary
copy_dict.clear()
print(copy_dict)






