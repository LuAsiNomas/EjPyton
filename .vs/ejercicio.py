def actividad1():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for x in meses:
        print(x)



def actividad2():
    valores = [True, 5, False, "hola", "adios", 2]

    if len(valores[3]) > len(valores[4]):
        print("hola es mayor que adios")
    else:
        print("adios es mayor que hola")

    print(valores[1] + valores[5])
    print(valores[1] - valores[5])
    print(valores[1] / valores[5])
    print(valores[1] * valores[5])
    print(valores[5] - valores[1])
    print(valores[5] / valores[1])

    print(valores[0] and valores[2])
    print(valores[2] or valores[0])


def ejercicio1():

    n1 = int(input("Ingrese un número entero"))
    n2 = int(input("Ingrese otro número entero"))

    resultadosum = n1 + n2

    print("El resultado de la suma es: ", resultadosum)



def ejercicio2():

    n1 = int(input("Ingrese el primer número entero"))
    n2 = int(input("Ingrese el segundo número entero"))
    n3 = int(input("Ingrese tercer número entero"))
    n4 = int(input("Ingrese cuarto número entero"))

    suma = n1 + n2 + n3 + n4

    print("El resultado de la suma es: ", suma)


def ejercicio3():

    lado1 = int(input("ingrese la medida en cm de un lado: "))
    lado2 = int(input("Ingrese la medida de otro lado:"))

    superficie = (lado1 + lado2) * 2

    if lado1 == lado2:
        print("el cuadrado tiene una superficie de: ", superficie)
    else:
        print("La superficie del rectangulo es: ", superficie)




def ejercicio4():

    lado = float(input("Ingrese su número decimal del cuadrado:"))

    supercuadrado = lado * 4

    print("La superficie del cuadrado es", supercuadrado)



def ejercicio5():

    hora = int(input("Ingrese la hora: "))
    minuto = int(input("Ingrese el minuto: "))
    segundo = int(input("Ingrese los segundos: "))

    resul = hora * 3600 + minuto * 60 + segundo
    print("La hora ingresada es: ", resul)


def ejercicio6():

    base = int(input("Ingrese la base del triángulo: "))
    altura = int(input("Ingrese la altura del triángulo"))

    base2 = (base / 2) ** 2
    altura2 = altura ** 2
    auX = base2 + altura2
    hipo = auX ** 0.5
    supertri = (hipo * 2) + base

    print("La superficie del triángulo es: ", supertri)


def ejercicio7():

    n1 = int(input("Ingrese el primer número entero"))
    n2 = int(input("Ingrese el segundo número entero"))
    n3 = int(input("Ingrese el tercer número entero"))
    n4 = int(input("Ingrese el cuarto número entero"))
    n5 = int(input("Ingrese el quinto número entero"))
    n6 = int(input("Ingrese el sexto número entero"))
    n7 = int(input("Ingrese el séptimo número entero"))

    aUx = n1 + n2 + n3 + n4 + n5 + n6 + n7
    promedio = aUx / 7

    print("El promedio de los 7 numeros es: ", promedio)


def ejercicio8():

    total = int(input("Inserte el número entero: "))
    parte = int(input("Escriba una fracción del número total: "))
    Aux = parte / total
    fracción = Aux * 100

    if parte>total:
        print("El número menor que introdujo es mayor al número total")
    else:
        print(parte, " Es ", fracción, "% de ", total)


def ejercicio9():

    fecha = input("Ingrese la fecha usando 2 digitos pada dia y mes, y 4 para el año (DDMMAAA).")
    dia = fecha [0]+ fecha [1]
    mes = fecha [2]+ fecha [3]
    año = fecha [4]+ fecha [5]+ fecha [6]+ fecha [7]

    if len(fecha) > 8:
        print("El valor ingresado es incorrecto")
    else:
        print("Usted ingresó el día", dia, "mes", mes, "del año", año)


def ejercicio10():

    examenes = int(input("Nota de los examenes: ")) * 0.3
    tps = int(input("Nota de los trabajos prácticos: ")) * 0.2
    examenint = int(input("Nota del examen integrador: ")) * 0.5
    total = examenes + examenint + tps

    print("La nota total es: ", total)



def ejercicio11():

    autos = []
    inputUser = ""
    while inputUser != "SALIR":
        inputUser = input("ingrese el valor del auto vendido o SALIR")
        if inputUser != "SALIR":
            inputUser = float(inputUser)
            autos.append(inputUser)

    AUx = sum(autos)
    comision = AUx * 0.05
    salario = len(autos) * 200
    cobrar = 5500 + salario + comision

    print("el salario es de ", cobrar, " pesos.")

ejercicio11()