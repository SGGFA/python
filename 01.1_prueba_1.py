# intento calculadora
# input para poder introducir datos por teclado

tipo_operacion = input("Introduce el tipo de operación (+, -, *, /): ")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
resultado = float(0)

if tipo_operacion == "+":
    resultado = num1 + num2
elif tipo_operacion == "-":
    resultado = num1 - num2
elif tipo_operacion == "*":
    resultado = num1 * num2
else:
    resultado = num1 / num2

print("El resultado es: ",resultado)