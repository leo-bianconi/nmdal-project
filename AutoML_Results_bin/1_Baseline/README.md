# Summary of 1_Baseline

[<< Go back](../README.md)


## Baseline Classifier (Baseline)
- **n_jobs**: -1
- **num_class**: 4
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.6 seconds

### Metric details
|           |   0 |          1 |   2 |   3 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|----:|-----------:|----:|----:|-----------:|------------:|---------------:|----------:|
| precision |   0 |   0.368263 |   0 |   0 |   0.368263 |   0.0920659 |       0.135618 |   1.31166 |
| recall    |   0 |   1        |   0 |   0 |   0.368263 |   0.25      |       0.368263 |   1.31166 |
| f1-score  |   0 |   0.538293 |   0 |   0 |   0.368263 |   0.134573  |       0.198234 |   1.31166 |
| support   | 102 | 123        |  41 |  68 |   0.368263 | 334         |     334        |   1.31166 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |                0 |              102 |                0 |                0 |
| Labeled as 1 |                0 |              123 |                0 |                0 |
| Labeled as 2 |                0 |               41 |                0 |                0 |
| Labeled as 3 |                0 |               68 |                0 |                0 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
