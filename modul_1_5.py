immutable_var = (1,2,3,'Александр','Иван',True,False)
print(immutable_var)
# immutable_var[0] = 'Саша' (Ответ:выдаёт ошибку, потому что кортеж не поддерживает обращение по элементам)

mutable_var = [[1,2,3],'Александр','Иван', True,False]
mutable_var[0][0] = 'Елена'
print(mutable_var)
mutable_var[0][1] = 'Светлана'
print(mutable_var)
mutable_var[0][2] = 'Игорь'
print(mutable_var)
mutable_var.append('Татьяна')
print(mutable_var)
mutable_var.extend([1234])
print(mutable_var)
mutable_var.remove('Иван')
print(mutable_var)
mutable_var.remove(True)
print(mutable_var)