from student import Student
import json
import os
import shutil
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
        print(f"✅ Đã thêm học sinh {name} thành công!".center(width))
        self.luu_json()
        input()
        clear()

        

    def xoa_hoc_sinh(self):
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
                print(f"✅ Đã xóa học sinh {hoc_sinh.name} thành công!")
                self.luu_json()
                input()
                return
        else: 
                print("❌ Không tìm thấy học sinh với ID này!")
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
            for hoc_sinh in self.danhsach:
                hoc_sinh.hien_thi()
                
        

        
