import requests

def print_servidor(servidor):
    print("ID: ",servidor['id'])
    print("Nome: ", servidor['nome'])
    print("categoria: ", servidor['categoria'])
    print("matricula: ", servidor['matricula'])
    print("Telefone: ", servidor['telefone'])
    print("Campus: ", servidor['campus'])


def main():
    while True:
        print("-" * 50)
        print("Escolha uma opção:")
        print("0. Sair do programa")
        print("1. Atualizar banco")
        print("2. Buscar servidores por nome")
        print("3. Buscar servidores por matrícula")
        print("4. Buscar servidores por campus")
        print("5. Busca espeficífica de campus e servidores")
        print("6. Cadastrar uma nova senha")
        print("7. Sair do programa")

        opcao = int(input(">> "))
        print("-" * 50)

        if opcao == 0:
            print("Programa encerrado")
        elif opcao == 1:
            senha = input("Digite a senha: ")
            resposta = requests.post(f"http://localhost:3001/criar_tabela/{senha}")
            if resposta.status_code == 200:
                print(resposta.text)
            else:
                print('Erro na criação/atualização da tabela')
        elif opcao == 2:
            nome = input("Digite o nome do servidor: ")
            with requests.get(f"http://localhost:3001/consulta/nome/{nome}") as resposta:
                if resposta.status_code == 200:
                    servidor = resposta.json()
                    for c in servidor:
                        print_servidor(c)
                        print("=-" * 30)

                elif resposta.status_code == 404:
                    print("Nenhum contato encontrado!")
                else:
                    print("Ocorreu um erro ao buscar os servidores !")


        elif opcao == 3:
            matricula = input("Digite a matricula do servidor: ")
            with requests.get(f"http://localhost:3001/consulta/matricula/{matricula}") as resposta:
                if resposta.status_code == 200:
                    servidor = resposta.json()
                    print_servidor(servidor)
                elif resposta.status_code == 404:
                    print("Servidor não encontrado!")
                else:
                    print("Ocorreu um erro ao buscar o Servidor!")

        elif opcao == 4:
            campus = input("digite o campus dos servidores: ")
            with requests.get(f"http://localhost:3001/consulta/campus/{campus.upper()}") as resposta:
                if resposta.status_code == 200:
                    servidor = resposta.json()
                    for c in servidor:
                        print_servidor(c)
                        print("=-" * 30)

                elif resposta.status_code == 404:
                    print("Nenhum servidor encontrado!")
                else:
                    print("Ocorreu um erro ao buscar os servidor!")
        elif opcao == 5:
            print("Escolha uma categoria e um campus para uma pesquisa específica ")
            categoria = input("Digite a categoria do servidor")
            campus = input("Digite o campus do servidor")
            with requests.get(f"http://localhost:3001/consulta/esp/{categoria}/{campus.upper()}") as resposta:
                if resposta.status_code == 200:
                    servidor = resposta.json()
                    for c in servidor:
                        print_servidor(c)
                        print("=-" * 30)

        elif opcao == 6:
            senha =  input("Digite uma senha de verificação:")
            senha_nova =  input("digite a nova senha para ser cadastrada")
            with requests.get(f"http://localhost:3001/nova_senha/{senha}/{senha_nova}") as resposta:
                print(resposta.text)
        elif opcao == 8:
            print("Programa encerrado")
            break

        else:
            print("Escolha uma opção  válida")

main()