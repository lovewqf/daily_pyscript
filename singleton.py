# import time
# class B(object):
    # print('***')
    # instant = None
    # print('*****')
    # flag = True
    # print('********')

    # def __new__(cls, *args, **kwargs):
        # print(cls)
        # if cls.instant is None:
            # cls.instant = super().__new__(cls)
            # print(time.time())
        # return cls.instant

    # def __init__(self):
        # if not B.flag:
            # return
        # self.name = '张三'
        # self.age = 23
        # B.flag = False
        # print('B已经被初始化了')


# d = B()
# print('d对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(d), id(B)))
# e = B()
# print('e对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(e), id(B)))
# f = B()
# print('f对象所在的内存地址是 %d, B类所在的内存地址是 %d' % (id(f), id(B)))
# print(getattr(f,'flag'))




# -*- coding: utf-8 -*-

class A(object):
    """
    Class A.
    """

    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def test(self):
        print('a normal func.')

    @staticmethod
    def static_test(self):
        print('a static func.')

    @classmethod
    def class_test(self):
        print('a calss func.')


obj = A()
print(A.__dict__)
print(obj.__dict__)