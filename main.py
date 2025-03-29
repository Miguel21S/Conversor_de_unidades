from conversor_unidades import Longitud, Temperatura, Peso, Velocidade

opcao = """ 
Tipos de conversão
Escolha a unidade a converter
    1º Longitude
    2º Temperatura
    3º Peso
    4º Velocidade
    0 Sair
"""

longitude = """ 
    1º Metro a Kilometro
    2º Kilometros a Millas
    3º Millas a Metros
    0 sair
"""
temperatura = """ 
    1º Celsius a Fahrenheit
    2º Fahrenheit a Celsius
    3º Celsius a Kelvein
    0 sair
"""
peso = """ 
    1º Kilogramo a Libra
    2º Libra a Kilogramo
    3º Gramo a Kilogramo
    4º Calcular kilogramo material (cartón)
    0 sair
"""
velocidade = """ 
    1º kilometro/h a Metro/s
    2º Metro/s a kilometro/h
    3º kilometro/h a Millas/h
    0 sair
"""

while True:
    print(opcao)
    op = int(input("Digite a opção: "))

    if op == 1:
        
        while True:
            print(longitude)
            op_long = int(input("Digite a opção: "))
            
            if op_long == 1:
                metro = int(input("Digite o valor do metro: "))
                print(Longitud.metro_a_kilometro(metro),"\n")

            elif op_long == 2:
                kilometro = int(input("Digite o valor do kilometros: "))
                print(Longitud.kilometros_a_millas(kilometro),"\n")


            elif op_long == 3:
                millas = int(input("Digite o valor do millas: "))
                print(Longitud.millas_a_metros(millas),"\n")
            
            elif 3 < op_long or op_long < 0:
                print("Digite uma opção valida ou um número positivo")
            elif op_long == 0:
                break
                
    elif op == 2:
        while True:
            print(temperatura)
            op_temp = int(input("Digite a opção: "))
            if op_temp == 1:
                celsius = int(input("Digite o valor do celsius: "))
                print(Temperatura.celsius_a_fahrenheit(celsius),"\n")

            elif op_temp == 2:
                fahrenheit = int(input("Digite o valor do fahrenheit: "))
                print(Temperatura.fahrenheit_a_celsius(fahrenheit),"\n")

            elif op_temp == 3:
                celsius = int(input("Digite o valor do celsius: "))
                print(Temperatura.celsius_a_kelvin(celsius),"\n")
                
            elif 3 < op_temp or op_temp < 0:
                print("Digite uma opção valida ou um número positivo")
            elif op_temp == 0:
                break
            
    elif op == 3:
        while True:
            print(peso)
            op_peso = int(input("Digite a opção: "))

            if op_peso == 1:
                kg = int(input("Digite o valor do kg: "))
                print(Peso.kg_a_libras(kg),"\n")
                
            elif op_peso == 2:
                libra = int(input("Digite o valor do libra: "))
                print(Peso.libras_a_kg(libra),"\n")
                
            elif op_peso == 3:
                gramos = int(input("Digite o valor do gramos: "))
                print(Peso.libras_a_kg(gramos),"\n")
                
            elif op_peso == 4:
                altura = int(input("Digite o valor do altura: "))
                comprimento = int(input("Digite o valor do comprimento: "))
                longitude = int(input("Digite o valor do longitude: "))
                print(Peso.kilogramo(altura, comprimento, longitude),"\n")
                
            elif 4 < op_peso or op_peso < 0:
                print("Digite uma opção valida ou um número positivo")
            elif op_peso == 0:
                break
            
    elif op == 4:
        while True:
            print(velocidade)
            op_veloc = int(input("Digite a opção: "))

            if op_veloc == 1:
                kmh = int(input("Digite o valor do kmh: "))
                print(Velocidade.kmh_a_ms(kmh),"\n")
                
            elif op_veloc == 2:
                ms = int(input("Digite o valor do libra: "))
                print(Velocidade.ms_a_kmh(ms),"\n")
                
            elif op_veloc == 3:
                kmh = int(input("Digite o valor do gramos: "))
                print(Velocidade.kmh_a_mph(kmh),"\n")
                
            elif 3 < op_veloc or op_veloc < 0:
                print("Digite uma opção valida ou um número positivo")
            elif op_veloc == 0:
                break

    elif 4 < op or op < 0:
        print("Digite uma opção valida ou um número positivo")
    elif op == 0:
        break
