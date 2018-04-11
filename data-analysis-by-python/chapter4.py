import numpy as np
from numpy.random import randn

if __name__ == '__main__':
    # data = np.array([[1,2,3],[4,5,6]])
    # print(data)
    # shape:数组几行几列  dtype:数组元素的数据类型
    # print(data.shape,data.dtype)

    # data1 = [6,7.5,8,0,2]
    # arr1 = np.array(data1)
    # print(arr1.dtype)
    # print(arr1.shape)

    # data2 = [[1,2,3,4],[5,6,7,8]]
    # arr2 = np.array(data2)
    # print(arr2.ndim)

    # zeros 创建全0的数组
    # print(np.zeros(10))
    # print(np.zeros((3,6)))

    # empty :创建没有任何具体值的数组,返回的都是未初始化的垃圾值,不是0
    # print(np.empty((2,3,2)))

    # range函数的数组版
    # print(np.arange(15))

    # print(np.ones((2,3)))
    # eye :创建单位矩阵
    # print(np.eye(5))

    # np.array([1,2,3],dtype=np.float64)

    # arr3 = np.array([1,2,3])
    # print(arr3.dtype)
    # arr3.astype(np.float64)
    # print(arr3.dtype)

    # numberic_strings = np.array(['1.251','2.43','0.12'],dtype=np.string_)
    # numberic_strings.astype(np.float64)
    # print(numberic_strings.astype(np.float64))

    # astype 应该是转化数据类型的,但是这里不起作用?
    # astype 会创建出一个新的数组,不会影响原始数组,

    # arr = np.array([[1,2,3],[4,5,6]])
    # print(arr * arr)
    # print(arr - arr)
    # print(1 / arr)
    # print(arr ** 0.5)

    # 三维数组
    # arr = np.array([[[1,2,3],[2,3,4]],[[7,8,9],[10,11,12]]])
    # print(arr)
    # print(arr[1,0])
    # old_arr = arr[0].copy()
    # print(old_arr)
    # arr[0] = 41
    # print(arr)
    # arr[0] = old_arr
    # print(arr)

    # arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
    # print(arr[:2,1:])
    # print(arr[:,:1])

    # 切片操作对原始的数组起作用,处理大数据时候多次复制的开销很大

    # 布尔型索引
    # names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
    # data = randn(7,4)
    # print(names)
    # print(data)
    # print(names == 'Bob')
    # print(data[names == 'Bob'])
    # print(data[names == 'Bob',2:])
    # print(data[names == 'Bob',3])

    # 花式索引:传入一个数组作为索引
    # arr = np.empty((8,4))
    # for i in range(8):
    #     arr[i] = i
    # print(arr)
    # print(arr[[4,3,0,6]])

    # 传入多个数组作为索引,返回的是一个一维数组
    # arr = np.arange(32).reshape((8,4))
    # print(arr)
    # print(arr[[1,5,7,2],[0,3,1,2]])

    # 花式索引跟切片不同,它总是将数据复制到新数组中

    # 数据的转置和轴对换
    # arr = np.arange(15).reshape((3,5))
    # print(arr)
    # print(arr.T)
    # print(arr)

    # dot 计算内积 X^T * X
    # arr = randn(6,3)
    # print(arr)
    # print(np.dot(arr,arr.T))

    # print(np.arange(12).reshape((3,4)))

    # print(np.arange(12) * 2)

    # 元素级数组函数
    # 一元ufunc
    # print(np.sqrt(np.arange(5)))
    # print(np.modf(np.arange(10)))
    # 二元ufunc
    # print(np.mod(np.arange(6,11) * 3,np.arange(1,6)))

    # arr = randn(5,4)
    # print(arr)
    # arr.sort(0)
    # print(arr)

    # 唯一化,unique
    # names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    # print(np.unique(names))
    # values = np.array([2,3,6,1,0,5,5])
    # print(np.in1d(values,[2,3,6]))

    # 数组文件的保存输入输出
    # arr = np.arange(10)
    # np.save('some_arr',arr)
    # print(np.load('some_arr.npy'))
    # arr = randn(5,4)
    # np.savetxt('some_arr_txt',arr)

    pass