#Importar as biblotecas 
import json
import pandas as pd # type: ignore

#Arquivo vendas
baseDeDados = open('dados/vendas.json')

#data
dadosTratados = json.load(baseDeDados)

#print(dadosTratados)
df = pd.DataFrame.from_dict(dadosTratados)
print(df)

baseDeDados.close()