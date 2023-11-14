from bs4 import BeautifulSoup
from scrapper_utils import grab_pic


with open('webpage.html', 'r', encoding="utf8") as file: 
    soup = BeautifulSoup(file.read(), 'html.parser')

    content = soup.find('img', class_='img_practice')
    
    img_url = grab_pic(content)
    
    print("NO IMAGE" if not img_url else img_url)
    
