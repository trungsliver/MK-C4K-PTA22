import oop

stu1 = oop.Student("Trí", 11, 'male', 'Tân Định')
stu2 = oop.Student("An", 15, 'male', 'Vinschool')

# sử dụng phương thức của lớp cha (HUman)
stu1.introduce()
# Sử dụng phương thức __str__
print(stu1)  
# Sử dụng phương thức show_info
stu2.show_info()