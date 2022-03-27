import os

cadastrar_membro = 's'
nome_arquivo = "membros.txt"
nome_igreja = "IGREJA BATISTA CENTRAL DE JABOATÃO"
separador = "-" * len(nome_igreja)
cabecalho = separador + "\n" + nome_igreja + "\n" + separador

if not os.path.exists(nome_arquivo):
    arquivo_cadastro = open(nome_arquivo, 'w+t', encoding="utf-8")
    arquivo_cadastro.write(cabecalho)
    arquivo_cadastro.close()

def salvar_membro(membro):
    arquivo_cadastro = open(nome_arquivo, 'r', encoding="utf-8")
    posicao_membro = arquivo_cadastro.read().count("membro") + 1
    arquivo_cadastro.close()

    arquivo_cadastro = open(nome_arquivo, 'a+t', encoding="utf-8")
    arquivo_cadastro.write("\nmembro " + str(posicao_membro) + "\n")

    for chave in membro:
        arquivo_cadastro.write("- " + chave + ": " + membro[chave] + "\n")

    arquivo_cadastro.write(separador)
    arquivo_cadastro.close()

while cadastrar_membro == 's':

    membro = {
        "Nome": "",
        "CPF": "",
        "Fone": "",
        "E-mail": "",
        "Cidade": "",
        "Bairro": "",
        "Pastor(a)": "",
        "Batizado": ""
    }

    print("Digite os campos abaixo para cadastrar um membro:")
    for chave in membro:
        membro[chave] = input(chave + ":")

    salvar_membro(membro)
    cadastrar_membro = input("Deseja cadastrar mais um membro? (s ou n)").lower()