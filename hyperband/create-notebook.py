import coiled
import yaml

software_name = "coiled-examples/hyperband-optimization"
coiled.delete_software_environment(name=software_name)
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda="environment.yml",
)

coiled.create_job_configuration(
    name="coiled/hyperband-optimization",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["hyperband-optimization.ipynb", "torch_model.py", "workspace.json", "run.sh"],
    ports=[8888],
    description="Tune a PyTorch model with Hyperband cross-validation",
)
