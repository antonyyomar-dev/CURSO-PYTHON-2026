# Definción de variables

num1  = 10
texto = 'Python fundamentals'
num2 = 10.24
sensor = True

# Función PRINT()

print(texto)
print(2026)
print()
print("Hola mundo")
print(True)
print() # En este caso solo imprime un espacio en blanco


# Operadores matemáticos
numero1 = 300
numero2 = 125

potencia = 3**3 # Potencia (**)
modulo = 33%5
division_entera = numero1 // numero2
divisionDecimal = numero1 / numero2 
multiplicacion = 10 * 7
suma = 4000 + 5000
resta = 1000 - 580


print("RESULTADO DE LAS OPERACIONES")
print()
print("POTENCIA: ", potencia)
print("MODULO  : ", modulo)
print("DIVISION ENTERA : ", division_entera)
print("DIVISIÓN DECIMAL: ", divisionDecimal)
print("MULTIPLICACIÓN: ", multiplicacion)
print("SUMA: ", suma)
print("REST: ", resta)
print()

# Función imput()
nombre = input("Ingrese su nombre: ").title()
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura: "))

print("Hola soy ", nombre, " Tengo ", edad, " años  y mi estatura es: ",
      altura)

# ejemplo de ingreso de datos con imput()

texto1 = str(input("Ingrese un texto cualquiera: "))
print(texto1)

cantidad_de_personas = int(input("Ingrese la cantidad de personas: "))
print(cantidad_de_personas)

peso = float(input("Ingrese el peso de un producto: "))
print(peso)


while True:
    try:
        cantidad_de_personas = int(input("Ingrese la cantidad de personas: "))
        if cantidad_de_personas > 0:
            break
        else:
            print("Error en el ingreso de datos")
    except ValueError:
        print("El valor debe ser un entero")
        
     
print(cantidad_de_personas)






























