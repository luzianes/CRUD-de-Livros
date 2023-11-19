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
    categoria_consultada = input("digite a categoria de livros que que você deseja visualizar: ").upper()
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    for linha in arquivo:
            if categoria_consultada in linha:
                    print(linha.strip())
    arquivo.close()


####    Função para alterar livros      ####
def alterar():
    arquivo = open ("CRUD.txt", "r+", encoding = "utf8")
    #Armazena na variável <tituloa> o nome do título a ser alterado
    tituloa = input ("Digite o título que deseja alterar: ").upper()
    alterado = "N"
    #Armazena no vetor <texto> as linhas do arquivo TXT
    texto = arquivo.readlines()
    livro = ""
    vetor_alteracao=[]
    for i in range (len(texto)):
        for j in range (0, texto[i].find(",")):
            #Armazena na variável <livro> apenas o título do livro na linha i
            livro = livro + texto[i][j]
        #Se o título que quer alterar for igual ao da variável <livro>, reescreve o arquivo com ele alterado    
        #Se não for igual, esvazia a string <livro> e continua o loop para o próximo título
        if tituloa == livro:
            #Cria um novo vetor <novo_texto>, para não modificar o vetor texto original, que será utilizado posteriormente
            novo_texto=texto
            #Coloca a linha da obra a ser modificada em um vetor, para uma melhor manipulação
            vetor_alteracao=novo_texto[i].split(", ")
            #Pergunta que informação da obra deve ser alterada
            resposta_alteracao=int(input("Qual mudança você quer realizar? Digite [1] se você quiser alterar o título, [2] se você quiser alterar o autor, [3] se você quiser alterar a categoria, [4] se você quiser alterar o preço ou [5] para alterar tudo: "))
            
            #Apenas altera o título, através de seu índice no vetor
            if resposta_alteracao == 1:
                subst_titulo=input("Qual o novo título que você gostaria de atribuir à obra? ")
                vetor_alteracao[0] = subst_titulo.upper()

            #Apenas altera o autor, através de seu índice no vetor                    
            elif resposta_alteracao == 2:                
                subst_autor=input("Qual o nome do autor que você gostaria de atribuir à obra? ")
                vetor_alteracao[1] = subst_autor.upper()
            
            #Apenas altera a categoria, através de seu índice no vetor
            elif resposta_alteracao == 3:
                subst_categoria=input("Em qual categoria você deseja inserir à obra? ")
                vetor_alteracao[2] = subst_categoria.upper()

            #Apenas altera o preço, através de seu índice no vetor
            elif resposta_alteracao == 4:                
                subst_preco=input("Qual preço você gostaria de atribuir à obra? ")
                vetor_alteracao[3] = subst_preco.upper()+"\n"

            #Altera tudo, cada categoria através de seu índice no vetor, respectivamente
            elif resposta_alteracao == 5:
                subst_titulo=input("Qual o novo título que você gostaria de atribuir à obra? ")
                vetor_alteracao[0] = subst_titulo.upper()
                subst_autor=input("Qual o nome do autor que você gostaria de atribuir à obra? ")
                vetor_alteracao[1] = subst_autor.upper()
                subst_categoria=input("Em qual categoria você deseja inserir à obra? ")
                vetor_alteracao[2] = subst_categoria.upper()
                subst_preco=input("Qual preço você gostaria de atribuir à obra? ")
                vetor_alteracao[3] = subst_preco.upper()+"\n"

            #Deleta toda informação antiga da obra, afinal, ela já está gravada em um vetor, que pode ser livremente manipulado
            del texto[i]
            #Transforma a linha alterada de um vetor para uma string separada por vírgulas
            vetor_alteracao=", ".join(vetor_alteracao)
            #Insere no texto, na mesma posição da antiga informação da obra, a descrição atualizada
            texto.insert(i, vetor_alteracao)
            arquivo = open ("CRUD.txt", "w", encoding = "utf8")
            for i in range(len(texto)):
                #Escreve-se todas as linhas de novo (incluindo a modificada)
                arquivo.write (f"{texto[i]}")
            alterado = "S"
            print ("Livro alterado com sucesso!")
        else:
            livro = ""
            continue
    if alterado == "N":
        print ("Livro não encontrado")
    arquivo.close()


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


####    Função para manipular os favoritos  ####
def favoritos():
    #Abrir os dois TXT, o do arsenal de livros da biblioteca e dos favoritos
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    arquivo2 = open ("CRUD2.txt", "r+", encoding = 'utf-8')
    #Oferece as opções de adcionar, remover ou consultar os livros favoritados
    opcoes_favoritos=int(input("O que você deseja fazer com os favoritos? Digite [1] para adicionar livro aos favotitos ou [2] para remover um livro do favoritos ou [3] para consultá-lo: "))
    #Opção de adicionar livro da bilbioteca aos favoritos
    if opcoes_favoritos == 1:
        titulof=input("Digite o título do livro que você deseja adicionar como favorito: ").upper()
        favoritado = "N"
        #Armazena nos vetores <texto> e <texto2> as linhas dos arquivo TXTs
        texto = arquivo.readlines()
        texto2 = arquivo2.readlines()
        livro = ""
        #Procura o titulo digitado <titulof> no arsenal de livros
        for j in range (len(texto)):
            for k in range (0, texto[j].find(",")):
                #Armazena na variável <livro> apenas o título do livro na linha i
                livro = livro + texto[j][k]
                #Se o título <titulof> que quer adicionar for igual ao da variável <livro>, pega as informações da obra do CRUD, para adicionar aos favoritos (CRUD2)
                #Se não for igual, esvazia a string <livro> e continua o loop para o próximo título
            if titulof == livro:
                #Adiciona todas informações do livro no vetor dos favoritos
                texto2.append(texto[j])
                #Apaga todas informações do CRUD2 e reescreve com a obra adicionada
                arquivo2 = open ("CRUD2.txt", "w", encoding = "utf8")
                for l in range (len(texto2)):
                    arquivo2.write (f"{texto2[l]}")
                favoritado = "S"
                print ("Livro adicionado aos favoritos com sucesso!")
            else:
                livro = ""
                continue
            if favoritado == "N":
                print ("Livro não encontrado")
    #Opção de remover livro da bilbioteca nos favoritos
    elif opcoes_favoritos == 2:
        titulof=input("Digite o título do livro que você deseja remover dos favorito: ").upper()
        excluido_favoritos = "N"
        #Armazena no vetor <texto2> as linhas do arquivo TXT
        texto2 = arquivo2.readlines()
        livro = ""
        for i in range (len(texto2)):
            for j in range (0, texto2[i].find(",")):
                #Armazena na variável <livro> apenas o título do livro na linha i
                livro = livro + texto2[i][j]
                #Se o título que quer excluir for igual ao da variável <livro>, apaga do vetor <texto> (índice i) e reescreve o arquivo sem ele    
                #Se não for igual, esvazia a string <livro> e continua o loop para o próximo título
            if titulof == livro:
                del texto2[i]
                arquivo2 = open ("CRUD2.txt", "w", encoding = "utf8")
                for k in range (len(texto2)):
                    arquivo2.write (f"{texto2[k]}")
                excluido_favoritos = "S"
                print ("Livro excluído com sucesso!")
            else:
                livro = ""
                continue
            if excluido_favoritos == "N":
                print ("Livro não encontrado")
    
    #Opção de consultar os livros dos favoritos
    elif opcoes_favoritos == 3:
        arquivo2 = open ("CRUD2.txt", "r", encoding = "utf8")
        print()
        for linha in arquivo2:
            print(linha.strip())
    
    arquivo.close()
    arquivo2.close()

print (f"\n### CRUD DE LIVROS ###\n")

opcao = int(input ("Escolha a opção desejada: [1] Adicionar, [2] Consultar, [3] Alterar,[4] Gastos Totais [5] Excluir, [6] Favoritos ou [7] Sair: "))
if opcao == 1:
    quantidade = int(input ("Quantos livros deseja adicionar? "))
    adicionar(quantidade)

elif opcao == 2:
    consultar()

elif opcao == 3:
    alterar()

elif opcao == 4:
    print (gastos_totais(gastos))

elif opcao == 5:
    excluir()
    
elif opcao == 6:
    favoritos()
    
