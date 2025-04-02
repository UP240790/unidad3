#day 1,2,3

Age = int(20)
Height = float(1.73) 
Age = complex (10+10)

#Excercise 4

Base = int(input('Base: '))
height = int(input('height: '))
Area = int(0.5 * Base * height)
print('Area of a triangle:',' Area')

#Excercise 5

lado1, lado2, lado3, = int(input('lado1')), int(input('lado2')), int(input('lado3'))
perimetro=int(lado1 + lado2 + lado3)
print('el perimetro es: ',perimetro)

#Excercise 6

longitud=int(input('ingrese longitud'))
ancho=int(input('ingrese ancho'))
area=int(longitud*ancho)
perimetro=int(2*area)
print('el area es: ',area)
print('el perimetro es: ',perimetro)

#Excercise 7

radio=int(input('ingrese el radio'))
pi=3.14
area=float(pi*radio*radio)
circunferencia=float(2*pi*radio)
print('el area es: ',area)
print('la circunferencia es: ', circunferencia)

#Excercise 8

x1 = int(input("ingresar x1"))
x2 = int(input("ingresar x3"))
y1 =complex(2*x1-2)
y2 =complex(2*x2-2)
p = (y2-y1/x2-x1)
print("la pendiente es: ", p )


#03_DayExcercise 9

x1 = 2
x2 = 6
y1 = 2
y2 = 10
p = (y2-y1/x2-x1)
print('la pendiente es:' , p)


#03_DayExcersice10
x1 = int(input("ingresar x1"))
x2 = int(input("ingresar x2"))
y1 =(2*x1-2)
y2 =(2*x2-2)
p1 = (y2-y1/x2-x1)
print("la pendiente es: ", p1 )



z1 = 2
z2 = 6
y1 = 2
y2 = 10
p2 = (y2-y1/z2-z1)
print('la pendiente es:' , p2)


print(p1 > p2)    
print(p1 >= p2)    
print(p1 < p2)     
print(p1 < p2)    
print(p1 <= p2)    
print(p1 == p2)    
print(p1 != p2)

#03_DayExcersice11,py

x = 2
y = (x^2 + 6*x + 9)

print(y == 0)    

x1 = 2
y = (x1^2 + 6*x + 9)



#Excersise 12

print(len('python') == len('dragon'))
print(len('python') != len('dragon'))
print(len('python') < len('dragon'))
print(len('python') > len('dragon'))
print(len('python') >= len('dragon'))
print(len('python') <= len('dragon'))


#Excersise 13
#boolean
#True, False

python = 'python'
dragon = 'dragon'
print("on" in python and "on" in dragon)


#Excersise 14
Frase= 'I hope this course is not full of jargon'
print(Frase)
print("jargon" in Frase)


#Excersise 15

print("no" in 'python' and "no" in 'dragon')


#Excersise 16

len('python')
print(float(len('python')))
print(str(len('python')))


#Excersise 17
#Boolean

Valor_1 = (input('Enter a number: ')) 
Remainder = float(Valor_1) % 2
if Remainder == 0:
    print('el valor es par:', Remainder)
else:
    print('el valor es impar:', Remainder)


    #Excersise 18
#Boolean

Valor1 = (7)
Divisor = float(Valor1) / 3
if Divisor == int(2.7):
    print('True')
else:
    print('False')


#Excersise 19

if type(10) == '10':
    print('True')
else:
    print('False')


#Excersise 20

if int('9.8') == 10:
    print('True')
else:
    print('False')

    #Excersise 21

Horaschambeadas= int(input('Horas trabajadas: '))
Pago= int(input('Pago por hora: '))
Salario= int(Horaschambeadas * Pago)
print('Salario:', Salario)


#Excersise 22

Years= int(input('Enter a number: '))
Valor_1= str(Years*365*24*60*60)
print('los segundos que has vivido son: ', Valor_1)


#Excersise 23

for i in range(1, 6):
   print ( i, 1, i**2, i**3)



