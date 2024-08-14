meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Função para validar e converter a data digitada
def converter_data(data):
    try:
        # Tenta separar a data em dia, mês e ano
        dia, mes, ano = map(int, data.split('/'))
        
        # Verifica se o mês está no intervalo válido
        if mes < 1 or mes > 12:
            raise ValueError
        
        # Verifica se o dia está no intervalo válido considerando meses com 30, 31 dias e fevereiro
        if dia < 1 or (mes == 2 and dia > 29) or (mes in [4, 6, 9, 11] and dia > 30) or (mes not in [4, 6, 9, 11] and dia > 31):
            raise ValueError
        
        # Retorna a data por extenso
        return f"{dia} de {meses[mes-1]} de {ano}"
    except ValueError:
        return None

# Função para solicitar a data ao usuário até que ele digite corretamente
def solicitar_data():
    while True:
        data = input("Digite a data no formato DD/MM/AAAA: ")
        data_extenso = converter_data(data)
        if data_extenso:
            return data_extenso
        else:
            print("Data inválida. Tente novamente.")

# Função para exibir o menu de opções
def menu():
    print("\nMenu de Opções:")
    print("1 – Converter Data")
    print("2 – Listar Datas por extenso")
    print("3 – Sair")

    return input("Escolha uma opção: ")

# Função para salvar datas convertidas em um arquivo
def salvar_datas_em_arquivo(datas):
    with open("datas_por_extenso.txt", "w", encoding="utf-8") as arquivo:
        for data in datas:
            arquivo.write(data + "\n")
    print("Datas salvas com sucesso!")

# Função principal
def main():
    datas_convertidas = []
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            data_extenso = solicitar_data()
            datas_convertidas.append(data_extenso)
            print(f"Data convertida: {data_extenso}")
        
        elif opcao == '2':
            if datas_convertidas:
                print("\nDatas convertidas por extenso:")
                for data in datas_convertidas:
                    print(data)
            else:
                print("Nenhuma data convertida ainda.")
        
        elif opcao == '3':
            if datas_convertidas:
                salvar_datas_em_arquivo(datas_convertidas)
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if _name_ == "_main_":
    main()