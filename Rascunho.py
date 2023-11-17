import os
os.system ("cls")

biblioteca = {}

#Função para adicionar livros no arquivo CRUD.txt
def adicionar(q):
    for i in range (q):
        #Coleta dados dos livros e alimenta em um dicionário
        titulo = input (f"Digite o título do livro: ")
        autor = input (f"\nDigite o autor: ")
        categoria = input (f"\nDigite a categoria: ")
        valor = input (f"\nDigite o valor pago: ")
        biblioteca[i] = titulo, autor, categoria, valor
    arquivo = open ("CRUD.txt", "a")  #O parâmetro <a> permite que sejam inseridos dados sem apagar os anteriores

    #O trecho a seguir salva os dados coletados na etapa anterior no arquivo CRUD.txt
    for i in range (q):
        arquivo.write (f"{biblioteca[i]}\n")
    arquivo.close()


print (f"\n### CRUD DE LIVROS ###\n")

opcao = int(input ("Escolha a opção desejada: [1] Adicionar, [2] Consultar, [3] Alterar, [4] Excluir ou [5] Sair: "))
if opcao == 1:

    quantidade = int(input ("Quantos livros deseja adicionar? "))
    adicionar(quantidade)



#Função para consultar livros




#Função para alterar livros




#Função para excluir livros
def excluir 



#Função para calcular o total de dinheiro gasto

