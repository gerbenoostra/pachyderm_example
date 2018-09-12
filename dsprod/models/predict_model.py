import logging
import pandas as pd
import os
from sklearn.externals import joblib
import click


def predict_model(m, path):
    logger = logging.getLogger(__name__)
    logger.info("Predicting on {}".format(path))
    dataset = pd.read_csv(path).drop('Name', axis=1)
    results = m.predict(dataset)
    results = pd.DataFrame(data={"prediction": results, "index": dataset.index})
    return results


def load_model(path):
    logger = logging.getLogger(__name__)
    logger.info("Loading the model from {}".format(path))
    return joblib.load(path)


@click.command()
def main():
    # type: (str, str)->None
    """ Trains the model, and stores the model in the provided output_path
    """
    logger = logging.getLogger(__name__)
    m = load_model("models/model.p")
    for dirpath, dirs, files in os.walk("/pfs/iris"):
        for file in files:
            out = predict_model(m, os.path.join(dirpath, file))
            out.to_csv(os.path.join("/pfs/out/", file))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
