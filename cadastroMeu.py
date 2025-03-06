def cadastrar_pessoas():
    while True:
        print('Vagas de Trabalho, digite o seus dados')
        nome = input('Digite o seu nome:')
        idade = int(input('Digite a sua idade:'))
        sexo = input('Digite o seu sexo:')
        natural = input('Digite a sua nacionalidade:')
        confirm = input('Os dados estão corretos? Digite ok para confirmar ')
        if confirm.lower() == 'ok':
            print('Cadastro realizado com sucesso!')
            break
        else:
            print('Falha no cadastro, tente novamente!')
cadastrar_pessoas()

    
