from bs4 import BeautifulSoup
from scrapper_utils import grab_img_url, download_img
import asyncio

def main():
    with open('webpage.html', 'r', encoding="utf8") as file: 
        soup = BeautifulSoup(file.read(), 'html.parser')

        img = soup.find('img', class_='img_practice')
        
        text = [p.text[::-1] for p in soup.find_all('p')]
        
        print(text)
        
        img_url = grab_img_url(img)

        download_img(img_url, 'LIGMA')
        
        print("NO IMAGE" if not img_url else img_url)

if __name__ == "__main__":
    main()
