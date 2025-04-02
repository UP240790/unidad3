#1
p= 'thirty'
space= ' '
q='days'
r='of'
s='python'
full_word= p + space + q + space + r + space  + s
print(full_word)
#2
pro= 'programacion'
pa= 'para' 
t= 'todos' 
full_word2= pro + space + pa + space + t
#3
empresa= 'programacion para todos'
print(empresa)
#4
print(len(empresa))
#5
print(empresa)
#6
print(empresa.upper())
#7
x='PROGRAMACION PARA TODOS'
print(x.lower())
#8
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
#9
cut= empresa[0:6]
print(cut)
#10
print(empresa.index('programacion'))
#11
empresa2 = empresa.replace('programacion', 'Python')
print(empresa2)
#12
empresa3 = empresa2.replace('todos', 'cualquiera')
print(empresa3)
#13
sp = empresa.split(' ')
print(sp)
#14
redes="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(redes.split(','))
#15,16,17
letra1=empresa[0]
letra10=empresa[10]
letralast=empresa[-1]
print(letra1 , letra10, letralast)
#18
acronym = ''.join(word[0].upper() for word in empresa2.split())
print(acronym)
#19
acronym2 = ''.join(word[0].upper() for word in empresa.split())
print(acronym2)
#20
print(empresa.index('p'))
#21
print(empresa.index('a'))
#22
palabra2 = "Coding For All People"
print(palabra2.rindex('l'))
oracion='You cannot end a sentence with because because because is a conjunction'
print(oracion.index('b'))
#23
parrafo = "You cannot end a sentence with because because because is a conjunction"
inicio = parrafo.index("because")
final = parrafo.rindex("because")
print(inicio, " ", final)
print(parrafo[inicio:final+7])
#24
if (empresa.rindex("empresa") == len(empresa)):
    print("YES")
else:
    print("NO")
#25
word3 = "   Coding For All      "
print("|",word3.strip(" "),"|")
#26-31
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())
#32
librarias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lista = ""
for i in librarias:
    lista =lista + " " + i
print(lista)
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\tAge\tCountry\tCity")
print("Dante\t18\tMexico\tAguascalientes")