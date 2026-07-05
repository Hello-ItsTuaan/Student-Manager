from prettytable import PrettyTable
import os
from colorama import Style, init, Fore
import json

def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)

def edit_hs(manager):
    if len(manager.danhsach) == 0:
        print("There isn't any student!")
        input("Nhấn Enter để quay lại...")
        return  # Thoát hàm ngay nếu không có học sinh nào

    # Vòng lặp chính: Bắt buộc nhập đúng ID học sinh hoặc chọn thoát ra ngoài
    while True:
        clear()
        table = PrettyTable()
        table.field_names = ["ID", "Tên", "Lớp", "GPA", "Xếp Loại", "Số điện Thoại Phụ Huynh", "Tên Giáo Viên"]

        for hoc_sinh in manager.danhsach:
            gpa = hoc_sinh.tinh_gpa()
            gpa_str = "Không Có" if gpa is None else round(gpa, 2)
            table.add_row([
                hoc_sinh.id,
                hoc_sinh.name,
                hoc_sinh.lop,
                gpa_str,
                hoc_sinh.xep_loai(),
                hoc_sinh.sdt_cha_me,
                hoc_sinh.giao_vien
            ])
        print(table)
        
        id_can_sua = input("Nhập ID (của học sinh cần sửa, hoặc gõ 'exit' để thoát): ").strip()
        
        if id_can_sua.lower() == 'exit':
            break  # Thoát khỏi hàm để về menu chính

        tim_thay = False
        
        # Duyệt qua toàn bộ danh sách để tìm học sinh khớp ID
        for hoc_sinh in manager.danhsach:
            if hoc_sinh.id == id_can_sua:   
                tim_thay = True
                
                # Vòng lặp quản lý menu các trường thông tin cần sửa của học sinh này
                while True:
                    try:
                        print("\n[1] Tên [2] Lớp [3] SĐT Phụ huynh [4] Tên Giáo Viên [5] Thoát")
                        sualuachon = input("Nhập lựa chọn bạn muốn chọn: ").strip()
                        
                        if sualuachon == "1":
                            old_name = hoc_sinh.name
                            new_name = input(f"Tên cũ: {hoc_sinh.name}, bạn muốn sửa thành gì?: ")
                            hoc_sinh.name = new_name
                            manager.luu_json()
                            print(Fore.GREEN + f"SUCCESSFULLY: Changed student's name from [{old_name}] to [{new_name}]!")
                            input("Nhấn Enter để tiếp tục...")
                            clear()
                            
                        elif sualuachon == "2":
                            old_lop = hoc_sinh.lop
                            new_lop = input(f"Lớp cũ: {hoc_sinh.lop}, bạn muốn sửa thành gì?: ")
                            hoc_sinh.lop = new_lop
                            manager.luu_json()
                            print(Fore.GREEN + f"SUCCESSFULLY: Changed student's class from [{old_lop}] to [{new_lop}]!")
                            input("Nhấn Enter để tiếp tục...")
                            clear()
                    
                        elif sualuachon == "3":
                            old_sdt = hoc_sinh.sdt_cha_me
                            new_sdt = input(f"SĐT cũ: {hoc_sinh.sdt_cha_me}, bạn muốn sửa thành gì?: ")
                            hoc_sinh.sdt_cha_me = new_sdt
                            manager.luu_json()
                            print(Fore.GREEN + f"SUCCESSFULLY: Changed student's parents phone number from [{old_sdt}] to [{new_sdt}]!")
                            input("Nhấn Enter để tiếp tục...")
                            clear()

                        elif sualuachon == "4":
                            old_giaovien = hoc_sinh.giao_vien
                            new_giaovien = input(f"Giáo viên cũ: {hoc_sinh.giao_vien}, bạn muốn sửa thành gì?: ")
                            hoc_sinh.giao_vien = new_giaovien
                            manager.luu_json()
                            print(Fore.GREEN + f"SUCCESSFULLY: Changed student's TEACHER NAME from [{old_giaovien}] to [{new_giaovien}]!")
                            input("Nhấn Enter để tiếp tục...")
                            clear()

                        elif sualuachon == "5":
                            quitorno = input("Bạn thật sự muốn thoát?, Y/N: ").strip().lower()
                            if quitorno == "n":
                                clear()
                                continue
                            elif quitorno == "y":
                                clear()
                                break  # Thoát khỏi menu chọn trường, quay lại menu nhập ID
                                
                    except Exception as e:
                        print(Fore.LIGHTYELLOW_EX + f"WARNING: The Operation cannot complete! Error: {e}")
                        input("Nhấn Enter để thử lại...")
                        clear()
                        continue
                
                break  # Thoát khỏi vòng lặp `for` duyệt học sinh sau khi đã sửa xong

        # ĐOẠN KHỐI LOGIC CỐT LÕI ĐƯỢC ĐƯA RA NGOÀI VÒNG LẶP FOR
        if tim_thay:
            break  # Nếu đã tìm thấy và sửa thành công, thoát hẳn vòng lặp chính để về Menu quản lý học sinh chính
        else: 
            # Chỉ báo lỗi khi đã duyệt qua TẤT CẢ học sinh mà không có ai trùng ID
            print(Fore.LIGHTYELLOW_EX + "\nPlease enter a valid student's ID!")
            input("Nhấn Enter để làm mới danh sách và nhập lại...")
