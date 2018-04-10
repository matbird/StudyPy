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


    pass