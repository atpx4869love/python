playinput = input()
print("用户输入的字符为：",playinput)
if 'f' in playinput and 'r' in playinput and 'i' in playinput and 'e' in playinput and 'n' in playinput and  'd' in playinput : print("用户输入的字符含有friend字符")
else:print("用户输入的字符中不含有friend字符")

F = playinput.count('f')
R = playinput.count('r')
I = playinput.count('i')
E = playinput.count('e')
N = playinput.count('n')
D = playinput.count('d')

print("其中'f'有:",F,"个")
print("其中'r'有:",R,"个")
print("其中'i'有:",I,"个")
print("其中'e'有:",E,"个")
print("其中'n'有:",N,"个")
print("其中'd'有:",D,"个")

AA={F,R,I,E,N,D}
num = min(AA)
print("最多可以组成",num,"个friend")

