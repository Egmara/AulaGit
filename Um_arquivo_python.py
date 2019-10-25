# Exemplo de dicionario em python

#dados = dict()
dados1 = {'nome': Pedro, 'idade': 24}
dados2 = {'nome': Pedro, 'idade': 24}

# mostra dados
print(dados1['nome'])
print(dados1.values())
print(dados1.keys())
print(dados1.items())

for k,v in dados1.items():
    print(f'o {k} é {v}')

# guarda numa lista
pessoas = []
pessoas.append(dados1)
pessoas.append(dados2) 
