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

Link to our [W&B Project](https://wandb.ai/tantsuraviktoria/mnist_digit_classification?workspace=user-tantsuraviktoria)

To accomplish Task 2, we started by creating a new Dockerfile, specifically designed to integrate seamlessly with Weights & Biases (W&B). This new Dockerfile, similar to our previous version, focuses on incorporating all necessary dependencies for W&B.   
A key feature of this update is the addition of the docker_entrypoint.sh script. This script is configured to automatically execute at the start of our Docker container, where it efficiently loads the W&B token from a .env file and sets it as an environment variable.  
To ensure security and confidentiality, we added the .env file to our .gitignore, preventing it from being tracked in our Git repository.  

**Requirements and script updates:**

The requirement file was updated to include wandb and scikit-learn packages with fixed versions.

|   Package  | Version |                             SHA256                             |
|------------|---------|----------------------------------------------------------------|
|   wandb    |0.16.2   |6b119cf3c01f35e7276b62d052128e5320621d182c9eb5796a12cf62a9b3134f|
|scikit-learn| 1.4.0   |c408b46b2fd61952d519ea1af2f8f0a7a703e1433923ab1704c4131520b2083b|

We made several updates to the 1_main.py script:
- We removed the database connection feature from our previous task, as it was no longer required.
- A new project named mnist_digit_classification was set up in W&B.
- To monitor our model's performance during training and relaying this information to W&B, we used a function WandbCallback().
- After the training phase, we also saved the model on W&B using wandb.save("model.h5").  

For **model evaluation**, since we are working on multi-class classification problem, we initially chose **accuracy** because it gives a quick idea of how well model is performing overall by showing the proportion of correctly predicted instances out of all predictions.This is particularly relevant in a well-balanced dataset like our MNIST, where each class (digit) is roughly equally represented.  
However, we recognized that accuracy alone doesn’t account for the type of errors made by the model. So, we also decided to include more complex metrics for a comprehensive evaluation(F1 score, confusion matrix).   
The **F1 score**, a single metric balancing both false positives and false negatives, was selected for its ability to provide a more nuanced understanding of the model's performance.  
Additionally, we used a **confusion matrix** for a detailed breakdown of where our model is making correct and incorrect predictions, to understand the model's performance across different classes.  

We updated the training module by adding a "callbacks" parameter the same as for main script and added history tracking for capturing the training and validation results of each epoch in the "history" variable, providing a complete record of the model's progress throughout training.  

**Experimentation with parameters**

We experimented with various aspects of our neural network to observe the effects on model performance.
We tried adding a new layer, changing batch sizes to 256 and 64, and switching the optimizer to SGD and  learning rate to 0.01.  
These changes let us see how they affected the model.  
We observed that modifications to the learning rate and optimizer with increase in batch size (to 256) resulted in a noticeable decrease in both the F1 score and accuracy compared to the original configuration and other tested variants.  
On the other hand, adjustments such as changing the batch size and adding an additional layer to the network architecture led to only minor changes in these performance metrics.
 
**Uploading model predictions to W&B**  

Given the multi-class nature of the task, predictions were in a one-hot encoded format. To make them more interpretable, we used np.argmax to transform each prediction into a class index, representing the most likely class for each input. Next, we created a W&B artifact, added the transformed predictions as a wandb.Table to this artifact and, finally, uploaded it to W&B.  

At the end, we added **logging the Git commit hash in W&B**.  
This was achieved by first creating a shell script to get the Git commit hash. Then, we updated the Dockerfile and the docker-entrypoint to enable the process of retrieving and logging the Git commit hash. We also updated main.py to include the code necessary for fetching and logging this information.  
Initially, this setup didn't work. But, after realizing that the .git folder was included in .dockerignore, we removed it from there. This change fixed the issue, and now the logging of the Git commit hash in W&B works as should.

## Task 3

We created the exploratory Jupyter Notebook to analyze the [MNIST](https://www.tensorflow.org/datasets/catalog/mnist) dataset, which we have been working with for these projects. 

The notebook 
- display a sample of images, 
- explores the dimensions, 
- explores the distribution of the labels,
- displays the distribution of the pixel values (greyscale, 0-255),
- averages the pixel intensity by category, creating an "average picture" of the category,
- shows the variety of the images withing one category.

Furthermore, we wanted to try the same tasks on a colored (RGB) dataset, for which we chose the [CIFAR-10](https://www.tensorflow.org/datasets/catalog/cifar10) dataset. Due to the nature of the RBG channels, there are some differences:
- the pixel distributions are separated by channels (colors), 
- color channel distributions are added, 
- the "average images" are one block of color. 

The notebooks are found under 'script/4_mnist_exploratory.ipynb' and 'script/4_cifar10_exploratory.ipynb' respectively.


### References:

1. https://www.linkedin.com/pulse/ml-experiment-tracking-what-why-matters-how-implement-jakub-czakon/
2. https://resources.experfy.com/ai-ml/experiment-management-how-to-organize-your-model-development-process/
3. https://blog.devgenius.io/precision-vs-recall-understanding-the-trade-off-in-classification-models-a1bdae527d7c
4. https://www.v7labs.com/blog/performance-metrics-in-machine-learning
5. https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5
6. https://medium.com/tebs-lab/how-to-classify-mnist-digits-with-different-neural-network-architectures-39c75a0f03e3
7. https://www.tensorflow.org/datasets/catalog/mnist
8. https://www.tensorflow.org/datasets/catalog/cifar10