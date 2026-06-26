from student import Student
import json
from discord_notifier import gui_discord
import os
import shutil
from prettytable import PrettyTable
from datetime import datetime
width = shutil.get_terminal_size().columns

def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")

class Manager:
    """QUAN LY HOC SINH"""
    def __init__(self):
        self.danhsach = []
    def luu_json(self):
        data = []
        for hs in self.danhsach:
            data.append({
                "id": hs.id,
                "ten": hs.name,
                "lop": hs.lop,
                "giao_vien": hs.giao_vien,
                "sdt_phu_huynh": hs.sdt_cha_me,
                "mon_hoc": hs.mon_hoc,
                "gpa": hs.tinh_gpa(),
                "xep_loai": hs.xep_loai(),
            })
        with open("danh_sach_hoc_sinh.json", "w", encoding="utf-8") as file: 
            json.dump(data, file, ensure_ascii=False, indent=4)
        
    def tai_json(self):
        try:
            with open("danh_sach_hoc_sinh.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                for hs in data:
                    hoc_sinh = Student(hs["ten"], hs["lop"], hs["giao_vien"], hs["sdt_phu_huynh"])
                    hoc_sinh.id = hs["id"]         
                    hoc_sinh.mon_hoc = hs["mon_hoc"] 
                    self.danhsach.append(hoc_sinh)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass


    def them_hoc_sinh(self):
        print("Nhập Tên của bạn")
        name = input(">>>")
        print("Nhập lớp của bạn")
        lop = input(">>>")
        print("Nhập tên giáo viên của bạn")
        ten_giao_vien = input(">>>")
        print("Nhập Số Điện Thoại phụ huynh (Cha/Mẹ)")
        sdt_phuhuynh = input(">>>")
        clear()
        hoc_sinh_moi = Student(name, lop, ten_giao_vien, sdt_phuhuynh)
        self.danhsach.append(hoc_sinh_moi)
        gio_hien_tai = datetime.now().strftime("%H:%M %d/%m/%Y")
        self.luu_json()
        
        message = f"""➕ Đã thêm học sinh mới
👤 Tên: {name}
🏫 Lớp: {lop}
👨‍🏫 GVCN: {ten_giao_vien}
📞 SĐT phụ huynh: {sdt_phuhuynh}
🕐 Thời gian: {gio_hien_tai}
                """
        gui_discord(message)
        print(f"✅ Đã thêm học sinh {name} thành công!".center(width))
        input()
        clear()

        

    def xoa_hoc_sinh(self):
        gio_hien_tai = datetime.now().strftime("%H:%M %d/%m/%Y")
        clear()
        print(f"""
==================================
📋 DANH SÁCH HỌC SINH
""")
        for hoc_sinh in self.danhsach:
            print(f"ID: {hoc_sinh.id} | 👤 {hoc_sinh.name} | 🏫 {hoc_sinh.lop}")
        print("==================================")

        id_can_xoa = input("Nhap ID cua Hoc Sinh can xoa: ")
        
        for hoc_sinh in self.danhsach:
            if hoc_sinh.id == id_can_xoa:
                self.danhsach.remove(hoc_sinh)
                print(f"✅ Đã xóa học sinh {hoc_sinh.name} thành công!".center(width))
                self.luu_json()
                message = f"""❌ Đã xóa học sinh mới
👤 Tên: {hoc_sinh.name}
🏫 Lớp: {hoc_sinh.lop}
👨‍🏫 GVCN: {hoc_sinh.giao_vien}
📞 SĐT phụ huynh: {hoc_sinh.sdt_cha_me}
🕐 Thời gian: {gio_hien_tai}
"""
                gui_discord(message)
                input()
                return
        else: 
                print("❌ Không tìm thấy học sinh với ID này!".center(width))
                input()
    
    def tim_hoc_sinh(self):
        hoc_sinh_khop = []
        hoc_sinh_can_tim = input("Nhập tên học sinh cần tim: ")
        for hoc_sinh in self.danhsach:
            if hoc_sinh_can_tim.lower() in hoc_sinh.name.lower():
                hoc_sinh_khop.append(hoc_sinh)
        if len(hoc_sinh_khop) == 0:
            print("❌ Không tìm thấy!")
            input()
        else:
            for hs in hoc_sinh_khop:
                hs.hien_thi()
                input()

    
    def hien_thi_tat_ca(self):
        if len(self.danhsach) == 0:
            print("📭 Danh sách trống!")
            input()
        else:
            table = PrettyTable()
            table.field_names = ["ID", "Tên", "Lớp", "GPA", "Xếp Loại"]

            for hoc_sinh in self.danhsach:
                gpa = hoc_sinh.tinh_gpa()
                if gpa is None:
                    gpa_str = "Chưa có"
                else:
                    gpa_str = round(gpa, 2)
                table.add_row([
                    hoc_sinh.id[:8],
                    hoc_sinh.name,
                    hoc_sinh.lop,
                    gpa_str,
                    hoc_sinh.xep_loai()
                ])
            print(table)
            input()