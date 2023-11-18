import os
os.system ("cls")

biblioteca = {}
gastos=[]

####    Função para adicionar livros    ####
def adicionar(q):
    for i in range (q):
        #Coleta dados dos livros e alimenta em um dicionário
        titulo = input (f"Digite o título do livro: ").upper()
        autor = input (f"Digite o autor: "). upper()
        categoria = input (f"Digite a categoria: ").upper()
        valor = input (f"Digite o valor pago: ")
        biblioteca[i] = titulo, autor, categoria, valor
    arquivo = open ("CRUD.txt", "a", encoding='utf-8')  #O parâmetro <a> permite que sejam inseridos dados sem apagar os anteriores

    #O trecho a seguir salva os dados coletados na etapa anterior no arquivo CRUD.txt
    for i in range (q):
        arquivo.write (f"{', '.join(biblioteca[i])}\n")
    arquivo.close()

####    Função para consultar livros    ###
def consultar():
    categoria = input("Digite a categoria que você deseja visualizar: ").upper()
    return categoria


####    Função para alterar livros      ####




####    Função para excluir livros      ####
def excluir ():
    arquivo = open ("CRUD.txt", "r+", encoding = "utf8")
    #Armazena na variável <tituloe> o nome do título a ser excluído
    tituloe = input ("Digite o título que deseja excluir: ").upper()
    excluido = "N"
    #Armazena no vetor <texto> as linhas do arquivo TXT
    texto = arquivo.readlines()
    livro = ""
    for i in range (len(texto)-1):
        for j in range (0, texto[i].find(",")):
            #Armazena na variável <livro> apenas o título do livro na linha i
            livro = livro + texto[i][j]
        #Se o título que quer excluir for igual ao da variável <livro>, apaga do vetor <texto> (índice i) e reescreve o arquivo sem ele    
        #Se não for igual, esvazia a string <livro> e continua o loop para o próximo título
        if tituloe == livro:
            print (texto[i].find(","))
            del texto[i]
            arquivo = open ("CRUD.txt", "w", encoding = "utf8")
            for i in range (len(texto)):
                arquivo.write (f"{texto[i]}")
            excluido = "S"
            print ("Livro excluído com sucesso!")
        else:
            livro = ""
            continue
    if excluido == "N":
        print ("Livro não encontrado")


    arquivo.close()
    
    





####    Função para calcular o total de dinheiro gasto  ####
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



elif opcao == 4:
    print (gastos_totais(gastos))

elif opcao == 5:
    excluir()
    

    