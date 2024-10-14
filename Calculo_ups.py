# Licencia MIT
# 
# Copyright (c) 2024 Jorge Menéndez S.
# 
# Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para utilizar el
# Software sin restricción, incluyendo sin limitación los derechos para usar, copiar, modificar,
# fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y para permitir a
# las personas a quienes se les proporcione el Software que lo hagan, sujeto a las siguientes
# condiciones:
# 
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes
# sustanciales del Software.
# 
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO
# PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DEL COPYRIGHT SERÁN
# RESPONSABLES POR NINGUNA RECLAMACIÓN, DAÑO O OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE
# CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL
# USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.

def calcular_duracion_ups():
    print("CÁLCULO DE DURACIÓN DE UPS".center(40))
    print("=" * 40)
    
    try:
        capacidad_ups_va = float(input("Introduce la capacidad del UPS (en VA): "))
        factor_potencia = float(input("Introduce el factor de potencia (entre 0.6 y 0.9): "))
        consumo_aparato = float(input("Introduce el consumo del aparato eléctrico (en W): "))
        
        if capacidad_ups_va <= 0 or consumo_aparato <= 0 or not (0.6 <= factor_potencia <= 0.9):
            print("La capacidad del UPS, el consumo y el factor de potencia deben ser válidos.")
            return
        
        capacidad_ups_wh = capacidad_ups_va * factor_potencia
        duracion = capacidad_ups_wh / consumo_aparato
        print(f"\nEl aparato puede estar encendido durante aproximadamente {duracion:.2f} horas.")
    
    except ValueError:
        print("Por favor, introduce números válidos.")

# Llamada a la función para ejecutar el programa
calcular_duracion_ups()
