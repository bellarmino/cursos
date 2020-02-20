import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.\n\n")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    ''' Grau de similaridade é dado pela media da diferença absoluta entre cada traço linguístico'''
    somatorio = 0
    for i in range(0, 6):
        somatorio = somatorio + abs(as_a[i] - as_b[i])

    return (somatorio / 6)

def calcula_assinatura(texto):
    wal = tamanho_medio_palavra(texto)
    ttr = type_token(texto)
    hlr = hapax_legomana(texto)
    sal = tamanho_medio_sentenca(texto)
    sac = complexidade(texto)
    pal = tamanho_medio_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    qtdTextos = len(textos)

    assinaturas = []
    for i in range(0, qtdTextos):
        assinaturas.append(calcula_assinatura(textos[i]))

    similaridade = []
    for i in range(0, qtdTextos):
        similaridade.append(compara_assinatura(assinaturas[i], ass_cp))

    for i in range(0, qtdTextos):
        if similaridade[i] == min(similaridade):
            return (i+1)    

def lista_palavras(texto):
    sentencas = separa_sentencas(texto)
    qtdSentencas = len(sentencas)

    frases = []
    for i in range(0, qtdSentencas):
        frases.extend(separa_frases(sentencas[i]))
    qtdFrases = len(frases)

    palavras = []
    for i in range(0, qtdFrases):
        palavras.extend(separa_palavras(frases[i]))        

    return palavras

def qtd_frases(texto):
    sentencas = separa_sentencas(texto)
    qtdSentencas = len(sentencas)

    frases = []
    for i in range(0, qtdSentencas):
        frases.extend(separa_frases(sentencas[i]))
    qtdFrases = len(frases)

    return qtdFrases

def qtd_caracteres_texto(texto):
    palavras = lista_palavras(texto)
    
    qtd = len(palavras)
    caracteres = 0
    for i in range(0, qtd):
        caracteres += len(palavras[i])

    return caracteres

def tamanho_medio_palavra(texto):
    tamanho = qtd_caracteres_texto(texto)
    palavras = lista_palavras(texto)
    qtd = len(palavras)
    
    return (tamanho/qtd)

def type_token (texto):
    palavras = lista_palavras(texto)
    
    diferentes = n_palavras_diferentes(palavras)
    total = len(palavras)

    return (diferentes / total)
    
def hapax_legomana(texto):
    palavras = lista_palavras(texto)
    unicas = n_palavras_unicas(palavras)
    total = len(palavras)

    return (unicas / total)

def qtd_caracteres(lista):
    qtd = len(lista)
    caracteres = 0
    for i in range(0, qtd):
        caracteres += len(lista[i])

    return caracteres

def tamanho_medio_sentenca(texto):
    sentencas = separa_sentencas(texto)
    caracteres = qtd_caracteres(sentencas)

    return (caracteres / len(sentencas))

def complexidade(texto):
    qtdFrases = qtd_frases(texto)
    sentencas = separa_sentencas(texto)
    qtdSentencas = len(sentencas)

    return (qtdFrases / qtdSentencas)

def tamanho_medio_frase(texto):
    sentencas = separa_sentencas(texto)
    qtdSentencas = len(sentencas)
    
    frases = []
    for i in range(0, qtdSentencas):
        frases.extend(separa_frases(sentencas[i]))
    
    caracteres = qtd_caracteres(frases)
    qtdFrases = qtd_frases(texto)

    return (caracteres / qtdFrases)
    

def main():
    assinatura = le_assinatura()
    textos = le_textos()

    provavelCopia = avalia_textos(textos, assinatura)
    print('\nO autor do texto',provavelCopia,'está infectado com COH-PIAH')

main()
