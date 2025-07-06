# Tính chất kế thừa
class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi")

# Lớp Student kế thừa từ lớp Human
class Student(Human):
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender, school):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(name, age, gender)
        # school là thuộc tính đặc trưng của lớp Student
        self.school = school

    # Ghi đè (overwrite) phương thức lớp cha
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, học tại {self.school}')

    # Phương thức có sẵn (để dùng print)
    def __str__(self):
        return f'Student: {self.name}, {self.age} tuổi, {self.gender}, {self.school}'
    
    # Phương thức hiển thị thông tin 
    def show_info(self):
        print(f'''
========== THÔNG TIN ==========
Họ tên:         {self.name}
Tuổi:           {self.age}
Giới tính:      {self.gender}
Trường học:     {self.school}
===============================''')
        
    # Phương thức chỉnh sửa thông tin
        # Chỉnh sửa tuổi
    def edit_age(self):
        new_age = int(input('Nhập tuổi mới: '))
        if new_age <= 0:        # Sai tuổi
            print('Tuổi không hợp lệ')
        else:                   # Đúng tuổi
            # cập nhật tuổi cho đối tượng
            self.age = new_age
            print('Tuổi đã được cập nhật')
        # Hiển thị lại thông tin sau chỉnh sửa
        self.show_info()

        # Chỉnh sửa tên
    def edit_name(self, new_name):
        # Chỉnh sửa tên của đối tượng
        self.name = new_name
        # Hiển thị lại thông tin sau chỉnh sửa
        self.show_info()

# Bài tập

class Animal:
    # Khởi tạo thuộc tính
    def __init__(self, ten, loai):
        self.ten = ten
        self.loai = loai
    
    # Phương thức hiển thị thông tin
    def show_info(self):
        print(f'''
========== THÔNG TIN =========
Tên: {self.ten}
Loài: {self.loai}
==============================''')
        
    # Phương thức ăn
    def eat(self):
        print(f'{self.ten} đang ăn')

class Dog(Animal):
    # Khởi tạo thuộc tính
    def __init__(self, ten, loai, giong):
        super().__init__(ten, loai)  
        self.giong = giong

    # Phương thức hiển thị thông tin
    def show_info(self):
        print(f'''
========== THÔNG TIN =========
Tên: {self.ten}
Loài: {self.loai}
Giống: {self.giong}
==============================''')
        
    # Phương thức cắn vật thể
    def bite(self, obj):
        print(f'{self.ten} đang cắn {obj}')


    # Phương thức sửa tên
    def edit_name(self, new_name):
        # Chỉnh sửa tên của đối tượng
        self.ten = new_name
        # Hiển thị lại thông tin sau chỉnh sửa
        self.show_info()

    # Phương thức sửa giống
    def edit_breed(self):
        # Nhập thông tin mới
        new_breed = input("Nhập giống mới: ")
        # Chỉnh sửa giống của đối tượng
        self.giong = new_breed
        # Hiển thị lại thông tin sau chỉnh sửa
        self.show_info()


        
    