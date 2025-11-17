# Bài 5: Chuyển đổi chuỗi số sang giá trị boolean

# Yêu cầu người dùng nhập một chuỗi số
chuoi_so = input("Nhập một số: ")

# Chuyển đổi từ string sang int, sau đó sang bool
so_nguyen = int(chuoi_so)
gia_tri_bool = bool(so_nguyen)

# In kết quả ra màn hình
print("Giá trị boolean sau khi chuyển đổi là:", gia_tri_bool)
