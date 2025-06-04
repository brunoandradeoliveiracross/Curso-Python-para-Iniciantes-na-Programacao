# Variáveis são container para armazenar dados
# Variáveis diferenciam letras minusculas de maisculas

a = 5
A = 10

# Variáveis podem ser do tipo int mas podem mudar para strings

a = 5
a = "Bom dia"

# Está variável a agora é uma string você também pode converter uma variável

a = str(5) # está variável é uma string "5"
b = int(10) # está variável é do tipo inteiro 10
c = float(30) # está variável é do tipo float 30.0

# Você pode usar a função type para identificar o tipo de variável

x = 5
y = "Cross" # A variável string pode ser com aspas simples 'Cross' ou "Duplas"

print (type(x))
print (type(y))

# A primeira letra da variável deve ser uma letra e ela difere letras maísculas exemplo:

carro = 20000
endereco_casa = "Rua Sete, número 555 Bairro Cristal"
precoTotal = 50

# python permite adicionar valores a variáveis em uma única linha usando virgula
 
x,y,z = 50, 30, 10
print (x) # retorna 50
print (y) # retorna 30
print (z) # retorna 10

# e você pode adicionar o mesmo valor a varias variáveis usando sinal de igual

x = y = z = 50
print (x) # retorna 50
print (y) # retorna 50
print (z) # retorna 50

# você também pode fazer um desempacotamento extraindo dados de uma lista, tupla etc.

frutas = ["maça", "laranja", "pera"]
x,y,z = frutas # cada variável está pegando uma string desta lista

print (x) # Retorna maça
print (y) # Retorna laranja
print (z) # Retorna pera

# Você pode usar o comando print para printar varias variáveis ao mesmo tempo

x = "Bom"
y = "dia"
f = "Cross"

print (x,y,f) # Retorna Bom dia Cross

# Você também pode usar o sinal de + porem deve adicionar espaço dentro da string para não retornar BomdiaCross junto
# Porem se deseja imprimir dois dados diferentes como um número e uma string se usa virgula

x = 10
y = "Olá"

print (x,y) # Retorna 10 Olá, porém se usar sinal de + gera erro porque vai tentar somar string com inteiro

# Você pode fazer operações matemáticas com print

x = 10
y = 2

print (x + y)
print (x * y)
print (x - y)
print (x / y)

# A variável pode ser global ou local
# quando você cria ela de fato ela se torna uma variável global porem se você criar a 
# variável dentro de uma função ela se torna local e só pode ser usada dentro da função
# também é possivel criar uma variável global dentro da função mas para isso é necessário 
# usar o codigo global

# Para se criar uma função se usa def + nomedafunção():

x = 10 # Variável Global

# Criação de uma função
def suafuncao():
    print ("Hoje é dia", x)

# Executar função, você precida chamar sua função para ser executada senão ela não é ativada
suafuncao()

# Está função tem uma variável local que só existe dentro da função

x = 10 # Variável Global

def suafuncao():
    x = 5 # mesmo com o mesmo nome que a variável global são duas variaveis diferentes uma é local e outra global
    print (5)

# Executar função
suafuncao()

# Criando uma variável global dentro da função

def suafuncao():
    global x # Determinar que x é Global
    x = 5
    print ("Variavel Global é : ", x)

suafuncao()




