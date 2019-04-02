# -----------------Zillow Kaggle Competition ------------------
Zillow log error Prediction Model


## INTRODUCTION

* Zillow is an online real estate database with data on homes across the United States. One of Zillow’s most popular features is a proprietary property value prediction algorithm: the Zestimate.  As one might imagine, Zillow is constantly trying to improve its Zestimate.  To help advance its accuracy even further,  it launched a Kaggle competition with a $1.2 million prize. 

## PROBLEM DEFINITION

* The target variable is the log error between Zillow's estimated value for the property (Zestimate) and the actual sales price. This is significant because your model will be picking up only whatever signal Zillow's internal model for predicting home value isn't picking up on.

    logerror=log(Zestimate)−log(SalePrice)

* There are two types of files you need to worry about: properties which has attributes ( attributes) of the properties you're trying to predict on and train which has the sale date ( transactiondate) and  logerror for the sale. Your model will be of the form 
    logerror≈f(transactiondate, attributes)+ϵ
 
* The evaluation metric will be Mean Absolute Error(MAE), or the average absolute value of the difference between the predicted  logerrorˆ and the true  logerror
 
* Your goal is to predict the  logerror for 6 transaction dates: October, November, and December of both 2016 and 2017. Note that the train data comes from 2016, but we're asked to predict on 2017 data.

## ABOUT THE DATA

* Data Source : [Zillow Kaggle Data](https://www.kaggle.com/c/zillow-prize-1/data)

* File descriptions
    * properties_2016.csv - all the properties with their home features for 2016. Note: Some 2017 new properties don't have any data yet except for their parcelid's. Those data points should be populated when properties_2017.csv is available.
    * properties_2017.csv - all the properties with their home features for 2017 (released on 10/2/2017)
    * train_2016.csv - the training set with transactions from 1/1/2016 to 12/31/2016
    * train_2017.csv - the training set with transactions from 1/1/2017 to 9/15/2017 (released on 10/2/2017)
    * sample_submission.csv - a sample submission file in the correct format

* Data fields
    * Please refer to zillow_data_dictionary.xlsx
    
## DEPENDENCIES

1. Matplotlib
    * conda install pandas xlrd matplotlib scikit-learn

## PREPROCESSING

## EXPLORATION AND WRANGLING
