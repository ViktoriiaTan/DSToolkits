# Milestone 4 Report

## Task 1

**What is Experiment Management and why is it important?**

Experiment management is a systematic process that involves tracking and organising critical experiment metadata.  
This includes:
- Keeping track of different versions of the code used in various experiments;
- Documenting the versions of datasets utilised in training and evaluation;
- Recording the hyperparameter settings for each experiment;
- Documenting the computational environment, including software and hardware configuration;
- Logging key metrics that measure the performance of models.  

The main purpose of experiment management is to organise this information set in a meaningful way, to facilitate access, analysis and collaboration across the organisation. It ensures that experiments are reproducible, scalable and easily understandable by different team members, thereby fostering a collaborative and productive research environment.

**What is a Metric in ML?**

In Machine Learning, a Metric is a quantifiable measure used to evaluate and assess the performance of a ML model. They're a key element of every machine learning pipeline, allowing developers to fine-tune their algorithms and drive improvements.  
Metrics provide a way to objectively measure the effectiveness of a model in making predictions or classifications and they vary depending on the specific task (classification/ regression) that the model is designed for.

**What is Precision and Recall? Why is there often a Trade-off between them?**

*Precision*, or positive predictive value is the ratio of the True Positive (TP) values to all positive (TP + FP) values. It measures the accuracy of the positive predictions made by the classifier. High precision indicates that the model is likely to be correctly classifying positive instances.

*Recall* is a measure for identifying the True Positives correctly. It is calculated by dividing the True Positive (TP) values by the sum of True Positives and False Negatives (TP + FN)


Improving one usually costs the other metric: to improve Precision, False Positive instances should be reduced, while Recall can be improved by reducing False Negatives. This trade-off is particularly evident in situations where the classes are imbalanced.

In case there is a need to consider both false positives and false negatives, the *F1 score* can be introduced, which combines them into a single value. It is the harmonic mean of Precision and Recall.
The formula is the following: F1 Score = 2 * (Precision * Recall) / (Precision + Recall)


**What is AUC-ROC Metric?**

AUC - ROC curve is a performance measurement for the classification problems at various threshold settings.  
ROC is a probability curve and AUC represents the degree or measure of separability. It tells how much the model is capable of distinguishing between classes.   
Higher the AUC, the better the model is at predicting 0 classes as 0 and 1 classes as 1.

**What is a Confusion Matrix?**

The Confusion Matrix is used to evaluate the performance of a classification model. Having N classes to classify into, the matrix takes the shape of NxN.
In the case of a binary classifier, it is a 2x2 matrix and the cells are the following: 


|                | Actual Positive | Actual Negative |
|----------------|------------------|------------------|
| Predicted Positive |        TP                |        FP                |
| Predicted Negative |        FN                |        TN                |



## Task 2

## Task 3
