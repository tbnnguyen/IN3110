"""
Module renders different visualizations of one or more classifiers efficiency when it comes to classifying
instances of diabetes in women. It uses Matplotlib for this. See https://matplotlib.org/. 

The model renders differently depending on: the number of classifiers and the number of parameters.
"""


import numpy as np
import matplotlib.pyplot as plt
from itertools import product
import fitting
import math
import base64
import io
import datetime

def format_axes(models):
    """
    Function instantiates the classifiers and returns the long name

    Arguments:
        models:         list of short model names

    Returns:
        classifiers:    list of instantiated classifiers
        model_names:    list of long version of classifier name (i.e svm = Support Vector Machine)
    """

    model_names = []
    classifiers = []
    
    for m in models:
        model_names.append(fitting.get_model_name(m[0]))
        classifiers.append(m[1])
    del(models) #deleting array of tuples
    
    return classifiers, model_names


def visualize_multiple(models, control_data, y_true):
    """
    Function inspired by https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html

    Function visualizes the prediction of one (1) model

    Arguments:
        model:          the models that performs the predictions
        control_data:   the control dataset
        y_true:         the real values

    Returns:
        Nothing, but stores the image in /images as 'last-graph.png'

    """

    #converting from Pandas dataframes to numpy arrays
    control_data = control_data.to_numpy()
    y_true = y_true.to_numpy()

    x_min, x_max = control_data[:, 0].min() - 1, control_data[:, 0].max() + 1
    y_min, y_max = control_data[:, 1].min() - 1, control_data[:, 1].max() + 1
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                        np.arange(y_min, y_max, 0.1))

    x_mesh_size =   (2 if any([(len(models) == 2), (len(models) == 4), (len(models) == 8)]) else
                    3)

    y_mesh_size = 2

    fig, axarr = plt.subplots(x_mesh_size, y_mesh_size, sharex='col', sharey='row', figsize=(10, 8))

    classifiers, model_names = format_axes(models)

    #Generates one subplot per chosen classifier
    for i, classifier, name in zip(product(range(0, x_mesh_size), range(0, y_mesh_size)), classifiers, model_names):
        print("Rendering visualisation for {}...".format(name))

        Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        score, c_matrix = fitting.get_metrics(classifier, control_data, y_true)

        if y_mesh_size == 1:
            axarr[i[0], 0].contourf(xx, yy, Z, alpha=0.4)
            axarr[i[0], 0].scatter(control_data[:, 0], control_data[:, 1], c=y_true, s=20, edgecolor='k')
            axarr[i[0], 0].set_title("{0}, {1}%".format(name, score))
        else:
            axarr[i[0], i[1]].contourf(xx, yy, Z, alpha=0.4)
            axarr[i[0], i[1]].scatter(control_data[:, 0], control_data[:, 1], c=y_true, s=20, edgecolor='k')
            axarr[i[0], i[1]].set_title("{0}, {1}%".format(name, score))

    image_name = "multiple_graph_{}.png".format(datetime.datetime.now().strftime("%d%m%Y_%H%M%S"))
    plt.savefig("images/{}".format(image_name))

    return "images/{}".format(image_name)

def visualize_one(model, control_data, y_true):
    """
    Function visualizes the prediction of one (1) model

    Arguments:
        model:          the model that performs the prediction
        control_data:   the control dataset
        y_true:         the real values

    Returns:
        Nothing, but stores the image in /images as 'last-graph.png'
    """

    control_data = control_data.to_numpy()
    y_true = y_true.to_numpy()

    x_min, x_max = control_data[:, 0].min() - 1, control_data[:, 0].max() + 1
    y_min, y_max = control_data[:, 1].min() - 1, control_data[:, 1].max() + 1
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                        np.arange(y_min, y_max, 0.1))
    
    classifier, model_name = format_axes(model)

    Z = classifier[0].predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    score, c_matrix = fitting.get_metrics(classifier, control_data, y_true)

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(control_data[:, 0], control_data[:, 1], c=y_true, s=20, edgecolor='k')
    plt.title("{0}, {1}%".format(model_name[0], score)) #sets title to classifier name and score
    

    image_name = "graph_{}.png".format(datetime.datetime.now().strftime("%d%m%Y_%H%M%S"))
    plt.savefig("images/{}".format(image_name))

    return "images/{}".format(image_name)

def metrics_multiple(models, control_data, y_true):
    """
    Function renders metrics and performance of multiple models/classifiers
    
    Arguments:
        model:          the model that performs the prediction
        control_data:   the control dataset
        y_true:         the real values

    Returns:
        Nothing, but stores the image in /images as 'last-graph.png'

    """

    #converting from Pandas dataframes to numpy arrays
    control_data = control_data.to_numpy()
    y_true = y_true.to_numpy()

    classifiers, model_names = format_axes(models)

    values = []

    for classifier, name in zip(classifiers, model_names):
        print("Rendering metrics for {}...".format(name))
        
        score, c_matrix = fitting.get_metrics(classifier, control_data, y_true)

        values.append(score)
    
    y_pos = np.arange(len(model_names))
    
    fig, ax = plt.subplots()
    rects = ax.bar(y_pos, values, align='center', color='orange')
    ax.set_ylim(top=100, bottom=0)
    ax.set_xticks(y_pos)
    ax.set_xticklabels(model_names, rotation=45)
    ax.set_ylabel('Performance')
    ax.set_title('Performance index of different models \n (Accuracy in %)')
    plt.gcf().subplots_adjust(bottom=0.30)

    for r in rects:
        height = r.get_height()
        ax.text(r.get_x() + r.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')

    image_name = "multiple_metrics_{}.png".format(datetime.datetime.now().strftime("%d%m%Y_%H%M%S"))
    plt.savefig("images/{}".format(image_name))

def metrics_one(model, control_data, y_true):
    """
    Function renders metrics and performance of one model/classifier
    
    Arguments:
        model:          the model that performs the prediction
        control_data:   the control dataset
        y_true:         the real values

    Returns:
        Nothing, but stores the image in /images as 'last-graph.png'

    """

    #converting from Pandas dataframes to numpy arrays
    control_data = control_data.to_numpy()
    y_true = y_true.to_numpy()

    classifier, model_name = format_axes(model)

    score, c_matrix = fitting.get_metrics(classifier, control_data, y_true)
    print(c_matrix)

    labels = ['pos', 'neg']

    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(c_matrix, cmap='RdBu')
    
    plt.title("{0}, {1}%".format(model_name[0], score)) #sets title to classifier name and score
    fig.colorbar(cax)

    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels)

    plt.xlabel('Predicted')
    plt.ylabel('True')

    image_name = "metrics_{}.png".format(datetime.datetime.now().strftime("%d%m%Y_%H%M%S"))
    plt.savefig("images/{}".format(image_name))

def render_visualization(model_names, features, svm_settings, knn_settings, lda_settings):
    features.append('diabetes') #Adds data which contains 0/1 or True/False values
    models, training_data, target_data, control_data = fitting.fit('data/diabetes.csv', model_names, features, 
                                                                    svm_settings, knn_settings, lda_settings)
    y_true = control_data['diabetes']
    control_data = control_data.drop(columns=['diabetes'])
    
    if len(model_names) == 1:
        return visualize_one(models, control_data, y_true)
    elif len(model_names) > 1:
        return visualize_multiple(models, control_data, y_true)
    else:
        return ('Something went wrong', 'error')


def render_metrics(model_names, features, svm_settings, knn_settings, lda_settings):
    features.append('diabetes') #Adds data which contains 0/1 or True/False values
    models, training_data, target_data, control_data = fitting.fit('data/diabetes.csv', model_names, features, 
                                                                    svm_settings, knn_settings, lda_settings)
    y_true = control_data['diabetes']
    control_data = control_data.drop(columns=['diabetes'])

    if len(model_names) == 1:
        return metrics_one(models, control_data, y_true)
    elif len(model_names) > 1:
        return metrics_multiple(models, control_data, y_true)
    else:
        return ('Something went wrong', 'error')


if __name__ == "__main__":
    pass