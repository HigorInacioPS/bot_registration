# Bot de Automação para Registro de Produtos

Este projeto consiste em um **bot de automação** que simula o processo de **cadastro de produtos** em um sistema web de uma empresa fictícia. O script automatiza as ações de abrir o navegador, realizar o login e registrar os produtos um a um a partir de uma base de dados.

## 🧠 Objetivo

Automatizar o processo repetitivo de cadastro de produtos para fins de estudo em **automação com Python**, utilizando a biblioteca `pyautogui`.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

| Biblioteca   | Finalidade                                      |
|--------------|--------------------------------------------------|
| `pandas`     | Leitura da base de dados de produtos (CSV)       |
| `pyautogui`  | Automação do teclado e mouse                      |
| `time`       | Gerenciamento de pausas e delays entre ações     |

> ✅ Observação: recomenda-se usar **Python 3.12.3** para evitar problemas de compatibilidade.

## 📂 Arquivos

- `bot_register.py` — Script principal da automação.
- `produtos.csv` — Base de dados com os produtos a serem cadastrados.
- `take_mouse_position.py` — Script auxiliar para capturar as coordenadas do mouse (utilizado para configurar os cliques no navegador).

## 🔗 Site de Testes

A automação foi projetada para funcionar em um site disponibilizado pela empresa **Hashtag Programação**, acessado via:

```
https://dlp.hashtagtreinamentos.com/python/intensivao/login
```

> ⚠️ **Nota:** Este site pode ficar **indisponível** ou **fora do ar** eventualmente, pois é parte de um ambiente de testes temporário.

## 🚀 Como Executar

1. Garanta que as bibliotecas estão instaladas:
```bash
pip install -r requirements.txt
```

2. Abra o terminal e execute o script auxiliar para capturar posições do mouse (opcional):
```bash
python take_mouse_position.py
```

3. Execute o bot principal:
```bash
python bot_register.py
```

> 🖱️ O mouse será controlado automaticamente. **Não mova o cursor ou interaja com o computador** durante a execução.

## ✅ Considerações

- A base de dados deve estar no mesmo diretório que o script principal, com o nome `produtos.csv`.
- É importante testar as posições do mouse com o script auxiliar para garantir que os cliques aconteçam corretamente em seu ambiente.

## ✍️ Autor

- Nome: *[Seu nome aqui]*
- Projeto criado para fins educacionais com foco em automação e uso do `pyautogui`.