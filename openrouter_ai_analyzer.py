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
    print("Loading...")
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
                {"role": "user", "content": f"""Bạn là trợ lý phân tích học tập. Dưới đây là dữ liệu học sinh (định dạng JSON):

{data_str}

Hãy phân tích và trình bày theo cấu trúc sau, VẼ BẢN PHÂN TÍCH (VISUAL ANALYTIC nhưng không bị lỗi format/thụt lề, phải KIỂM TRA LẠI, vì response của bạn sẽ được hiện thị trong Terminal thay vì trình duyệt hoặc markdown nên cần cẩn thận, k để bị lỗi thụt lề cho các ký tự ở cuối bản như "|") (chạy được trong terminal, có thể xài markdown và vẽ bản bằng _, |,...):

1. TỔNG QUAN: GPA trung bình, số học sinh mỗi xếp loại
2. HỌC SINH CẦN CHÚ Ý: liệt kê học sinh có GPA thấp hoặc môn yếu rõ rệt
3. MÔN HỌC YẾU NHẤT: môn nào điểm trung bình thấp nhất trong toàn bộ danh sách
4. GỢI Ý: 2-3 gợi ý cụ thể, ngắn gọn

Trả lời bằng tiếng Việt và cả Tiếng Anh, càng chi tiết càng tốt, sử dụng Markdown"""}
            ],
        )
        
        
        

        clear()
        print(response.choices[0].message.content)
        guiorno = str(input(Fore.LIGHTBLUE_EX + "Do you want to send this response to your Discord through your Discord Webhook? yes/no: "))
        if guiorno.lower() =="yes":
            gui_discord(message=response.choices[0].message.content)
        elif guiorno.lower() == "no":
            time.sleep(1)
            pass

        
        
        
