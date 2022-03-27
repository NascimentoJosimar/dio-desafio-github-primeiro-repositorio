import os

cadastrar_aluno = 's'
nome_arquivo = "alunos.txt"
nome_escola = "ESCOLA MUNICIPAL FULANO DA SILVA"
separador = "-" * len(nome_escola)
cabecalho = separador + "\n" + nome_escola + "\n" + separador

if not os.path.exists(nome_arquivo):
    arquivo_cadastro = open(nome_arquivo, 'w+t', encoding="utf-8")
    arquivo_cadastro.write(cabecalho)
    arquivo_cadastro.close()

def salvar_aluno(aluno):
    print(aluno)

while cadastrar_aluno == 's':
    # Cadastro do aluno
    aluno = {
        "Nome": "",
        "CPF": "",
        "Mãe": "",
        "Data de nascimento": "",
        "Idade": 0,
        "Série": ""
    }

    aluno["Nome"] = input("Digite o nome do aluno: ")
    aluno["CPF"] = input("Digite o CPF do aluno: ")
    aluno["Mãe"] = input("Digite o nome da mãe do aluno: ")
    aluno["Data de nascimento"] = input("Digite a data de nascimento do aluno: ")
    aluno["Idade"] = input("Digite a idade do aluno: ")
    aluno["Série"] = input("Digite a série do aluno: ")

    salvar_aluno(aluno)

    cadastrar_aluno = input("Deseja cadastrar mais um aluno? (s ou n)").lower()
