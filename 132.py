import requests
from datetime import datetime

def check_target():
    target_url = "https://www.104.com.tw"
    
    # --- [ 偽裝面具：模擬真實瀏覽器 ] ---
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.google.com/"
    }
    
    try:
        # 加入 headers 進行請求
        response = requests.get(target_url, headers=headers, timeout=15)
        
        # 只要回傳 200 或 403 (代表至少有觸碰到伺服器) 都算初步成功
        if response.status_code == 200:
            status = "【正常 - 成功潛入】"
        elif response.status_code == 403:
            status = "【異常 - 被門衛發現(403)】"
        else:
            status = f"【異常 - 狀態碼：{response.status_code}】"
            
    except Exception as e:
        status = f"【偵查失敗：連線超時或被攔截】"
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report = f"報告主公：分身執行偵查。\n狀態：{status}\n--- 數位分身進化中 ---"
    print(report)

if __name__ == "__main__":
    check_target()
