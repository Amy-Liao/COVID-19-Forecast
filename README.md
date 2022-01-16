# COVID-19-Forecast
This is an assignment from "Introduction to Machine Learning" course in 2020.  
It takes the COVID-19 cases data in each country from Dec 31, 2019 to Oct 8, 2020 and applies linear regression to predict the COVID-19 cases from Oct 9 to Oct 15 in 2020.  
(It was Oct 8, 2020 when this code is finished)

## Dataset
The dataset is retrieved from https://reurl.cc/q8LWap in csv format

## How to use model file
Paste your dataset file path on the variable, “dataset_file_path”, in the last section of the code, "file import". 
This code will then create a file called “StudentID_HW1.csv” with the predicted 
cases for each country after execution.

## Description of the model
“main” is where the data preprocessing function and model training function are called. The model for cases 
prediction is linear regression.

For the data preprocessing, the independent variable is the date and the dependent 
one is the cases. The date is converted to integer starting from 0.  

For the model training, only the last 70% data is selected to eliminate the extreme value at the beginning of the virus outbreak.

## Update (Add mortality_prediction_from_CXR.ipynb)
mortality_prediction_from_CXR.ipynb is added.  
This model takes the patients' CXR images and predicts the 30-day mortality of patients.
Transfer learning was applied. The base model is MobileNet V2. We followed the tutorial on https://www.tensorflow.org/tutorials/images/transfer_learning#evaluation_and_prediction
