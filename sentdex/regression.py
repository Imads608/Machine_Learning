import pandas as pd
import quandl
import math
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
import sklearn
import numpy as np

def part2():
    df = quandl.get('WIKI/GOOGL')
    df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
    df["HL_PCT"] = ((df["Adj. High"] - df["Adj. Low"]) / df["Adj. Low"]) * 100
    df["PCT_change"] = ((df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]) * 100

    df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]
    print(df.head())

def part3():
    df = quandl.get('WIKI/GOOGL')
    df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
    df["HL_PCT"] = ((df["Adj. High"] - df["Adj. Low"]) / df["Adj. Low"]) * 100
    df["PCT_change"] = ((df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]) * 100

    df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]
    forecast_col = "Adj. Close"
    df.fillna(-999999, inplace=True)
    print(len(df))
    forecast_out = int(math.ceil(0.01*len(df)))
    print(forecast_out)
    print(df.head(40))
    df["label"] = df[forecast_col].shift(-forecast_out)
    df.dropna(inplace=True)
    print(df.head(40))

def part4():
    df = quandl.get('WIKI/GOOGL')
    df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
    df["HL_PCT"] = ((df["Adj. High"] - df["Adj. Low"]) / df["Adj. Low"]) * 100
    df["PCT_change"] = ((df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]) * 100

    df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]
    forecast_col = "Adj. Close"
    df.fillna(-999999, inplace=True)
    print(len(df))
    forecast_out = int(math.ceil(0.01 * len(df)))
    print(forecast_out)
    #print(df.head(40))
    df["label"] = df[forecast_col].shift(-forecast_out)
    df.dropna(inplace=True)
    print(df.head(40))

    X = np.array(df.drop(["label"], 1))
    y = np.array(df["label"])
    print(y)
    X = preprocessing.scale(X)
    #y = np.array(df["label"])

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print(confidence)


if __name__ == "__main__":
    part4()