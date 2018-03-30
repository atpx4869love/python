#1
def machine(x, y):
    print('制作一个%d元的%s口味的冰激凌' % (x, y))


#2
def machine1(x, y='牛奶'):
    print('制作一个%d元的%s口味的冰激凌' % (x, y))


#3
def machine2(x=5, y='菠萝'):
    print('制作一个%d元的%s口味的冰激凌' % (x, y))


machine(5, '牛奶')

machine1(5)

machine2(10, '香蕉')
machine2()

#多参数及冗余处理
#如果传递的是列表或者元组 前面加*
l = [5, '巧克力']  #列表
l1 = (10, '菊花')  #元组
machine(*l)
machine(*l1)
#如果是字典 就需要加两个*
d1 = {'x': 15, 'y': '牙膏'}
machine(**d1)


#冗余处理
def machine3(x=5, y='奶油', *arg, **kv):
    # *对应列表或元组的冗余处理 **对应字典的冗余处理
    print('制作一个%d元的%s口味的冰激凌' % (x, y))
	
machine3(3, '香草', 7)
machine3(x=3, y='大蒜', z=10)
