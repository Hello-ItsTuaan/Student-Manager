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
  {Fore.BLUE}1. ➕ Thêm học sinh
  {Fore.RED}2. 🗑️ Xóa học sinh
  {Fore.WHITE}3. 🔍 Tìm học sinh
  {Fore.YELLOW}4. 📋 Xem tất cả
  {Fore.CYAN}5. 💯 Nhập điểm 
  {Fore.GREEN}6. 📊 Xuất File .CSV (Microsoft Excel)
  {Fore.RED}7. 🚪 Thoát
{Fore.WHITE}==================================""")
    lua_chon = input(">>> ").strip()

    if lua_chon == "1":
        manager.them_hoc_sinh()
        
    elif lua_chon == "2":
        manager.xoa_hoc_sinh()
        
    elif lua_chon == "3":
        manager.tim_hoc_sinh()
        
    elif lua_chon == "4":
        manager.hien_thi_tat_ca()
    
    elif lua_chon == "5":
        manager.nhap_diem()
    elif lua_chon == "6":
        manager.xuat_bang_diem_csv()
    elif lua_chon == "7":
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
        