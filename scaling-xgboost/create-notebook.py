import coiled

conda = {
    "channels": ["conda-forge"],
    "dependencies": [
        "dask>=2.23.0",
        "coiled=0.0.26",
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

software_name = "coiled-examples/scaling-xgboost-notebook"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda=conda,
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
