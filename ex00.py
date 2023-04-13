dicionario = {'gato': 'chat', 'dog': 'chien', 'cavalo': 'cheval'}
palavras = ['gato', 'lion', 'cavalo']

for p in palavras:
    if p in dicionario:
        print(p, '->', dicionario[p])
    else:
        print(p, 'não esta no dicionario')