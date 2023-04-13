agenda = {}
while True:
    nome = input('Digite o nome da pessoa: ')
    if nome == '':
        break
    telefone = input('Digite o telefone: ')
    # Adiciona o telefone ao dicionario
    agenda[nome] = telefone
    
#pesquisa um telefone na agenda
nome_perquisa = input('digite o nome para pesquisar: ')
if nome_perquisa in agenda:
    print('Telefone de', nome, ':', agenda[nome_perquisa])
else:
    print('Nome não encontrado na agenda.')