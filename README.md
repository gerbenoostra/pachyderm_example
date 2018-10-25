Pachyderm example
==============================

An example project used to test how Pachyderm works, resulting in the following [Blogpost on medium](https://medium.com/bigdatarepublic/pachyderm-for-data-scientists-d1d1dff3a2fa)

The project structure has been taken from our own [BigData republic cookiecutter data science project](https://github.com/BigDataRepublic/cookiecutter-data-science).
For clarity all unused folders have been removed.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── environment.yml    <- The conda environment file to reproduce the analysis environment. eg.
    │                         `conda env create -f environment.yml`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so dsprod can be imported
    ├── dsprod                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes dsprod a Python module
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py


--------

## Getting started:

One should be up and running as follows:

    make create_environment
    source activate hackathon_ds_to_prod

This will create & activate the anaconda environment.
Any other command will verify that the `environment.yml` file has not changed.
Otherwise it will update the environment.
You can update the environment manually using:

    make requirements

Creating the pickle file should be as easy as:

    make model

### Shortcut creating the environment using conda 
Instead of using make, it's also possible to setup the required environment manually:

    conda env create -f environment.yml

## Setting up pachyderm

To get a working instance of pachyderm, one can start with:

    brew cask install minikube
    brew install kubectl
    minikube start
    brew tap pachyderm/tap
    brew install pachyderm/tap/pachctl@1.7
    pachctl deploy local

Repeatedly run the following, until every pod is up and running:

    kubectl get all

Then it's possible to start the `pachctl` daemon (also hosts the Pachdash dashboard):

    pachctl port-forward
 
## Testing pachyderm

One can test this project agains an existing Pachyderm cluster as follows:

    pachctl create-repo iris
    pachctl put-file iris master /raw/iris_1.csv  -f data/raw/iris_1.csv
    docker build . --tag gerbeno/iris:1538732911
    docker login
    docker build . --tag gerbeno/iris:1538732911
    pachctl create-pipeline -f iris.json
    pachctl put-file iris master /raw/iris_2.csv  -f data/raw/iris_2.csv

If you have changed the code/docker image, you need to run  

    docker build . --tag gerbeno/iris:`date +%s`

Copy the tag, and use it in place of `[tag]` in the next commands.
But first update the file `iris.json` to hold the new tag.
Then:

    docker push gerbeno/iris:[tag]
    pachctl update-pipeline -f iris.json

To reprocess the files again:

    pachctl update-pipeline -f iris.json --reprocess    

### Installing Python module as egg
If you want to reuse the code developed in other projects, you can install an egg directly from your checkout:

    pip install -e .


<p><small>Project based on the <a target="_blank" href="https://github.com/BigDataRepublic/cookiecutter-data-science">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
