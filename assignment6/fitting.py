"""
Module implements some data parsing and formatting, but mostly - training and checking metrics of models.

It can be called from the terminal as python3 fitting.py "filepath". The user will have a terminal interface
for choosing and applying different classifiers on a dataset. 

"""

from sklearn import linear_model
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import data
import models
import sys
import csv
import visualize

def select_features(csv_file):
    """
    Function gets the features from the user and asserts it as an existing feature

    Arguments:
        csv_file:           The csv-file containing data

    Returns:
        input_features:     The array of features
    """

    with open(csv_file) as f:
        available_features = ""

        reader = csv.reader(f)
        row1 = next(reader)

        for feature in row1:
            if feature == "":
                pass
            else:
                available_features += (feature + ", ")

        print("Available variables: ", available_features)
        input_features = input("Select feature(s) (separate with commas): ").replace(' ', '').strip("\n").split(",")    

        if input_features == ["all"]:
            return row1
        elif all(elem in row1 for elem in input_features):
            if "diabetes" not in input_features:
                input_features.append("diabetes") #Asserts diabetes column at the end
            return input_features
        else:
            print("One or more of the features are not available. Please try again.")
            return select_features(csv_file)

def select_classifiers():
    """
    Function gets the features the user wants to perform the fitting on and asserts it's as
    existing feature

    Returns:
        models:     The array of models chosen
    """

    classifiers = ["ALL MODELS (all)", "Linear Regression (linreg)", "Support Vector Machine (svm)", 
    "Decision Tree (cart)", "K-Nearest-Neighbor (knn)", "Linear Discriminant Analysis (lda)", "Gaussian NB (nb)",
     "Logistic Regression (lr)"]

    classifiers_short = ["linreg", "svm", "cart", "knn", "lda", "nb", "lr"]
    
    print("Available classifiers: \n", str(classifiers).strip("\[").strip("\]"))
    input_classifiers = input("Please select the classifier(s) - short form is in the paranthesis (separate with commas): ").replace(' ', '').strip("\n").split(",")

    if input_classifiers == ["all"]:
        print("Will ignore regressive classifiers so the metrics still can be performed")
        return ["linreg", "svm", "cart", "knn", "lda", "nb", "lr"]
    elif all(elem in classifiers_short for elem in input_classifiers):
        return input_classifiers
    else:
        print("One or more of the classifiers you chose are not available. Please try again")
        return select_classifiers()

def get_model(classifier_name, training_data, target_data, model_settings=None):
    """
    Function returns a trained model based on the csv file and features chosen.
    Creation and training of models has been separated into their own file:
    models.py

    Arguments:
        training_data:      the data the training is performed on
        target_data:        the targets for supervised learning
        model_settings:     dict of settings for the classifier

    Returns:
        model:              the trained model

    """

    model = ((models.linreg(training_data, target_data)) if (classifier_name == "linreg")           else
            (models.svm(training_data, target_data, model_settings)) if (classifier_name == "svm")  else
             (models.cart(training_data, target_data)) if (classifier_name == "cart")               else
            (models.knn(training_data, target_data, model_settings)) if (classifier_name == "knn")  else 
            (models.lda(training_data, target_data, model_settings)) if (classifier_name == "lda")  else 
            (models.nb(training_data, target_data)) if (classifier_name == "nb")                    else 
            (models.lr(training_data, target_data)) if (classifier_name == "lr")                    else
            None)
    
    return model


def fit(csv_file, classifiers=None, features=None, svm_settings=None, knn_settings=None, lda_settings=None):
    """
    Function gets user input of which features to perform the fitting on. 
    User can also choose which classifier to use

    Arguments:
        csv_file:       the file path to csv file containing data. This is formatted and split into
                        training and control data
        classifiers:    the array of classifier names
    
    Returns:
        models:         array of trained classifiers
        control_data:   data you can use to control the fit of the data per classifier
    """

    if (classifiers == None):
        classifiers = select_classifiers()

    if (features == None):
        features = select_features(csv_file)

    training_data, control_data = data.get_dataframes(csv_file, features)
    target_data = training_data['diabetes']
    training_data = training_data.drop(columns=['diabetes'])

    models = [] #The array containing trained models
    for c in classifiers:
        if c == 'svm':
            model = get_model(c, training_data, target_data, svm_settings)
        elif c == 'knn':
            model = get_model(c, training_data, target_data, knn_settings)
        elif c == 'lda':
            model = get_model(c, training_data, target_data, lda_settings)
        else:
            model = get_model(c, training_data, target_data)
        
        if model == None:
            pass
        else:
            models.append((c, model))

    return models, training_data, target_data, control_data


def get_model_name(model_short):
    """Function returns the long version of the model name
    Arguments:
        model_short:        the short version of the model name

    Returns:
        model_name          the long version of the model name
    """

    model_name = (  "Support Vector Machine" if model_short == "svm"           else
                    "K Nearest Neighbor" if model_short == "knn"               else
                    "Linear Discriminant Analysis" if model_short == "lda"     else
                    "Decision Tree" if model_short == "cart"                   else
                    "Gaussian NB" if model_short == "nb"                       else
                    "Logistic Regression" if model_short == "lr"               else
                    "Linear Regression" if model_short == "linreg"             else
                    model_short)
    
    return model_name


def get_metrics(model, control_data, y_true):
    """
    Function returns the metrics of the trained model.

    Arguments:
        model:          the trained model
        control_data:   the control data
        y_true:         the true values

    Returns:
        score:          The accuracy score
        c_matrix:       The confusion matrix

    """
    # Controls where the call is coming from - incoming data has differenct formats
    if (isinstance(model, tuple)):
        y_pred = model[1].predict(control_data)
    elif (isinstance(model, list)):
        y_pred = model[0].predict(control_data)
    else:
        y_pred = model.predict(control_data)

    score = round(accuracy_score(y_true, y_pred, normalize=False)/len(control_data)*100, 2)
    c_matrix = confusion_matrix(y_true, y_pred)

    return score, c_matrix

if __name__ == "__main__":
    """
    This is called when the file is called directly as 'python3 fitting.py filepath'

    sys.argv[1] is the filepath to the data that is used for the analysis

    """

    if (sys.argv[1] == None):
        print("Please provide the .csv-file")
        quit()
    
    models, training_data, target_data, control_data = fit(sys.argv[1])
    y_true = control_data['diabetes']
    control_data = control_data.drop(columns=['diabetes'])

    input_metrics = input("Do you want to check the metrics of the classifier? [yes|no]: ").lower()
    input_visualize = input("Do you want to visualize the metrics of the classifier? [yes|no]: ").lower()

    met =   (True if input_metrics == "yes" else
            True if input_metrics == "y"    else
            False)

    vis =   (True if input_visualize == "yes"   else
            True if input_visualize == "y"      else
            False)

    if (met):
        print("Checking metrics of the model(s)...")
        try:
            for m in models:
                score, c_matrix = get_metrics(m, control_data, y_true)
                print("\n {}".format(get_model_name(m[0])))
                print("Accuracy Score: {}%".format(score))
                print("Confusion Matrix: \n", c_matrix)
        except ValueError:
            print("The analysis can't seem to handle the data.")
    else:
        print("Not checking metrics of the model(s)...")

    if (vis):
        print("Visualizing the model(s)...")
        try:
            if len(models) > 1:
                visualize.visualize_multiple(models, control_data, y_true)
            elif len(models) == 1:
                visualize.visualize_one(models, control_data, y_true)
            else:
                print("ERROR: No model(s) provided")
        except ValueError:
            print("The analysis can't seem to handle the data.")
    else:
        print("Not visualizing the data")
    
