import random

import requests
from bs4 import BeautifulSoup


def get_img():
    url = "https://www.google.com/search?q=%D0%BA%D0%BE%D1%88%D0%BA%D0%BE%D0%B4%D0%B5%D0%B2%D0%BE%D1%87%D0%BA%D0%B8" \
          "&client=firefox-b-d&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiC0vH609DwAhVFrosKHbEBB4IQ_AUoAXoECAEQAw&biw=1920" \
          "&bih=906 "
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    images = soup.find_all('img')

    return random.choice(images)['src']
