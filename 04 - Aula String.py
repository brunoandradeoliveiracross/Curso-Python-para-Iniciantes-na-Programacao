# Você pode printar uma string (text) com print

print ("Bom Dia")

# Você pode usar aspas simples dentro de uma string 

x = "Bom dia 'você está bem ?' "
print (x)

# Você também pode adicionar um texto a uma variavel usando aspas triplas """ ou '''

x = """ Está é a descrição de um filme,
Alice no país das Maravilhas é um classico
que já foi relançado varias vezes
conta a história de uma garota que acha uma toca
de coelho e vive diversas aventuras """

print (x)

# Está é uma variavel que guarda a descrição de filme, como a dos sites que você assiste
# Ou seja aquela descrição que você lê pode ser uma variavel sendo printada na tela

# Você também pode contar quantas letras tem a string com a função len()

a = "Este é um texto de redação ou descrição de algo"
print (len(a))

# Você já deve ter visto na internet que certos campos exigem que você digite um minimo
# de caracteres como descrição, redação ou algum site que conta quantas letras tem sua redação

# Você pode verificar se uma palavra está dentro de uma string

a = "O filme Alice é maravilhoso" # Titulo de um post de um blog
print ("filme Alice" in a) # retorna true porque a palavra filme alice está presente na variavel

# Este é um exemplo rudimentar de como os bots de buscadores como google encontram aquilo que você
# procura na internet quando digita algo como filme alice e ele retorna links com sites e blogs
# falando sobre o assunto

txt = "Alice é um filme antigo"

if "Alice" in txt:
    print ("A palavra Alice econtrase no texto") 

# Aqui usamos uma estrutura de condição que só responde se encontrar a palavra

txt = "Alice é um filme antigo"
print ("Filme Chuck" not in txt)

# Aqui imprimimos true caso a palavra não seja encontrada através do codigo 'not in'

# Você pode usar metodo upper() para retornar letras maiúsculas

a = "cross andrade oliveira?"
print (a.upper()) # vai retornar CROSS ANDRADE OLIVEIRA

# Ou letras minúsculas com metodo lower()

a = "RUA CRISTAL BAHIA CRISTAL"
print (a.lower())

# Você deve ter visto isso em formulários que retornavam seu texto em maiúsculas
# O metodo strip() é usado para remover os espaçamentos em branco

a = " Rua cristal, Bahia cristal   "
print(a.strip())

# Você também pode substituir strings com o metodo replace

a = "bom Dia"
print (a.replace("b","B"))

# Este tipo de código pode ajudar a criar um sistema de criptografia
# para embaralhar sua mensagem enviada na internet

# Você também pode concatenar strings

a = "Bom"
b = "Dia"
c = a + "" + b
print (c) # Retorna Bom Dia

# Não é possivel concatenar numero e string a menos que se use o f-string
# basta adicionar o f e usar {} para juntar string com números

a = 31
b = f"Sua idade é: {a} "
print(b)

# Em jogos que você jogou você pode adicionar seu nome no jogo e os npcs
# te chamam pelo nome durante as conversas graças a este código, seu nome
# fica salvo em uma variavel que é usada dentro das conversas.











