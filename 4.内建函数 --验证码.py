'''
chr()

ord()
'''

#四位验证码实现（包含数字 大小写字母）

'''
Ascii
0 - 9 ==> 48~57
A - Z ==> 65~90
a - z ==> 97~122
'''

import random

while 1:
    yzm = []
    l = []
    for i in range(4):
        l = [random.randint(48,57),random.randint(65,90),random.randint(97,122)]
        yzm.append(chr(random.choice(l)))    
    print('验证码为：%s'%(''.join(yzm)))
    ch = input("请问是否继续生成（y/n）")
    if ch == 'n':break
