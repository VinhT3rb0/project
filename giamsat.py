import time
import json
import os
import matplotlib.pyplot as plt

NGUONG_NHIET_DO = 35  # °C
NGUONG_DO_AM = 80     # %
NGUONG_TOC_DO_GIO = 50  # km/h

TEN_FILE = 'thong_so_moi_truong.json'

def nap_du_lieu():
    if os.path.exists(TEN_FILE):
        with open(TEN_FILE, 'r') as f:
            return json.load(f)
    return []

def luu_du_lieu(danh_sach_thong_so):
    with open(TEN_FILE, 'w') as f:
        json.dump(danh_sach_thong_so, f)

def nhap_thong_so():
    nhiet_do = float(input("Nhập nhiệt độ (°C): "))
    do_am = float(input("Nhập độ ẩm (%): "))
    huong_gio = input("Nhập hướng gió (Bắc, Nam, Đông, Tây...): ")
    toc_do_gio = float(input("Nhập tốc độ gió (km/h): "))
    
    return {
        'Nhiệt độ': nhiet_do,
        'Độ ẩm': do_am,
        'Hướng gió': huong_gio,
        'Tốc độ gió': toc_do_gio
    }

def kiem_tra_canh_bao(thong_so):
    if thong_so['Nhiệt độ'] > NGUONG_NHIET_DO:
        print("CẢNH BÁO: Nhiệt độ vượt ngưỡng!")
    if thong_so['Độ ẩm'] > NGUONG_DO_AM:
        print("CẢNH BÁO: Độ ẩm vượt ngưỡng!")
    if thong_so['Tốc độ gió'] > NGUONG_TOC_DO_GIO:
        print("CẢNH BÁO: Tốc độ gió vượt ngưỡng!")

def tinh_toan_thong_so(danh_sach, key):
    gia_tri_hien_tai = danh_sach[-1][key]
    gia_tri_cao_nhat = max(danh_sach, key=lambda x: x[key])[key]
    gia_tri_thap_nhat = min(danh_sach, key=lambda x: x[key])[key]
    gia_tri_trung_binh = sum(x[key] for x in danh_sach) / len(danh_sach)
    
    return gia_tri_hien_tai, gia_tri_cao_nhat, gia_tri_thap_nhat, gia_tri_trung_binh

def hien_thi_thong_so(danh_sach_thong_so):
    if danh_sach_thong_so:
        for key in ['Nhiệt độ', 'Độ ẩm', 'Tốc độ gió']:
            hien_tai, cao_nhat, thap_nhat, trung_binh = tinh_toan_thong_so(danh_sach_thong_so, key)
            print(f"{key}: Hiện tại = {hien_tai}, Cao nhất = {cao_nhat}, Thấp nhất = {thap_nhat}, Trung bình = {trung_binh:.2f}")
    else:
        print("Chưa có thông số nào được lưu trữ.")

def ve_bieu_do(danh_sach_thong_so):
    nhiet_do_list = [x['Nhiệt độ'] for x in danh_sach_thong_so]
    do_am_list = [x['Độ ẩm'] for x in danh_sach_thong_so]
    toc_do_gio_list = [x['Tốc độ gió'] for x in danh_sach_thong_so]

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(nhiet_do_list, label='Nhiệt độ', color='r')
    plt.ylabel('Nhiệt độ (°C)')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(do_am_list, label='Độ ẩm', color='b')
    plt.ylabel('Độ ẩm (%)')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(toc_do_gio_list, label='Tốc độ gió', color='g')
    plt.ylabel('Tốc độ gió (km/h)')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    danh_sach_thong_so = nap_du_lieu() 

    while True:
        print("\nNhập thông số môi trường mới:")
        thong_so = nhap_thong_so()
        danh_sach_thong_so.append(thong_so) 
        
        kiem_tra_canh_bao(thong_so)  
        hien_thi_thong_so(danh_sach_thong_so) 

        ve_bieu_do(danh_sach_thong_so)

        luu_du_lieu(danh_sach_thong_so)
        tiep_tuc = input("\nBạn có muốn nhập thêm thông số? (y/n): ").lower()
        if tiep_tuc != 'y':
            break

    luu_du_lieu(danh_sach_thong_so)
    print("Dữ liệu đã được lưu trước khi dừng chương trình.")

if __name__ == "__main__":
    main()
