#pg 5 "牛刀"大"试
# 写一个程序，使用input（）函数让用户输入 5 个名字。程序要把这 5 个名字保存在一个列表中，最后打印出来。
#name1=input("input 1st people's name: ")
#name2=input("input 2nd people's name: ")
#name3=input("input 3rd people's name: ")
#name4=input("input 4th people's name: ")
#name5=input("input 5th people's name: ")
#names=[name1,name2,name3,name4,name5]
# -->print(names)
# names = []
# name = input("input your name:")
# names.append(name)

#pg 5 牛刀"大"试
# 修改上一题的程序，要求不仅显示原来的名字列表，还要显示出排序后的列表。
#newname=sorted(names)
# -->print("the unordered list: ")
# -->print(names)
# -->print("the ordered list: ")
# -->print(newname)

#pg 5 牛刀"大"试
# 修改上一题的程序，要求只显示用户键入的第 3 个名字
# -->print("the third people's name is: ")
# -->print(name3)
# nameToPrint = names[2]
# print(nameToPrint)

#pg 5 牛刀"大"试
# 有5名某界大佬xiaoyun、xiaohong、xiaoteng、xiaoyi和xiaoyang，其QQ号分别是88888、5555555、11111、12341234和1212121，用字典将这些数据组织起来。编程实现以下功能：用户输入某一个大佬的姓名后输出其QQ号，如果输入的姓名不在字典中则输出字符串“Not Found”。
contact={"xiaoyun":88888,"xiaohong":5555555,"xiaoteng":11111,"xiaoyi":12341234,"xiaoyang":1212121}
name=input("input your friend's name: ")
for key in contact.keys():
    if name==key:
        print(contact[key])
        break
    elif key=="xiaoyang":
        print("Not Found")
    else:
        continue

        
        
    


# #pg 6 牛刀"大"试
# #创建购物清单列表：['牛奶'，'面包'，'苹果'，'香蕉'，'薯条'，'可乐'，'果汁']
# list=['milk','bread','apple','banana','fries','coke','juice']

# #pg 6 牛刀"大"试
# #将“布丁”添加到购物清单索引3的位置，并且打印列表。
# list.insert(3,'jelly')

# #pg 6 牛刀"大"试
# #在购物清单的后面添加列表['柠檬'，'饼干'，'彩虹豆']，并且打印列表。
# list.extend(['lemon','cookie','Skittles'])

# #pg 6 牛刀"大"试
# #修改购物清单中索引3的值，将它改成葡萄，并且打印列表
# list[3]='grapes'

# #pg 6 牛刀"大"试
# #删除购物清单中的“苹果”元素，打印新的列表。
# #list.pop(2)

# #pg 6 牛刀"大"试
# #通过列表切片获取购物清单中索引2到索引4之间的元素，并且打印出来。
# #print(list[2:4])