print("escolha uma unidade: \n")
print("1) ºC    2) ºF\n")
opcao = int(input(""))
temperatura = int(input("digite a temperatura: "))
match opcao:
    case 1: 
        fahrenheit = 5/9*temperatura-32
        print(f'temperatura de celcios para fahrenheit = {fahrenheit}')

    case 2: 
        celcius = 5/9*(temperatura+32)
        print(f"temperatura de fahrenheit para celcius = {celcius}")
