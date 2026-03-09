import os
import requests

def send_to_line(message):
    # 從保險箱讀取 Token
    token = os.getenv('LINE_NOTIFY_TOKEN') 
    if not token:
        print("❌ 錯誤：找不到 LINE_NOTIFY_TOKEN")
        return

    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"message": message}
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("✅ 戰報已成功送達主公手機")

# 在爬蟲抓到資料後，直接調用
# send_to_line("\n[戰報] 發現 104 自動化 QA 職缺！")