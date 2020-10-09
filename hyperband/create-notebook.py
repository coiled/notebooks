import coiled

conda = {
    "channels": ["conda-forge", "pytorch", "defaults"],
    "dependencies": [
        "dask>=2.29.0",
        "coiled=0.0.26",
        "numpy",
        "pandas>=1.1.0",
        "dask-ml",
        "skorch",
        "scipy",
        "matplotlib",
        "pytorch>1.1.0",
        "s3fs",
    ],
}
software_name = "coiled-examples/hyperband-optimization"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda=conda,
)

coiled.create_job_configuration(
    name="coiled/hyperband-optimization",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=[
        "hyperband-optimization.ipynb",
        "torch_model.py",
        "workspace.json",
        "run.sh",
    ],
    ports=[8888],
    description="Tune a PyTorch model with Hyperband cross-validation",
)
