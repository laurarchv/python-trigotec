# TRIGOTEC

import math

def graus_para_radianos(graus):
    return graus * (math.pi / 180)

def radianos_para_graus(radianos):
    return radianos * (180 / math.pi)

def main():
    while True:
        print("\nCalculadora de Círculo Trigonométrico")
        print("1. Converter Graus para Radianos")
        print("2. Converter Radianos para Graus")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            graus = float(input("Digite o ângulo em graus: "))
            radianos = graus_para_radianos(graus)
            print(f"{graus} graus é igual a {radianos:.6f} radianos.")
        elif escolha == '2':
            radianos = float(input("Digite o ângulo em radianos: "))
            graus = radianos_para_graus(radianos)
            print(f"{radianos} radianos é igual a {graus:.6f} graus.")
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()