import threading
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options

# ===== 공통 함수 =====
def get_random_comment():
    comments = [
        "댓노 하기 힘들다",
        "오늘도 자기 전까지 달려보자!",
        "댓노 하는 분들 다들 화이팅",
        "슬슬 지치는구만~"
    ]
    return random.choice(comments)

def wait_random_delay(speed_level):
    base = max(1, 11 - speed_level)
    time.sleep(random.uniform(base, base + 2))


# ===== 사이트별 작업 함수 =====

def oncapan_worker(start_page, end_page, speed, window_pos=0):
    driver = create_browser(window_pos)
    driver.get("https://oncapan.com/bbs/free")
    input("[온카판] 로그인 후 Enter...")

    next_lottery_time = datetime.now() + timedelta(hours=3)

    for page in range(start_page, end_page - 1, -1):
        try:
            print(f"[온카판] 작업중... 페이지 {page}")
            # 여기에 온카판 전용 처리 로직 작성
            # 예: 게시글 클릭, 댓글 확인, 작성

            # 예시:
            page_url = f"https://oncapan.com/bbs/free?page={page}"
            driver.get(page_url)

            # 게시글 클릭, 댓글 찾기, 댓글 쓰기 등 직접 구현 필요

            wait_random_delay(speed)

            if datetime.now() >= next_lottery_time:
                driver.get("https://oncapan.com/lottery/l_list.php")
                try:
                    btn = driver.find_element(By.XPATH, "//button[contains(text(), '복권발급')]")
                    btn.click()
                    print("[온카판] 복권 발급 완료")
                except:
                    print("[온카판] 복권 버튼 없음")
                next_lottery_time = datetime.now() + timedelta(hours=3)

        except Exception as e:
            print(f"[온카판] 에러: {e}")

    driver.quit()


def onca112_worker(start_page, end_page, speed, window_pos=0):
    driver = create_browser(window_pos)
    driver.get("https://onca112.com/Category/free")
    input("[온카112] 로그인 후 Enter...")

    for page in range(start_page, end_page - 1, -1):
        try:
            print(f"[온카112] 작업중... 페이지 {page}")
            # 온카112 전용 처리 로직 작성
            # driver.get(f"https://onca112.com/Category/free?page={page}")
            # 게시글 클릭, 댓글 찾기, 작성 등 구현

            wait_random_delay(speed)
        except Exception as e:
            print(f"[온카112] 에러: {e}")

    driver.quit()


def allin42_worker(start_page, end_page, speed, window_pos=0):
    driver = create_browser(window_pos)
    driver.get("https://www.allin42.com/free")
    input("[올인42] 로그인 후 Enter...")

    for page in range(start_page, end_page - 1, -1):
        try:
            print(f"[올인42] 작업중... 페이지 {page}")
            # 올인42 전용 처리 로직 작성
            # driver.get(f"https://www.allin42.com/free?page={page}")
            # 게시글 클릭, 댓글 찾기, 작성 등 구현

            wait_random_delay(speed)
        except Exception as e:
            print(f"[올인42] 에러: {e}")

    driver.quit()


def create_browser(position_index):
    options = Options()
    driver = webdriver.Chrome(options=options)

    # 위치 및 크기 지정
    width = 600
    height = 800
    x = position_index * width  # 왼쪽에서 오른쪽으로 정렬
    y = 0  # 필요 시 세로 정렬도 가능
    driver.set_window_size(width, height)
    driver.set_window_position(x, y)

    return driver

if __name__ == "__main__":
    start_page = int(input("댓글작성 시작페이지: "))
    end_page = int(input("댓글작성 종료페이지: "))
    speed = int(input("작업 속도 (1~10): "))

    threads = [
        # threading.Thread(target=oncapan_worker, args=(start_page, end_page, speed, 0)),
        # threading.Thread(target=onca112_worker, args=(start_page, end_page, speed, 1)),
        threading.Thread(target=allin42_worker, args=(start_page, end_page, speed, 2)),
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()
