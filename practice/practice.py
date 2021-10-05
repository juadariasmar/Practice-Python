print("Hola, bienvenido")
print("Por favor ingresa tus tres notas")

nota1 = input("Nota 1: ")
nota1 = int(nota1)

nota2 = input("Nota 2: ")
nota2 = int(nota2)

nota3 = input("Nota 3: ")
nota3 = int(nota3)

mediaNotas = ((nota1 + nota2 + nota3)/3)

while (mediaNotas < 5):
  print("Suspendido")
  break;

if (mediaNotas >= 5 and mediaNotas <= 8):
  print("Aprobado")
elif (mediaNotas > 8):
  print("Excelente")

#quiero ver si se puede hacer un commit de una rama a development y luego a master, ya despues de cerrado el pull request para