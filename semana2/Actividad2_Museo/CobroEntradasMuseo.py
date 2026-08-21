#Constantes (precio base y porcentajes de Descuento)
costo_bebe=0
costo_menoresEdad=30
costo_mayoresEdad=45
desc_estudiante=0.10
desc_profesor=0.10
desc_adultomayor=0.12
#Inicio
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
             print("No es una edad existente.\n---Intente de nuevo---")
             #Revisa la condición del while de nuevo
             continue
        #sino la edad es válida
        else:
            #Edad válida: rompe el ciclo y continua con el for.
            
             break
    #Aplicar descuentos, inicializar variable de descuento
    monto_descuento = 0

    #condicionantes edades para precio base

    #Si tiene menos de 3 años el precio de boleto es $0
    if edad < 3:
        precioBoleto = costo_bebe
        print("Niño menor de 3 años.\nSu boleto es gratis. ")
        

    #Si es menor de edad: su precio de boleto base es $30
    elif edad >= 3 and edad <= 17:
        precioBoleto = costo_menoresEdad 
        
        #Puede tener descuento UNICAMENTE DE ESTUDIANTE, por la edad no puede ser profesor ni adulto mayor.
        tipo_visitante = int(input("¿Eres estudiante?\n 1. Sí\n 2. No\n Opción (número): "))

        #Si es estudiante: el descuento es del 10% sobre precio base de $30
        if tipo_visitante==1:
         monto_descuento = precioBoleto * desc_estudiante
         print("Aplica descuento estudiante.\nPorcentaje de descuento: 10%")
        else:
            monto_descuento = 0
            print("Menor de edad.\nNo es estudiante, no aplica descuento")
    #Si es mayor de edad edad >= 18: su precio base del boleto es $45
    else:
        precioBoleto = costo_mayoresEdad
       
        tipo_visitante = int(input("Elige una:\n 1. Estudiante\n 2. Profesor\n 3. AdultoMayor\n 4. Ninguno\n Opción (número): "))

        if tipo_visitante == 3 and edad < 60:
            print("Opción no válida, Adulto Mayor en México es a partir de los 60 años.")

        elif tipo_visitante == 3:
            monto_descuento = precioBoleto * desc_adultomayor
            print("Aplica descuento adulto mayor.\nPorcentaje de descuento: 12%")

        elif tipo_visitante == 1:
            monto_descuento = precioBoleto * desc_estudiante
            print("Aplica descuento estudiante.\nPorcentaje de descuento: 10%")

        elif  tipo_visitante == 2:
            monto_descuento = precioBoleto * desc_profesor
            print("Aplica descuento profesor.\nPorcentaje de descuento: 10%")
        
        else: 
            monto_descuento = 0
            print("Mayor de edad sin descuento")
    #Imprimir precio base:
    print(f"Precio de boleto base: ${precioBoleto:.2f}")
    #Operacion descuento
    preciocondescuento = precioBoleto - monto_descuento
    print(f"Monto de descuento: ${monto_descuento:.2f}")
    print(f"El precio del boleto final: ${preciocondescuento:.2f}")
    #Acumular el total de los boletos
    total += preciocondescuento
    print(f"===============================\nPrecio acumulado: ${total:.2f}\n=============================== ")
print(f"\n=======REGISTRO FINALIZADO======")
print(f"El total por los {num_visitantes} visitantes: ${total:.2f}")