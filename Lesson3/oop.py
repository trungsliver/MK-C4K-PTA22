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