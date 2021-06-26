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

mydivs = soup.find_all("a", {"class": "anime-card-block"})

find = mydivs[31].find_all("p",{"class":""})

print(type(find))
print(type(list(find)))
print(list(find))


print(list(find)[0].string)
print(list(find)[1].string)
print(list(find)[2].string)



if "萬" in list(find)[2].string:
   ans = list(find)[2].string.replace("萬","")
   ans2 = int(float(ans))*10000
   x = [1,2] 
   y = [int(ans2),3000000]
   test = [2700000,2900000]
   plt.title('Anime view on ani.gamer.com.tw', fontsize=14)
   plt.xlabel('date', fontsize=14)
   plt.ylabel('view', fontsize=14)
   plt.plot(x , test , label = "test")
   plt.plot(x,y , label = list(find)[1].string)
   plt.grid(True)
   plt.legend()
   plt.show()

