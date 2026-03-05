import pyautogui as pt
import pandas as pd

tabela_produtos = pd.read_csv("produtos.csv")
link_site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pt.PAUSE = 0.5

# Abrir o navegador e acessar o site
pt.press('win')
pt.write('chrome')
pt.press('enter')
pt.click(x=850, y=650)
pt.click(x=850, y=420)
pt.write(link_site)
pt.press('enter')
pt.sleep(2)
# Fazer login
pt.press('tab')
pt.write('aluno')
pt.press('tab')
pt.write('hashtag')
pt.press('enter')
pt.sleep(2)
#Inserir os produtos
pt.PAUSE = 0.1
for linha in tabela_produtos.index:
    codigo_produto = str(tabela_produtos.loc[linha, "codigo"])
    marca_produto = str(tabela_produtos.loc[linha, "marca"])
    tipo_produto = str(tabela_produtos.loc[linha, "tipo"])
    categoria_produto = str(tabela_produtos.loc[linha, "categoria"])
    preco_unitario_produto = str(tabela_produtos.loc[linha, "preco_unitario"])
    custo_produto = str(tabela_produtos.loc[linha, "custo"])
    obs_produto = str(tabela_produtos.loc[linha, "obs"])
    pt.click(x=950, y=300)
    pt.write(codigo_produto)
    pt.press('tab')
    pt.write(marca_produto)
    pt.press('tab')
    pt.write(tipo_produto)
    pt.press('tab')
    pt.write(categoria_produto)
    pt.press('tab')
    pt.write(preco_unitario_produto)
    pt.press('tab')
    pt.write(custo_produto)
    pt.press('tab')
    if obs_produto != 'nan':
        pt.write(obs_produto)
    pt.press('tab')
    pt.press('enter')

print("Processo finalizado")