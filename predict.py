from fastai.vision.all import *
from fastai.vision.widgets import *
import pathlib
from pathlib import Path

def get_prediction(img):
    path = Path()
    learn_inf = load_learner(path/'export.pkl')
    img = PILImage.create(img)
    pred,pred_idx,probs = learn_inf.predict(img)
    result = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'
    return result