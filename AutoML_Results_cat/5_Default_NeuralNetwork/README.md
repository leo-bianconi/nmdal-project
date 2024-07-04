# Summary of 5_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
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

1.8 seconds

### Metric details
|           |          0 |          1 |   2 |   3 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|-----------:|-----------:|----:|----:|-----------:|------------:|---------------:|----------:|
| precision |   0.270073 |   0.365482 |   0 |   0 |   0.326347 |    0.158889 |       0.220354 |    1.3218 |
| recall    |   0.362745 |   0.571429 |   0 |   0 |   0.326347 |    0.233543 |       0.326347 |    1.3218 |
| f1-score  |   0.309623 |   0.44582  |   0 |   0 |   0.326347 |    0.188861 |       0.262739 |    1.3218 |
| support   | 102        | 126        |  42 |  64 |   0.326347 |  334        |     334        |    1.3218 |


## Confusion matrix
|              |   Predicted as 0 |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 0 |               37 |               65 |                0 |                0 |
| Labeled as 1 |               54 |               72 |                0 |                0 |
| Labeled as 2 |               22 |               20 |                0 |                0 |
| Labeled as 3 |               24 |               40 |                0 |                0 |

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
