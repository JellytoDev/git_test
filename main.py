from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

driver = webdriver.Chrome(executable_path="chromedriver.exe")

def tdd_test():
    driver.get("https://www.naver.com")

    # driver로 특정 페이지를 크롤링한다.
    driver.get('https://auto.naver.com/bike/mainList.nhn')

    print("+" * 100)
    print(driver.title)  # 크롤링한 페이지의 title 정보
    print(driver.current_url)  # 현재 크롤링된 페이지의 url
    print("바이크 브랜드 크롤링")
    print("-" * 100)

    while (True):
        pass

def tdd_connect_wiz():
    driver.get("http://192.168.6.10:3000")

    while (True):
        pass

def tdd_github_test1():
    driver.maximize_window()

    # "Google"에 접속한다
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

    # 페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
    assert "Google" in driver.title
    # assert "Naver" in driver.title

    # 검색 입력 부분에 커서를 올리고
    # 검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
    elem = driver.find_element(By.NAME,"q")
    elem.send_keys("키워드")
    elem.submit()

    prev_height = driver.execute_script("return document.body.scrollHeight")
    # 웹페이지 맨 아래까지 무한 스크롤
    while True:
        # 스크롤을 화면 가장 아래로 내린다
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        # 페이지 로딩 대기
        time.sleep(2)

        # 현재 문서 높이를 가져와서 저장
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if (curr_height == prev_height):
            try:
                driver.find_element(By.CSS_SELECTOR,".mye4qd".click())
            except:
                break
        prev_height = curr_height

    images = driver.find_element(By.CSS_SELECTOR,".rg_i.Q4LuWd")
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(2)
            # imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
            imgUrl = driver.find_element(By.XPATH,
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
            count = count + 1
        except:
            pass

    driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tdd_github_test1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
