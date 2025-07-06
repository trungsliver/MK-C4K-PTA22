import oop

stu1 = oop.Student("Trí", 11, 'male', 'Tân Định')
stu2 = oop.Student("An", 15, 'male', 'Vinschool')

# sử dụng phương thức của lớp cha (HUman)
stu1.introduce()
# Sử dụng phương thức __str__
print(stu1)  
# Sử dụng phương thức show_info
stu2.show_info()
# sử dụng phương thức chỉnh sửa tên
stu2.edit_name('Duy An VipPro')
# stu2.edit_age()

# Đề bài:
# Tạo class Animal gồm các thuộc tính: tên, loài
# Viết 2 phương thức cho class Animal

# Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
# Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
# Viết 1 phương thức mới cho class Dog

# Yêu cầu:
# - Tạo class ở file oop.py
# - Viết chương trình test tại file main.py

dog1 = oop.Dog("Ki", "Dog", "Husky")
dog2 = oop.Dog("Vàng", "Dog", "Corgi")

dog1.show_info()
dog2.bite("bone")

dog2.edit_name('con mèo')
dog2.edit_breed()