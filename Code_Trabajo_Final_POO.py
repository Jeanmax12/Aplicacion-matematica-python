from typing import List 
import os 
import time 
from csv import writer 
import pandas as pd 
import matplotlib.pyplot as plt #libreria de graficos

def clear():
    time.sleep(0.5)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Pregunta:
    def __init__(self,pregunta,alternativas,respuesta):
        self.pregunta=pregunta
        self.alternativas=alternativas
        self.respuesta=respuesta
        
    def ver_Pregunta(pregunta):
        print("Pregunta: ",pregunta)

    def ver_Alternativas(alternativas):
        for a in alternativas:
            print(alternativas.index(a)+1,')',a)

class Niveles:
    def __init__(self, nivel, tema):
        self.nivel = nivel
        self.tema = tema

nivel1:List[Pregunta]=[  
    Pregunta("3+1",['4','3','5'],1),
    Pregunta("(5-3)+2",['3','2','4'],3),
    Pregunta("3-(12+1)",['-10','10','10.1'],1),
    Pregunta("5+210",['215','214','213'],1),
    Pregunta("9+0",['9','8','7'],1),
    Pregunta("5+3",['9','8','3'],2),
    Pregunta("2.3+4.1",['6.4','3.3','3'],1),
    Pregunta("2.1-5.9",['7.1','8','-3.8'],3),
    Pregunta("55.1+1.1",['54.0','56.2','54.1'],2),
    Pregunta("22.2-1.2",['23.4','21.1','21.0'],3)
    ]
nivel2:List[Pregunta]=[
    Pregunta("3*1",['4','3','5'],2), 
    Pregunta("5*3*3",['45','32','55'],1),
    Pregunta("3*5",['2','15','8'],2),
    Pregunta("4*3",['12','13','7'],1),
    Pregunta("42*10*1*0",['420','4200','0'],3),
    Pregunta("5*20",['100','50','25'],1),
    Pregunta("3*2.1*5.2",['30.2','31.76','32.76'],3),
    Pregunta("5*3*2",['30','15','6'],1),
    Pregunta("5.3*3.2",['15.96','16.96','17.69'],2),
    Pregunta("6.2*2.5",['2.48','2.45','2.4'],1)
    ]    
nivel3:List[Pregunta]=[
    Pregunta("3/1",['1.3','3.1','3'],3), 
    Pregunta("5/2",['2.5','3.2','3.5'],1),
    Pregunta("3/2",['1.3','1.4','1.5'],3),
    Pregunta("7/4",['3.75','3.25','1.75'],3),
    Pregunta("8/4",['4','2','8'],2),
    Pregunta("10/2",['5','12','3'],1),
    Pregunta("9/2",['4.5','4.4','4.7'],1),
    Pregunta("35/4",['6.75','8.75','5.75'],2),
    Pregunta("100/4",['23','24','25'],3),
    Pregunta("50/10",['5','10','40'],1)
    ]    
nivel4:List[Pregunta]=[ 
    Pregunta("2**3",['6','8','12'],2),
    Pregunta("9**2",['72','18','81'],3),
    Pregunta("6**2",['66','45','36'],3),
    Pregunta("4**3",['12','64','96'],2),
    Pregunta("2**7",['128','64','256'],1),
    Pregunta("12**2",['144','169','216'],1),
    Pregunta("3**4",['27','96','81'],3),
    Pregunta("8**2",['64','68','48'],1),
    Pregunta("5**3",['50','145','125'],3),
    Pregunta("6**3",['256','216','126'],2)
    ]  
nivel5:List[Pregunta]=[ 
    Pregunta("Si el radio es 5, cuanto es el area del Circulo(pi=3.14159)",['15.70795','14.71795','13.33453'],1),
    Pregunta("Si la base y la altura de un triangulo son 4 y 6 respectivamente, cuanto es su area",['10','24','12'],3),
    Pregunta("Si el largo de un rectangulo es 10 y su ancho 5, cuanto es su area",['50','15','25'],1),
    Pregunta("Si el lado de un cuadrado es igual a 3, cuanto es su area",['3','1','9'],3),
    Pregunta("Si el radio de un circulo es 4, cuanto sera su diametro",['6','8','2'],2),
    Pregunta("Los lados de un triangulo valen 3, 15, 12, cuanto sera su perimetro",['17','18','30'],3),
    Pregunta("El area de un cuadrado es 9, cuando medira su lado",['3','18','6'],1),
    Pregunta("El area de un rectangulo es 15, halle el largo si el ancho mide 3",['45','3','5'],3),
    Pregunta("El perimetro de un triangulo equilatero es 12, cuanto medira sus lados",['5','4','3'],2),
    Pregunta("Si la base mayor y menor de un trapecio son 10 y 4 respectivamente, y su altura es 5, cuanto sera su area ",['45','35','8'],2)
    ]    
nivel6:List[Pregunta]=[  
    Pregunta("En un triangulo rectangulo un cateto es 1 y la hipotenusa raiz de 2, cuanto es el valor del otro cateto ",['0','1','3'],2),
    Pregunta("En un triangulo rectangulo la hipotenusa es 2 raiz de 2 y un cateto es 2 , cuanto es el valor del otro cateto",['2','4','6'],1),
    Pregunta("En un triangulo rectangulo la hipotenusa es 5, un cateo es 3, cuanto es el valor del cateto faltante ",['8','3','4'],3), 
    Pregunta("En un triangulo rectangulo los catetos son 5 y 12, respectivamente, cuanto es el valor su hipotenusa ",['17','7','13'],3),
    Pregunta("En un triangulo rectangulo los catetos son 8 y 15, respectivamente, cuanto es el valor su hipotenusa ",['17','11','12'],1),
    Pregunta("En un triangulo rectangulo un cateto es 24 y la hipotenusa es 25, cuanto es el valor del cateto faltante ",['23','8','7'],3),
    Pregunta("En un triangulo rectangulo la hipotenusa es 29 y un cateto es 21, cuanto es el valor del otro cateto",['22','20','23'],2),
    Pregunta("En un triangulo rectangulo los catetos son 9 y 40, respectivamente, cuanto es el valor su hipotenusa ",['41','43','42'],1),
    Pregunta("En un triangulo rectangulo un cateto es 35 y la hipotenusa es 37, cuanto es el valor del cateto faltante",['11','12','13'],2),
    Pregunta("En un triangulo rectangulo los catetos son 13 y 84, respectivamente, cuanto es el valor su hipotenusa",['75','95','85'],3),
    ]
nivel7:List[Pregunta]=[ 
    Pregunta("Cuanto es el sen(0)",['1','0','1/3'],2),
    Pregunta("Cuanto es el cos(30)",['(raiz de 3)/2','1','1/2'],1),
    Pregunta("Cuanto es el tan(45)",['4','1/4','1'],3),
    Pregunta("Cuanto es el sen(60)",['1','1/2','(raiz de 3)/2'],3),
    Pregunta("Cuanto es el cos(90)",['0','1','infinito'],1),
    Pregunta("Cuanto es el tan(0)",['0','3','5'],1),
    Pregunta("Cuanto es el sen(30)",['0.3','1/2','4/3'],2),
    Pregunta("Cuanto es el cos(45)",['(raiz de 2)/2','1','5'],1),
    Pregunta("Cuanto es el tan(60)",['1/2','raiz de 3','1.3'],2),
    Pregunta("Cuanto es el sen(90)",['0','infinito','1'],3)
    ]  
nivel8:List[Pregunta]=[ 
    Pregunta("Cuanto es la derivada de sen(x)",['-sen(x)','cos(x)','sen(x)'],2),
    Pregunta("Cuanto es la derivada de cos(x)",['-sen(x','1','tan(x)'],1),
    Pregunta("Cuanto es la derivada de tan(x)",['csc(x)','0','sec al cuadrado de x'],3),
    Pregunta("Cuanto es la derivada de sec(x)",['sec al cuadrado de x','tan(x).sen(x)','tan(x).sec(x)'],3),
    Pregunta("Cuanto es la derivada de csc(x)",['-csc(x).cot(x)','tan al cuadrado de x','-sen al cuadrado de x'],1),
    Pregunta("Cuanto es la derivada de cot(x)",['-csc al cuadrado de x','-tan(x).cot(x)','infinito'],1),
    Pregunta("Cuanto es la derivada de sen(5x)",['5.cos(5x)','cos(5x)','5.sen(5x)'],1),
    Pregunta("Cuanto es la derivada de cos(6x)",['6.cos(6x)','-6.sen(6x)','-6.cos(6x)'],2),
    Pregunta("Cuanto es la derivada de sen(4x)",['4.cos(4x)','-4.cos(4x)','-sen(4x)'],1),
    Pregunta("Cuanto es la derivada de cos(x al cudrado)",['2x.cos(x al cuadrado)','-2x.cos(x)','-2x.sen(x al cuadrado)'],3),
    ]

niveles: List[Niveles] = [
    Niveles('Nivel 1', 'Sumas y Restas'),
    Niveles('Nivel 2', 'Multiplicacion'),
    Niveles('Nivel 3', 'Division'),
    Niveles('Nivel 4', 'Potencia'),
    Niveles('Nivel 5', 'Areas y perimetros'),
    Niveles('Nivel 6', 'Pitagoras y triangulos pitagoricos'),
    Niveles('Nivel 7', 'Razones trigonometricas de los angulos 0, 30, 45, 60 y 90 grados'),
    Niveles('Nivel 8', 'Derivadas'),
]
def apreciacion(n):
    if n<=10 and n>=0:
        if n==10:
            print("Eres muy bueno")
        elif n>=7:
            print("Casi")
        elif n>=5:
            print("Puedes hacerlo mejor")
        elif n<5:
            print("Aun puedes mejorar")

def Resultados(index, tema, correctas):
    print("Nivel ",index,": ",tema ," terminado")
    print("Respondiste:",correctas,"de 10 preguntas")
    apreciacion(correctas)


def Salir():
    print('Quieres con el siguiente nivel')
    print('1. Continuar\n2. Salir')
    res = 0
    while res == 0 or res > 2:
        res = int(input('Seleccione su respuesta: '))
    if (res == 2): 
        return True

    return False

def SalioNivel():
    print('Saliste del juego')

#Main
totalcorrectas=0
totalerrores=0
totalpuntos=0
for i in niveles:
   correctas = 0 
   maximo = 3 
   indexnivel = niveles.index(i)
   if indexnivel==0:
       niv = nivel1
   elif indexnivel==1: 
       niv = nivel2
   elif indexnivel==2: 
       niv = nivel3
   elif indexnivel==3: 
       niv = nivel4
   elif indexnivel==4: 
       niv = nivel5
   elif indexnivel==5: 
       niv = nivel6
   elif indexnivel==6: 
       niv = nivel7
   elif indexnivel==7: 
       niv = nivel8
   print("Empezemos")
   print(i.tema)
   for p in niv:
        print("")   
        respuesta = 0 
        Pregunta.ver_Pregunta(p.pregunta)
        Pregunta.ver_Alternativas(p.alternativas)
        while respuesta==0 or respuesta>maximo:
            respuesta=int(input("Ingrese una alternativa: "))
        if respuesta==p.respuesta:
            print("Correcto\n")
            correctas +=1
            totalcorrectas +=1
            totalpuntos +=100
            print('\n')
        else: 
            print("**Incorrecto**\n")
            totalerrores +=1
            print('\n')
        if niv.index(p)+1!=len(niv):
            print("---------------------------------")
            print("SIGUIENTE PREGUNTA")
            print("---------------------------------")
        clear()
   Resultados(indexnivel + 1, i.tema, correctas)
   time.sleep(1)
   print('\n')
   if niveles.index(i) + 1 < len(niveles):
       salir = Salir()
       if (salir):
            clear()
            SalioNivel()
            print("Total correctas: ",totalcorrectas)
            print("Total correctas: ",totalerrores)
            print("Total correctas: ",totalpuntos)
            time.sleep(2)
            clear()
            print("Los datos ingresados se encuentran en el csv ")
            break
       clear()

#hay un fallo si almaceno nuevos datos en el csv el comando para hacer la grafica ocasiona un conflicto.
#por esta razon es un adicional 

#sexo=int(input("Ingrese el sexo(0:Hombre/1: Mujer): "))
#nombre=input("Ingrese el nombre: ")
#edad=int(input("Ingrese la edad: "))
#Lista = [sexo,nombre,edad,totalerrores,totalcorrectas,indexnivel+1,totalpuntos]
#with open('Resultados.csv', 'a') as file: 
#    escribir = writer(file) 
#    escribir.writerow(Lista) 
#    file.close() 

#Grafica
df_Resultados = pd.read_csv('Resultados.csv')

fig, ax = plt.subplots()

df_Resultados.Errores.plot(kind = "hist", title = "Histograma de errores")
plt.show()

df_Resultados.Correctas.plot(kind = "hist", title = "Histograma de respuestas correctas")
plt.show()

df_Resultados.groupby(["Nivel", "Sexo"]).size().unstack().plot(kind = "bar", title = "Numero de alumnos en cada nivel regidos por sexo")
plt.show()

df_Resultados.Sexo.value_counts().plot(kind = "bar", title = "Cantidad de hombres y mujeres en un curso I")
plt.show()

df_Resultados.Sexo.value_counts().plot(kind = "pie", labels = ["Hombres", "Mujeres"], title = "Cantidad de hombres y mujeres en un curso II")
plt.show()
clear()

archivo = pd.read_csv("Resultados.csv")
print(archivo)


print('Primeras 10 filas:\n', archivo.head(10))
print('Ultimas 10 filas:\n', archivo.tail(10))


print("\n")
print("Obtuvieron mayor de 60 correctas(buen trabajo)")
print("       Buen Trabajo")
print(archivo["Correctas"]>40)
print("\n")

print("Obtubieron mas de 50 incorrectas")
print("       Mas de 50 errores")
print(archivo["Errores"]>50)
print("\n")

print("Porcentaje de personas en cada nivel")
print(archivo['Nivel'].value_counts(normalize=True) * 100)
print("\n")

print("Promedio de Puntos de las mujeres por cada nivel")
print(archivo.groupby(['Nivel','Sexo'])['Puntos'].mean().unstack()[1])
print("\n")

print("Promedio de Puntos de los hombres por cada nivel")
print(archivo.groupby(['Nivel','Sexo'])['Puntos'].mean().unstack()[0])
print("\n")

print("Personas que llegaron al nivel 8")
print("       Llego ")
print(archivo["Nivel"]==8)