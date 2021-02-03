import pandas as pd
import numpy  as np
import csv

from product.models import *
from user.models    import * 
from order.models import *

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes     import CategoricalNB
from sklearn                 import preprocessing
from sklearn.preprocessing   import OrdinalEncoder


def create_order_data(file_name):
    orders   = Order.objects.filter(order_status=OrderStatus.objects.get(status=True))
    filename = file_name
    f        = open(filename, "w", encoding="utf-8-sig", newline="")
    writer   = csv.writer(f)

    writer.writerow("age-gender-subcategory".split("-"))
    for order in orders:
        age    = order.user.age
        gender = order.user.gender
        for cart in order.carts.all():
            subcategory = cart.drink.sub_category.name
            writer.writerow([age, gender, subcategory])
    
    return file_name

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