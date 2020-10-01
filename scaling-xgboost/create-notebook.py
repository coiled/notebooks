import coiled
import fsspec
import yaml

path = "https://raw.githubusercontent.com/coiled/coiled-examples/master/scaling-xgboost/environment.yml"
with fsspec.open(path, "r") as f:
    conda = yaml.safe_load(f.read())

software_name = "coiled-examples/scaling-xgboost-notebook"
coiled.delete_software_environment(name=software_name)
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda=conda,
    pip=["coiled==0.0.25"],
)

coiled.create_job_configuration(
    name="coiled/scaling-xgboost",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["scaling-xgboost.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Perform distributed training of an XGBoost classifier",
)
