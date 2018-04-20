from pandas import Series,DataFrame
import pandas as pd
import numpy as np
from numpy.random import randn

if __name__ == '__main__':
    # obj = Series([4,7,2,8])
    # print(obj)
    # print(obj.values)
    # print(obj.index)

    # obj = Series([4,7,2,8],index=['a','b','c','d'])
    # print(obj)
    # print(obj.values)
    # print(obj.index)
    # print(np.exp(obj))
    # print('b' in obj)
    # print('e' in obj)

    # sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
    # obj = Series(sdata)
    # print(obj)
    # states = ['Califonia','Ohio','Oregon','Texas']
    # obj2 = Series(sdata,index=states)
    # print(obj2)
    # print(pd.isnull(obj2))
    # print(pd.notnull(obj2))
    # print(obj2.isnull())
    # print(obj+obj2)
    # obj2.name = 'population'
    # obj2.index.name = 'state'
    # print(obj2)

    # data = {'state':['Ohio','Texas','Nevada','Utah','Ohio'],'year':[2000,2001,2002,2003,2001],'pop':[1.5,1.7,3.6,2.4,2.9]}
    # frame = DataFrame(data)
    # print(frame)
    # frame = DataFrame(data,columns=['year','state','pop'])
    # print(frame)
    # frame2 = DataFrame(data, columns=['year', 'state', 'pop','debt'],index=['a','b','c','d','e'])
    # print(frame2)
    # print(frame2.state)
    # print(frame2.ix['c'])
    # frame2.debt = 20
    # print(frame2)
    # val = Series([1.2,1.6,2.3],index=['a','b','f'])
    # frame2.debt = val
    # print(frame2)
    # frame2['extern'] = frame2.state == 'Ohio'
    # print(frame2)
    # print(frame2.columns)

    # data = {'state':['Ohio','Texas','Nevada','Utah','Ohio'],'year':[2000,2001,2002,2003,2001],'pop':[1.5,1.7,3.6,2.4,2.9]}
    # frame = DataFrame(data)
    # frame2 = DataFrame(data, columns=['year', 'state', 'pop','debt'],index=['a','b','c','d','e'])
    # print(frame2.values)

    # index = pd.Index(np.arange(3))
    # obj = Series([1,3.4,2.1],index=index)
    # print(obj.index is index)

    data = DataFrame(randn(5,4))
    print(data)

    data.fillna()

    pd.read_csv()
    pass