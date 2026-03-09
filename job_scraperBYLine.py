
import os
import requests

def send_to_line(message):
    token = os.getenv('LINE_NOTIFY_TOKEN') 
    if not token:
        print("❌ 錯誤：環境變數中找不到 LINE_NOTIFY_TOKEN")
        return

    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"message": message}
    
    response = requests.post(url, headers=headers, data=payload)
    # 在日誌中印出結果，方便我們在 GitHub 診斷
    print(f"📡 LINE 回應狀態：{response.status_code}, 內容：{response.text}")
    
    if response.status_code == 200:
        print("✅ 戰報已成功送達主公手機")

# --- 這裡開始是執行邏輯 ---

# 1. 先發送一則開機測試（確保 GitHub 與 LINE 的橋樑是通的）
send_to_line("🛡️ 澗蒼國・雲端戰報系統：已於 GitHub Actions 成功登陸！")

# 2. 接下來才是您的爬蟲邏輯（範例）
# found_jobs = ["自動化QA工程師 - 台中", "軟體測試工程師"]
# for job in found_jobs:
#     send_to_line(f"發現職缺：{job}")