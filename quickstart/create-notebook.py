import coiled

software_name = "examples/quickstart-notebook"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    pip=["coiled==0.0.27"]
)

coiled.create_job_configuration(
    name="coiled/quickstart",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["quickstart.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Quickly launch a Dask cluster on the cloud with Coiled",
)
