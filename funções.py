# Lista para armazenar os contatos da agenda
agenda = []

# Variável para marcar se houve alguma alteração na agenda
# Utilizada para verificar se é necessário salvar as mudanças
alterada = False

# Função para solicitar o nome do usuário
# Se o usuário não digitar nada, retorna o valor padrão fornecido
def pede_nome(padrão=""):
    nome = input("Nome: ")
    if nome == "":  # Se o nome estiver vazio, usa o valor padrão
        nome = padrão
    return nome

# Função para solicitar o telefone do usuário
# Se o usuário não digitar nada, retorna o valor padrão fornecido
def pede_telefone(padrão=""):
    telefone = input("Telefone: ")
    if telefone estiver vazio, usa o valor padrão
    return telefone

# Função para exibir os dados de um contato
# Recebe o nome e o telefone como parâmetros e os exibe formatados
def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")

# Função para solicitar o nome de um arquivo ao usuário
# Retorna o nome do arquivo digitado pelo usuário
def pede_nome_arquivo():
    return input("Nome do arquivo: ")

# Função para pesquisar um nome na agenda
# Converte o nome para minúsculas e busca na lista de contatos
# Retorna a posição do contato na lista ou None se não for encontrado
def pesquisa(nome):
    mnome = nome.lower()  # Converte o nome para minúsculas para busca case-insensitive
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p  # Retorna a posição do contato se encontrado
    return None  # Retorna None se o contato não for encontrado

# Função para verificar se um nome já existe na agenda
# Retorna True se o nome já estiver na agenda, caso contrário, False
def nome_existe(nome):
    return pesquisa(nome) is not None

# Função para adicionar um novo contato à agenda
# Solicita o nome e o telefone do usuário e os adiciona à lista
# Verifica se o nome já existe antes de adicionar
def novo():
    global agenda, alterada
    nome = pede_nome()
    if nome_existe(nome):
        print("Erro: O nome já existe na agenda.")
        return  # Sai da função sem adicionar o contato
    telefone = pede_telefone()
    agenda.append([nome, telefone])  # Adiciona o novo contato à agenda
    alterada = True  # Marca que houve alteração na agenda

# Função para solicitar confirmação do usuário para uma operação específica
# Recebe a operação como parâmetro (ex.: "apagamento") e retorna "S" ou "N"
def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":  # Verifica se a resposta é válida (S ou N)
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

# Função para remover um contato da agenda
# Solicita o nome do contato e, se encontrado, remove-o após confirmação
def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:  # Se o contato for encontrado
        if confirma("apagamento") == "S":  # Confirma o apagamento
            del agenda[p]  # Remove o contato da lista
            alterada = True  # Marca que houve alteração na agenda
    else:
        print("Nome não encontrado.")  # Exibe mensagem se o contato não for encontrado

# Função para alterar os dados de um contato existente na agenda
# Solicita o nome do contato, permite alterar nome e telefone, e atualiza a agenda
def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:  # Se o contato for encontrado
        nome = agenda[p][0]  # Obtém o nome atual do contato
        telefone = agenda[p][1]  # Obtém o telefone atual do contato
        print("Encontrado:")
        mostra_dados(nome, telefone)  # Exibe os dados atuais do contato
        nome = pede_nome(nome)  # Permite alterar o nome, mantendo o atual se nada for digitado
        if nome_existe(nome):
            print("Erro: O nome já existe na agenda.")
            return  # Sai da função sem alterar o contato
        telefone = pede_telefone(telefone)  # Permite alterar o telefone
        if confirma("alteração") == "S":  # Confirma a alteração
            agenda[p] = [nome, telefone]  # Atualiza os dados do contato na agenda
            alterada = True  # Marca que houve alteração na agenda
    else:
        print("Nome não encontrado.")  # Exibe mensagem se o contato não for encontrado

# Função para listar todos os contatos da agenda
# Exibe a posição e os dados de cada contato armazenado
def lista():
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1])  # Exibe os dados de cada contato
    print("------\n")

# Função para ler e carregar a última agenda gravada, se disponível
# Se houver uma agenda salva anteriormente, ela é carregada na inicialização
def lê_última_agenda_gravada():
    última = última_agenda()
    if última is not None:  # Se houver uma última agenda registrada
        leia_arquivo(última)

# Função para retornar o nome do último arquivo de agenda gravado
# Lê o nome do arquivo salvo em "ultima agenda.dat" ou retorna None se não existir
def última_agenda():
    try:
        with open("ultima agenda.dat", "r", encoding="utf-8") as arquivo:
            última = arquivo.readline().strip()  # Lê o nome do arquivo na primeira linha
    except FileNotFoundError:
        return None  # Retorna None se o arquivo não for encontrado
    return última

# Função para atualizar o nome do último arquivo de agenda gravado
# Salva o nome do arquivo atual em "ultima agenda.dat"
def atualiza_última(nome):
    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")  # Grava o nome do arquivo da última agenda

# Função para ler e carregar os contatos de um arquivo específico para a agenda
# Lê o arquivo fornecido e popula a lista de contatos
def leia_arquivo(nome_arquivo):
    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []  # Limpa a agenda atual antes de carregar a nova
        for l in arquivo.readlines():
            nome, telefone = l.strip().split("#")  # Separa nome e telefone no arquivo
            agenda.append([nome, telefone])  # Adiciona cada contato à lista
    alterada = False  # Reseta a marcação de alteração após carregar

# Função para carregar uma nova agenda de um arquivo e atualizar o registro
# Se houver alterações não salvas, solicita confirmação antes de continuar
def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()  # Grava as alterações antes de carregar a nova agenda
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()  # Solicita o nome do arquivo a ser carregado
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)  # Atualiza o nome do último arquivo carregado

# Função para ordenar a agenda por nome usando o método de bolhas (bubble sort)
# A ordenação é feita em ordem alfabética do nome dos contatos
def ordena():
    global alterada
    fim = len(agenda)  # Define o limite do loop de ordenação
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i][0] > agenda[i + 1][0]:  # Compara os nomes de dois contatos adjacentes
                agenda[i], agenda[i + 1] = agenda[i + 1], agenda[i]  # Troca de posição se necessário
                trocou = True  # Marca que houve troca
            i += 1
        if not trocou:  # Se não houve trocas, a lista já está ordenada
            break
    alterada = True  # Marca que houve alteração na agenda

# Função para salvar a agenda atual em um arquivo
# Solicita o nome do arquivo e grava os dados de todos os contatos
def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return  # Não grava se o usuário escolher "N"
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()  # Solicita o nome do arquivo para salvar a agenda
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")  # Grava cada contato no arquivo
    atualiza_última(nome_arquivo)  # Atualiza o nome do último arquivo salvo
    alterada = False  # Reseta a marcação de alteração após salvar

# Função para validar a entrada de um número inteiro dentro de uma faixa específica
# Repete a solicitação até que o usuário insira um valor válido
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:  # Verifica se o valor está dentro da faixa permitida
                return valor
        except ValueError:  # Captura exceções caso o valor não seja um inteiro
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

# Função para exibir o menu de opções e solicitar que o usuário escolha uma
# Mostra a quantidade de contatos na agenda e se houve alterações
def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

# Lê a última agenda gravada ao iniciar o programa
lê_última_agenda_gravada()

# Loop principal do programa
# O loop continua até que o usuário escolha a opção de sair (0)
while True:
    opção = menu()  # Exibe o menu e obtém a escolha do usuário
    if opção == 0:
        break  # Sai do loop e termina o programa
    elif opção == 1:
        novo()  # Adiciona um novo contato
    elif opção == 2:
        altera()  # Altera um contato existente
    elif opção == 3:
        apaga()  # Apaga um contato da agenda
    elif opção == 4:
        lista()  # Lista todos os contatos
    elif opção == 5:
        grava()  # Salva a agenda em um arquivo
    elif opção == 6:
        lê()  # Carrega uma nova agenda de um arquivo
    elif opção == 7:
        ordena()  # Ordena a agenda por nome