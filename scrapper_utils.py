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


def save_to_file(content, filename):
    try:
        os.mkdir('files')
        print('Created files directory')
    except:
        print('Got DIR')

    with open(f'files/{filename}', 'w', encoding="utf8") as file:
        file.write(content)
        
    print('File Saved')
        
        
def fix_hebrew(paragraphs):
    return str([p.text for p in paragraphs])    

def grab_text(content):
    return fix_hebrew(content)

