import os
os.system ("cls")

biblioteca = {}
gastos=[]


####    Função para adicionar livros    ####
def adicionar(q):
    for i in range (q):
        #Coleta dados dos livros e alimenta em um dicionário
        titulo = input (f"\nDigite o título do livro: ").upper()
        autor = input (f"Digite o autor: "). upper()
        categoria = input (f"Digite a categoria: ").upper()
        valor = input (f"Digite o valor pago: ")
        biblioteca[i] = titulo, autor, categoria, valor
    arquivo = open ("CRUD.txt", "a", encoding='utf-8')  #O parâmetro <a> permite que sejam inseridos dados sem apagar os anteriores

    #O trecho a seguir salva os dados coletados na etapa anterior no arquivo CRUD.txt
    for i in range (q):
        arquivo.write (f"{', '.join(biblioteca[i])}\n")
    arquivo.close()
    print("\nLivro adicionado com sucesso!")


####    Função para consultar biblioteca    ###
def consultar():
    def isnum(i):
    #Checa se o elemento i é um número
        try:
            float(i)
            return valor_consultado.append(float(i))
        except ValueError:
    #Se o elemento não for um nûmero, ele é ignorado
            pass   
    categorias=[]
    consulta = []
    livros_por_categoria = []
    valor_consultado=[]
    #Input do usuário para verificar a categoria desejada
    categoria_consultada = input("\nDigite a categoria de livros que que você deseja visualizar ou escreva [TUDO] para imprimir todas as categorias que você possui: ").upper()
    print()
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    if categoria_consultada == "TUDO":
        for linha in arquivo:
            valores = linha.strip().split(", ")
            if len(valores) == 4:
                titulo, autor, categoria, valor = valores
                if categoria not in categorias:
                    categorias.append(categoria)
                    livros_por_categoria.append([])

                livros_por_categoria[categorias.index(categoria)].append(", ".join(valores))
                numeros_na_linha = [float(s) for s in valor.split() if isnum(s)]
                valor_consultado.extend(numeros_na_linha)
   
    else:
        for linha in arquivo:
            if categoria_consultada in linha:
                    consulta.append(linha.strip())
                    numeros_na_linha = [float(s) for s in linha.split() if isnum(s)]
                    valor_consultado.extend(numeros_na_linha)
    arquivo.close

    if categorias:
        categorias_ordenadas = sorted(categorias)
        for categoria in categorias_ordenadas:
            print(f"\n{categoria}:\n")
            livros_na_categoria_ordenados = sorted(livros_por_categoria[categorias.index(categoria)])
            for livro in livros_na_categoria_ordenados:
                print(livro)
    
    #Se a quantidade de valores atribuidos forem maior que 0, mostra os valores e os livros dessa categoria
    if len(consulta) > 0 or "TUDO":
        consulta.sort()
        consulta_formatada='\n'.join(consulta)
        return (f"{consulta_formatada} \nO valor total da categoria consultada é R$ {sum(valor_consultado):.2f}")
    else:
        return "Categoria inválida ou sem valor atribuido"
    

####    Função para calcular o total de dinheiro gasto  ####
def gastos_totais(gastos):
    def isnum(i):
    #Checa se o elemento i é um número
        try:
            float(i)
            return gastos.append(float(i))
        except ValueError:
    #Se o elemento não for um nûmero, ele é ignorado
            pass    
    arquivo = open ("CRUD.txt", "r", encoding='utf-8')
    arquivo_formatado=arquivo.read()
    arquivo_formatado=arquivo_formatado.split()
    for i in arquivo_formatado:
    #Checa em todos os elementos se há numeros
        isnum(i)
    arquivo.close()
    #Soma todos os valores encontrados
    total_gasto=sum(gastos)
    #Retorna a soma desses números
    return (f"\nForam gastos R$ {total_gasto:.2f} no total")


####    Função para alterar livros      ####
def alterar():
    arquivo = open ("CRUD.txt", "r+", encoding = "utf8")
    #Armazena na variável <tituloa> o nome do título a ser alterado
    tituloa = input ("\nDigite o título que deseja alterar: ").upper()
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
            resposta_alteracao=int(input("\nQual mudança você quer realizar? Digite [1] se você quiser alterar o título, [2] se você quiser alterar o autor, [3] se você quiser alterar a categoria, [4] se você quiser alterar o preço ou [5] para alterar tudo: "))
            if resposta_alteracao >= 1 and resposta_alteracao <= 5:
                #Apenas altera o título, através de seu índice no vetor
                if resposta_alteracao == 1:
                    subst_titulo=input("\nQual o novo título que você gostaria de atribuir à obra? ")
                    vetor_alteracao[0] = subst_titulo.upper()

                #Apenas altera o autor, através de seu índice no vetor                    
                elif resposta_alteracao == 2:                
                    subst_autor=input("\nQual o nome do autor que você gostaria de atribuir à obra? ")
                    vetor_alteracao[1] = subst_autor.upper()
            
                #Apenas altera a categoria, através de seu índice no vetor
                elif resposta_alteracao == 3:
                    subst_categoria=input("\nEm qual categoria você deseja inserir à obra? ")
                    vetor_alteracao[2] = subst_categoria.upper()

                #Apenas altera o preço, através de seu índice no vetor
                elif resposta_alteracao == 4:                
                    subst_preco=input("\nQual preço você gostaria de atribuir à obra? ")
                    vetor_alteracao[3] = subst_preco.upper()+"\n"

                #Altera tudo, cada categoria através de seu índice no vetor, respectivamente
                elif resposta_alteracao == 5:
                    subst_titulo=input("\nQual o novo título que você gostaria de atribuir à obra? ")
                    vetor_alteracao[0] = subst_titulo.upper()
                    subst_autor=input("\nQual o nome do autor que você gostaria de atribuir à obra? ")
                    vetor_alteracao[1] = subst_autor.upper()
                    subst_categoria=input("\nEm qual categoria você deseja inserir à obra? ")
                    vetor_alteracao[2] = subst_categoria.upper()
                    subst_preco=input("\nQual preço você gostaria de atribuir à obra? ")
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
                print ("\nLivro alterado com sucesso!")
                #Se o número não estiver entre 1 e 5, printa essa mensagem. O alterado vira "S" para não rodar a mensagem de livro não encontrado.
            else:
                print("\nNúmero inválido. Por favor, insira um número entre 1-5")
                alterado = "S"
        else:
            livro = ""
            continue
    if alterado == "N":
        print ("\nLivro não encontrado")
    arquivo.close()


####    Função para excluir livros      ####
def excluir ():
    arquivo = open ("CRUD.txt", "r+", encoding = "utf8")
    
    #Armazena na variável <tituloe> o nome do título a ser excluído e "N" na variável <excluido> (N = não excluído)
    tituloe = input ("\nDigite o título que deseja excluir: ").upper()
    excluido = "N"
    
    #Armazena no vetor <texto> as linhas do arquivo TXT
    texto = arquivo.readlines()
    livro = ""
    a_excluir = []

    #Armazena na variável <livro> apenas o título do livro na linha i          
    #Se o título que quer excluir estiver contido em <livro>, alimenta o vetor <a_excluir>    
    #Se não, esvazia a string <livro> e continua o loop para o próximo título
    for i in range (len(texto)):
        for j in range (0, texto[i].find( ",")):
            livro = livro + texto[i][j]       
        
        if tituloe in livro:
            a_excluir.append(livro)
            livro = ""
            
        else:
            livro = ""
            continue
             
    #Continua o processamento a depender da existência (ou não) de mais de um título existente com o termo pesquisado
    if len(a_excluir) == 0:
        print ("\nLivro não encontrado!")
        return
    elif len(a_excluir) > 1:
        #Se tiver mais de um livro com o termo digitado, vai exibir os livros que têm o mesmo termo e pedir para escolher qual vai excluir
        print ("\nExiste mais de um livro para o termo pesquisado:")
        for i in range (len(a_excluir)):
            print (f"{[i]} {a_excluir[i]}")
        escolhido = input ("\nDigite o código do livro que deseja excluir: ")
        tituloe = a_excluir[int(escolhido)]
        
    elif len(a_excluir) == 1:        
        tituloe = a_excluir[0]

    #Percorre <texto> para encontrar o título a ser excluído
    for i in range (len(texto)):
        livro = ""
        for j in range (0, texto[i].find( ",")):
            #Armazena na variável <livro> apenas o título do livro na linha i
            livro = livro + texto[i][j]  
     
        if tituloe in livro:
            livro = tituloe
            break
        else:
            continue
    #Confirma se quer realmente excluir o livro a partir do título informado
    #Apaga o arquivo e reescreve sem o título excluído
    resposta = input (f"\nDeseja realmente excluir o livro -{livro}- [S] ou [N]? ").upper()
    if resposta == "S":
        del texto[i]
        arquivo = open ("CRUD.txt", "w", encoding = "utf8")
        for i in range (len(texto)):
            arquivo.write (f"{texto[i]}")
        excluido = "S"
        print ("\nLivro excluído com sucesso!")
    elif resposta == "N":
        return
    else:
        print ("\nOpção inválida!")         
            
    if livro == "" :
        print ("\nLivro não encontrado")

    arquivo.close()


####    Função para manipular os favoritos  ####
def favoritos():
    #Abrir os dois TXT, o do arsenal de livros da biblioteca e dos favoritos
    arquivo = open ("CRUD.txt", "r", encoding = "utf8")
    arquivo2 = open ("CRUD2.txt", "r+", encoding = 'utf-8')
    #Oferece as opções de adcionar, remover ou consultar os livros favoritados
    opcoes_favoritos=int(input("\nO que você deseja fazer com os favoritos? Digite [1] para adicionar livro aos favoritos ou [2] para remover um livro do favoritos ou [3] para consultá-lo: "))
    #Opção de adicionar livro da bilbioteca aos favoritos
    if opcoes_favoritos == 1:
        titulof=input("\nDigite o título do livro que você deseja adicionar como favorito: ").upper()
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
                print ("\nLivro adicionado aos favoritos com sucesso!")
            else:
                livro = ""
                continue
            if favoritado == "N":
                print ("\nLivro não encontrado")
    #Opção de remover livro da bilbioteca nos favoritos
    elif opcoes_favoritos == 2:
        titulof=input("\nDigite o título do livro que você deseja remover dos favorito: ").upper()
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
                print ("\nLivro excluído com sucesso!")
            else:
                livro = ""
                continue
            if excluido_favoritos == "N":
                print ("\nLivro não encontrado")
    
    #Opção de consultar os livros dos favoritos
    elif opcoes_favoritos == 3:
        arquivo2 = open ("CRUD2.txt", "r", encoding = "utf8")
        print()
        for linha in arquivo2:
            print(linha.strip())
    
    arquivo.close()
    arquivo2.close()


####    Nosso Menu  ####
while True:
    try:
        
        print (f"\n### CRUD DE LIVROS ###\n")

        opcao = int(input ("\nEscolha a opção desejada: [1] Adicionar, [2] Consultar Biblioteca ou Gastos Totais, [3] Alterar , [4] Excluir, [5] Favoritos ou [6] Sair: "))
        
        if opcao >= 1 and opcao <= 7:
                    
            if opcao == 1:
                resposta = 'S'
                while resposta == 'S':
                    quantidade = int(input ("\nQuantos livros deseja adicionar? "))
                    adicionar(quantidade)
                    resposta = input("\nVocê deseja adicionar mais livros? Digite [S] para Sim e [N] para Não: ").upper()


            elif opcao == 2:
                resposta = 'S'
                while resposta == 'S':
                    alternativas = input("\nDigite [BIBLIOTECA] para consultar a Biblioteca ou [GASTOS] para consultar os Gastos Totais: ").upper()
                    if alternativas == "BIBLIOTECA":
                        print(consultar())
                    elif alternativas == "GASTOS":
                        print (gastos_totais(gastos))
                    else:
                        print("\nOpção inválida!")
                    resposta = input("\nVocê gostaria de fazer mais consultas? Digite [S] para Sim e [N] para Não: ").upper()
                
            elif opcao == 3:
                resposta = 'S'
                while resposta == 'S':
                    alterar()
                    resposta = input("\nVocê deseja alterar mais livros? Digite [S] para Sim e [N] para Não: ").upper()

            elif opcao == 4:
                resposta = 'S'
                while resposta == 'S':
                    excluir()
                    resposta = input("\nVocê deseja excluir mais livros? Digite [S] para Sim e [N] para Não: ").upper()
        
            elif opcao == 5:
                resposta = 'S'
                while resposta == 'S':
                    favoritos()
                    resposta = input("\nVocê deseja continuar no menu dos favoritos? Digite [S] para Sim e [N] para Não: ").upper()
        
            elif opcao == 6:
                print("\nEncerrando biblioteca!")
                break

        else:
            print("\nPor favor, insira um numero de 1-7")
            continue
        
    except ValueError:
        print("\nErro de valor! Por favor, insira um numero.")
        continue
    
    
