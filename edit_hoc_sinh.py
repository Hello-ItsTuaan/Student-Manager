from prettytable import PrettyTable
from colorama import Style, init, Fore
import json

def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)
def edit_hs(manager):
    if len(manager.danhsach) == 0:
        print("There isn't any student! ")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Tên", "Lớp", "GPA", "Xếp Loại", "Số điện Thoại Phụ Huynh", "Tên Giáo Viên"]

        for hoc_sinh in manager.danhsach:
            gpa = hoc_sinh.tinh_gpa()
            if gpa is None:
                gpa_str = "Không Có"
            else:
                gpa_str = round(gpa, 2)
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
        id_can_sua = input("Nhập ID (của học sinh cần sửa): ")

    for hoc_sinh in manager.danhsach:
        if hoc_sinh.id == id_can_sua:   
            while True:
                try:
                    print("[1] Tên [2] Lớp [3] SĐT Phụ huynh [4] Tên Giáo Viên [5] Thoát")
                    sualuachon = int(input("Nhập lựa chọn bạn muốn chọn: "))
                    
                    if sualuachon == "1":

                        old_name = hoc_sinh.name
                        new_name = input(f"Tên cũ: {hoc_sinh.name}, bạn muốn sửa thành gì?: ")
                        hoc_sinh.name = new_name

                        manager.luu_json()

                        print(Fore.GREEN + f"SUCCESSFULLY: Changed student's name from [{old_name}] to [{new_name}]!")
                        input()
                        break
                    elif sualuachon == "2":

                        old_lop = hoc_sinh.lop
                        new_lop = input(f"Lớp cũ: {hoc_sinh.lop}, bạn muốn sửa thành gì?")
                        new_lop = hoc_sinh.lop
                        manager.luu_json()

                        print(Fore.GREEN + f"SUCCESSFULLY: Changed student's class from [{old_lop}] to [{new_lop}]!")
                        input()
                        break
                
                    elif sualuachon == "3":
                        #TODO: Continue implementing this features, otherwise add more information into your Prettytable table (Giao vien, SDT phu huynh,...)
                        old_sdt = hoc_sinh.sdt_cha_me
                        new_sdt = input(f"Lớp cũ: {hoc_sinh.sdt_cha_me}, bạn muốn sửa thành gì?")
                        new_sdt = hoc_sinh.sdt_cha_me
                        manager.luu_json()

                        print(Fore.GREEN + f"SUCCESSFULLY: Changed student's parents phone number from [{old_sdt}] to [{new_sdt}]!")
                        input()
                        break

                    elif sualuachon == "4":
                        old_giaovien = hoc_sinh.giao_vien
                        new_giaovien = input(f"Lớp cũ: {hoc_sinh.giao_vien}, bạn muốn sửa thành gì?")
                        new_giaovien = hoc_sinh.giao_vien
                        manager.luu_json()

                        print(Fore.GREEN + f"SUCCESSFULLY: Changed student's TEACHER NAME from [{old_giaovien}] to [{new_giaovien}]!")
                        input()
                        break

                    elif sualuachon == "5":
                        quitorno = input("Bạn thật sự muốn thoát?, Y/N: ")

                        if quitorno.lower() == "n":
                            clear()
                            continue
                            

                        elif quitorno.lower() == "y":
                            clear()
                            break
                except ValueError:
                    print(Fore.YELLOW + "WARNING: The Operation cannot complete! Did you type something that isn't in the list? ")
                    input()
                    clear()
                    continue
