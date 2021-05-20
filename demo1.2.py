#!/usr/bin/python
# coding: utf-8

from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack(padx=10, pady=10)

v1 = StringVar() #总楼层数
v2 = StringVar() #每层户数
v3 = StringVar() #单元数
v4 = StringVar() #租赁房号
v5 = StringVar() #面积

v6 = StringVar() #小区
v7 = StringVar() #楼栋
v8 = StringVar() #地址

v9 = StringVar() #结果1
v10 = StringVar() #结果2



def test(content):
    # 如果是数字，返回真，否则返回假
    return content.isdigit()


# 把test函数包装起来，用于validatecommand中

testCMD = root.register(test)

#一

Label(frame, text="单元数").grid(row=0, column=0)
Entry(frame,
      textvariable=v3,
      # validate="key",
      validatecommand=(testCMD, "%P"),
      ).grid(row=1, column=0)

#二
Label(frame, text="租赁房号").grid(row=0, column=1)
Entry(frame,
      textvariable=v4,
      # validate="key",
      validatecommand=(testCMD, "%P"),
      ).grid(row=1, column=1)

#三
Label(frame, text="总楼层数").grid(row=0, column=2)

Entry(frame,
      textvariable=v1,  # 设置当v1的值改变的时候，当前框体中的值也发生变化
      # validate="key",  # 当在输入框输入东西的时候直接进行验证
      validatecommand=(testCMD, "%P"),
      ).grid(row=1, column=2)



#五
Label(frame, text="每层户数").grid(row=0, column=3)
Entry(frame,
      textvariable=v2,  # 设置当v1的值改变的时候，当前框体中的值也发生变化
      # validate="key",  # 当在输入框输入东西的时候直接进行验证
      validatecommand=(testCMD, "%P"),
      ).grid(row=1, column=3)


#六
Label(frame, text="面积").grid(row=0, column=4)
Entry(frame,
      textvariable=v5,
      # validate="key",
      validatecommand=(testCMD, "%P"),
      ).grid(row=1, column=4)

#七
Label(frame, text="小区").grid(row=2, column=0)
Entry(frame,
      textvariable=v6,
      # validate="key",
      validatecommand=(testCMD, "%P"),
      ).grid(row=3, column=0)
#八
Label(frame, text="栋").grid(row=2, column=1)
Entry(frame,
      textvariable=v7,
      # validate="key",
      validatecommand=(testCMD, "%P"),
      ).grid(row=3, column=1)
#九
Label(frame, text="地址").grid(row=2, column=2)
Entry(frame,
      textvariable=v8,
      # validate="key",
      validatecommand=(testCMD, "%P"),
      ).grid(row=3, column=2)

#四 结果
Label(frame, text="房屋信息序列").grid(row=4, column=0)
Entry(frame,
      textvariable=v9,
      state="readonly"  # 设置不能修改这个框体中的值
      ).grid(row=4, column=1)
# Label(frame, text="房屋面积序列").grid(row=3, column=2)
# Entry(frame,
#       textvariable=v10,
#       state="readonly"  # 设置不能修改这个框体中的值
#       ).grid(row=3, column=3)






def enter_excel_c():
    re = ''
    loop = int(v3.get())
    row = int(v1.get())
    colonms = int(v2.get())
    house = int(v4.get())
    area = int(v5.get())
    community = str(v6.get().strip())
    house_num = str(v7.get())
    address = str(v8.get().strip())
    # for l in range(loop):
    for i in range(row):
        for j in range(colonms):
            # print(str(i+1)+'\t')
            # 小区楼栋名称
            re1 = str(community + house_num + '栋')
            #单元
            re3 = str(loop)
            #层号
            re4 = str(i+1)
            #户号
            if j < 10:
                re5 = str(i + 1) + '0' + str(j + 1)
            else:
                re5 = str(i + 1) + str(j + 1)
            # 房屋地址
            re6 = str(address + re1 + re3 + "单元" + re4 + "层" + re5 + "号")
            #面积
            if j + 1 == house:
                re7 = str(area)
            else:
                re7 = '0'
            re += re1 + '\t' + house_num + '\t' + re3 + '\t' + re4 + '\t' + re5 + '\t' + re6 + '\t' + re7 + '\n'


    return v9.set(str(re))
    # return v4.set(str(re1)),v5.set(str(re2)),v6.set(str(re3))

# def enter_excel_h():
#     loop = int(v3.get())
#     row = int(v1.get())
#     colonms = int(v2.get())
#     for l in range(loop):
#         for i in range(row):
#             for j in range(colonms):
#     #             print(str(j+1))
#                 if j<10:
#                     print(str(i+1)+'0'+str(j+1)+'\t')
#                 else:
#                     print(str(i+1)+str(j+1)+'\t')
#
# def enter_excel_m(house,area):
#     loop = int(v3.get())
#     row = int(v1.get())
#     colonms = int(v2.get())
#     for i in range(row):
#         for j in range(colonms):
#             if j+1 in house:
#                 print(str(area)+'\t')
#             else:
#                 print('0'+'\t')

#
# def calc():
#     result = int(v1.get()) + int(v2.get())
#     return v4.set(str(result))
a = 0
# color = 'blue'
def dingzhi():
    global a,text1
    if  a==0:
        # 置顶
        root.wm_attributes('-topmost', 1)
        a = 1
        # tcolor = 'red'
    else:
        # 取消置顶
        root.wm_attributes('-topmost', 0)
        # text1 = "blue"
        a = 0



Button(frame, text="计算结果", command=enter_excel_c).grid(row=1, column=5)
Button(frame, text= "顶置", command=dingzhi).grid(row=0, column=5)
# color = 'blue'
root.mainloop()

