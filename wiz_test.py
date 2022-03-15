from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects import PageObject, PageElement
import time
import urllib.request
import redgreenunittest
from selenium.webdriver.common.keys import Keys
import json
from unittest import TestCase
import unittest



# test_driver = webdriver.Chrome(executable_path="chromedriver.exe")
public_url = "http://192.168.6.10:3000"

class MyTests(TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1 + 2, 3)

class PythonOrgSearch(TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome(executable_path="chromedriver.exe")
        # self.driver.implicitly_wait(30)
    def test_connect_check(self):
        urls = ["/test/front_ref","/test/angularjs","/test/fdsa","/test/model","/test/db",
                "/test/sql","/test/fdsa"]
        error_urls = []

        for url in urls:
            self.driver.get(public_url + url)
            if self.driver.page_source.__contains__("404"):
                error_urls.append(url)
                print("\nerror url : ",url,sep="\n")

    def test_connect_home(self):
        self.driver.get(public_url)

    def test_reference(self):
        self.driver.get("http://www.google.com")

        # 검색창 선택
        search_box = self.driver.find_element(By.NAME,"q")

        # 검색어 입력
        search_box.send_keys('greeksharifa.github.io')

        # 해당 페이지로 초기화
        search_box.send_keys(Keys.RETURN)

        # element 찾고 해당 글 클릭
        posting = self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div/a/h3')
        posting.click()

        # 뒤로가기 함수
        self.driver.back()

        # 화면 이동(맨밑으로 내려가기)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # 브라우저 최소화 / 최대화
        self.driver.minimize_window()
        self.driver.maximize_window()

        # 스크린샷 저장
        self.driver.save_screenshot('screenshot.png')


    def test_small1(self):
        self.driver.implicitly_wait(15)  # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

        # 페이지 가져오기(이동)
        self.driver.get('https://www.google.co.kr')
        self.driver.get('https://www.wikidocs.net')
        self.driver.get('https://www.naver.com')

        # 이전 창으로 이동 2번하기
        self.driver.back()
        self.driver.back()

        # 다음 창으로 2번 이동하기
        self.driver.forward()
        self.driver.forward()

    def test_naver_search(self):
        keyword = "강아지"

        # 웹
        ## 네이버 이미지 접속
        print('[ 접속중... ]')
        self.driver.implicitly_wait(15)
        self.driver.minimize_window() # 최대화

        url = 'https://search.naver.com/search.naver?where=image&query={}'.format(keyword)
        self.driver.get(url)

        ## 페이지 아래로 내리기
        body = self.driver.find_element(By.CSS_SELECTOR,'body')

        ##스크롤 다운 - 5회
        for i in range(5):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # 활성화 기다려주기

        # 이미지 요소 모두 찾기
        imgs = self.driver.find_elements(By.CSS_SELECTOR,'img._img')
        # print(len(imgs))

        ## 이미지 링크 추출
        links = []
        for img in imgs:
            link = img.get_attribute('src')
            if 'http' in link:  # 반드시 이미지 주소에 http가 들어간 것만 추출
                links.append(link)

        print('[ 정보 수집 완료 ] ')

        ## 폴더 생성
        print('[ 폴더 생성 중 ] ')
        import os
        if not os.path.isdir('./{}'.format(keyword)):  # 만들려고 하는 디렉토리 있는지 확인
            os.mkdir('./{}'.format(keyword))  # 없으면 생성

        ## 다운로드
        print('[ 다운로드 중 ] ')
        from urllib.request import urlretrieve
        from tqdm import tqdm

        for index, link in tqdm(enumerate(links), total=len(links)):
            # 확장자가 무엇인지 추출
            start = link.rfind('.')
            end = link.rfind('&')

            file_type = link[start:end]  # 확장자 : .jpg
            filename = './{0}/{0}{1:03d}{2}'.format(keyword, index, file_type)  # 파일명 : 아이스크림001.jpg
            urlretrieve(link, filename)

        print('[ 다운로드 완료 ] ')

        # 압축 - 메일
        import zipfile
        zip_file = zipfile.ZipFile('./{}.zip'.format(keyword), 'w')

        # print(os.listdir('./{}'.format(keyword)))
        for image in os.listdir('./{}'.format(keyword)):
            print(image, "압축파일에 추가중")
            zip_file.write('./{}/{}'.format(keyword, image), compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()
        print("압축완료")

    def tearDown(self):
        self.driver.close()



# 메인문
if __name__ == "__main__":
    unittest.main()