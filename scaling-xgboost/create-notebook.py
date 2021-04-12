import coiled

# Create cluster software environment
software_name = "examples/scaling-xgboost"
coiled.create_software_environment(
    name=software_name,
    conda="environment.yaml",
)

# Create notebook job software environment
software_notebook_name = software_name + "-notebook"
coiled.create_software_environment(
    name=software_notebook_name,
    container="coiled/notebook:latest",
    conda="environment.yaml",
)

coiled.create_job_configuration(
    name="examples/scaling-xgboost",
    software=software_notebook_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["scaling-xgboost.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Perform distributed training of an XGBoost classifier",
)
