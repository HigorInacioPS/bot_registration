import pyautogui
import pandas as pd
import time
# Importar a Base de Produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)
pyautogui.PAUSE = 0.5
pyautogui.press("win") # - Apertar Botão do Windows (abrir "iniciar")
pyautogui.write("Chrome") # - Pesquisar pelo navegador Chrome
time.sleep(2)
pyautogui.press("enter") # - Acessar Chrome
time.sleep(3) # - Tempo de aguardo para carregamento da página
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # - Digitar Site
pyautogui.press("enter") # - Acessar Site
time.sleep(3) # - Tempo de carregamento
pyautogui.click(x=462, y=371) # - Clicar na área de e-mail
pyautogui.write("emailaleatorio@aleatorio.com") # - Digitar e-mail
pyautogui.press("tab") # Pular para sessão de senha
pyautogui.write("senhaqualquer") # - Escrever senha
pyautogui.press("tab") # - Ir para botão enter
pyautogui.press("enter") # - Acessar site
for linha in tabela.index:
    pyautogui.click(x=610, y=261) # - Clicar na primeira sessão de cadastramento
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # - Preenche a sessão de Código
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"])) # - Preenche a sessão de Marca
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"])) # - Preenche a sessão de Tipo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # Preenche a sessão de Categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # - Preenche a sessão de Preço
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"])) # - Preenche a sessão de Custo
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]): # - Evita preencher a sessão de Obs sem informação
        pyautogui.write(str(tabela.loc[linha, "obs"])) # - Preenche a sessão de Obs
    pyautogui.press("tab") # - Passa para a tecla de envio
    pyautogui.press("enter") # - Aperta o botão enter para enviar o cadastro
    pyautogui.scroll(50000)