import requests
from bs4 import BeautifulSoup
from datetime import datetime

def grab_job_data():
    # 搜尋「QA」關鍵字的 104 網址
    search_url = "https://www.104.com.tw/jobs/search/?keyword=QA&mode=s&jobsource=2018indexpoc"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.104.com.tw/"
    }
    
    try:
        response = requests.get(search_url, headers=headers, timeout=15)
        if response.status_code == 200:
            # 使用 BeautifulSoup 解析 HTML 結構
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 嘗試抓取第一個職缺標題與公司名稱 (根據 104 目前的標籤特徵)
            # 註：104 網頁結構經常變動，這裡抓取特定的 class 屬性
            # info-job__text jb-link jb-link-blue jb-link-blue--visited h2
            first_job = soup.find('a', class_='jb-link')
            first_company = soup.find('ul', class_='b-list-inline b-clearfix').find('a') if soup.find('ul', class_='b-list-inline b-clearfix') else None
            
            job_name = first_job.text.strip() if first_job else "找不到職缺名稱"
            company_name = first_company.text.strip() if first_company else "找不到公司名稱"
            
            status = f"【成功奪取】\n職缺：{job_name}\n公司：{company_name}"
        else:
            status = f"【潛入失敗 - 狀態碼：{response.status_code}】"
            
    except Exception as e:
        status = f"【技術崩潰：{str(e)}】"
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"報告主公：分身於 {current_time} 完成偵蒐。")
    print(status)

if __name__ == "__main__":
    grab_job_data()
