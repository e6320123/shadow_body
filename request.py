import requests
from datetime import datetime

def grab_job_api():
    # 這是 104 搜尋 API 的真實路徑 (QA 關鍵字)
    api_url = "https://www.104.com.tw/jobs/search/list?ro=0&kw=QA&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page=1&mode=s&jobsource=2018indexpoc"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.104.com.tw/jobs/search/"
    }
    
    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        data = response.json() # API 直接回傳 JSON 格式，不需要 BeautifulSoup
        
        # 嘗試從 JSON 數據中提取第一筆
        job_list = data.get('data', {}).get('list', [])
        
        if job_list:
            first_job = job_list[0]
            job_name = first_job.get('jobName', '未知職缺')
            company_name = first_job.get('custName', '未知公司')
            salary = first_job.get('salaryDesc', '薪資不詳')
            
            status = f"【成功奪取・數據核心】\n職缺：{job_name}\n公司：{company_name}\n薪資：{salary}"
        else:
            status = "【異常：API 回傳空列表，可能關鍵字無結果】"
            
    except Exception as e:
        status = f"【技術崩潰：解析 JSON 失敗 - {str(e)}】"
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"報告主公：分身於 {current_time} 完成偵蒐。")
    print(status)

if __name__ == "__main__":
    grab_job_api()
