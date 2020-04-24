

(please add newer changelog messages to the top of this file)

(Note that you can always get the latest model at  https://labs.deep-insights.ai/models/latest.pkl).

# version 0.8  (2020/4/24)

This is the final model for the paper.

* model is a resnet50, pixelsize 448x448
* model now achieves the following accuracy, sensitivity and specificity on the validation set:

|----------------|---------------|---------|------------|
|                | precision     | recall  | f1-score   |
| COVID          |   0.96        | 0.92    | 0.94       |
| Non-COVID      | 0.93          | 0.97    | 0.95       |


* and on the independent test set:
```
sensitivity: 84.44%
specificity: 93.33%
precision: 92.68%
negative predictive value: 85.71%
accuracy: 88.88%
```

The model can be downloaded at https://labs.deep-insights.ai/models/rn50-448px-v0.8-export.pkl. 
