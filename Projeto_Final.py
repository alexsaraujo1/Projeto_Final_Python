fornecedor = {"Código": [], "Nome": [], "Telefone": [], "Email": []}


# print(fornecedor)


opção = input(
    "Digite a opção desejada:\n1 - Para adicionar novo fornecedor:\n2 - Para buscar um fornecedor:\n3 - Para apagar dados do fornecedor:\n4 - Para sair do sistema:\n"
)

if opção == "1":
    adic_forn1: input(
        "Digite nome completo do  fornecedor",
    )
    adic_forn2: int(
        input(
            "Digite o numero de telefone do  fornecedor",
        )
    )
    adic_forn3: input(
        "Digite o e-mail do  fornecedor",
    )


else:
    print("Comando não reconhecido! Digite novamente o comando desejado:")
