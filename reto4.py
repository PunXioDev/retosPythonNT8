#Escriba un programa que pida el ancho y largo de un rectángulo y permita calcular:

#- Área
#- Perímetro
#- Graficar el rectángulo

#Ejemplo: Ancho=5 Altura=3
#*****
#*****
#*****

ancho=int(input('Ingrese el ancho del rectangulo: '))
largo=int(input('Ingrese el largo del rectangulo: '))
p=''

calcularArea = lambda largo, ancho: largo*ancho
resultadoArea=calcularArea(ancho,largo)

def calcularPerimetro(largo,ancho):
    return 2*(largo+ancho)

resultadoPerimetro=calcularPerimetro(ancho,largo)

for i in range(ancho):
    p = p + '*'


print(f'El area del rectangulo es: {resultadoArea}')
print(f'El perimetro del rectangulo es: {resultadoPerimetro}')
print('Dibujo del Rectangulo \n')
for i in range(largo):
    print(p)

