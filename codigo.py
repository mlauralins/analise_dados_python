#Passo 1: Importar base de dados
import pandas as pd 
tabela = pd.read_csv("cancelamentos.csv")

#Passo 2: Visualizar a base de dados e suas informações gerais
print(tabela)
tabela.info()

#Passo 3: Tratar os dados
  #Excluir colunas inúteis
tabela = tabela.drop(columns="CustomerID", axis=1)
print(tabela)

  #Excluir os valores vazios
tabela = tabela.dropna()
tabela.info()

#Passo 4: Analisar os dados de forma geral
#Começar descobrindo quantas pessoas cancelaram e quantas não cancelaram
print(tabela["cancelou"].value_counts())

#percentual
print(tabela["cancelou"].value_counts(normalize=True))

#Criar grafico (abre no navegador)
import plotly.express as px

for coluna in tabela.columns:
  grafico=px.histogram(tabela, x=coluna, color="cancelou")
  grafico.show()

#Passo 5: Conclusões das análises

tabela = tabela[tabela["idade"]<=50]
print(tabela["cancelou"].value_counts())
#percentual
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["ligacoes_callcenter"]<=4]
print(tabela["cancelou"].value_counts())
#percentual
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts())
#percentual
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
print(tabela["cancelou"].value_counts())
#percentual
print(tabela["cancelou"].value_counts(normalize=True))