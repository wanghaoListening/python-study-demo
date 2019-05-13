"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

"""

score = float(input("输入学生得分"))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'E'

print('学生的考试等级为：',grade)