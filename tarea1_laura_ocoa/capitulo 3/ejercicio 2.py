try:
    # Solicitar al usuario el número de horas y la tarifa por hora
    horas = float(input("Introduzca el número de horas trabajadas: "))
    tarifa_por_hora = float(input("Introduzca la tarifa por hora: "))

    # Calcular el salario, considerando horas extras
    
   
if horas > 40:
        horas_extras = horas - 40

        salario = ( 40 * tarifa_por_hora) + (horas_extras * 1.5 * tarifa_por_hora)
    else:
        salario = horas * tarifa_por_hora

       
# Mostrar el salario
print("El salario total es:", salario)

except ValueError:
    
   
print("Error, por favor introduzca un número")
