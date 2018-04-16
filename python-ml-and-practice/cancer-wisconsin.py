import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

if __name__ == '__main__':
    columns_names = ['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape',
                     'Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin',
                     'Normal Nucleoli','Mitoses','Class']
    data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
                       names=columns_names)

    # print(data[:10])
    data = data.replace(to_replace='?',value=np.nan)
    # 丢弃带有缺失值的数据
    data = data.dropna(how='any')
    # print(data.shape)

    # 分割训练集,训练标签,测试集,测试标签
    X_train,X_test,y_train,y_test = train_test_split(data[columns_names[1:10]],data[columns_names[10]],test_size=0.25,random_state=33)
    # print(y_train.value_counts())

    # 标准化数据,保证每个维度的特征数据方差为1,均值为0,使得预测结果不会被某些维度过大的特征值而主导
    ss = StandardScaler()
    # print(X_train)
    X_train = ss.fit_transform(X_train)
    X_test = ss.fit_transform(X_test)
    # print(X_train)

    lr = LogisticRegression()
    sgdc = SGDClassifier(max_iter=5)

    # 调用fit函数用来训练模型数据
    lr.fit(X_train,y_train)
    # 使用训练好的模型lr对X_test进行预测,结果存储在变量lr_y_predict中
    lr_y_predict = lr.predict(X_test)

    sgdc.fit(X_train,y_train)
    sgdc_y_predict = sgdc.predict(X_test)

    print(lr.score(X_test,y_test))
    print(classification_report(y_test,lr_y_predict,target_names=['Benign','Malignant']))

    print(sgdc.score(X_test,y_test))
    print(classification_report(y_test, sgdc_y_predict, target_names=['Benign', 'Malignant']))

    pass