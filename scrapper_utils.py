def grab_pic(content):
    try:
        return content.attrs['src']  
    except:
        print('No Image in the page.\nSkipped Adding a photo')
        
        
def grab_text():
    pass