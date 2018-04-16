from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

if __name__ == '__main__':
    news = fetch_20newsgroups(subset='all')
    # print(len(news.data))
    # print(news.data[0])

    X_train, X_test, y_train, y_test = train_test_split(news.data,news.target,test_size=0.25,random_state=33)

    # 使用朴素贝叶斯分类器对新闻文本进行类别预测
    # https://blog.csdn.net/cicilover/article/details/77336337
    vec = CountVectorizer()
    X_train = vec.fit_transform(X_train)
    vectorizer_test = CountVectorizer(vocabulary=vec.vocabulary_)
    X_test = vectorizer_test.transform(X_test)

    mnb = MultinomialNB()
    mnb.fit(X_train,y_train)
    y_predict = mnb.predict(X_test)

    print(mnb.score(X_test,y_test))
    print(classification_report(y_test,y_predict,target_names=news.target_names))

    pass