import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.data import apply_label
from ml.model import compute_model_metrics, train_model


def test_apply_label():
    """Test that binary predictions are converted to expected labels."""
    assert apply_label(np.array([1])) == ">50K"
    assert apply_label(np.array([0])) == "<=50K"


def test_train_model():
    """Test that train_model returns a RandomForestClassifier."""
    X_train = np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ]
    )
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


def test_compute_model_metrics():
    """Test metrics against known classification results."""
    y = np.array([0, 0, 1, 1])
    preds = np.array([0, 1, 1, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert np.isclose(precision, 2 / 3)
    assert np.isclose(recall, 1.0)
    assert np.isclose(fbeta, 0.8)