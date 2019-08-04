import threading
import time
import datetime
import requests
import re
# 停止SSL報錯
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def simpleLogin(login):
    login.get("https://www.pixiv.net/", verify=False)


def getRanking(login):
    login.get("https://www.pixiv.net/rpc/index.php?mode=message_thread_unread_count")
    Url_collect = []
    Pages = 90#enter what u wnat to search total pages
    for p in range(1, Pages + 1):
        ranking_url = login.get("https://www.pixiv.net/search.php?word=中野三玖&order=date_d&p=" + str(p))
        Urls = re.findall('(?<=&quot;illustId&quot;:&quot;)(.*?)(?=&quot;)', ranking_url.text)
        Url_collect = Url_collect + Urls
    return Url_collect


def enterBoard(login, id):
    img_src = login.get("https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + id + "",
                        verify=False)
    match_img = re.search('(?<=\"regular\":\")(.*?)(?=\",)', img_src.text)[0]
    return match_img.replace('\\', '')


def getImg(login, img_id, img_download, i, x):
    login.headers.update({
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.142 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'referer': 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + img_id
    })
    img = login.get(img_download,
                    verify=False
                    )
    saveImg(img.content, i, x)


def saveImg(data, i, x):
    # change your img save path
    SavePath = 'change your save path/' + str(x) + '_' + str(i) + '.jpg'
    open(SavePath, 'wb').write(data)


def thrGO(bang, i):
    print(i)
    for index, url in enumerate(bang):
        getImg(base, url, enterBoard(base, url), index+1, i)


if __name__ == '__main__':
    base = requests.session()
    base.headers.update(
        {
            # your cookie
            "cookie": "enter your cookies here",
            # your cookie
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/75.0.3770.142 Safari/537.36 ",
            "accept-encoding": "gzip, deflate, br",
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3 '
        }
    )
    start = datetime.datetime.now()
    simpleLogin(base)
    urls = getRanking(base)
    print("取得", len(urls), "張圖片")
    urls_half = int(len(urls)/2)
    New_Urls = urls[0:urls_half]
    print("開始下載")
    thread1 = threading.Thread(target=thrGO, args=(New_Urls, 1,))
    print(len(New_Urls))

    New_Urls = urls[urls_half:]
    thread2 = threading.Thread(target=thrGO, args=(New_Urls, 2,))
    print(len(New_Urls))

    thread1.start()
    print("執行緒1啟動")
    thread2.start()
    print("執行緒2啟動")
    thread1.join()
    thread2.join()
    Etime = datetime.datetime.now()
    print(start, Etime)
