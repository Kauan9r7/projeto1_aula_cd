# Analise de Vendas de Videogames

Trabalho em grupo da disciplina **Introducao a Ciencia de Dados** com uma analise exploratoria da base **Video Game Sales** em um Jupyter Notebook.

Esta pasta foi reduzida para conter apenas o necessario:

- `README.md`
- `vgsales_analise.ipynb`

## Base de dados

O notebook usa a base `gregorut/videogamesales`, baixada via `kagglehub`.

```python
import kagglehub
from pathlib import Path
import pandas as pd

path = Path(kagglehub.dataset_download("gregorut/videogamesales"))
df = pd.read_csv(path / "vgsales.csv")
```

Se precisar instalar as dependencias:

```bash
pip install kagglehub pandas matplotlib seaborn jupyter
```

## O que o notebook responde

1. Quais sao os 10 jogos mais vendidos globalmente?
2. Qual genero gera mais vendas globais?
3. Como o mercado evoluiu ao longo dos anos?
4. Quais plataformas dominaram historicamente?
5. Como as vendas se distribuem entre as regioes?
6. Quais publishers lideram em vendas globais?
7. Cada regiao do mundo prefere um genero diferente?

## Como abrir

Abra `vgsales_analise.ipynb` no Jupyter, VS Code ou diretamente pelo GitHub.

- Notebook no repositorio: https://github.com/Kauan9r7/Ciencias_de_Dados_projetos/blob/master/analise-vgsales/vgsales_analise.ipynb
- Pagina dedicada do projeto: https://kauan9r7.github.io/Ciencias_de_Dados_projetos/analise-vgsales.html

## Observacoes sobre a base

- A base cobre vendas fisicas e nao representa todo o mercado digital moderno.
- Os anos finais do dataset tem menos registros e devem ser interpretados com cuidado.
- O notebook mantem o foco em analise exploratoria e interpretacao visual.
