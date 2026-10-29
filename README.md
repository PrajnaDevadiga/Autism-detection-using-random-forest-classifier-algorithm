# Autism Detection Using Random Forest Classifier

## Project Overview

This project explores the use of machine learning classification algorithms to analyze an Autism Spectrum Disorder (ASD)-related dataset and predict the target class. The primary model is a **Random Forest Classifier**, implemented using Python and Scikit-learn.

The project includes data preprocessing, exploratory data analysis, visualization, model training, performance evaluation, and comparison with other machine learning algorithms.

## Objectives

- Analyze the ASD dataset to understand patterns in the data.
- Preprocess categorical attributes for machine learning.
- Visualize relationships between selected attributes and the target class.
- Train a Random Forest classification model.
- Evaluate model performance using accuracy and a classification report.
- Compare Random Forest with AdaBoost and Support Vector Machine (SVM).

## Technologies Used

- **Programming Language:** Python
- **Data Processing:** NumPy, Pandas
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Data Files:** CSV and Excel

## Project Workflow

1. **Data Loading:** Load the ASD dataset from a CSV file using Pandas.
2. **Data Exploration:** Inspect dataset records, columns, unique values, and descriptive statistics.
3. **Data Preprocessing:** Convert selected categorical values into numerical representations.
4. **Exploratory Data Analysis:** Generate count plots to examine attributes such as sex, age in months, and family history of ASD against the target class.
5. **Data Splitting:** Separate the features and target variable and split the dataset into training and testing sets.
6. **Model Training:** Train a Random Forest Classifier using 600 estimators.
7. **Model Evaluation:** Generate predictions and evaluate the model using accuracy and a classification report.
8. **Model Comparison:** Train and compare Random Forest, AdaBoost, and SVM classifiers.
9. **Prediction:** Use the trained Random Forest model to make a sample prediction.

## Machine Learning Algorithms

### 1. Random Forest Classifier

The primary model is a Random Forest Classifier configured with 600 decision trees. The dataset is divided into training and testing subsets, with 20% allocated to testing.

### 2. AdaBoost Classifier

An AdaBoost Classifier configured with 500 estimators is trained and evaluated for comparison.

### 3. Support Vector Machine (SVM)

An SVM classifier is trained on the same training data, and its predictions are evaluated against the test labels.

The accuracy values of the three models are compared using a bar plot.

## Evaluation Metrics

The code uses the following evaluation methods:

- **Accuracy Score:** Measures the proportion of correct predictions.
- **Classification Report:** Displays precision, recall, F1-score, and support for each class.
- **Confusion Matrix:** Examines correct and incorrect classifications; the provided code generates this for the AdaBoost and SVM models.

Actual performance results should be added after running the notebook with the dataset.


## Installation and Setup

### Prerequisites

- Python 3.9 or a compatible Python version
- Jupyter Notebook or JupyterLab
- The dataset used by the notebook

### Install Dependencies

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn openpyxl jupyter
```

### Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Autism-Detection-Random-Forest.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Autism-Detection-Random-Forest
   ```

3. Place the authorized dataset in the appropriate directory.

4. Open Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Open the project notebook and execute the cells in sequence.


## Limitations

- Model performance depends on the dataset's quality, size, and class distribution.
- The results require validation using appropriate evaluation methods and, ideally, independent data.
- The provided code preprocesses selected categorical columns. Other categorical columns, if present, may require additional preprocessing before model training.
- The current implementation is a notebook-based machine learning project, not a deployed web or mobile application.


