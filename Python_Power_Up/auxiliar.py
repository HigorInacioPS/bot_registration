import pyautogui
import time
import pandas as pd
time.sleep(5)
print(pyautogui.position())

# - for linha in tabela.index:  <- repete um procedimento (semelhante ao código "para" em portugol). "Para linha em tabela.indice".
# - index - "índice". No Python, cada linha de uma base de dados (tabela) é chamada de índice. Quando combinado "tabela" com "index", é informado ao Python que trabalhe em cima de cada linha da base nomeada como tabela.
# - linha é entendido pelo Python como uma "linha" após atribuição feita com o "tabela.index".
# - tabela.loc[] - Localiza uma informação ([] - é o padrão de localização de tabelas do pandas). 
# - Quando usado o tabela.loc[] é necessária a atribuição de uma linha e uma coluna - tabela.loc[linha, coluna]
# - Pode se informar apenas uma linha onde a atribuição ocorrerá numerando a mesma. Para que seja feita em todas as linhas, escreve-se apenas a palavra linha (como na atribuição feita pelo tabela.index anteriormente). De maneira análoga, pode se fazer uma atribuição de coluna, ou definir apenas uma coluna com o titulo da coluna posto entre aspas.
# - Textos no Python tem o nome de "string". A abreviação "str" transforma informações como por exemplo, números reais ou inteiros, em informações no formato de texto. str() - para utilizar a função pyautogui.write(), todas as informações devem ser em texto.
# - Em células vazias, caso a mesma esteja sendo localizada em alguma tabela dentro da função str(), a informação vazia será preenchida com o texto "nan", que em Python significa "not a number". A informação de "nan" é preenchida automaticamente na base de dados importada quando uma célula está vazia (pelo Pandas).
# - Para evitar o preenchimento da célula com o indicativo "nan", é possível usar a linha de código "if". Por exemplo -> if obs != "nan"
# - != significa "diferente"
pd.read
