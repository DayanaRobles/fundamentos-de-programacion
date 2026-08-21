total=0
print("=======BIENVENIDO AL REGISTRO DEL MUSEO=======")
#Solicita el número de visitantes
num_visitantes=int(input("Ingrese el número total de visitantes: "))

#Registro con ciclo for para cada uno de los visitantes.

for v in range(1 , num_visitantes + 1):
    print(f"\n======== Hola, visitante {v} de {num_visitantes}!========\n Registro {v}:")

    # While para checar si es una edad posible
    while True:
        edad=int(input("Ingrese su edad: "))
        #si la edad es un número negativo no es válida
        if edad < 0:
             print("No es una edad existente.\nIntente de nuevo.")
             #Revisa la condición del while de nuevo
             continue
        #sino la edad es válida
        else:
            #Edad válida: rompe el ciclo y continua con el for.
            
             break
    #Aplicar descuentos, inicializar variable de descuento
    descuento = 0

    #condicionantes edades para precio base

    #Si tiene menos de 3 años el precio de boleto es $0
    if edad < 3:
        precioBoleto = 0
        print(" Menor de edad, su boleto es gratis ")

    #Si es menor de edad: su precio de boleto base es $30
    elif edad >= 3 and edad <= 17:
        precioBoleto = 30  

        #Puede tener descuento UNICAMENTE DE ESTUDIANTE, por la edad no puede ser profesor ni adulto mayor.
        tipo_visitante = int(input("¿Eres estudiante? (número)\n 1. Sí\n 2. No\n "))

        #Si es estudiante: el descuento es del 10% sobre precio base de $30
        if tipo_visitante==1:
         descuento = precioBoleto * 0.10
         print("Aplica descuento estudiante/profesor: 10%")
        else:
            descuento = 0
            print("No aplica descuento")
    #Si es mayor de edad edad >= 18: su precio base del boleto es $45
    else:
        precioBoleto = 45
        tipo_visitante = int(input("Elige una opción (número):\n 1. Estudiante\n 2. Profesor\n 3. AdultoMayor\n 4. Ninguno "))

        
        if tipo_visitante==3 and edad<60:
            print("Opción no válida, Mayores de edad a partir de los 60 años en México.")

        elif tipo_visitante == 3:
            descuento = precioBoleto * 0.12
            print("Aplica descuento adulto mayor: 12%")

        elif tipo_visitante == 1 or tipo_visitante == 2:
            descuento = precioBoleto * 0.10
            print("Aplica descuento estudiante/profesor: 10%")
        
        else: 
            descuento = 0
            print("No aplica descuento")
    #Operacion descuento
    precioBoleto = precioBoleto - descuento
    print(f"El precio del boleto final:{precioBoleto}")
    #Acumular el total de los boletos
    total += precioBoleto
    print(f"Precio acumulado: ${total} ")
    
print(f"El total por los {num_visitantes} visitantes, es de : ${total:.2f}")