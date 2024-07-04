# Summary of 6_Default_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
- **eval_metric_name**: logloss
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

4.8 seconds

### Metric details
|           |          0 |          1 |   2 |          3 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|-----------:|-----------:|----:|-----------:|-----------:|------------:|---------------:|----------:|
| precision |   0.428571 |   0.419847 |   0 |  0.2       |    0.41018 |    0.262105 |       0.32759  |   1.29847 |
| recall    |   0.235294 |   0.873016 |   0 |  0.046875  |    0.41018 |    0.288796 |       0.41018  |   1.29847 |
| f1-score  |   0.303797 |   0.56701  |   0 |  0.0759494 |    0.41018 |    0.236689 |       0.321232 |   1.29847 |
| support   | 102        | 126        |  42 | 64         |    0.41018 |  334        |     334        |   1.29847 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |               24 |               74 |                0 |                4 |
| Labeled as 1 |               12 |              110 |                0 |                4 |
| Labeled as 2 |                6 |               32 |                0 |                4 |
| Labeled as 3 |               14 |               46 |                1 |                3 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
