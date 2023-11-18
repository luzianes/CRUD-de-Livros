import os
os.system ("cls")

biblioteca = {}
gastos=[]

#Função para adicionar livros no arquivo CRUD.txt
def adicionar(q):
    for i in range (q):
        #Coleta dados dos livros e alimenta em um dicionário
        titulo = input (f"Digite o título do livro: ").capitalize()
        autor = input (f"Digite o autor: "). capitalize()
        categoria = input (f"Digite a categoria: ").capitalize()
        valor = input (f"Digite o valor pago: ").capitalize()
        biblioteca[i] = titulo, autor, categoria, valor
    arquivo = open ("CRUD.txt", "a", encoding='utf-8')  #O parâmetro <a> permite que sejam inseridos dados sem apagar os anteriores

    #O trecho a seguir salva os dados coletados na etapa anterior no arquivo CRUD.txt
    for i in range (q):
        arquivo.write (f"{', '.join(biblioteca[i])}\n")
    arquivo.close()

#Função para consultar livros
def consultar():
    categoria = input("Digite a categoria que você deseja visualizar: ").capitalize()
    return categoria



#Função para alterar livros




#Função para excluir livros
def excluir ():
    titulo = input("Digite o nome do livro a ser excluído: ")
    return titulo

    



#Função para calcular o total de dinheiro gasto
def gastos_totais(gastos):
    def isnum(i):
    #checa se o elemento i é um número
        try:
            float(i)
            return gastos.append(float(i))
        except ValueError:
            pass    
    arquivo = open ("CRUD.txt", "r", encoding='utf-8')
    arquivo_formatado=arquivo.read()
    arquivo_formatado=arquivo_formatado.split()
    for i in arquivo_formatado:
        isnum(i)
    arquivo.close()
    return (f"Foram gastos R$ {sum(gastos)} no total")


print (f"\n### CRUD DE LIVROS ###\n")

opcao = int(input ("Escolha a opção desejada: [1] Adicionar, [2] Consultar, [3] Alterar,[4] Gastos Totais [5] Excluir ou [6] Sair: "))
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



elif opcao == 4:
    print (gastos_totais(gastos))


#elif opcao == 5:

    #excluir () 

#elif opcao == 6:
    #Verifica a quantidade de livros cadastrados a partir da quantidade de linhas no arquivo TXT