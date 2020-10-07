import coiled

conda = {
    "channels": ["conda-forge"],
    "dependencies": [
        "python=3.8",
        "coiled==0.0.25",
        "dask",
        "optuna",
        "numpy",
        "scikit-learn",
        "xgboost",
        "joblib",
    ],
}

software_name = "coiled-examples/optuna-xgboost-notebook"
coiled.create_software_environment(
    name=software_name,
    container="coiled/notebook:latest",
    conda=conda,
    pip=["dask-optuna"],
)

coiled.create_job_configuration(
    name="coiled/optuna",
    software=software_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["optuna-xgboost.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Hyperparameter optimization with Optuna",
)
