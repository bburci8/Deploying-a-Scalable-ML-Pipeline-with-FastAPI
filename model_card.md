# Model Card

## Model Details
The model is a Random Forest classifier implemented with scikit-learn. It is trained to classify whether an individual's annual income is greater than $50K or less than or equal to $50K based on census data.
The categorical features are transformed using one-hot encoding before training. The trained model and encoder are serialized and stored in the model/ directory for later inference.

## Intended Use
The model is intended for educational purposes as part of the Udacity Machine Learning DevOps Engineer Nanodegree project. It demonstrates the development of a machine learning pipeline that preprocesses census data, trains a classification model, evaluates its performance, and produces predictions.
The model is not intended for production use or for making real-world decisions about individuals.

## Training Data
The model is trained using the census.csv dataset provided with the project. The dataset contains demographic and employment-related attributes together with the salary target variable.
The dataset is divided into training and testing subsets using an 80/20 train-test split with a random state of 42.
Categorical features are processed using a OneHotEncoder, while the target variable is transformed using a LabelBinarizer.

## Evaluation Data
The evaluation data consists of the 20% test portion of the Census dataset that is separated before model training.
The same encoder and label binarizer fitted on the training data are reused to transform the test data. This allows the model to be evaluated on data that was not used to train the classifier.
Model performance is also evaluated on categorical slices of the test data. Metrics are calculated separately for every unique value of each categorical feature and stored in slice_output.txt.

## Metrics
The assessment of the model involves precision, recall, and the F1 score.
On the test dataset, the model achieved:
Precision: 0.7419
Recall: 0.6384
F1 score: 0.6863
Precision measures the percentage of the predicted positives that are true, whereas recall measures the percentage of the actual positives that have been predicted. The F1 score provides a balance between precision and recall.
Performance is additionally evaluated across categorical data slices. These slice metrics are recorded in slice_output.txt to make differences in performance between groups easier to identify.

## Ethical Considerations
The dataset contains demographic and socioeconomic attributes. Models trained using these attributes can exhibit different performance across groups represented in the data.
For this reason, overall model metrics alone should not be used to determine whether the model performs appropriately for all populations. Slice-level evaluation should also be considered when assessing model behavior.
The model should not be used to make decisions that could significantly affect individuals.

## Caveats and Recommendations
The model was developed as an educational project and has not been validated for production use.
Some categorical values in the dataset are represented by ?, indicating that some information may be unknown or unavailable. The distribution of observations across categorical slices is also uneven. Metrics calculated from slices containing very few observations can therefore be unstable or unrepresentative.
The model should be tested on extra data before it can be used outside the parameters of this study. Future studies might include data cleaning, tuning the hyperparameters, using different algorithms for classification, and investigating the differences in performance of different data sub-groups.