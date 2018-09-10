import logging
from pathlib import Path

import click
from dotenv import find_dotenv, load_dotenv
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn import datasets


def train_model():
    logger = logging.getLogger(__name__)
    clf = SVC()
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    logger.info("Trained a SVC model on the iris dataset")
    return clf.fit(X, y)


def store_model(m, path):
    logger = logging.getLogger(__name__)
    joblib.dump(m, path)
    logger.info("Stored the model at {}".format(path))

@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    # type: (str, str)->None
    """ Trains the model, and stores the model in the provided output_path
    """
    logger = logging.getLogger(__name__)
    m = train_model()
    store_model(m, output_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
