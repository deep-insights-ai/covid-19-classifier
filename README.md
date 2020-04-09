# covid-19-classifier

A [fastai2](https://www.fast.ai/) based Covid-19 classifier.

This Covid-19-classifier is a Deep Learning based image classifier which is able to categorize lung X-rays as well as CT Scans as either COVID-19, PNEUMONIA (which groups together MERS, viral pneumonia and other diseases), or as NORMAL (non-pathological) lungs scans.
Our **accuracy is 98.3%**. To the best of our knowledge this beats all previous Covid-19 lung radiology AI classifiers. 


Please see the [methodology page](https://labs.deep-insights.ai/methodology.html) for more details how we achieved this high detection rate.

# Open Source

We believe that this project needs to be open source! Open source allows us to:
  * make sure you can reproduce our results
  * make sure that you can actively deploy our project in your country (without license fees) __in order to help patients now__
  * get constructive feedback from you (pull requests welcome!)
  * make sure you can validate our research
  * build on top of the best of the internet to further improve this project.
  
  
# Installation

Here is how to get started:

## Jupyter notebooks

Please first follow the [installation guides](https://github.com/fastai/fastai2) of fastai version 2 to get fastai running upfront.

Next, make sure you can execute jupyter notebooks.

Then start jupyter-notebooks:
```bash
cd v0.4/
jupyter-notebook cov-19-training.ipynb      # for training
# ... or
jupyter-notebook inference.py
```

## Server

<XXX coming XXX>

