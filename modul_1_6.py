my_dict = {'Sasha': 1999, 'Tanya': 1985}
print(my_dict)
print(my_dict.get('Tanya'))
print(my_dict.get('Vasya'))
my_dict.update({'Ivan': 1996,'Lena':1989})
a = my_dict.pop('Sasha')
print(a)
print(my_dict)

print() #Разделил для удобства :)
my_set = {1,2,3,4,4,5,6,7,7,6,'Sasha',4.23}
print(my_set)
my_set.add('Privet')
my_set.add(23)
print(my_set)
my_set.discard(5)
print(my_set)