def fatorial(numero=0, show=False):
    """
    Calcula o fatorial de um número.
    :param numero: Número cujo fatorial será calculado.
    :param show: (Opcional) Mostra o cálculo passo a passo se for True.
    :return: O fatorial de 'numero'.
    """
    resultado = 1

    if show:
        for i in range(1, numero + 1):
            resultado *= i
            print(f"{i}", end=" x " if i < numero else " = ")
        print(resultado)  # Exibe o resultado final após o cálculo
    else:
        for i in range(1, numero + 1):
            resultado *= i
    return resultado


# Solicitação de entrada do usuário
numero = int(input("Digite um número a ser fatorado: "))
show = input("Digite 'show' para ver a fatoração ou pressione Enter para ocultar: ").strip().lower() == 'show'

# Chamada da função com os argumentos fornecidos
print(f"O fatorial de {numero} é: {fatorial(numero, show)}")