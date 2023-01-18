# Ejercicio 5
numhoras=int(input("Digite su numero de horas trabajadas: "))
valhora=int(input("Digite el costo por hora trabajada: "))
resultado=numhoras*valhora
print(f'Su pago seria de: {resultado}')

#Ejercicio 6
nombre=(input("Digite su nombre: "))
print(f'Hola {nombre}')

#Ejercicio 7
peso=float(input("Digite su peso en Kilogramos: "))
estatura=float(input("Digite su estatura en centimetros: "))
imc=peso/estatura**2
print(f'Tu índice de masa corporal es: {imc}')

# Ejercicio 8
num1=float(input("Digite un numero: "))
num2=float(input("Digite un numero: "))
print(str(num1)+' entre '+ str(num2) + 'da un cociente '+ str(int(num1)/int(num2)) + ' y un residuo de '+ str(int(num1)%int(num2)))

# Ejercicio 9
cantinv=float(input("Digite la cantidad a invertir: "))
interes=float(input("Digite el interés anual: "))
anos=int(input("Digite el número de años: "))
capital=(cantinv*(interes / 100 + 1)**anos)
print(f"Capital final {capital}")

# Ejercicio 10
numpaya=int(input("Digite el número de payasos vendidos: "))
numnecas=int(input("Digite el número de munecas vendidas: "))
pesototal= (numpaya*112)+(numnecas*75)
print(f"El peso total del paquete a enviar es de: {pesototal}")

# Ejercicio 11
deposito= float(input("Digite el dinero depositado en la cuenta de ahorros "))
interes=0.04
ano1= deposito*(1+interes)
print("Balance tras el primer año:" + str(round(ano1, 2)))
ano2 = ano1 * (1+interes)
print("Balance tras el primer año:" + str(round(ano2, 2)))
ano3 = ano2 * (1+interes)
print("Balance tras el primer año:" + str(round(ano3, 2)))

# Ejercicio 12
panvend=int(input("Digite el número de barras vendidas que no son del día: "))
descuento=0.6
precio=3.49
calculo=panvend*precio*(1-descuento)
print("El precio de una barra fresca es: " + str(precio) + "Pesos")
print("El descuento del pan no fresco es:  " + str(descuento * 100) + "%")
print("El precio final a pagar es: " + str(round(precio, 2)) + "Pesos")