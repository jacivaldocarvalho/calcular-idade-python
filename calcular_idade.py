def calcular_idade(ano_nascimento):
    ano_atual = 2022
    return ano_atual - ano_nascimento


def main():
    # Solicita o nome completo
    nome_completo = input("Digite seu nome completo: ")

    # Loop até obter um ano válido
    while True:
        pergunta_nascimento = ("Digite seu ano de nascimento (entre 1922 e 2021): ")
        ano_nascimento = input(pergunta_nascimento)
        # Verifica se a entrada é um número
        if ano_nascimento.isdigit():
            ano_nascimento = int(ano_nascimento)
            # Verifica se o ano está no intervalo correto
            if 1922 <= ano_nascimento <= 2021:
                print("Ano válido!\n")
                break
            else:
                print("Ano inválido!")
                print("Por favor, digite um ano entre 1922 e 2021.")
        else:
            print("Entrada inválida. Por favor, digite um número.")

    # Calcula a idade
    idade = calcular_idade(ano_nascimento)

    # Exibe o resultado
    print(f"{nome_completo}")
    print(f"você completou ou completará {idade} anos em 2022.")


if __name__ == "__main__":
    main()
