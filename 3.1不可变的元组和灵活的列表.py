#作业


list_0 =('Name','Age','Sex','Specialy')
player = [['zhanghuan',19,'male','eat! eat! eat!...,'],
          ['penglinhao',27,'male','read! read! read!...'],
          ['wusiping',26,'female','play! play! play!...']]

print("欢迎使用征兵采集系统，请按指令进行操作！")
while 1:
    choise1 = int(input( "\n1.浏览列表\n"
                         "2.报名参加\n"
                         "3.删除信息\n"
                         "4.查找\n"
                         "5.另存为\n"
                         "请输入你的选择："))

    if choise1 == 1:
        print(">>>>>>>>>>>>>>>浏 览 列 表<<<<<<<<<<<<<<<")
        for i in range(len(player)):
            print(player[i])

    elif choise1 == 2:
        print(">>>>>>>>>>>>>>>报 名 参 兵<<<<<<<<<<<<<<<")
        name_add = input("请输入你的名字：")
        age_add = input("请输入你的年龄：")
        sex_add = input("请输入你的性别：")
        specialy_add = input("请输入你的特长：")
        ist_play = [name_add,age_add,sex_add,specialy_add]
        print("你输入的数据为：",ist_play)
        player.append(ist_play)

    elif choise1 == 3:
        del_choise = int(input(">>>>>>>>>>>>>>>删 除 信 息<<<<<<<<<<<<<<<\n"
                               "请选择你要根据什么条件删除信息：\n"
                               "1.姓名\n"
                               "2.性别\n"
                               "3.年龄\n"
                               "请输入你的选择："))

        if del_choise == 1:
            del_name = input("请输入你要删除的名字：")
            list_name = []
            for j in range(len(player)):
                list_name.append(player[j][0])
            #判断del_name是否在list_name里面
            if del_name in list_name:
                del_index = list_name.index(del_name)
                player.remove(player[del_index])
                print("删除成功！")
            else:print("没要找到此人")

        elif del_choise == 2:
            del_sex = input("请选择你要删除的性别：\n"
                            "1.male\n"
                            "2.female\n"
                            "请选择：")
            if del_sex == 1:
                for k in range(len(player)):
                    if 'male' == player[k][2]:
                        player.pop(k)
            else:
                for k in range(len(player)):
                    if 'female' == player[k][2]:
                        player.pop(k)

        elif del_choise == 3:
            age_choise = int(input("请选择操作\n"
                               "1.筛选大于某一个值的名单\n"
                               "2.筛选小于某一个值的名单\n"
                               "请选择："))
            if age_choise == 1:
                num_age = int(input("请输入临界值："))
                for l in range(len(player)):
                    if num_age >= player[l][1]:
                        print(player[l])
                        player.pop(l)




    elif choise1 == 4:
        pass
    elif choise1 == 5:
        pass
    else:
        print("输入有误，请重新输入！")