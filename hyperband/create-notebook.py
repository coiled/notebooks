import coiled

conda = {
    "channels": ["conda-forge", "pytorch", "defaults"],
    "dependencies": [
        "python=3.8",
        "dask=2021.3.0",
        "coiled=0.0.38",
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

# Create cluster software environment
software_name = "examples/hyperband-optimization"
coiled.create_software_environment(
    name=software_name,
    conda=conda,
)

# Create notebook job software environment
software_notebook_name = software_name + "-notebook"
coiled.create_software_environment(
    name=software_notebook_name,
    container="coiled/notebook:latest",
    conda=conda,
)

coiled.create_job_configuration(
    name="examples/hyperband-optimization",
    software=software_notebook_name,
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
