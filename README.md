# covid-19-classifier

A [fastai2](https://www.fast.ai/) based Covid-19 classifier.

**Homepage**: https://labs.deep-insights.ai

# Summary

This Covid-19-classifier is a Deep Learning based image classifier which is able to categorize lung CT Scans as either COVID, or Non-COVID (which groups together a range of diseases such as viral pneumonia, bacterial pneumonia, abscess, lipoid pneumonia, idiopathic pulmonary fibrosis, lung cancer and other diseases).
**The accuracy on our validation set is 94.5%, and on our more difficult testset which contains more hard to distinguish cases the accuracy is 88.9%**. 

Our very latest model can always be downloaded [here](https://labs.deep-insights.ai/models/latest.pkl). 

Please see the [methodology page](https://labs.deep-insights.ai/methodology.html) for more details on how we achieved this high detection rate.

# Accuracy

```
VALIDATION SET:
stats for COVID
========================================
sensitivity: 0.918918918918919
specificity: 0.9660056657223796
positive predictive value (= precision): 0.9577464788732394
negative predictive value: 0.9342465753424658
accuracy: 0.9445300462249615
```

```
TEST SET:
stats for COVID
========================================
sensitivity: 0.8444444444444444
specificity: 0.9333333333333333
positive predictive value (= precision): 0.926829268292683
negative predictive value: 0.8571428571428571
accuracy: 0.8888888888888888
```

![accuracy.png](static/accuracy.png)

## Confusion matrix

![confusion-matrix.png](static/confusion-matrix.png)

## Training and validation loss

![training-and-validation-loss.png](static/training-and-validation-loss.png)


# Open Source

We believe that this project needs to be open source! Open source allows us to:
  * make sure that you can reproduce our results
  * make sure that you can actively deploy our project in your country (without license fees) __in order to help patients now__
  * get constructive feedback from you (pull requests welcome!)
  * make sure that you can validate our research
  * build on top of the best of the internet to further improve this project.
  
  
# Installation

## Prerequisites

Required for training as well as inference (classification of images):
  * fastai2

If you want to run our jupyter notebook and train the model yourself:
  * jupyter notebook

Here is how to get started:

### Fastai2

At the moment of writing (April 2020) the easiest installation method for fastai version 2 is:
```bash
pip install fastai2
```
Later in 2020, with the release of the new [course](https://course.fast.ai/) on [fast.ai](https://www.fast.ai/) the original fastai library will be updated to version 2. We are already using this newer version 2.
For more information and additional installation instructions (e.g. via conda) please see the github repos for:

[fastai](https://github.com/fastai/fastai)

[fastai version 2](https://github.com/fastai/fastai2)


### Jupyter notebooks

If you only want to use our model for inference you don't need Jupyter notebooks.
But if you want to play around with our training notebook and train the model yourself, perhaps on your own data,
then we recommend to install jupyter notebook for quick experimentations.

To install jupyter notebooks please follow the [installation guides](https://jupyter.org/install) and make sure you are able to run jupyter notebooks.

# Running our code

## Training

Run the training notebook:
```bash
cd v0.8/
jupyter-notebook training.ipynb
```

**NOTE**: if you want to train a model yourself we heavily recommend you have access to a GPU as this will speed up training times drastically compared to running it on the CPU. Sadly, only nVidia GPUs are currently supported.
If you do not have access to a nVidia GPU we recommend a free service like [Kaggle](https://www.kaggle.com/) which gives anyone 30 hours of GPU compute time per week, which is more than enough to train a state of the art image classifier thanks to transfer learning.

## Inference (classifying images)

See the [inference](https://github.com/deep-insights-ai/covid-19-classifier/blob/master/v0.8/inference.py) example.
