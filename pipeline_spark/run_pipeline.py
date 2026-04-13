import papermill as pm
from pathlib import Path

PIPELINE_ORDER = [
    "pipeline_spark/notebooks/1.bronze/compras_ordens_itens.ipynb",
    "pipeline_spark/notebooks/1.bronze/compras_ordens.ipynb",
    "pipeline_spark/notebooks/1.bronze/estoques.ipynb",
    "pipeline_spark/notebooks/1.bronze/pedidos_itens.ipynb",
    "pipeline_spark/notebooks/1.bronze/pedidos.ipynb",
    "pipeline_spark/notebooks/1.bronze/pessoas.ipynb",
    "pipeline_spark/notebooks/1.bronze/produtos_estoques_movimentacoes.ipynb",
    "pipeline_spark/notebooks/1.bronze/produtos.ipynb",
    "pipeline_spark/notebooks/1.bronze/rel_compras_ordens_referenciadas_saldos.ipynb",

    "pipeline_spark/notebooks/2.silver/compras_ordens_itens.ipynb",
    "pipeline_spark/notebooks/2.silver/compras_ordens.ipynb",
    "pipeline_spark/notebooks/2.silver/estoques.ipynb",
    "pipeline_spark/notebooks/2.silver/pedidos_itens.ipynb",
    "pipeline_spark/notebooks/2.silver/pedidos.ipynb",
    "pipeline_spark/notebooks/2.silver/pessoas.ipynb",
    "pipeline_spark/notebooks/2.silver/produtos_estoques_movimentacoes.ipynb",
    "pipeline_spark/notebooks/2.silver/produtos.ipynb",
    "pipeline_spark/notebooks/2.silver/rel_compras_ordens_referenciadas_saldos.ipynb",

    "pipeline_spark/notebooks/3.gold/saldos_oc.ipynb",
    "pipeline_spark/notebooks/3.gold/pedidos_ordem_compras.ipynb"
]

output_path = Path("pipeline_spark/notebooks/executed")
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