print("Hello Python interpreter")

message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)

name = "ada lovelacE"
print(name.title())  # 标题
print(name.upper())  # 全部转为大写
print(name.lower())  # 全部转为小写

print("-----------------------------------1")

# 合并（拼接）字符串
first_name = 'ada '
last_name = "lovelace"
full_name = first_name + last_name

print(full_name)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("-----------------------------------2")

# 删除字符串中开头和结尾的空白  rstrip()
favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())

# 使用函数str()避免类型错误
"""
    Python判断变量的类型有两种方法：type() 和 isinstance()
    对于基本的数据类型两个的效果都一样
        isinstance() 和 type() 的区别在于：
                type()不会认为子类是一种父类类型
                isinstance()会认为子类是一种父类类型
"""
age = 3
print(type(age))
message = "Happy " + str(age) + "rd Birthday!"  # 这个地方与java不太一样
print(message)

print(5 + 4)  # result: 9

print("-----------------------------------3")

"""
    列表
        是一系列按特定顺序排序的元素组成
        可以将任何东西加入列表中，其中的元素之间没有任何的关系
"""
# 列表的格式
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("列表：", end='')
print(bicycles)

print("访问列表bicycles中的第一个元素：", end='')
print(bicycles[0])

# 修改、添加和删除元素
print("修改列表中第一个元素trek的值：", end='')
bicycles[0] = "t"
print(bicycles)

print("添加元素honda后的列表：", end='')
bicycles.append("honda")
print(bicycles)

print("在列表的任意位置添加元素，如在首位：", end='')
bicycles.insert(0, "qijun")
print(bicycles)

# 用del语句删除元素
del bicycles[0]  # 根据索引删除任意元素
print("删除列表中第一个元素：", end='')
print(bicycles)

# 使用pop()删除元素
# 如果你要将元素从列表中删除，并接着使用它的值，可以用pop()
popped_motorcycle = bicycles.pop()  # 默认删除最后一个元素，也可以在()中指定要删除元素的索引进行删除
print("用pop()删除元素：", end='')
print(bicycles)

# 根据列表中的值删除元素
bicycles.remove('specialized')
print("根据值specialized删除元素：", end='')
print(bicycles)

print("-----------------------------------4")

# 使用sort()方法对列表进行永久排序  按字典顺序排序
bicycles.sort()
print("使用sort()方法对列表进行永久排序：", end='')
print(bicycles)

# # 使用函数sorted()对列表进行临时排序
# print("使用函数sorted()对列表进行临时排序：", end='')
# print(sorted(bicycles))


# reverse() -- 反转列表元素顺序打印
print("reverse() -- 反转列表元素顺序打印：", end='')
bicycles.reverse()
print(bicycles)

# 确定列表长度
print("确定列表长度；", end='')
length = len(bicycles)
print(length)

# 遍历列表
print("遍历整个列表")
for bicycle in bicycles:
    print(bicycle)
print("遍历结束")

print("-----------------------------------5")

# 创建数值列表

# 函数range()
for value in range(1, 5):
    print(value)  # 结果为：1 2 3 4
print("=======1")

# list()
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 3))
print(even_numbers)

print("列表numbers元素中的最小值：", end='')
print(min(numbers))
print("列表numbers元素中的最大值：", end='')
print(max(numbers))

squares = [value ** 2 for value in range(1, 11)]
print("列表squares：", end='')
print(squares)

# 切片
players = ['charles', 'martina', 'florence', 'eli']
print(players[1:3])  # 包左不包右
print(players[:3])
print(players[-3:])

print("-----------------------------------6")

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are：", end='')
print(friend_foods)

# 这种方式不可取，两个变量（friend_foods、my_foods）都指向同一个列表
# friend_foods = my_foods


"""
    元组
        定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样
        不能修改
"""
print("-----------------------------------元组")
# 元组的格式
dimensions = ('200', 50, 34, 144)
print(dimensions[0])
print(dimensions)

print("遍历dimensions元组")
for dimension in dimensions:
    print(dimension)
print("遍历结束")

print("-----------------------------------7")

'''
    if语句
'''
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("-----------------------------------8")

# if-elif-else

'''
    and   所有条件都满足才为true
    or    只要满足一个条件就为true
'''

# 检查特定值是否包含在列表中
print('audi' in cars)  # result；true

if 'aud' not in cars:
    print("you can post a response if you wish.")

# 确定列表不为空
requested_toppings = []
print("确定列表不为空：", end='')
if requested_toppings:
    print("列表为空")
else:
    print("列表不为空")
print("-----------------------------------9")

"""
    字典
        字典存储的信息量几乎不受限制
"""

# 字典的格式
alien_0 = {'color': 'green', 'points': 5, 4: 'jin'}
print("字典：", end='')
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])
print(alien_0[4])
print("-------------")

# 添加键值对
alien_0['qi'] = 'jun'
print("添加键值对后的字典：", end='')
print(alien_0)

# 修改字典中的值
alien_0['qi'] = 7
print("修改键为'qi'的值为7：", end='')
print(alien_0)

# 删除键值对
del alien_0['qi']  # 删除指定键的键值对
print("删除键值对：", end='')
print(alien_0)

# 遍历字典
# 键值对返回顺序与存储顺序不同？？？？书上是这么说的
user_0 = {'color': 'green', 'a': 'a', 'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
print("\n遍历字典：", end='')
print(user_0)
for key, value in user_0.items():
    print("key：", end='')
    print(key, end='')
    print("\tvalue：", end='')
    print(value)
print("遍历结束")

# 遍历字典中所有的键
print("\n遍历字典中所有的键：")
for key in user_0.keys():
    print("key：", end='')
    print(key)
print("遍历结束")

# 遍历字典中所有的值
print("\n遍历字典中所有的值：")
for value in user_0.values():
    print("value：", end='')
    print(value)
print("遍历结束")

print("-----------------------------------10")

print(type(user_0))
# 按顺序遍历字典中的所有键
print("按顺序遍历字典中的所有键：")
for key in sorted(user_0.values()):
    print("key：", end='')
    print(key)
print("遍历结束")

'''
    嵌套
'''

# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print("\n遍历字典列表：")
for alien in aliens:
    print(alien)
print("遍历结束")

print("-----------------------------------11")

# 在字典中存储列表
pizza = {'crust': 'thick',  # 这个结果比较有意思
         'toppings': ['mushrooms', 'extra cheese'],
         7: [1, 2, 3, 4, 5, 6]
         }
for key, values in pizza.items():
    print("key：", end='')
    print(key)
    for value in values:
        # print("\tvalue：", end='')
        print("\t", end='')
        print(value)

print("-----------------------------------11")

# 在字典中存储字典
users = {
    'aeinstein': {
        'first1': 'albert',
        'last1': 'einstein',
        'location1': 'princeton'
    },
    'mcurie': {
        'first2': 'marie',
        'last2': 'curie',
        'location2': 'paris'
    }

}

for keys, values in users.items():
    print(keys)
    for k, v in values.items():
        print("\tkey：", end='')
        print(k, end='')
        print("\tvalue：", end='')
        print(v)

print("-----------------------------------12")

# 比较有意思
# a = 'inoaiv'
# for i in a:
#     print(i)


"""
    用户输入和while循环
"""

# 函数input()--和java中的Scanner()差不多
# message = input("请输入内容：")  # 得到的结果为字符串
# print("打印刚刚输入的内容：" + message)

'''
    Python3中有六个标准的数据类型：
        字符串（String）
        数字（Digit）
            int--整型
            float--浮点型
            bool--布尔型
            fractions--分数
            complex--复数
        列表（List）
        元组（Tuple）
        集合（Sets）
        字典（Dictionary）
        日期（date）
'''
# 函数int()--将变量转换成整型
age = '21'
print(type(age))
age = int(age)
print(type(age))

# while循环
current_number = 1
while current_number < 5:
    print(current_number)
    current_number += 1

print("-----------------------------------13")

# break、continue--和java中的一样

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

"""
    函数
"""
print("\n函数\n")


# 定义一个简单的函数
def greet_user():
    # 显示简单的问候语
    print("Hello!")


greet_user()

print("-----------------------------------14")

username1 = 'qijun'


def greet_users(username='qi'):  # 函数默认值
    print("Hello，" + username)


greet_users(username1)

print("-----------------------------------15")


# 返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    # 函数可返回任何类型的值
    return full_name


musician = get_formatted_name('qi', 'jun')
print(musician)

print("-----------------------------------16")

# 传递列表
def greet_users1(names):
    ''' 向列表中的每位用户都发出简单的问候 '''
    for name in names:
        mag = "Hello," + name.title() + "!"  # titile()中的()不会自动加载出来，需要手打！！！
        print(mag)


username = ['hannah', 'ty', 'margot']
greet_users1(username)

print("-----------------------------------17")

'''
    禁止函数修改列表
    greet_users1(username[:])
        这样写是将列表的副本传递给函数，列表本身不会发生改变
'''

# 传递任意数量的实参
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print(toppings)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参
#   def make_pizza(size, *toppings):

print("-----------------------------------18")

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    '''创建一个字典，其中包括我们知道的有关用户的一切'''
    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

print("-----------------------------------19")

















