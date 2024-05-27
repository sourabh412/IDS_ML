import pickle
import pandas as pd
import numpy as np
from utils import *
from sklearn.metrics import accuracy_score, precision_score, recall_score
import seaborn as sns
import matplotlib.pyplot as plt

model = pickle.load(open("./Saved_models/Randomforest_classifier.pkl", "rb"))

x_test = pd.read_csv("./Dataset/Preprocessed_data/x_test.csv")
y_test = pd.read_csv("./Dataset/Preprocessed_data/y_test.csv")

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)*100
precision = precision_score(y_test, y_pred, average="weighted")*100
recall = recall_score(y_test, y_pred, average="weighted")*100

# sns.barplot({"Test Accuracy": accuracy, "Test Precision": precision, "Test Recall": recall})
colors = ['#17C37B', '#D9DFEB']
my_pie, _, _ = plt.pie([accuracy, 100.00-accuracy], radius = 1.2, colors=colors, autopct="%.2f%%")
plt.setp(my_pie, width=0.6, edgecolor='white')
plt.title("Test Accuracy")
plt.show()

colors = ['#FACA0C', '#D9DFEB']
my_pie, _, _ = plt.pie([precision, 100.00-precision], radius = 1.2, colors=colors, autopct="%.2f%%")
plt.setp(my_pie, width=0.6, edgecolor='white')
plt.title("Test Precision") 
plt.show()

colors = ['#F92969', '#D9DFEB']
my_pie, _, _ = plt.pie([recall, 100.00-recall], radius = 1.2, colors=colors, autopct="%.2f%%")
plt.setp(my_pie, width=0.6, edgecolor='white')
plt.title("Test Recall")
plt.show()

print(f"Test Accuracy   : {accuracy}")
print(f"Test Precision  : {precision}")
print(f"Test Recall     : {recall}")