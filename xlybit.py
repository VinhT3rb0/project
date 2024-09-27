import time
from EmulatorGUI import GPIO
def kiem_tra_byte(byte_str):
    if len(byte_str) == 8 and all(bit in '01' for bit in byte_str):
        return True
    else:
        return False
def xoa_bit(byte_str):
    byte_list = list(byte_str)
    for i in range(len(byte_list)):
        byte_list[i] ='0'
        print("".join(byte_list))
        time.sleep(1)
def hien_thi(byte_list):
    print("".join(byte_list))  
    time.sleep(1)  

def chuyen_dong_bit():
    byte_list = ['0'] * 8  
    
    while True: 
        byte_list[3], byte_list[4] = '1', '1'
        hien_thi(byte_list)
        for i in range(1, 4): 
            byte_list[3-i], byte_list[4+i] = '1', '1'  
            byte_list[3-i+1], byte_list[4+i-1] = '0', '0'  
            hien_thi(byte_list)

        byte_list[0], byte_list[7] = '0', '0'
        hien_thi(byte_list)

        for i in range(3, 0, -1):  
            byte_list[3-i], byte_list[4+i] = '0', '0'  
            byte_list[3-i+1], byte_list[4+i-1] = '1', '1'  
            hien_thi(byte_list)
def main():
    byte_str = input("Nhập vào một byte (8 bit): ")
    if(kiem_tra_byte(byte_str)):
        print("Byte đã nhập:",byte_str)
        xoa_bit(byte_str)
        chuyen_dong_bit()
    else:
        print("Lỗi chuỗi phải có 8 ký tự chứa các số 0 và 1")
main()