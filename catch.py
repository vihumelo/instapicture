import requests
from bs4 import BeautifulSoup
import shutil

def get_profile_pic(profile):

    html = requests.get(f'http://www.instagram.com/{profile}')
    bs = BeautifulSoup(html.text, 'html.parser')
    tag_finder = bs.find_all('script')

    scripts_tags = []
    for n in range(len(tag_finder)):
        scripts = [i.split('"') for i in tag_finder[n]]
        scripts_tags.append(scripts)

    for i in scripts_tags:
        for x in i:
            if 'profile_pic_url' in x:
                index = x.index('profile_pic_url')
                url = x[index+2] 

    url = url.replace('\\', "") # profile instagram picture url
    data = requests.get(url, stream=True)

    with open(f'{profile}_picture.png','wb') as f:
        shutil.copyfileobj(data.raw, f)
    print('Profile image sucessfully downloaded and saved!')


if __name__ == '__main__':

    instagram_profile = 'neymarjr'
    get_profile_pic(instagram_profile)
