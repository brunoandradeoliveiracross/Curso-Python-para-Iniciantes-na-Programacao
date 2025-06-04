# Estes são os tipos de dados presentes em python

# Tipo de texto:	str
# Tipos numéricos:	int, float, complex
# Tipos de sequência:	list, tuple, range
# Tipo de mapeamento:	dict
# Tipos de conjuntos:	set,frozenset
# Tipo booleano:	bool
# Tipos binários:	bytes, bytearray, memoryview
# Nenhum Tipo:	NoneType

# Usando a função type() você pode descobrir o tipo de dado da variavel

x = 5
print (type(x))

# Exemplo de definindo os tipos e dados

x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType	

# Existem três tipos de dados para números 

x = 10 # int é um número inteiro sendo negativo ou positivo
b = 5.00 # float é um número positivo ou negativo que possue casa decimais
c = 2j # complex são números imaginários e são escritos com a letra j

# você pode converter um número dessa forma

x = 5
x = float(x) # o número 5 é convertido para 5.00
x = complex(x) # o número 5.00 é convertido para 5j
x = str(x) # o número 5j foi convertido para string "5j"

# você pode gerar números aleatórios usando este código

import random # importar modulo aleatório

print (random.randrange(1, 10)) 

# gera um número aleatório de 1 a 10 um exemplo pratico seria lançar um dado
# de seis faces sendo esse código usado para programar o back end
# jogos de tabuleiro online usam este tipo de back end

print (random.randrange(1,6)) # para jogar dado de 6 faces
print (random.randrange(1,20)) # para jogar dado d20 do popular jogo DeD


# Para receber dados de um usuário basta usar o comando input

a = input("Digite seu nome: ")
print(a) # imprimi o texto armazenado dentro da variavel

# este comando vai armazenar o nome do usuario dentro da variavel a e depois vai imprimir na tela
# porem tudo que é digitado é armazenado como string até mesmo números se deseja armazenar
# o dado como inteiro vai ter que converter o dado recebido pelo usuario

a = input ("Digite um número: ") # O número será armazenado como string 'numero'
a = int(a) # aqui convertemos a string para número inteiro para ser usado em equações e algoritimos









