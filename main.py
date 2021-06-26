import matplotlib.pyplot as plt
import requests
import bs4
import os

def draw(data):
    plt.legend()
    plt.show()


def get_data():
    print("ji")

if os.path.exists("text.html"):
    os.remove("text.html")

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    
r = requests.get("https://ani.gamer.com.tw" , "html.parser" , headers= header)

soup = bs4.BeautifulSoup(r.text , 'lxml')

with open("text.html", "w", encoding="utf-8") as f:
    f.write(str(soup.prettify()))
