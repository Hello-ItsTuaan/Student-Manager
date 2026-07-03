import csv
from discord_notifier import gui_discord
from colorama import Style, init, Fore
import platform
init(autoreset=True)

def xuat_csv(danhsach, ten_file="bang_diem.csv"):
    tat_ca_mon = set()
    for hoc_sinh in danhsach:
        for mon in hoc_sinh.mon_hoc:
            tat_ca_mon.add(mon["ten"])
    
    with open(ten_file, "w", newline="", encoding="utf-8") as file: 
        writer = csv.writer(file)
        writer.writerow(["ID", "Ten", "Lop", "SDT_PH", "Xep_Loai"] + list(tat_ca_mon))

        for hoc_sinh in danhsach:
            diem_cua_hoc_sinh = {}
            for mon in hoc_sinh.mon_hoc:
                diem_cua_hoc_sinh[mon["ten"]] = mon["diem"]
            
            hang = [hoc_sinh.id, hoc_sinh.name, hoc_sinh.lop, hoc_sinh.sdt_cha_me, hoc_sinh.xep_loai()]
            for ten_mon in tat_ca_mon:
                hang.append(diem_cua_hoc_sinh.get(ten_mon, None))
                writer.writerow(hang)
            print(Fore.WHITE + "File saved successfully!")
            input()
        
            
            