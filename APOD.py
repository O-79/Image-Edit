import os
import requests

class APOD:
    with open('key.txt', 'r') as F:
        API_KEY = F.read().strip()

    APOD_URL = 'https://api.nasa.gov/planetary/apod'
    
    RESOURCES_PATH = 'output'

    @staticmethod
    def GET_APOD():
        try:
            params = {
                'api_key': APOD.API_KEY
            }
            
            RES = requests.get(APOD.APOD_URL, params=params)
            
            if RES.status_code == 200:
                DAT = RES.json()
                
                print(f"Title: {DAT['title']}")
                print(f"Date: {DAT['date']}")
                print(f"URL: {DAT['url']}")
                print()
                
                return APOD.GET_IMG(DAT['url'], DAT['title'])
            else:
                print(f"{RES.status_code}")
                print(RES.text)
        except Exception as e:
            print(f"{e}")

    @staticmethod
    def GET_IMG(URL, NAME):
        try:
            if not os.path.exists(APOD.RESOURCES_PATH):
                os.makedirs(APOD.RESOURCES_PATH)
            
            IMG_NAME = f"{NAME.upper().replace(' ', '_').replace('-', '_')}.png"
            
            if not os.path.exists(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}')):
                os.makedirs(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'))
            
            if not os.path.exists(os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), 'HUE')):
                os.makedirs(os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), 'HUE'))
            
            if not os.path.exists(os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), 'COL')):
                os.makedirs(os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), 'COL'))
            
            if not os.path.exists(os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), 'HLT')):
                os.makedirs(os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), 'HLT'))
            
            IMG_PATH = os.path.join(os.path.join(APOD.RESOURCES_PATH, f'DIR-{IMG_NAME}'), IMG_NAME)
            
            IMG_DAT = requests.get(URL).content
            with open(IMG_PATH, 'wb') as IMG_F:
                IMG_F.write(IMG_DAT)
            
            return IMG_NAME
        except Exception as e:
            print(f"{e}")