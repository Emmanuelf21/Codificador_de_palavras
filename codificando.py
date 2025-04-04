# PERGUNTAS
# O que ord() faz em Python?
# Ele transforma as letras nos seus respectivos números localizados na tabela ASCII

# O que chr() faz?
# Transforma os números em seus respectivos caracteres localizados na tabela ASCII

# Como transformar uma string em uma lista de letras? (ex: list("texto"))
# É possível percorrer uma string utilizando a função 'map' e utilizar 'list' para transformar em lista list(map(variavel))

# O que são f-strings? Dê um exemplo com variáveis.
# É uma ferramento do Python para formatar strings: print(f'\nPalavras codificadas: {codigo1} {codigo2} {codigo3}')

# Como acessar letras específicas de uma string com índice (palavra[0], etc)?
# Uma String pode ser tratada da mesma forma que um array desde que esteja atribuída a uma variável, 
# basta passar o índice para acessar cada letra,
# palavra[0], neste caso, o '0' é o índice e 'palavra' é uma variável

# O que acontece se tentarmos acessar uma letra que não existe (ex: palavra[6] em uma palavra com só 4 letras)?
# O programa retornará um erro por não existir nada no índice indicado

# O que é a  tabela ASCII.?
# A tabela ASCII coloca todos os caracteres em uma tabela e enumera cada um deles, além disso têm seu código Hexadecimal

palavra1 = input('Digite a primeira palavra (até 5 letras): ')
palavra2 = input('Digite a segunda palavra (até 5 letras): ')
palavra3 = input('Digite a terceira palavra (até 5 letras): ')
palavraCod = input('Digite uma palavra codificada (até 5 letras): ')

def codigoPalavras(palavra1, palavra2, palavra3, palavraCod):
    if(len(palavra1)==5 and len(palavra2)==5 and len(palavra3)==5 and len(palavraCod)==5):
        codigo1 = ''.join(tuple(map(getLetrasCodificadas,palavra1)))
        codigo2 = ''.join(tuple(map(getLetrasCodificadas, palavra2)))
        codigo3 = ''.join(tuple(map(getLetrasCodificadas, palavra3)))

        print(f'\nMensagem codificada: {codigo1} {codigo2} {codigo3}')
        descodificar(palavraCod)
    else:
        print('Palavra(s) não contêm 5 letras!')

def getLetrasCodificadas(letra):
    return chr(ord(letra)+1)

def descodificar(palavraCod):
    descodificado = ''.join(tuple(map(getPalavra, palavraCod)))
    print(f'Palavra Descodificada: {descodificado}')
    
def getPalavra(letraCod):
    return chr(ord(letraCod)-1)

codigoPalavras(palavra1, palavra2, palavra3, palavraCod)