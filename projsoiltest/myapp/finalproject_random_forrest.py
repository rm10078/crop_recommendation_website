

# Importing libraries

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
import pickle



def predict_with_random_forest(n,p,k,tem,hum,ph,rain):


    warnings.filterwarnings('ignore')

    #all file are present in same folder
    df = pd.read_csv('/home/rajib/Documents/S_roy_project/backend/ml_back/projsoiltest/myapp/DATASET FOR NEW .csv')
    # Extracting features and target
    features = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]	#i added
    target = df['label']
    acc=[]
    model=[]

    pkl_file_path='/home/rajib/Documents/S_roy_project/backend/ml_back/projsoiltest/myapp/RandomForest.pkl' #store the pkl file path

    # Splitting into train and test data

    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

    from sklearn.ensemble import RandomForestClassifier

    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    RF.fit(Xtrain,Ytrain)

    predicted_values = RF.predict(Xtest)

    x = metrics.accuracy_score(Ytest, predicted_values)
    acc.append(x)
    model.append('RF')
    # Dump the trained Naive Bayes classifier with Pickle
    RF_pkl_filename=pkl_file_path
    # Open the file to save as pkl file
    RF_Model_pkl = open(RF_pkl_filename, 'wb')
    pickle.dump(RF, RF_Model_pkl)
    # Close the pickle instances
    RF_Model_pkl.close()
    model_path=pkl_file_path
    # Load the trained Random Forest model
    with open(pkl_file_path, 'rb') as file:
        model = pickle.load(file)
    # Define the feature names
    feature_names = ['N', 'P', 'K', 'Temperature','Humidity','pH','Rainfall']
    # Get input values from the user
    input_features = [float(n),float(p),float(k),float(tem),float(hum),float(ph),float(rain)]
    
    #-----------not need
    # for feature_name in feature_names:
    #     feature = float(input(f"Enter value for {feature_name}: "))
    #     input_features.append(feature)

    # Convert the input features to a numpy array
    input_features = np.array(input_features).reshape(1, -1)

    # Make predictions using the input features
    predictions = model.predict(input_features)

    return predictions[0]


#--------------------not need    

# model_path = pkl_file_path  # Replace with the path to your trained model file

# predictions = predict_with_random_forest(model_path)

# print("The recommended crop is :",predictions)

#-----------------only for first testing
#print(predict_with_random_forest(141, 45, 151, 31, 50, 7, 210))

