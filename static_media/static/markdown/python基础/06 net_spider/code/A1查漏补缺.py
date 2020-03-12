# coding:utf-8
__author__ = "superlaker"
__date__ = '2019/4/27 23:57'


# 字符串格式化
def main0():
    new_str = "在{}内填充".format("hello")
    print(new_str)

    new_str1 = "{}多处填充{}".format(["list_can", "dict_can"], (1, 2, 3))
    print(new_str1)


# 列表推导式
def main1():
    my_list0 = [i for i in range(5) if i % 2 == 1]  # 奇数
    my_list = [i for i in range(5) if i > 2]  # 大于2

    print(my_list)


# 生成器
def main2():
    gen_list = (i for i in range(5))  # 生成器对象

    print(type(gen_list))  # <class 'generator'>

    my_list = gen_list  # 引用传递
    print(my_list)  # <generator object main.<locals>.<genexpr> at 0x0000015662639408>

    the_list = list(gen_list)
    # the_tuple = tuple(gen_list)  # error
    print(the_list)


# 三目运算
def main():
    age = 10
    result = "能进网吧" if age > 18 else "不能进网吧"
    print(result)


if __name__ == '__main__':
    main()
