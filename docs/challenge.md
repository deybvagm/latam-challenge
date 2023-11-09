## Part I: selected model

The model to operationalize is the one in the experiment `6.b.iii` (Logistic Regression with feature importance and class balance) given these reasons:
- It has class balance which proves to have a positive effect
- It does not degrade the performance by reducing the number of features to the most important ones
- Both XGBoost and Logistic Regression with feature importance and class balance have similar scores (precision, recall and f1-score) given by the classification report but in many cases is preferable to opt by a simpler model which in this case is the Logistic Regression. It is true that looking at the confusion matrix it seems that the XGBoost seems to have a slightly better performance than Logistic Regression, but in overall it does not impact the classification metrics, Moreover if we are interested in the performance of the model for class 1, then Logistic Regression is a good model as there is almost no difference in the results for this class. Below is the evidence for this argument:
  * Precision for class 0: 0.88 for XGBoost, 0.88 for Logistic Regression.
  * Recall for class 0: 0.52 for XGBoost, 0.52 for Logistic Regression
  * F1-score for class 0: 0.66 for XGBoost, 0.65 for Logistic Regression
  * Precision for class 1: 0.25 for XGBoost, 0.25 for Logistic Regression.
  * Recall for class 1: 0.69 for XGBoost, 0.69 for Logistic Regression
  * F1-score for class 1: 0.37 for XGBoost, 0.36 for Logistic Regression
  * * Confusion matrix for XGBoost `[[9556, 8738],
       [1313, 2901]]`
  * Confusion matrix for Logistic Regression `[[9487, 8807],
       [1314, 2900]]`
