print('Hola mundo')             # La primera palabra reservada es print que significa imprimir


nombre = "Jhoel"
my_var1int = 21
estatura = 1.75
estudiante = True

print(type(nombre))
print(type(my_var1int))
print(type(estatura))
print(type(estudiante))

print('Hola mi nombre es:', nombre, 'Tengo', my_var1int,'años de edad.', 'Mido', estatura, 'Es estudiante de Desarrollo de Software?:', estudiante)

print(f'Hola mi nombre es: {nombre} Tengo {my_var1int} años de edad. Mido {estatura} Es estudiante de Desarrollo de Software?: {estudiante}')
      

# IMC = peso/altura maxima^2

peso = 64
altura = 1.70

imc = peso / (altura**2)

print(f"Tu IMC es:", imc)

print("Listas")

my_list = ["Alejandro", 'Castellano', 21, 1.70, 64, 'Estudiante']
print(my_list)

# my_list.append     ---: Para agregar elementos
# my_list.insert     ---: El insert se usa para agregar elementos en la posicion en que nosotros queramos
# my_list[1]         ---: Se utiliza para cambiar o actualizar una variable
# my_list.remove     ---: Elimina el primer valor que encuentra primero por ejemplo si tenemos 2 veces el 22 solo elimina el primero
#                    ---: El remove se usa para eliminar elementos que conocemos que estan dentro de nuestra lista
# del my_list[1]     ---: Se usa del para eliminar una variable por indice
# my_list.clear      ---: Este se usa para eliminar todos los elemntos que estan dentro de nuestra lista
# my_list.reverse    ---: Para darle la vuelta a la lista que tenemos
# my_list.sort       ---: Sirve para ordanar la lista en su defecto ya sea en orden numerico u alfabetico
# print(len(my_list))---: Para saber cuantos elementos tenemos en nuestra lista


print("Diccionario")

my_dict = {
    'Nombre': 'Alejandro',
    'Apellido': 'Castellano',
    'Edad': 21,
    'Altura': 1.70,
    'Peso': 64
}

print(len(my_dict))

# print(my_dict["Nombre"]) Para acceder a un elemento

print(my_dict)

print('Hola mi nombre es',my_dict['Nombre'], 'Tengo', my_dict['Edad'],'años de edad.','Mido', my_dict['Altura'], 'Y mi peso es:', my_dict['Peso'])


# IMC = peso/altura maxima^2

peso = 90

altura = 1.70

imc = peso / (altura**2)

print(f"Tu IMC es:", imc)

if imc >= 18.5 and imc <= 24.9:
    print('NORMAL')

if imc >= 25 and imc <= 29.9:
    print('INTERMEDIO')

if imc >= 30 and imc <= 34:
    print('ANORMAL')
