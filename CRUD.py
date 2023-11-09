import os
os.system ("cls")

biblioteca = {}

print (f"\n### CRUD DE LIVROS ###\n")

#FALTA - não está criando um código para cada item!!!

opcao = int(input ("Escolha a opção desejada: [1] Adicionar, [2] Consultar, [3] Alterar, [4] Excluir ou [5] Sair: "))

if opcao == 1:

    quantidade = int(input ("Quantos livros deseja adicionar? "))
    for i in range (quantidade):
        #coletar dados dos livros e alimentar em um dicionário
        titulo = input (f"Digite o título do livro: ")
        autor = input (f"\nDigite o autor: ")
        categoria = input (f"\nDigite a categoria: ")
        valor = float(input (f"\nDigite o valor pago: "))
        biblioteca[i] = titulo, autor, categoria, valor
    arquivo = open ("biblioteca.csv", "a")  #o parâmetro <a> permite que sejam inseridos dados sem apagar os anteriores
    
    #o trecho a seguir salva os dados coletados na etapa anterior em um arquivo .csv (separados por vírgula)
    
    for i in range (quantidade):
        arquivo.write (f"{biblioteca[i]}\n")
    arquivo.close()

elif opcao == 2:
    #arquivo = open ("biblioteca.csv", "r")
    #for linha in arquivo 
    





    #o trecho a seguir imprime o conteúdo do arquivo .csv
    arquivo = open ("biblioteca.csv", "r")
    for i in arquivo.readlines():
        print (f"\n{i}")
         
    arquivo.close()












