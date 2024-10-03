"""
Turma - G93313
Nome das componentes:
Lara de Araújo
Jamile Reis
"""

import os
from dataclasses import dataclass


os.system("cls || clear")

idade = []
sexo = []
salario = []
mulheres_salario_maior = []
habitantes = 0

while True:
    print(""" 
   ========MENU=========
-------------------------------
Código | Descrição            |
-------|----------------------|
1      | Adicionar Habitantes |
2      | Exibir resultados    |
3      | Sair                 |

          
""")
    opcao = int(input("digite a opção desejada: "))
    if opcao == 1:

        habitantes += 1
        salario_habitante = float(input("digite seu salário: "))
        salario.append(salario_habitante)

        sexo_habitante = input("digite seu sexo(M-masculino ou F-feminino): ").upper()
        sexo.append(sexo_habitante)

        idade_habitante = int(input("digite sua idade: "))
        idade.append(idade_habitante)

        if sexo_habitante == "F" and salario_habitante >= 5000:
            mulheres_salario_maior.append(1)

        soma_salario = sum(salario)
        media_salario = soma_salario / habitantes

        maior_idade = max(idade)
        menor_idade = min(idade)

        mulheres_5000 = sum(mulheres_salario_maior)  
        os.system("cls || clear")

    elif opcao == 2: 

       print(f"media salario: {media_salario}")
       print(f"maior idade do grupo: {maior_idade}")
       print(f"menor idade do grupo: {menor_idade}")
       print(f"quantia de mulheres com salario acima de R$5000: {mulheres_5000}")
    elif opcao == 3:
        break
    else:
        print("código inválido")


nome_do_arquivo = "pesquisa_habitantes.txt"

with open(nome_do_arquivo, "a") as arquivo_habitantes:
    arquivo_habitantes.write(f"\n média salário: {media_salario}")
    arquivo_habitantes.write(f"\n maior idade do grupo: {maior_idade}")
    arquivo_habitantes.write(f"\n menor idade do grupo: {menor_idade}")
    arquivo_habitantes.write(f"\n quantia de mulheres com salario acima de R$5000: {mulheres_5000} ")

arquivo_habitantes.close()
print("===========DADOS SALVOS COM SUCESSO============")


with open(nome_do_arquivo,"r")as arquivo_de_origem:
    for linha in arquivo_de_origem:
       linha.strip().split("\n")

arquivo_habitantes.close()

print("==========EXIBINDO DADOS=============")

print(f"\n média salário: {media_salario}")
print(f"\n maior idade do grupo: {maior_idade}")
print(f"\n menor idade do grupo: {menor_idade}")
print(f"\n quantia de mulheres com salario acima de R$5000: {mulheres_5000} ")

