from dsprod.models.predict_model import load_model, predict_model


def test_predict():
    m = load_model("models/model.p")
    predict_model(m, "data/raw/iris_1.csv")
