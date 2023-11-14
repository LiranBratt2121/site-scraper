import urllib.request 
import os

def grab_img_url(content):
    try:
        return content.attrs['src']  
    except:
        print('No Image in the page.\nSkipped Adding a photo')
        
def download_img(url: str, name: str) -> None:
    try:
        os.mkdir('img')
        print('Created IMG directory')
    except:
        print('Got DIR')

    urllib.request.urlretrieve(url, f'img/{name}.jpg')
    
    print('Image Downloaded')
            
def grab_text():
    pass
