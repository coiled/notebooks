import coiled

conda = {
    "channels": ["conda-forge"],
    "dependencies": [
        "dask>=2.23.0",
        "coiled=0.0.33 ",
        "pandas>=1.1.0",
        "xgboost",
        "dask-ml",
        "dask-xgboost",
        "scikit-learn",
        "s3fs",
        "python-snappy",
        "fastparquet",
        "matplotlib",
    ],
}

# Create cluster software environment
software_name = "examples/scaling-xgboost"
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
