# Bài 7: Làm tròn số thập phân và chuyển thành số nguyên

# Yêu cầu người dùng nhập một chuỗi số thập phân
chuoi_so = input("Nhập một số thập phân: ")

# Chuyển đổi chuỗi thành số thực
so_thuc = float(chuoi_so)

# Làm tròn số đến một chữ số thập phân
so_lam_tron = round(so_thuc, 1)

# Chuyển đổi thành số nguyên
so_nguyen = int(so_lam_tron)

# In kết quả ra màn hình
print("Số sau khi làm tròn và chuyển thành số nguyên:", so_nguyen)
