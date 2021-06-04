import coiled

software_name = "examples/pytorch"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda="environment.yaml"
)

coiled.create_job_configuration(
    name="examples/pytorch",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["pytorch-example.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Learn how to use Dask and Coiled with PyTorch",
)
