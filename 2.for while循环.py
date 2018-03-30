#海龟绘图
import turtle
'''
for j in range(5):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.forward(10)
'''

#for 迭代变量 in 序列：
#   代码块

'''
for i in range(5,15,2):         #range 首值 尾值 步长值
    print(i)
'''

#while 条件 ：
#   代码块
'''
j = 0
while j<5:
    turtle.forward(100)
    turtle.right(144)
    i += 1
'''

#随堂作业

result = 0
for i in range(1,101):
    result +=  i
print(result)

result1 = 0
for j in range(1,100):
    if j%3==0 or j%5==0 : result1 += j
else:print("ceui")
print(result1)

