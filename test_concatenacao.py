# Da erro string + int
# nome = "Denis"
# idade = 23
# print(nome+idade)
#


num = "20x"
nums  = num*20
print(nums)

nome = "Denis"
sobrenome = "Feliciano"
print("Olá {} {}".format(nome,sobrenome))
print("Olá {0} {1}".format(nome,sobrenome))
print("Olá {1} {0}".format(nome,sobrenome))


print("R$ {} ".format(1.54))
print("R$ {:f} ".format(1.54))
print("R$ {:.2f} ".format(1.54))
print("R$ {:7.2f} ".format(1.54))
print("R$ {:7.2f} ".format(1.423424))
print("R$ {:.2f} ".format(1.423424))
print("R$ {:2.2f} ".format(13122.423424))
print("R$ {:07.2f}".format(12.423424))
print("R$ {:07.2f}".format(4.5))
print("123{:07.2f}".format(7.89101112))
print("Number integer = {:7d}".format(44))

print("Data: {}/{}/{}".format(2,7,2020))
print("Data: {:02d}/{:02d}/{}".format(2,7,2020))

lastname = 'DA SILVA'
print(f'interpolação de strings, seu nome é  {nome} {sobrenome} {lastname.lower()}')