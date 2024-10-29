'''
AND OR NOT
Laços de repetição (while e for)
Condicionais (If elif else, Switch case)
'''
# AND = &&
# OR = ||
# NOT = ! 

'''
AND -> Para retornar true (verdadeiro) TODAS AS COMPARAÇÕES tem de ser verdadeiras
OR -> Para retornar true (verdadeiro) pelo menos UMA das comparações tem de ser verdadeira
NOT -> Converte o true para false e false para true
'''
#idade = 18
#print(idade<=18 and idade>16) # true

# ------------------------------------------------------------------------------------------------
# while -> geralmente usado quando nao se sabe quantas vezes irá repetir o bloco de codigo
# for ---> geralmente usado quando se sabe quantas vezes irá repetir o bloco de codigo

# for (int i = 0; i < 10; i++)
#    print(i)
'''
for i in range(10):
    print(i)

conteAte10 = 0
while conteAte10 < 10:
    print(conteAte10)
    somador = int(input("Digite um valor para somar até 10"))
    conteAte10 += somador
print("Parabens vc chegou ao 10")

enquanto uma condição for verdadeira
    execute esse codigo
    com esse bloco de codigo
quando encerrar execute esse

idade = 18
if idade >= 18:
    print("Maior de idade")
elif not idade==18 :
    print("Somente com autorização dos pais")
else:
    print()

while True:
    decisao = int(input("[1] Adicionar produto\n[2] Remover Produto\n[3] Sair"))

    match decisao:
        case 1:
            print("Produto adicionado")
        case 2:
            print("Produto removido")
        case 3:
            print("Saindo")
            break
        case _:
            print("Nenhum valor encontrado")

'''