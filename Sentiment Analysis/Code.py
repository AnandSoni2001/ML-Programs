#import libraries
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report 
import pandas as pd
import seaborn
import matplotlib.pyplot as plt

#Taking data and splitting it
data = pd.read_csv('train.csv')
X, Y = data.tweet, data.label
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3)

#Transform the data into dtm matrix
CountVector = CountVectorizer()
xtrain = (CountVector.fit_transform(x_train)).toarray()
xtest = (CountVector.transform(x_test)).toarray()

#Define Model and train it
Model = MultinomialNB()
Model.fit(xtrain, y_train)
#Predict the results
predict = Model.predict(xtest)

#Print Metrics and Accuracy
cm = confusion_matrix(y_test, predict)
print('Confusion Matrix :\n' ,cm)
print('\nClassification Report :\n' ,classification_report(y_test, predict))
print('\nAccuracy :' ,accuracy_score(y_test, predict), '\n\nHeatMap : \n')

#Heatmap
seaborn.heatmap(cm, annot=True, square = True,  cmap = 'jet')
plt.show()
