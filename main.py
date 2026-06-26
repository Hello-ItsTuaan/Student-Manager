from manager import Manager
import os
def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")
manager = Manager()
manager.tai_json()

while True:
    clear()
    print("""
==================================
      📚 STUDENT MANAGER 📚
==================================
  1. ➕ Thêm học sinh
  2. 🗑️  Xóa học sinh
  3. 🔍 Tìm học sinh
  4. 📋 Xem tất cả
  5. 💯 Nhập điểm 
  6. 🚪 Thoát
==================================""")
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
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
        