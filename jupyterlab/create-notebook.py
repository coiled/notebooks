import coiled

software_name = "coiled-examples/jupyterlab-notebook"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda={
        "channels": ["conda-forge"],
        "dependencies": ["coiled==0.0.26", "traitlets==5.0.4"],
    },
)

coiled.create_job_configuration(
    name="coiled/jupyterlab",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["jupyterlab.ipynb", "workspace.json", "run.sh", "dask-extension.png"],
    ports=[8888],
    description="See how Coiled intergrates with JupyterLab",
)
