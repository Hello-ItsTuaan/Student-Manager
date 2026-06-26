import shutil
from colorama import Fore, Style, init

init(autoreset=True)  # Tự động reset màu sau mỗi lần print, không cần reset thủ công
width = shutil.get_terminal_size().columns


def chon_mon():
    vietnamese_subjects = {
        # --- Cấp 1, 2, 3 ---
        1: "Toán",
        2: "Tiếng Việt",
        3: "Ngữ văn",
        4: "Tiếng Anh",
        5: "Đạo đức",
        6: "Giáo dục công dân",
        7: "Tự nhiên và Xã hội",
        8: "Khoa học tự nhiên",
        9: "Lịch sử và Địa lí",
        10: "Tin học",
        11: "Công nghệ",
        12: "Âm nhạc",
        13: "Mĩ thuật",
        14: "Giáo dục thể chất",
        15: "Vật lí",
        16: "Hóa học",
        17: "Sinh học",
        18: "Lịch sử",
        19: "Địa lí",
        20: "Giáo dục kinh tế và pháp luật",
        21: "Giáo dục quốc phòng và an ninh",

        # --- Đại học (Đại cương) ---
        22: "Triết học Mác - Lênin",
        23: "Kinh tế chính trị",
        24: "Chủ nghĩa xã hội khoa học",
        25: "Lịch sử Đảng",
        26: "Tư tưởng Hồ Chí Minh",
        27: "Toán cao cấp",
        28: "Xác suất thống kê",

        # --- Đại học (Chuyên ngành) ---
        29: "Cấu trúc dữ liệu và Giải thuật",
        30: "Lập trình hướng đối tượng",
        31: "Cơ sở dữ liệu",
        32: "Mạng máy tính",
        33: "Trí tuệ nhân tạo",
        34: "Hình họa - Vẽ kỹ thuật",
        35: "Lý thuyết ô tô",
        36: "Kinh tế vi mô",
        37: "Kinh tế vĩ mô",
        38: "Quản trị học",
        39: "Marketing căn bản",
        40: "Giải phẫu học",
        41: "Sinh lý học",
        42: "Dược lý học",
        43: "Bệnh học nội khoa",
        44: "Phát triển ứng dụng Web",
        45: "Kỹ năng Biên - Phiên dịch"
    }
    try:
        for so, ten in vietnamese_subjects.items():
            print(f"  [{so}] {ten}")

        lua_chon = input(f"Chọn môn học {Fore.GREEN}(VD: 1 3 5) {Fore.WHITE} or {Fore.GREEN} (VD: 1, 2, 3) : ")
        if "," in lua_chon:
            tong_mon_hoc = lua_chon.split(",")
            lua_chon = lua_chon.split()
        else:
            lua_chon = lua_chon.split()
        
        ketqua = []
        for mon_hoc in tong_mon_hoc:
            mon_hoc = int(mon_hoc)
            ketqua.append(vietnamese_subjects[mon_hoc])
                    
        for ten in ketqua:
            print(f"🟢 {ten}")

        print(f"\nĐã chọn {len(ketqua)} môn học!")
        input()
        
        xac_nhan = input(f"\nXác nhận? y/n")
        if xac_nhan.lower() == "y":
            return ketqua
        if xac_nhan.lower() == "n":
            return None

    except ValueError:
        print(Fore.RED + "ERROR: You can only input NUMBERS!")
        return
    except KeyError:
        print(Fore.RED + "ERROR: Make sure you have entered numbers that are around 1-45")
        return