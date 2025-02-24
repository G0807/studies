def cadastrar_pessoas():
    print('Vagas de Trabalho, digite o seus dados')
    nome = input('Digite o seu nome:')
    idade = int(input('Digite a sua idade:'))
    sexo = input('Digite o seu sexo:')
    natural = input('Digite a sua nacionalidade:')

    return nome, idade, sexo, natural

def confirmar_dados(nome, idade, sexo, natural):
    confirm = input(f'Os dados estão corretos? Nome: {nome},Idade: {idade}, Sexo: {sexo}, Nacionalidade: {natural}(Digite "ok" para confirmar):')

    if confirm.lower() == 'ok':
        print('Cadastro realizado com sucesso!')

        return True
    else:
        print('Falha no cadastro, tente novamente!')
        
        return False
    
def main():
    while True:
        nome, idade, sexo, natural = cadastrar_pessoas()
        cadastrar_pessoas()
        
        if confirmar_dados(nome, idade, sexo, natural):
          break

main()
        