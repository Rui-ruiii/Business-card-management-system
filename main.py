"""import number_1
import number_2


print("*" * 40)
print("欢迎使用【名片管理系统】v1.0")
item = ["1.新建名片","2.显示全部","3.查询名片","\n""0.退出系统"]
for cycle in item:
    print(cycle)


print("*" * 40)
number = int(input("请输入您选择的操作："))
if number == 1:
    print(number_1)
elif number == 2:
    print(number_2)"""



import tools
while True:
    print("*" * 40)
    print("欢迎使用【名片管理系统】v1.0")
    item = ["1.新建名片", "2.显示全部", "3.查询名片", "\n""0.退出系统"]
    for cycle in item:
        print(cycle)
    action_str = input("请选择您希望进行的操作：")
    print("您选择的操作是：%s" %action_str)
    #123是针对名片的操作，0退出系统，其他数值提示重新输入
    if action_str in ["1","2","3"]:
        #1是新建名片
        if action_str == "1":
           tools.new_card()
        #2是显示全部
        elif action_str == "2":
            tools.show_cards()
        #3是查询名片
        elif action_str =="3":
            tools.search_card()
    elif action_str == "0":
        print("欢迎再次使用名片管理系统")
        break
    else:
        print("您输入的不正确，请重新选择")
    print("*" * 40)