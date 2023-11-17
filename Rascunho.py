import os
os.system ("cls")

biblioteca = {}

#Função para adicionar livros no arquivo CRUD.txt
def adicionar(q):
    for i in range (q):
        #Coleta dados dos livros e alimenta em um dicionário
        titulo = input (f"Digite o título do livro: ").capitalize()
        autor = input (f"Digite o autor: "). capitalize()
        categoria = input (f"Digite a categoria: ").capitalize()
        valor = input (f"Digite o valor pago: ").capitalize()
        biblioteca[i] = titulo, autor, categoria, valor
    arquivo = open ("CRUD.txt", "a")  #O parâmetro <a> permite que sejam inseridos dados sem apagar os anteriores

    #O trecho a seguir salva os dados coletados na etapa anterior no arquivo CRUD.txt
    for i in range (q):
        arquivo.write (f"{biblioteca[i]}\n")
    arquivo.close()

#Função para consultar livros
def consultar():
    categoria = input("Digite a categoria que você deseja visualizar: ")
    return categoria



#Função para alterar livros




#Função para excluir livros
def excluir ():
    titulo = input("Digite o nome do livro a ser excluído: ")
    return titulo

    



#Função para calcular o total de dinheiro gasto





print (f"\n### CRUD DE LIVROS ###\n")

opcao = int(input ("Escolha a opção desejada: [1] Adicionar, [2] Consultar, [3] Alterar, [4] Excluir ou [5] Sair: "))
if opcao == 1:
    quantidade = int(input ("Quantos livros deseja adicionar? "))
    adicionar(quantidade)

elif opcao == 2:
    categoria_consultada = consultar()
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    for linha in arquivo:
            if categoria_consultada in linha:
                    print(linha.strip())
    arquivo.close()




#elif opcao == 3:



#elif opcao == 4:

    #excluir () 

elif opcao == 5:
    livro_apagar = excluir()

    #Verifica a quantidade de livros cadastrados a partir da quantidade de linhas no arquivo TXT
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    total_livros = sum(1 for linha in arquivo)
    print(total_livros)
    arquivo.close() 


    #Imprime o conteúdo do arquivo TXT
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    print(arquivo.read())
    arquivo.close()

    #Imprime uma linha no arquivo
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    

    




else:
    print ("Opção inválida! Digite um número de 1 a 5.")
    





