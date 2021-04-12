import coiled

software_name = "examples/jupyterlab-notebook"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda="environment.yaml",
)

coiled.create_job_configuration(
    name="examples/jupyterlab",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["jupyterlab.ipynb", "workspace.json", "run.sh", "dask-extension.png"],
    ports=[8888],
    description="See how Coiled integrates with JupyterLab",
)
