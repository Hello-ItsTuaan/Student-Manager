from manager import Manager
import os
from colorama import Fore, init, Style
init(autoreset=True)

def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")
manager = Manager()
manager.tai_json()

while True:
    clear()
    print(f"""
==================================
      📚 STUDENT MANAGER 📚
==================================
    1. ➕ Thêm học sinh
    2. 🗑️ Xóa học sinh
    3. Sửa Thông Tin HỌC SINH
    4. 🔍 Tìm học sinh
    5. 📋 Xem tất cả
    6. 💯 Nhập điểm 
    7. 📊 Xuất File .CSV (Microsoft Excel)
    8. 🚪 Thoát
==================================""")
    lua_chon = input(">>> ").strip()

    if lua_chon == "1":
        manager.them_hoc_sinh()
        
    elif lua_chon == "2":
        manager.xoa_hoc_sinh()
    elif lua_chon == "3":
        manager.edit_hoc_sinh()

    elif lua_chon == "4":
        manager.tim_hoc_sinh()
        
    elif lua_chon == "5":
        manager.hien_thi_tat_ca()
    
    elif lua_chon == "5":
        manager.nhap_diem()
    elif lua_chon == "7":
        manager.xuat_bang_diem_csv()
    elif lua_chon == "8":
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
        