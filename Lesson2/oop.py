# Khởi tạo đối tượng tổng quát
class Animal:
    # Hàm khởi tạo thuộc tính
    def __init__(self, type, name, age, color):
        # type, name, age, color là thuộc tính
        self.type = type
        self.name = name
        self.age = age
        self.color = color

    # Phương thức - hành động
    # Phương thức ăn
    def eat(self, food):
        print(f"{self.name} đang ăn {food}")

    # Phương thức hiển thị thông tin
        # Phương thức có sẵn (dùng được print)
    def __str__(self):
        return f'{self.type} - {self.name} - {self.age} - {self.color}'
    
        # Phương thức không có sẵn
    def show_info(self):
        print(f'''========== THÔNG TIN ==========
Type: {self.type}
Name: {self.name}
Age: {self.age}
Color: {self.color}
=================================''')
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Phương thức tính chu vi
    def cvi(self):
        return (self.width + self.height) * 2
    
    # Phương thức tính diện tích
    def dtich(self):
        return self.width * self.height
    
    # Phương thức hiển thị thông tin
    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'
    
    def show_info(self):
        print(f'''========== THÔNG TIN ===========
Width: {self.width}
Height: {self.height}
Chu vi: {self.cvi()}
Diện tích: {self.dtich()}
=================================''')
        
class BankAccount:
    def __init__(self, acc_number, balance):
        # Số tài khoản
        self.acc_number = acc_number
        # Số dư
        self.balance = balance
    
    def show_info(self):
        print(f'''========== THÔNG TIN ===========
Số tài khoản: {self.acc_number}
Số dư: ${round(self.balance, 2)}
=================================''')
        
    # Phương thức nạp tiền
    def deposit(self, amount):
        # amount: số tiền muốn nạp
        if amount > 0:
            # Cộng tiền vào số dư tài khoản
            self.balance += amount
            print(f'Nạp thành công ${amount}')
        else:
            print('Số tiền nạp không hợp lệ')
        # Hiển thị lại thông tin tài khoản
        self.show_info()

    # Phương thức rút tiền
    def withdraw(self, amount):
        # amount: số tiền muốn rút
        if 0 < amount <= self.balance:
            # Trừ tiền khỏi số dư tài khoản
            self.balance -= amount
            print(f'Rút thành công ${amount}')
        else:
            print('Số tiền rút không hợp lệ')
        # Hiển thị lại thông tin tài khoản
        self.show_info()
        
    def withdraw2(self):
        # amount: số tiền muốn rút
        amount = float(input('Nhập số tiền muốn rút: '))
        
        # Kiểm tra số tiền rút
        while amount <= 0 or amount > self.balance:
            print('Số tiền rút không hợp lệ')
            print(f'Số dư: {self.balance}')
            amount = float(input('Nhập số tiền muốn rút: '))

        # Rút tiền
        self.balance -= amount
        print(f'Rút thành công ${amount}')
        # Hiển thị lại thông tin tài khoản
        self.show_info()
        