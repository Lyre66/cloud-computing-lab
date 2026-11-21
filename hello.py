"""cloud-computing-lab · 第一个程序

一个简单的自我介绍程序，用于验证 Python 运行环境，同时作为
Git 工作流练习的「可修改代码」。

运行：
    python hello.py
"""

from datetime import datetime

STUDENT = {
    "name": "余乐",
    "class_name": "数据251",
    "student_id": "32564700006",
}


def print_line(char: str = "=", width: int = 46) -> None:
    """打印一条分隔线。"""
    print(char * width)


def show_profile(info: dict) -> None:
    """打印个人信息卡片。"""
    print_line()
    print("cloud-computing-lab".center(46))
    print_line()
    print(f"  姓名 : {info['name']}")
    print(f"  班级 : {info['class_name']}")
    print(f"  学号 : {info['student_id']}")
    print_line()
    print(f"  时间 : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("  版本 : v1.1")
    print_line("-")
    print("  欢迎来到云计算实验仓库！")


def main() -> None:
    show_profile(STUDENT)


if __name__ == "__main__":
    main()
