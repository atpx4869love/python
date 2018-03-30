player1 = ['milo',100,500]
milo = [100,60,50]
list1 = []

print(milo+player1+list1)

#遍历
for i in milo:
    print(i)

for i in player1:
    print(i)

# list.append( )  列表最后增加一个元素
milo.append(10)
print(milo)

# list.insert(index , object)  在索引前插入一个元素
player1.insert(1,'女')
print(player1)


# list.extnd(iterable)  将iterable(迭代) 依次放入到list中
box = ['a','b','c']

##对比append
player1.extend(box)
print(player1)

player1.append(box)
print(player1)

# list.remove(object)  删除list里面第一个object元素
player1.remove('c')
print(player1)

# list.pop(index)   弹出index的值 并删除元素
x = player1.pop(-2)
print(x,player1)

# list.sort(reverse=False or Ture)  按False(正序)或者Ture（逆序）排列list
box1 = [5,9,8,2,56,48,32,15,18]
box1.sort(reverse=False)  #正序
print(box1)
box1.sort(reverse=True)   #逆序
print(box1)

print( sorted( box1))    #独立的返回一个排完序的列表  原列表不变
str.split()    #字符串的切割
str.join()     #字符串的链接