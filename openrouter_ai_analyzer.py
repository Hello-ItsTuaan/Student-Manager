import json
import shutil
from discord_notifier import gui_discord
from colorama import Fore, Style, init
import os
import time
init(autoreset=True)  # Tự động reset màu sau mỗi lần print, không cần reset thủ công

width = shutil.get_terminal_size().columns

def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")
    
    
def lay_api_key():
    try:
        with open('config.json', 'r') as file:
            api_key = json.load(file)
    
    except json.JSONDecodeError:
        print(Fore.RED + "ERROR: Cannot locate your API KEY, did you put it in?")
        return {} # Trả về dict trống để xử lý tiếp, không bị sập app
    except FileNotFoundError:
        print(Fore.RED + "ERROR: Cannot locate your API KEY")

    
    if len(api_key.get("openrouter_api_key", "")) == 0:
        print("Cannot find your OpenRouter AI API key, did you put it in?".center(width))
        
        while True:
            print("=====".center(width))
            print("Do you want to add your API key to our system now? yes/no".center(width))
            put = input(">>>")
            put = str(put)
            if put.lower() == "yes":
                api_key["openrouter_api_key"] = input("Please enter your Openrouter API key: ")

                try:
                    with open("config.json", "w") as file:
                        json.dump(api_key, file, indent=4)
                        print(Fore.GREEN + "SUCCESS: API key SAVED!")
                        input()
                        return api_key
                    
                except FileNotFoundError:    
                    print(Fore.RED + "ERROR: FileNotFoundError")
                    
            elif put.lower() == "no":
                
                print(Fore.LIGHTYELLOW_EX + "Warning: Because you didn't enter your API key, you cannot use 'AI Analyzer' feature!")
                return None
            else: 
                continue
    else:
        return api_key

    
def ai_analyzer():
    from openrouter import OpenRouter
    import os
    try:
        print("Loading...(Or press Ctrl + C to cancle the progress)")
        
        with open("config.json", "r") as file:
            data = json.load(file)
        api_key = data.get("openrouter_api_key")
        
        #LAY danhsachhocsinh de import vao cho AI
        with open("danh_sach_hoc_sinh.json", "r", encoding="utf-8") as file:
            data_str = json.load(file)

        
        with OpenRouter(api_key=api_key) as client:
            response = client.chat.send(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"""Bạn là trợ lý phân tích học tập. Dưới đây là dữ liệu học sinh CỦA TÔI:
{data_str}

Hãy thực hiện các việc sau, viết bằng tiếng Việt, giọng văn tự nhiên như giáo viên chủ nhiệm:

1. Tổng quan tình hình học tập (2-3 câu ngắn gọn).
2. Bảng điểm chi tiết theo từng môn — trình bày dưới dạng bảng ASCII căn chỉnh thẳng hàng
   bằng ký tự `-` và `|`, và PHẢI đặt toàn bộ bảng bên trong code block ba dấu backtick (```)
   để Discord hiển thị đúng font monospace, không bị lệch cột.
3. Nhận xét môn học cần cải thiện và môn học đang làm tốt.
4. Đưa ra 2-3 lời khuyên cụ thể, ngắn gọn, có thể hành động ngay.

Yêu cầu định dạng bắt buộc:
- KHÔNG dùng cú pháp Markdown của Discord như **in đậm**, *in nghiêng*, # tiêu đề, gạch đầu dòng "-".
- Chỉ dùng bảng ASCII (trong code block ```) và văn xuôi thường cho phần còn lại.
- Toàn bộ nội dung trả về KHÔNG được vượt quá 1900 ký tự (để chừa khoảng trống an toàn dưới giới hạn 2000 ký tự của Discord webhook, tránh lỗi 400).
- Nếu dữ liệu quá dài không thể tóm gọn trong 1900 ký tự, hãy ưu tiên rút gọn phần nhận xét,
  giữ nguyên bảng điểm.
- Không thêm lời chào, lời dẫn thừa (ví dụ "Dưới đây là phân tích của tôi:"). + xưng hộ là tôi với bạn, sử dụng emoji càng tốt!"""}
                ]
            )
            
            
            

            clear()
            print(response.choices[0].message.content)
            guiorno = str(input(Fore.LIGHTYELLOW_EX + "Do you want to send this response to your Discord through your Discord Webhook? yes/no: "))
            if guiorno.lower() =="yes":
                gui_discord(message=response.choices[0].message.content)
            elif guiorno.lower() == "no":
                time.sleep(1)
                pass
    except KeyboardInterrupt:
        clear()
        print("Stand by...".center(width))
        time.sleep(0.5)
        pass

        
        
        
