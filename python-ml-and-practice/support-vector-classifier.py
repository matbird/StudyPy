import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

if __name__ == '__main__':
    digists = load_digits()
    # print(digists)
    # print(digists.data.shape)
    # print(digists.data)

    X_train, X_test, y_train, y_test = train_test_split(digists.data,digists.target,test_size=0.25,random_state=33)
    # print(X_train.shape)
    # print(X_test.shape)

    # 标准化
    ss = StandardScaler()
    X_train = ss.fit_transform(X_train)
    X_test = ss.fit_transform(X_test)

    lsvc = LinearSVC()
    lsvc.fit(X_train,y_train)

    y_predict = lsvc.predict(X_test)

    print(lsvc.score(X_test,y_test))
    print(classification_report(y_test,y_predict,target_names=digists.target_names.astype(str)))

    pass