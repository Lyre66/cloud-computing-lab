class Student:
    def __init__(self,name,gender,age,phone,describe):
        """
        初始化学生信息
        """
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.describe=describe
    def __str__(self):
        return f"学生姓名:{self.name},性别{self.gender},年龄:{self.age},电话{self.phone},特征描述:{self.describe}"
    #测试
    if __name__=="__main__":
        s=Student("王五","男","22","13900000003","喜欢打篮球")
        print(s)
    