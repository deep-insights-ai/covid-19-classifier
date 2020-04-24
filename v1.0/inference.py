from fastai2.vision.all import *

# REPLACE THIS MODEL WITH MOST UP TO DATE VERSION
MODEL = 'rn18-v-0.4-export.pkl'


def label_func():
    """dummy label function: loading model requires it despite never being used"""
    pass


LEARN = load_learner(MODEL)

CATEGORIES = LEARN.dls.vocab # classes in order of output neurons


def predict(img):
    """img: str or Path to image
    returns {category: probability}
    """
    y_hat, idx, probs = LEARN.predict(img)
    probabilities = [p.item() for p in probs]
    return dict(zip(CATEGORIES, probabilities))
