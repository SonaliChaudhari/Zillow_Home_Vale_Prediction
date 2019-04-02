# Zillow_Kaggle_Competition
Zillow log error prediction model


## INTRODUCTION

* Zillow is an online real estate database with data on homes across the United States. One of Zillow’s most popular features is a proprietary property value prediction algorithm: the Zestimate.  As one might imagine, Zillow is constantly trying to improve its Zestimate.  To help advance its accuracy even further,  it launched a Kaggle competition with a $1.2 million prize. 

## Problem Definition

* Your target variable is the log error between Zillow's estimated value for the property (Zestimate) and the actual sales price. This is significant because your model will be picking up only whatever signal Zillow's internal model for predicting home value isn't picking up on.

    logerror=log(Zestimate)−log(SalePrice)

* There are two types of files you need to worry about: properties which has attributes ( attributes) of the properties you're trying to predict on and train which has the sale date ( transactiondate) and  logerror for the sale. Your model will be of the form 
    logerror≈f(transactiondate, attributes)+ϵ
 
* The evaluation metric will be Mean Absolute Error, or the average absolute value of the difference between the predicted  logerrorˆ and the true  logerror
 
* Your goal is to predict the  logerror for 6 transaction dates: October, November, and December of both 2016 and 2017. Note that the train data comes from 2016, but we're asked to predict on 2017 data.