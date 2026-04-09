import papermill as pm
from pathlib import Path

PIPELINE_ORDER = [
    "notebooks/1.bronze/compras_ordens_itens.ipynb",
    "notebooks/1.bronze/compras_ordens.ipynb",
    "notebooks/1.bronze/estoques.ipynb",
    "notebooks/1.bronze/pedidos_itens.ipynb",
    "notebooks/1.bronze/pedidos.ipynb",
    "notebooks/1.bronze/pessoas.ipynb",
    "notebooks/1.bronze/produtos_estoques_movimentacoes.ipynb",
    "notebooks/1.bronze/produtos.ipynb",
    "notebooks/1.bronze/rel_compras_ordens_referenciadas_saldos.ipynb",

    "notebooks/2.silver/compras_ordens_itens.ipynb",
]

output_path = Path("notebooks/executed")
output_path.mkdir(parents=True, exist_ok=True)

for notebook in PIPELINE_ORDER:

    notebook_path = Path(notebook)

    output_notebook = output_path / f"{notebook_path.stem}_executed.ipynb"

    print(f"executando {notebook}")

    pm.execute_notebook(
        notebook_path,
        output_notebook
    )

print("pipeline finalizado")