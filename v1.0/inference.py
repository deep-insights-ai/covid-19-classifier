from fastai2.vision.all import *

# REPLACE THIS MODEL WITH MOST UP TO DATE VERSION
MODEL = 'rn50-448px-v0.9-export.pkl'

LBL_PATHO = 'Non-COVID'
LBL_COV = 'COVID'


# when loading the model for inference, the fastai learner requires
# that the functions which were used during training exist
# in the same namespace, even if not used, hence the definition here
def get_lbl(fname):
    """return the label of given image"""
    lbl = fname.parent.name
    if lbl == 'P':
        return LBL_PATHO
    elif lbl == 'C':
        return LBL_COV
    else:
        raise ValueError(f'could not extract label from {fname}')


def in_valid(fname):
    """return True if file in validationset, else False"""
    return fname.parent.parent.name == 'valid'


LEARN = load_learner(MODEL)

CATEGORIES = LEARN.dls.vocab  # classes in order of output neurons


def predict(img):
    """img: str or Path to image
    returns {category: probability}
    """
    y_hat, idx, probs = LEARN.predict(img)
    probabilities = [p.item() for p in probs]
    return dict(zip(CATEGORIES, probabilities))


if __name__ == "__main__":
    img = '<TODO: add img path to img in repo, (relative path names are great)'
    print(f'classifying image {img}:')
    print(predict(img))
