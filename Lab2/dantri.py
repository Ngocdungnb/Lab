from urllib.request import urlopen
from bs4 import BeautifulSoup

#1 connect to the page
url = "https://dantri.com.vn/"
conn = urlopen(url)

#2 download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")

#3 find ROI regoin 
soup = BeautifulSoup(page_content, "html.parser")
#print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew") #hred = "" , id =""
#print (ul.prettify())
#4 extract data
li_list = ul.find_all("li")
new_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    title = a.string
    link = url + a["href"]
    news = {
        "title": title,
        "link": link,
    }
    new_list.append(news)
    
print(new_list)
#5 save date
# with open ("dantri.html", "wb") as f:
#     f.write(raw_data)