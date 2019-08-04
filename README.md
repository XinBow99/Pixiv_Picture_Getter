# Replace cookie with Your Login Cookie
Main.py file
	# your cookie
    "cookie": "enter your cookies here",
    # your cookie
1. Open your browser
2. F12 to open Developer Tools on browser
3. Select NetWork
![](https://i.imgur.com/no6FMG3.png)
4. Sign in Pixiv
5. Clear Network datas and refresh page
6. Catch www.pixiv.net and copy Cookie value
![](https://i.imgur.com/bYbgr8F.png)
7. Rplace!
# Replace Path with Your Save Path
    def saveImg(data, i, x):
        # change your img save path
        SavePath = 'change your save path/' + str(x) + '_' + str(i) + '.jpg'
        open(SavePath, 'wb').write(data)
- For example change "change your save path" for "C:/Users/username/OneDrive/桌面/img"
# Search total pages
    def getRanking(login):
        login.get("https://www.pixiv.net/rpc/index.php?mode=message_thread_unread_count")
        Url_collect = []
        Pages = 90#enter what u wnat to search total pages
# Search Word
    for p in range(1, Pages + 1):
      ranking_url = login.get("https://www.pixiv.net/search.php?word=**here**&order=date_d&p=" + str(p))
	  #replace **here** with what you want 
	  #Example 中野三玖
	  #if u want 2 get Ranking Page,Please replace with https://www.pixiv.net/ranking.php?mode=daily&p=" + str(p))
	  #daily is ranking classification
# FINAL
#### py main.py
