#pos->  012345678
name = "Ana Maria "

print(f'{"="*10 } Cadenas {"="*10}' )

print("Accedienco a caracters de una cadena")
print(len(name))
print(name[0])
print(name[-1])
print(name[-2])
print(name[:3])
print(name[4:8])
print(name[::-1])
print()

print("Validacion y operaciones con cadenas")
print(name.index("a"))
print("p" in name)
print(name.upper())
print(name.lower())
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(name.startswith("a"))
print(name.endswith("Maria"))
print(name.strip().endswith("Maria"))
print(name.split())
print(name.split(' '))
print(name.strip().split(' '))
print(name.split('a'))
print(name.isnumeric())
print()

print("Validacion de si es un numero")
print("1234".isnumeric())
print("01234".isnumeric())
print("32 1234 4567".isnumeric())
print("32.32".isnumeric())
print("32 1234 4567".isdigit())
print("3".isdigit())
print("03".isdigit())
print("32.32".isdigit())
print("32 1234 4567".isalnum())
print("32.32".isalnum())
print()

print(f'{"="*10 } Listas {"="*10}' )

#pos->     0       1        2          3
names = ["Lis", "John", "Isabella", "Norman"]

print(len(names))
print(names[0])
print(names[-1])
print(names[-2])
print(names[:2])
print(names[1:3])
print(names[::-1])

print(names)
names.append("Yaneth")
print(names)

names.append("Danilo")
print(names)
names.remove("Danilo")
print(names)
names.pop()
print(names)
names.pop(0)
print(names)
print([name.upper() for name in names])
print([name for name in names if not "n" in name.lower()])

"""
names = ["John", "Isabella"]
print(names[0], names[1], sep='\n')
print(*names, sep='\n')
"""
n = 5
print("Matrix: referencia duplicada")
matrix = [[0]*n]*n
print(f"Matrix de {n}x{n}", *matrix, sep="\n")
matrix[0][0] = 1
print(f"Matrix de {n}x{n}", *matrix, sep="\n")

print("Matrix: sin referencia duplicada")
matrix = [[0]*n for _ in range(n)]
print(f"Matrix de {n}x{n}", *matrix, sep="\n")
matrix[0][0] = 1
print(f"Matrix de {n}x{n}", *matrix, sep="\n")
print("Desempaquetando una lista para crear una nueva")
print(*[*matrix, ['x']*n], sep="\n")
print()
print(*[['x']*n, *matrix], sep="\n")
print()
print(*(matrix + [['x']*n]), sep="\n")

age = 1
file_info = ["file.txt", 2000]
file_name, file_size = file_info

print(file_info[0], file_info[1])
print(file_name, file_size)
print()

print(f'{"="*10 } Tuplas {"="*10}' )

file_info = ('file.txt', 2000)
security_classes = ('LoginRequiredClass', 'PermissionRequiredClass')
user_classes = ('HomePageClass', 'SearchPageClass')
admin_classes = ('HomePageClass', 'SearchPageClass', 'UserPageClass',)

login_required_class, permission_required_class = security_classes
print(login_required_class, permission_required_class)
print(*security_classes)
print(list(security_classes))

print(file_info)
# file_info[0] = 'file.csv'

for security_class in security_classes:
    print(security_class) 


print()

print(f'{"="*10 } Diccionarios {"="*10}' )

person = {
    'name': 'Isabella',
    'age': 15
}

print(person['name'])
print(person)
person['salary'] = 5000000
print(person)
person['age'] = 20
print(person)
person['xyz'] = None
print(person)
del person['xyz']
print(person)

person = {**person, 'country': 'Colombia'}
print(person)

person.update({'age': 21, 'city': 'Medellin'})
print(person)

person = {**person, 'age': 22, 'job': 'Software Developer'}
print(person)
print()

print("Iterando diccionarios")
for key in person:
    print(key)

print(person.keys(), list(person.keys()))
print(person.values(), list(person.values()))
print()

print("Iterando diccionarios con clave, valor")
for feature, value in person.items():
    print(f'{feature}: {value}')


# Normalizacion de datos
# [] -> {}

students = [
    {'id': 1, 'name': 'Isabella', 'last_name': 'De la Barrera'},
    {'id': 2, 'name': 'Norman', 'last_name': 'Flores'},
    {'id': 3, 'name': 'Yaneth', 'last_name': 'De la Luz'},
    {'id': 4, 'name': 'Isabella', 'last_name': 'Restrepo'},
]

time_per_student = 1
total_time = 0
student_id = 3
awesome_student = None
for student in students:
    total_time += time_per_student
    
    if student['id'] == student_id:
        awesome_student = student
        break

print(f'total time is: {total_time}s')
print(f'Awesome student: {awesome_student}')
print()

students = {student['id']: student for student in students}
print(students)

total_time = 0
awesome_student = None
if student_id in students:
    total_time += time_per_student
    awesome_student = students[student_id]

print(f'total time is: {total_time}s')
print(f'Awesome student: {awesome_student}')
print()

import json
students = [
    {'id': 1, 'name': 'Isabella', 'last_name': 'De la Barrera'},
    {'id': 2, 'name': 'Norman', 'last_name': 'Flores'},
    {'id': 3, 'name': 'Yaneth', 'last_name': 'De la Luz'},
    {'id': 4, 'name': 'Isabella', 'last_name': 'Restrepo'},
]
print(json.dumps({student['name']: student for student in students}, indent=4))