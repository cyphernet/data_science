import csv
import sys
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import cross_val_score
from sklearn import linear_model
from sklearn import metrics

# Read trainin data into array
train_data = []
with open('train.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile)
	datareader.next()
	for row in datareader:
		train_data.append([row[0], row[2].replace('"','')])

# Split data to train and test on
train, test = train_test_split(train_data)

# initialize a vectorizer
vectorizer = CountVectorizer(stop_words='english', min_df=1)

# Get features from training set
features = vectorizer.fit_transform(train[:,1])

# Build linear model
model = linear_model.LogisticRegression(C=2.0)
lm_classifier = model.fit(features, train[:,0])

# how does it work on the training set?
print("Training score: {0:.1f}%".format(lm_classifier.score(features, train[:,0]) * 100))

# hoow does it work on the test set?
X_test = vectorizer.transform(test[:,1])
print("Testing score: {0:.1f}%".format(lm_classifier.score(X_test, test[:,0]) * 100))

# build naive model
model = MultinomialNB(fit_prior=True)
classifier = model.fit(features, train[:,0])
print("Training score: {0:.1f}%".format(classifier.score(features, train[:,0]) * 100))

X_test = vectorizer.transform(test[:,1])
print("Testing score: {0:.1f}%".format(classifier.score(X_test, test[:,0]) * 100))

# predict data
test_data = []
with open('test.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile)
	datareader.next()
	for row in datareader:
		test_data.append([row[0], row[2].replace('"','')])

x = np.array(test_data)
predictions = lm_classifier.predict_proba(vectorizer.transform(x[:,1]))

# print data
with open('prob.csv', 'wb') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['Id', 'Insult'])
	for i in range(len(test_data)):
		csvwriter.writerow([test_data[i][0], predictions[i][1]])