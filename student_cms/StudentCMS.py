from student import Student
import time
class Studentcms:
    def __init__(self):
        self.stu_list=[
            # Student("张三", "男", 20, "13800000001", "戴眼镜"),
            # Student("李四", "女", 18, "13800000002", "长发"),
         ]
    @staticmethod
    def show_meun():    
        print("-"*23)
        print("本系统可以完成如下操作:")
        print("\t1.添加学员")
        print("\t2.修改学员")
        print("\t3.删除学员")
        print("\t4.查询某个学员")
        print("\t5.显示所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print("-"*23)
    #4.添加学生信息
    def add_stu(self):
        name=input("请输入学生的名字:")
        gender=input("请输入学生性别:")
        age=int(input("请输入学生年龄:"))
        phone=input("请输入学生电话:")
        desc=input("请输入学生的特点:")
        s=Student(name,gender,age,phone,desc)
        self.stu_list.append(s)      
        print(f"添加{name}学生信息成功")  
    #修改学生信息
    def update_stu(self):
        new_name=input("请输入你要更改的人的名字")
        for stu in self.stu_list:
            if stu.name==new_name:
                stu.name=input("请输入更改后学生的名字:")
                stu.gender=input("请输入更改后学生性别:")
                stu.age=int(input("请输入更改后学生年龄:"))
                stu.phone=input("请输入更改后学生电话:")
                stu.desc=input("请输入更改后学生的特点:")
        else:
            print("查无此人,请重新输入")
    #删除学生信息
    def del_stu(self):
        del_name=input("请输入你要删除的学生:")
        remark=0
        for  stu in self.stu_list:
            if stu.name==del_name:
                remark+=1
        if remark==1:
            for stu in self.stu_list:
                if stu.name==del_name:
                    self.stu_list.remove(stu)
                    print("删除成功")
                    break
        elif remark>1:
             find_phone=input(f"有{remark}个名字相同,请按照他们的电话进行筛选")
             for stu in self.stu_list:
                 if stu.phone==find_phone:
                     self.stu_list.remove(stu)   
                     print("删除成功") 
                     break
             else:
                print("查无此人,请重新输入")
        else:
            print("查无此人,请重新输入")
    # ===== 另一种写法：列表法（注释保留，不影响运行） =====
    # def del_stu(self):
    #     del_name = input("请输入你要删除的学生:")
    #     matches = [stu for stu in self.stu_list if stu.name == del_name]
    #
    #     if not matches:
    #         print("查无此人,请重新输入")
    #         return
    #
    #     if len(matches) > 1:
    #         find_phone = input(f"有{len(matches)}个叫{del_name}的学生,请输入电话筛选:")
    #         matches = [stu for stu in matches if stu.phone == find_phone]
    #         if not matches:
    #             print("没有电话匹配的学生")
    #             return
    #
    #     for stu in matches:
    #         self.stu_list.remove(stu)
    #     print(f"学生{del_name}已经删除")
#查找某个学生
    def search_stu(self):
        find_name=input("请输入你要查询的某个学生:")
        for stu in self.stu_list:
            if find_name==stu.name:
                print(stu)
        else:
            print("查无此人,请重新输入")
#查询所有学生
    def all_stu(self):
        if len(self.stu_list)==0:
            print("里面没有学生信息")
        else:
            for stu in self.stu_list:
                print(stu)
            
            print("查询成功")
#保存学生信息
    def save_stu(self):

        with open("./stu_data.txt","w",encoding="utf-8") as stu_info:
            stu_dict=[stu.__dict__ for stu in self.stu_list]
            stu_info.write(str(stu_dict))
#加载学生信息:
    def load_stu(self):
        try: 
            with open("./stu_data.txt","r",encoding="utf-8") as read_stu:
                stu_data=read_stu.read()
                stu_list=eval(stu_data)#用eval,把字符串转化为列表
                if len(stu_list)==0:
                    stu_list=[]
                else:
                    self.stu_list=[Student(**stu_dict) for stu_dict in stu_list]
        except: 
            with open("./stu_data.txt","w",encoding="utf-8") as stu_info:
                pass
#开始运行,重点记住match case语句
    def start(self):
        self.load_stu()
        while True:
            time.sleep(2)
            Studentcms.show_meun()
            num=input("请输入你要操作的编号:")
            match num:#可能要加\n,后续先看满意与否
                case "1":
                    print("添加学生信息:")
                    self.add_stu()
                case "2":
                    self.update_stu()
                case "3":
                    self.del_stu()
                case "4":
                    print("查询某个学生信息:")
                    self.search_stu()
                case"5":
                    print("所有学生信息为:")
                    self.all_stu()
                case "6":
                    print("保存学生信息")
                    self.save_stu()
                    print("保存学生信息成功")
                case "0":
                    result=input(("请问您是否要退出系统(Y/N)->:"))
                    if result.lower()=="y":
                        self.save_stu()
                        print("谢谢您的使用")
                        break
                case _:
                    print("请重新输入")


