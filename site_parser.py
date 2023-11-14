from bs4 import BeautifulSoup
from scrapper_utils import grab_img_url, download_img, grab_text, save_to_file


def main():
    with open('webpage.html', 'r', encoding="utf8") as file: 
        soup = BeautifulSoup(file.read(), 'html.parser')

        img = soup.find('img', class_='img_practice')
        
        img_url = grab_img_url(img)
        site_text = grab_text(soup)

        download_img(img_url, input('Enter Image name: '))
        save_to_file(site_text, input('Enter File name: '))
        
        print("NO IMAGE" if not img_url else img_url)

if __name__ == "__main__":
    main()
