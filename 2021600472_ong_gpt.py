import tkinter as tk

class Ong:
    def __init__(self, loai, van_toc, thoi_gian):
        self.loai = loai
        self.van_toc = van_toc
        self.thoi_gian = thoi_gian

    def tinh_quang_duong(self):
        return self.van_toc * self.thoi_gian

# Tạo danh sách ong
danh_sach_ong = []

def nhap_danh_sach():
    n = int(input("Nhập số lượng ong: "))
    for i in range(n):
        loai = input("Nhập loại ong: ")
        van_toc = float(input("Nhập vận tốc bay của ong: "))
        thoi_gian = float(input("Nhập thời gian bay của ong: "))
        ong = Ong(loai, van_toc, thoi_gian)
        danh_sach_ong.append(ong)

def in_danh_sach():
    for ong in danh_sach_ong:
        print("Loại ong:", ong.loai)
        print("Vận tốc bay:", ong.van_toc)
        print("Thời gian bay:", ong.thoi_gian)
        print("Quãng đường:", ong.tinh_quang_duong())
        print()

def tim_ong_van_toc_nhanh_nhat():
    ong_nhanh_nhat = None
    for ong in danh_sach_ong:
        if ong_nhanh_nhat is None or ong.van_toc > ong_nhanh_nhat.van_toc:
            ong_nhanh_nhat = ong
    if ong_nhanh_nhat:
        print("Ong có vận tốc nhanh nhất là:")
        print("Loại ong:", ong_nhanh_nhat.loai)
        print("Vận tốc bay:", ong_nhanh_nhat.van_toc)
        print("Thời gian bay:", ong_nhanh_nhat.thoi_gian)
        print("Quãng đường:", ong_nhanh_nhat.tinh_quang_duong())
        print()
    else:
        print("Không có ong trong danh sách.")
        print()

def dem_ong_quang_duong_dai_nhat():
    quang_duong_max = 0
    count = 0
    for ong in danh_sach_ong:
        quang_duong = ong.tinh_quang_duong()
        if quang_duong > quang_duong_max:
            quang_duong_max = quang_duong
            count = 1
        elif quang_duong == quang_duong_max:
            count += 1
    print("Số lượng ong bay được quãng đường dài nhất:", count)
    print("Quãng đường dài nhất:", quang_duong_max)
    print()

# Giao diện đồ họa sử dụng Tkinter
window = tk.Tk()
window.title("Ứng dụng quản lý ong")

label = tk.Label(window, text="Nhập danh sách ong:")
label.pack()

button_nhap = tk.Button(window, text="Nhập", command=nhap_danh_sach)
button_nhap.pack()

button_in = tk.Button(window, text="In danh sách", command=in_danh_sach)
button_in.pack()

button_tim = tk.Button(window, text="Tìm ong vận tốc nhanh nhất", command=tim_ong_van_toc_nhanh_nhat)
button_tim.pack()

button_dem = tk.Button(window, text="Đếm ong quãng đường dài nhất", command=dem_ong_quang_duong_dai_nhat)
button_dem.pack()

window.mainloop()
