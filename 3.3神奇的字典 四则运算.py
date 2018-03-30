while 1:
    a = int(input('first:'))
    operator = input('operator:')
    b = int(input('secend:'))

    yunsuan = {
                '+':a+b,
                '-':a-b,
                '*':a*b,
                '/':a/b
               }

    result = yunsuan.get(operator,'input error,please try again')
    print(result)
