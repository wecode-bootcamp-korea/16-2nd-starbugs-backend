import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes     import CategoricalNB
from sklearn                 import preprocessing
from sklearn.preprocessing   import OrdinalEncoder

def classifier(input_file):
    df = pd.read_csv(input_file, header = 0)
    X  = df.iloc[:, :2].to_numpy()
    y  = df.iloc[:, 2].to_numpy()

    enc = OrdinalEncoder()
    enc.fit(X)
    OrdinalEncoder()

    le = preprocessing.LabelEncoder()
    le.fit(y)
    preprocessing.LabelEncoder()

    X = enc.transform(X)
    y = le.transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf        = CategoricalNB()
    classifier = clf.fit(X_train, y_train)
    
    return classifier

input_file = 'orderData'