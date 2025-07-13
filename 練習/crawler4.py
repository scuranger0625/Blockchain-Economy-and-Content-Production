from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 設定 Chrome 瀏覽器選項（無痕模式、無頭模式）
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")

# 啟動 Chrome 瀏覽器
driver = webdriver.Chrome(options=options)

# 設定初始頁面（第一頁）
base_url = "https://bitcointalk.org/index.php?board=161."
page_num = 0  # 代表第一頁 (161.0)

# 儲存爬取到的所有資料
data = []

# 自動翻頁函式，依照 URL 規則進行換頁
def go_next_page():
    global page_num
    page_num += 40  # 每次增加 40，對應 Bitcointalk 分頁規則
    next_page_url = f"{base_url}{page_num}"
    
    # 限制最大頁數，防止進入無效頁面（Bitcointalk 上目前約有 448 頁）
    if page_num > 448 * 40:
        return False
    
    driver.get(next_page_url)
    return True

# **主爬取迴圈**：爬取每一頁，直到沒有下一頁
while True:
    # 等待頁面載入
    time.sleep(3)

    # 取得當前頁面的所有貼文列（排除標題列）
    rows = driver.find_elements(By.XPATH, "//table[@class='bordercolor']//tr[position()>1]")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        if len(cols) < 7:
            continue

        try:
            # 提取主題標題與連結
            subject_element = cols[2].find_element(By.TAG_NAME, 'a')
            subject = subject_element.text
            link = subject_element.get_attribute('href')

            # 提取其他欄位
            author = cols[3].text
            replies = cols[4].text
            views = cols[5].text
            last_post_info = cols[6].text

            # 儲存到資料列表
            data.append({
                '主題': subject,
                '連結': link,
                '發文者': author,
                '回覆數': replies,
                '瀏覽數': views,
                '最後發文資訊': last_post_info
            })
        except Exception as e:
            print("擷取資料時發生錯誤:", e)

    # 嘗試進入下一頁，如果沒有下一頁則跳出迴圈
    if not go_next_page():
        print("✅ 已到達最後一頁，停止爬取")
        break

# 關閉瀏覽器
driver.quit()

# 存成 CSV 檔案
pd.DataFrame(data).to_csv('bitcointalk_altcoin_market.csv', encoding='utf-8-sig', index=False)

print("✅ 全部分頁爬取完成，資料已成功儲存為 bitcointalk_altcoin_market.csv")
