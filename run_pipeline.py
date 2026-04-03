import papermill as pm
from pathlib import Path

PIPELINE_ORDER = [
    "notebooks/1.bronze/bronze_ordem_compras.ipynb"
]

for notebook in PIPELINE_ORDER:

    output_notebook = notebook.replace(
        ".ipynb",
        "_executed.ipynb"
    )

    print(f"executando {notebook}")

    pm.execute_notebook(
        notebook,
        output_notebook
    )

print("pipeline finalizado")