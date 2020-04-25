# Arvato Customer segmentation

Capstone project for **Udacity Machine Learning Engineer Nanodegree**.

## Installation
To run the Jupyter notebooks and python scripts, you will need a standard installtion of Anaconda with Python 3.6.x

Additional libraries needed:
- catboost==0.22
- category_encoders==2.1.0
- imblearn==0.0
- scikit_learn==0.22.2
- xgboost

You can install these libraries using `pip install -r requirements.txt` available in the same repository.

## How to Run?
Once you have installed all the requirements, you run the notebook. First, the `Customer_Segmentation_Report.ipynb`, then `Supervised_Learning.ipynb`.

Make sure you have downloaded the `utils` repository, where customized functions are created and imported inside the notebook.

You need the data to run this repo, but it´s only available for Udacity Machine Learning Engineer Nanodegree. It was provided only to those participating in the "in class" competition.

## Customer Segmentation Report -- Unsupervised Learning Model
This project analyzes demographics data of customer, in comparison of general population demographics information, aiming to identify part of the general population that best describes core company customer base.

## Marketing Predictions -- Supervised Learning Model
The previous analysis will be used to build a machine learning model that predicts whether or not each individual will respond to the campaign. The model is used to predict unlabeled data, and submitted to Kaggle for evaluation. Its performance is evaluated by AUC score.

## Kaggle Competition
The prediction is submitted under this competition[Udacity+Arvato: Identify Customer Segments](https://www.kaggle.com/c/udacity-arvato-identify-customers/leaderboard). My current score and rank as below:
![](leaderboard_score(.73).PNG)

## Project Rubics

[Machine Learning Capstone project rubrics](https://review.udacity.com/#!/rubrics/2541/view)

## Documentation
[Project Report](Project_Report.pdf)
