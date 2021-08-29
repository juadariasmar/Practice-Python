#%%
"""
¿Qué es la programación orientada a objetos?
¿Que es la herencia en POO?
¿Qué un constructor?
¿Qué es un subprograma o funciones?
¿Qué es encapsulación?
¿Qué es una lista?
"""

class Persona():
    def __init__(self):
        self.cedula = 13765890
    def __mensaje(self):
        return "mensaje desde la clase Persona"
    def mensaje2(self):
        print("Este mensaje/metodo fue heredado")
    def getMensaje(self):
        return self.__mensaje()


class Obrero(Persona):
    def __init__(self):
        self.__especialista = 1

obrero_planta = Obrero()
obrero_planta.mensaje2()
print(obrero_planta.getMensaje())
# %%
class Animal:
    def ladrar(self):
        print("No sé que animal soy")

class Perro(Animal):
    def ladrar(self):
        print("Guau!")

class Gato(Animal):
    def ladrar(self):
        print("Miau!")

for animal in Perro(), Gato(), Animal():
    animal.ladrar()
# %%

"""
matrices
"""
import random
class matriz:
    def __init__(self, m, n, ini=0):
        self.m = m
        self.n = n
        self.mat = [] * (m)
        for i in range(m):
            a = [ini] * (n)
            self.mat.append(a)

    def construyeMatriz(self, r = 100):
        for i in range(0, self.m):
            for j in range(0, self.n):
                self.mat[i][j] = random.randint(1, r)

    def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre "):
        print("\n", mensaje)
        for i in range(0, self.m):
            for j in range(0, self.n):
                    print(self.mat[i][j], "\t", end="")
            print()
    
    def __str__(self, mensaje="Matriz sin nombre "):
        aux="\n"+mensaje+"\n"
        for i in range(0, self.m):
            for j in range(0, self.n):
                    aux=aux+str(self.mat[i][j])+"\t"
            aux=aux+"\n"
        return aux

    def shape(self):
        return (self.m,self.n)

    def __add__(self,b):

        if (self.shape()==b.shape()):

        #if (self.m == b.m and self.n ==b.n):  
            mat_result=matriz(self.m,self.n)

            for i in range(0, self.m):
                for j in range(0, self.n):
                    mat_result.mat[i][j] = self.mat[i][j]+b.mat[i][j]
            return mat_result
        else:
            return "Las dimensiones no coinciden."

    def suma(self,num):
        mat_result=matriz(self.m,self.n)

        for i in range(0, self.m):
            for j in range(0, self.n):
                mat_result.mat[i][j] = self.mat[i][j]+num
        return mat_result


    def __add__(self,b):

        if (self.shape()==b.shape()):

        #if (self.m == b.m and self.n ==b.n):  
            mat_result=matriz(self.m,self.n)

            for i in range(0, self.m):
                for j in range(0, self.n):
                    mat_result.mat[i][j] = self.mat[i][j]+b.mat[i][j]
            return mat_result
        else:
            return "Las dimensiones no coinciden."



mat=matriz(4,4)
mat.construyeMatriz()
mat1=matriz(2,4)
mat1.construyeMatriz()
print(mat)
print(mat1)

print(mat1.shape())


print(mat+mat1)
print(mat1.suma(5))

#%%
L=[]
L=[1,2,"nombre",1.4,[1,2]]


for i in L:
    print(i)

L.append(["1","2"])
print(L)
L.insert(2,3)
print(L)
L.clear()
print(L)
L=[0]
print(L)
L=[0]*5
print(L)
L[0]=4
for i in range(1,L[0]+1):
    L[i]=i
print(L)

copi_L=L[:]
print(copi_L)

copi_L[1]=5
print(copi_L)
print(L)

n="hola"

t=(1,2,4,"hola",(1,),[1,2,3])
print(t)
print(t[-1][1])
t[-1][1]=4
print(t)
#t[-2]="H"



# %%
import random
class vector:
    __nombre="Fredy"
    def __init__(self,n):
        self.n=n
        self.V=[0]*(n+1)
    
    def __str__(self):
        return "El vector es: "+str(self.V)
    
    
    def construyeVector(self,m,r):
        self.V[0]=m
        for i in range(1,m+1):
            self.V[i]=random.randint(1,r)
    
    def getNombre(self):
        print(self.__nombre)
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre
    
v=vector(4)
print(v.V)

v.getNombre()
v.setNombre("Jhon")
v.getNombre()

# %%

num1=5
num2=10
print(num1+num2)
str1="Hola"
str2=" soy Fredy"
print(str1+str2)
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)

# %%
matriz=[]
numero_filas=2
numero_columnas=3
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(3)
print(matriz)
# %%
