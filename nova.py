import os

def km_para_metros():
    try:
        valor_km = float(input("Digite o valor em quilometros (km): "))
        valor_m = valor_km * 1000
        print(f"{valor_km} km equivalem a {valor_m} m\n")
    except ValueError:
        print("Por favor, digite um valor numérico válido.\n")

def horas_para_minutos():
    try:
        valor_h = float(input("Digite o valor em horas (h): "))
        valor_min = valor_h * 60
        print(f"{valor_h} h equivalem a {valor_min} min\n")
    except ValueError:
        print("Por favor, digite um valor numérico válido.\n")


def segundos_para_horas():
    try:
        valor_s = float(input("Digite o valor em segundos (s): "))
        valor_h = valor_s / 3600
        print(f"{valor_s} s equivalem a {valor_h} h\n")
    except ValueError:
        print("Por favor, digite um valor numérico válido.\n")

def kmh_para_ms():
    try:
        valor_kmh = float(input("Digite o valor em quilometros por hora (Km/h): "))
        valor_ms = valor_kmh * 1000 / 3600
        print(f"{valor_kmh} Km/h equivalem a {valor_ms} m/s\n")
    except ValueError:
        print("Por favor, digite um valor numérico válido.\n")

print("### Seja bem vindo à calculadora de Conversão de unidades de medida! ###")
while True:
    print("Escolha uma das opções abaixo:")
    print("1: Quilometros(km) para Metros(m)")
    print("2: Horas (h) para Minutos(min)")
    print("3: Segundos (s) para Horas (h)")
    print("4: Quilometros por hora (Km/h) para Metros Por Segundo (m/s)")
    print("0: Sair")

    opcao = input("Digite o número da sua opção: ")

    if opcao == "1":
        km_para_metros()
    elif opcao == "2":
        horas_para_minutos()
    elif opcao == "3":
        segundos_para_horas()
    elif opcao == "4":
        kmh_para_ms()
    elif opcao == "0":
        print("Saindo do programa. Até logo!")
        break
        os.system('cls')
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.\n")
        os.system('cls')
