import tkinter as tk 

# 1 
# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def par_impar():
    n1 = int(input('Digite um numero'))
    n2 = int(input('Digite um numero'))
    if n1 % 2 == 0:
        print('n1 é par')
    else:
        print('n1 é impar')


# 2
# CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
        
def multiplicacao_tripla():
    n1 = int(input('>>'))
    n2 = int(input('>>'))
    n3 = int(input('>>'))

    mult = n1 * n2 * n3
    print(mult)

# multiplicacao_tripla()

# 3
# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.


# 4
# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 20 ANOS
    


def paisagem():
    idade = int(input('digite sua iade: '))
    if idade == 20:
        print('Voce tem 20 anos!')
        # root = tk.Tk()
        # root.title('MENSAGEM ')
        # tk.Label(root, text='Voce tem 20 anos')
        # root.mainloop()


# 5
# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA. SE PODE ENTRAR NUM SHOW PARA MAIORES DE 16 ANOS.  

def show():
    idade = int(input('Digite sua idade> '))
    if idade >= 16:
        print('Ta liberado ')
    elif idade < 16:
        print('Não pode entrar')

# 6
# DESENVOLVA UMA FUNÇÃO PARA VER QUAIS ANOS O FUTEBOL MASCULINO BRASILEIRO GANHOU AS OLIMPIADAS

titulos = [1996, 2016]

def analise_de_titulos():
    pergunta = input('Voce gpostaria de saber quais anos o Brasil ganhou as olimpidas? s/n')

    if pergunta == 's':
        print(f'O brasil ganhou nos seguintes anos: {titulos}')
    else:
        print('bLZ')

# 7 
# DESENVOLVA UM SISTEMA DE E-COMMERCE DE ELETRONICOS, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SSD, HD, NOTEBOOK ACER, FONE DE OUVIDO. CRIAR COM LISTAS OU DICIONÁRIOS.


def ecommerce():
    print('--------------------ECOMMERCE DE ELETRÔNICOS-------------------')
    pedido = input('Gostaria de comprar? s/n')
    carrinho = []
    while pedido == 's':
        produtos = {

            'SSD':125,
            'HD':70,
            'NOTE ACER': 1200,
            'FONE': 40

        }

        print(produtos)

        escolha = input('Escolha o seu produto: ')

        carrinho.append(produtos[escolha])
        print(carrinho)
        pedido = input('Algo mais? s/n')
    else:
        print(carrinho)
        resultado = sum(carrinho)
        print(resultado)


def pagamento():
    metodos = ['0 - pix', '1 - cc', '2 - cd']
    print(metodos)
    pagamento = int(input('Digite o método de pagamento: '))
    print(metodos[pagamento])


ecommerce()
pagamento()