'''
Saida de dados     - ok
Variaveis          - ok
Entrada de dados   - ok
Operadores Logicos -  
'''

carteira = float(input("Digite um valor: "))
print(carteira)

'''
float()
int(inpuut("digite um inteiro: "))
str(input("Digite uma string: "))
double()
bool() true ou false

AND NOT OR

pra tal bloco rodar, ele precisa que variavel1 seja igual a 2 AND seja menor que 5

idade == 18 -> sinal de igual a  
<= -> sinal de menor ou igual que
idade >= 18 -> maior ou igual que
< menor que
> maior que
idade != 18 diferente
'''
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Voce eh maior de idade")
elif idade > 15:
    print("Entrada so com responsaveis")
elif idade < 14:
    print("voce tem menos que 14 anos")
else:
    print("Idade invalida")


#----------------------------------------------------------------------  

def abrirChat():
    print("Chat aberto")

idadeUsuario = int(input("Digite a idade: "))

if idadeUsuario >= 18:
    print("Entrada no chat permitida")
    botao = int(input("Digite 1 para entrar n chat: "))
    
    if botao == 1:
        abrirChat()
    else:
        print("Botao nao apertado")
elif idadeUsuario < 18 and idade > 15:
    print("Entrada no chat somente com permissão dos pais")
    botao = int(input("Digite 1 para entrar no chat: "))
    if botao == 1:
        abrirChat()
    else:
        print("Botao nao apertado")
elif idadeUsuario <= 15:
    print("Entrada no chat proibida")
else:
    print("Idade Invalida")



# 2 funcoes, uma vai ser a principal para centralizar as outras -> main()  
def acenderLuz(nome):
    luzAcesa = True
    print(f"{nome} está em casa entao acescendo luzes")
    if luzAcesa == True:
        print("Luz acesa")
    else:
        print("Luz apagada")

def main():
    temPessoaEmCasa = int(input("Tem pessoa em casa? 1-Sim/2-Nao \n-> "))

    if temPessoaEmCasa == 1:
        print("Tem alguem em casa")
        nomePessoa = str(input("Qual o nome dessa pessoa? \n-> "))
        print(nomePessoa + " está na sua casa")
        print(f"{nomePessoa} está na sua casa")
        acenderLuz(nomePessoa)

main()