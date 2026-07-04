from manager import Manager
import os
from colorama import Fore, init, Style
import sys

init(autoreset=True)

def resize_terminal(cols, rows):
    # \x1b[8;ROWS;COLSxt is the standard ANSI escape sequence for resizing
    sys.stdout.write(f"\x1b[8;{rows};{cols}t")
    sys.stdout.flush()

# Example: Set terminal to 120 columns wide and 40 rows high
resize_terminal(150, 30)

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
    3. ✏️ Sửa Thông Tin HỌC SINH
    4. 🔍 Tìm học sinh
    5. 📋 Xem tất cả
    6. 💯 Nhập điểm 
    7. 📊 Xuất File .CSV (Microsoft Excel)
    8. 🪟 AI Analyzer (Require Openrouter API KEY!)
    9. 🚪 Thoát
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
    
    elif lua_chon == "6":
        manager.nhap_diem()
    elif lua_chon == "7":
        manager.xuat_bang_diem_csv()
    elif lua_chon == "8":
        manager.module_ai_analyzer()
    elif lua_chon == "9":
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
        