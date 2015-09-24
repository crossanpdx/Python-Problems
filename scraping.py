from bs4 import BeautifulSoup
import urllib.request
url="http://www.dsw.com/Kids-Shoes-Girls-Flats/_/N-lzvi?activeCategory=102265"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
dsw=soup.find_all('a',class_="primaryNavLink")
for shoes in dsw:
    print(shoes['href']+","+shoes.string)
