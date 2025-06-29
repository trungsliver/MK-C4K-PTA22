import oop

# Khởi tạo đối tượng
a1 = oop.Animal('Dog', 'Ki', 2, 'black')
a2 = oop.Animal('Beaver', 'Loopy', 3, 'pink')
a3 = oop.Animal(type = 'Cat', 
                name = 'Tom', 
                age = 1, 
                color = 'white')

# Hiển thị thông tin đối tượng
print(a3)
    # Hiển thị từng thuộc tính
print(a1.type, a1.name, a1.age, a1.color)
    # Dùng phương thức
a2.show_info()

# Bài tập Rectangle
    # Khởi tạo đối tượng cụ thể
hcn1 = oop.Rectangle(3, 5)
hcn2 = oop.Rectangle(4, 6)
    # Hiển thị tất cả thông tin
hcn1.show_info()
hcn2.show_info()
    # Gọi từng phương thức
print('Chu vi hcn1:', hcn1.cvi())

# Bài tập BankAccount
    # Khởi tạo đối tượng    
acc1 = oop.BankAccount('Gia Bach', 100)
    # Hiển thị thông tin tài khoản
acc1.show_info()
    # Phương thức nạp tiền
acc1.deposit(-50)
acc1.deposit(0.1)
    # Phương thức rút tiền
acc1.withdraw(-5)
acc1.withdraw(99)

acc1.withdraw2()