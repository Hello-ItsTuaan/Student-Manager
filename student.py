import uuid
import os
def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")
class Student:
    """Student's Informations"""
    def __init__(self, name, lop, giao_vien, sdt_cha_me):
        self.name = name
        self.lop = lop
        self.giao_vien = giao_vien
        self.sdt_cha_me = sdt_cha_me
        self.id = str(uuid.uuid4())
        self.mon_hoc = []

    def them_mon(self, ten, diem):
        self.mon_hoc.append({
            "ten": ten,
            "diem": diem
        })
    def tinh_gpa(self):
        tong_diem = 0
        tong_mon = 0
        for i in self.mon_hoc:
            tong_diem += i["diem"]
            tong_mon += 1
        
        if tong_mon == 0:
            return None
        else: 
            return tong_diem / tong_mon
        
    def xep_loai(self):
        gpa = self.tinh_gpa()
        if gpa is None:
            return "Chua co mon hoc"
        if gpa >= 9:
            return "Xuat Sac"
        elif gpa >= 8:
            return "Gioi"
        elif gpa >= 6.5:
            return "Kha"
        elif gpa >= 5:
            return "Trung binh"
        else:
            return "Yeu"
    
    def hien_thi(self):
        gpa = self.tinh_gpa()
        if gpa is None:
            gpa_str = "Chưa có môn học"
        else:
            gpa_str = round(gpa, 2)
        clear()
        print(f"""
==================================
👤 Tên: {self.name}
🏫 Lớp: {self.lop}
👨‍🏫 Giáo viên: {self.giao_vien}
📞 SĐT phụ huynh: {self.sdt_cha_me}
    ID: {self.id} 
----------------------------------
""")
        for mon in self.mon_hoc:
            print(f"    {mon['ten']:<12}: {mon['diem']}")
        print(f"""
----------------------------------
📊 GPA     : {gpa_str}
🏆 Xếp loại: {self.xep_loai()}
==================================""")
        input()
