# Loadinig required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading dataset
iris = datasets.load_iris()

# Printing description and fratures
# print(iris.DESCR)

features = iris.data  
labels = iris.target
# print(features[0], labels[0])  

# Training the Classifier
clf = KNeighborsClassifier()
clf.fit(features, labels) 

pred = clf.predict([[9.1, 9.5, 6.4, 0.2]])


if(pred == 0):
    print("Iris-Setosa")
elif(pred == 1):
    print("Iris-Versicolour")
else:
    print("Iris-Virginica")


#0 - Iris-Setosa
#1 - Iris-Versicolour
#2 - Iris-Virginica   