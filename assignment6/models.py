"""
The module performs instantiating and fitting of data on different models. 
The models included are developed by scikit-learn. See https://scikit-learn.org/.

The models included in this program are:
    Logistic regression
    Gaussian Naive Bayes
    Cartesian Decision Trees
    Linear Discriminant Analysis
    Linear Regression (not currently in use)
    Support Vector Machine
    K Nearest Neighbor
"""


import pandas as pd
import data
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

def lr(training_data, target_data):
    """
    Function implements logistic regression analysis for some features on the dataset

    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
    
    Returns:
        model:                  the trained classifier
    """

    model = linear_model.LogisticRegression()
    model.fit(training_data, target_data)

    return model


def nb(training_data, target_data):
    """
    Function implements gaussian NB analysis for some features on the dataset

    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
    
    Returns:
        model:                  the trained classifier
    """

    model = GaussianNB()
    model.fit(training_data, target_data)

    return model


def cart(training_data, target_data):
    """
    Function implements decision tree analysis for some features on the dataset

    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
    
    Returns:
        model:                  the trained classifier
    """
    
    model = DecisionTreeClassifier()
    model.fit(training_data, target_data)

    return model


def lda(training_data, target_data, lda_settings):
    """
    Function implements linear discriminant analysis for some features on the dataset

    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
        lda_settings:           dict of settings for the classifier
    
    Returns:
        model:                  the trained classifier
    """

    model = None

    if lda_settings == None:
        model = LinearDiscriminantAnalysis()
    else:
        model = LinearDiscriminantAnalysis(solver=str(lda_settings['lda_solver']))
        
    model.fit(training_data, target_data)
        
    return model


def linreg(training_data, target_data):
    """
    Function implements linear regression for some features on the dataset

    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
    
    Returns:
        model:                  the trained classifier

    """

    model = linear_model.LinearRegression()
    model.fit(training_data, target_data)

    return model


def svm(training_data, target_data, svm_settings):
    """
    Function implements support vector machine for some features on the dataset

    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
        svm_settings:           dict of settings for the classifier
    
    Returns:
        model:                  the trained classifier

    """

    model = None

    if svm_settings == None:
        model = SVC(kernel='rbf', C=1, gamma='auto')
    else:
        model = SVC(kernel=svm_settings['svm_kernel'], degree=svm_settings['svm_degree'], gamma='auto')
    
    model.fit(training_data, target_data)

    return model


def knn(training_data, target_data, knn_settings):
    """
    Function implements k-nearest-neighbor classification for some features on the dataset
    
    Arguments:
        training_data:          the dataframe with the selected features
        target_data:            the target(s) for supervised learning
        knn_settings:           dict of settings for the classifier
    
    Returns:
        model:                  the trained classifier
    """
    
    model = None

    if knn_settings == None:
        model = KNeighborsClassifier(n_neighbors=5)
    else:
        model = KNeighborsClassifier(algorithm=knn_settings['knn_algorithm'], weights=knn_settings['knn_weight'])
    
    model.fit(training_data, target_data)

    return model