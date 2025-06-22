# Lập trình hướng đối tượng
# Object-Oriented Programming - OOP

# Tổng quát: OOP là cách mà chúng ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Ví dụ: mô phỏng Human (con người)
    # Thuộc tính (đặc điểm): tên, tuổi, giới tính,...
    # Phương thức (hành động): ăn, ngủ, nói chuyện,...

# Khai báo lớp đối tượng
class Human:
    # Khởi tạo giá trị (thuộc tính) - đây là hàm có sẵn
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (hành động)
    # Phương thức giới thiệu 
    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi")

    # Phương thức hát
    def sing(self, song):
        print(f"{self.name} đang hát {song}")

    # Phương thức hiển thị thông tin (sử dụng được print)
    def __str__(self):
        return f'{self.name} - {self.age} - {self.gender}'

# Khởi tạo đối tượng cụ thể
h1 = Human('Duy An', 15, 'male')
# Hiển thị thông tin
print(h1)       # chỉ hiển thị nơi lưu
print(h1.name)  # hiển thị tên
# Sử dụng phương thức
h1.introduce()  
h1.sing('Baby Shark')  

