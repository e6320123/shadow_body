import socket
import requests

def network_test():
    targets = ["google.com", "notify-api.line.me", "1.1.1.1"]
    print("🛰️ 啟動全網偵察...")
    
    for target in targets:
        try:
            ip = socket.gethostbyname(target)
            print(f"✅ {target} 解析成功：{ip}")
        except Exception as e:
            print(f"❌ {target} 解析失敗：{e}")

    try:
        r = requests.get("https://www.google.com", timeout=5)
        print(f"🌐 Google 連線測試：{r.status_code}")
    except Exception as e:
        print(f"🚫 外部請求失敗：{e}")

if __name__ == "__main__":
    network_test()