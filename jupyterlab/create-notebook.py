import coiled

conda = {
    "channels": ["conda-forge"],
    "dependencies": [
        "python=3.8",
        "traitlets=5.0.4",
        "coiled=0.0.36",
    ],
}
software_name = "examples/jupyterlab-notebook"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda=conda,
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
    description="See how Coiled intergrates with JupyterLab",
)
