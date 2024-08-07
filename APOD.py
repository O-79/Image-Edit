import os
import requests

class APOD:
    API_KEY = os.getenv("NASA_API_KEY")
    if API_KEY is None:
        with open('key.txt', 'r') as F:
            API_KEY = F.read().strip()

    APOD_URL = 'https://api.nasa.gov/planetary/apod'
    
    OUTPUT_PATH = 'output'

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
                exit()
        except Exception as e:
            print(f"{e}")

    @staticmethod
    def GET_IMG(URL, NAME):
        try:
            if not os.path.exists(DEBUG_PATH):
                os.makedirs(DEBUG_PATH)
            
            IMG_NAME = f"{NAME.upper().replace(' ', '_').replace('-', '_').replace('\\', '_').replace('/', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('\"', '_').replace('<', '_').replace('>', '_').replace('|', '_')}.png"
            
            IMG_PATH = os.path.join(APOD.OUTPUT_PATH, f'DIR-{IMG_NAME}')
            if not os.path.exists(IMG_PATH):
                os.makedirs(IMG_PATH)
            
            if not os.path.exists(os.path.join(IMG_PATH, 'HUE')):
                os.makedirs(os.path.join(IMG_PATH, 'HUE'))
            
            if not os.path.exists(os.path.join(IMG_PATH, 'COL')):
                os.makedirs(os.path.join(IMG_PATH, 'COL'))
            
            if not os.path.exists(os.path.join(IMG_PATH, 'HLT')):
                os.makedirs(os.path.join(IMG_PATH, 'HLT'))
                
            if not os.path.exists(os.path.join(IMG_PATH, 'DST')):
                os.makedirs(os.path.join(IMG_PATH, 'DST'))
            
            IMG_DAT = requests.get(URL).content
            with open(IMG_PATH, 'wb') as IMG_F:
                IMG_F.write(IMG_DAT)
            
            return IMG_NAME
        except Exception as e:
            print(f"{e}")