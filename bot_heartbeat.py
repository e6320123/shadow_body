# --- [ 數位分身：心跳偵測模組 ] ---
import requests
from datetime import datetime

def check_target():
    # 這裡我們模擬偵查 104 的首頁是否正常運行
    target_url = "https://www.104.com.tw"
    
    try:
        response = requests.get(target_url, timeout=10)
        status = "【正常】" if response.status_code == 200 else "【異常】"
    except Exception as e:
        status = f"【偵查失敗：{e}】"
    
    # 格式化輸出報告
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report = f"報告主公：分身於 {current_time} 執行偵查任務。\n目標 104 狀態：{status}\n--- 數位分身運作中，請主公安心 ---"
    
    print(report)

if __name__ == "__main__":
    check_target()