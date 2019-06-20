card_list = []  # 记录所有的名片字典
card_dict = {}


def new_card():
    # 新建名片
    print("-" * 50)
    print("新建名片")
    # 提示用户输入详细的名片信息
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    QQ = input("请输入QQ号码：")
    email = input("请输入邮箱：")
    # 使用用户输入的信息建立一个名片字典
    card_dict = {"姓名": name,
                 "电话": tel,
                 "QQ号码": QQ,
                 "邮箱": email}
    # 使用字典信息完善名片列表
    card_list.append(card_dict)
    print(card_list)
    # 提示用户添加成功
    print("%s名片添加成功" % name)


def show_cards():

    # 显示全部名片
    print("-" * 50)
    print("显示全部名片")
    # 如果名片夹是空的，就提示空名片夹，请用户添加名片
    if len(card_list) == 0:
        print("暂无名片内容，请添加之后再查看")
    else:
        # 打印表头
        for title in ["姓名", "电话", "QQ", "邮箱"]:
            print(title, end="\t\t")
        print(" ")
        # 打印所有分割线
        print("=" * 50)
        # 打印名片信息
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["姓名"], card_dict["电话"], card_dict["QQ号码"], card_dict["邮箱"]))


def search_card():
    """

    :return: 返回上一级
    """
    # 查询名片
    print("-" * 50)
    print("查询名片")
    if len(card_list) == 0:
        print("名片夹暂无名片内容，请添加之后再进行查找")
    else:
        target = input("请输入要搜索的姓名")
        # 找不到相应的信息
        for card_dict in card_list:
            if card_dict["姓名"] == target:
             #   print("暂无%s的名片信息，请添加后尝试查看" % target)
              #  return
            #else:  # 找得到相应信息
               for title in ["姓名", "电话", "QQ号码", "邮箱"]:
                print(title, end="\t\t")
                print(" ")
                print("=" * 50)
                for target in card_dict:
                    print(
                        "%s\t\t%s\t\t%s\t\t%s" % (card_dict["姓名"], card_dict["电话"], card_dict["QQ号码"], card_dict["邮箱"]))
                    # opt = input("请选择对名片的操作：1：修改/2：删除/0：返回上级菜单：")
                    deal_card(card_dict)
                    break
            else:
                print("暂无%s的名片信息，请添加后尝试查看" % target)
                return

def deal_card(find_dict):
    """

    :param find_dict: 查找到的那条信息
    :return: 返回上一级操作
    """
    # 处理查找到的名片
    opt = input("请选择对名片的操作：1：修改/2：删除/0：返回上级菜单：")

    if opt == "1":
        # find_dict["name"] = input("姓名修改为：")
        # find_dict["tel"] = input("电话修改为")
        # find_dict["QQ"] = input("QQ号码修改为")
        # find_dict["email"] = input("邮箱修改为")
        # 这种方法不简洁，应该用一种只修改需要变动的信息，对其他信息不改动的方法（调用一个专门实现这个功能的新函数）如下
        find_dict["name"] = input_card_info(find_dict["name"], "姓名修改为[回车不改动]:")
        find_dict["tel"] = input_card_info(find_dict["tel"], "电话修改为[回车不改动]:")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "QQ号码修改为[回车不改动]:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱修改为[回车不改动]:")
        print("名片修改成功")
    elif opt == "2":
        card_list.remove(find_dict)
        print("删除成功")
    elif opt == "0":
        return
    else:
        print("请重新选择提示中的操作")


def input_card_info(dict_value, tip_message):
    """

    :param dict_value: 字典中的原有值
    :param tip_message: 提示信息
    :return:
    """
    # 1.提示用户修改内容
    result = input(tip_message)
    # 2.如果用户输入了内容，就返回结果
    if len(result) > 0:
        return result
    # 3.如果用户未输入内容，就返回原值
    else:
        return dict_value

