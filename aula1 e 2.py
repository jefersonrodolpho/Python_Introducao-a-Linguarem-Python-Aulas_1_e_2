# Dizendo Hello World
int
nome ='Jeferson'
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" %(nome))

# Usanto if e else  "se ou senão"
a = 20
b = 10

if a<b:

    print("a é menor do que b")

    r = a + b

    print(r)

else:
    print("a é maior do que b")

    r = a - b
    print(r)

# Usando elif (estrutura encadeada)
# O operador == em Python é usado para testar se duas coisas são iguais. Por exemplo, 10 == 10 retorna True, enquanto abacate == melancia retorna False
codigo_compra = 5111

if codigo_compra == 5222:

    print("Compra à vista")

elif codigo_compra == 5333:

    print("Compra à prazo no boleto")

elif codigo_compra == 5444:

    print("Compra à prazo no cartão")

else:

    print("Código não cadastrado")

# Usando operador "and"
qtde_faltas = int(input("Digite a quantidade de faltas: "))

media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:

    print("Aluno aprovado!")

else:

    print("Aluno reprovado!")

# Usando comando while (estrutura de repetição)
# Observação importante que me atentei agora (tem que tomar cuidado com os espaçamentos e tabulações para que fiquem dentro do trecho do código esperado senão vai gerar erro)
numero = 1

while numero != 0:

    numero = int(input("Digite um número: "))

    if numero % 2 == 0:

            print("Número par!")

    else:

            print("Número ímpar!")

# Usando o comando for (estrutura de repetição)
# Usamos o comando "for" seguido da variável de controle "c", na sequência o comando "in", que traduzindo significa "em", por fim, a sequência sobre a qual a estrutura deve iterar. Os dois pontos marcam o início do bloco que deve ser repetido.
nome = "Jeferson"

for c in nome:
     print(c)


# Usando a função "enumerate()" para retornar a posição do item dentro da sequência, o mesmo pode ser usado junto com o comando for
# Para que possamos capturar tanto a posição quanto o valor, vamos precisar usar duas variáveis de controle. Observe o código a seguir, veja que a variável "i" é usada para capturar a posição e a variável "c" cada caracter da palavra.
nome = "Jeferson"

for i, c in enumerate(nome):
     print(f"Posição = {i}, valor = {c}")

# Usando a função "range()" para criar a iteração em sequencia numérica
# No comando, "x" é a variável de controle, ou seja, a cada iteração do laço, seu valor é alterado, já a função range() foi utilizada para criar um "iterable" numérico (objeto iterável) para que as repetições acontecesse.
for x in range(6):
     print(x)

# Usando a funções "break" e "continue"
#Exemplo de uso do break
disciplina = "Linguagem de programação"

for c in disciplina:
     
     if c == 'a':
     
          break
     
     else:

          print(c)     
# No exemplo com uso do break, perceba que foram impressas as letras L i n g u, quando chegou a primeira letra a, a estrutura de repetição foi interrompida. 
#Exemplo de uso do continue
disciplina = "Linguagem de programação"

for c in disciplina:
     
     if c == 'a':
          
          continue
     else:
          
          print(c)
# No exemplo com uso do continue, perceba que foram impressas todas as letras, exceto as vogais "a", pois toda vez que elas eram encontradas, o continue determina que se pule, mas que a repetição prossiga para o próximo valor.

# Exercício da primeira aula: 
# Vamos criar uma solução que procura pelas vogais "a", "e" em um texto (somente minúsculas). Toda vez que essas vogais são encontradas, devemos informar que encontramos e qual posição do texto ela está. 
#Obs: aspas triplas (""") são usadas para criar strings de várias linhas. Isso é útil quando você precisa criar uma string que se estende por várias linhas
texto ="""

A inserção de comentários no código do programa é uma prática normal.

Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.

O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado (BANIN, p. 45, 2018)."

"""

for i, c in enumerate(texto):
     
     if c == 'a' or c == 'e':
          
          print(f"Vogal '{c}' encontrada, na posição {i}")
     else:
          continue
    
