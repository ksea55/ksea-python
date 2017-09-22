"""

python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。 pickle.dump()
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。 pickle.load()
基本接口：

pickle.dump(obj, file, [,protocol])

有了 pickle 这个对象, 就能对 file 以读取的形式打开:

x = pickle.load(file)

注解：从 file 中读取一个字符串，并将它重构为原来的python对象。

file: 类文件对象，有read()和readline()接口。

"""

import pickle


# 使用pickle模块将数据对象保存到文件

def pickleDump():
    data1 = {'a': [1, 2.0, 3, 4 + 6j],
             'b': ('string', u'Unicode string'),
             'c': None}

    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)

    with open('dump.pkl', 'wb') as output:
        # Pickle dictionary using protocol 0.
        pickle.dump(data1, output)

        # Pickle the list using the highest protocol available.
        pickle.dump(selfref_list, output, -1)


# pickleDump()




import pprint


# 使用pickle模块从文件中重构python对象
def pickleLoad():

    with open('dump.pkl', 'rb') as  pkl_file:

        data1 = pickle.load(pkl_file)
        pprint.pprint(data1)

        data2 = pickle.load(pkl_file)
        pprint.pprint(data2)

pickleLoad()



