import os
import shutil
import glob
from APOD import APOD
from Edit import Edit

if __name__ == "__main__":
    IMG_NAME = ''
    DEBUG_PATH = 'output'
    _DBG_ = input("Provide an image? (N -> requires NASA APOD API key in root dir under 'key.txt'!) (Y / N): ")
    if _DBG_.lower() == 'y':
        IMG_NAME_LST = []
        for EXT in ['jpg', 'jpeg', 'png']:
            IMG_NAME_LST.extend(glob.glob(f'*.{EXT}'))
        if len(IMG_NAME_LST) == 0:
            print("No images found")
            exit()
        elif len(IMG_NAME_LST) == 1:
            IMG_NAME = IMG_NAME_LIST[0]
            print(f"Selected {IMG_NAME}")
        else:
            print(f"Which image?")
            for IMG_NAME in IMG_NAME_LST:
                if IMG_NAME == IMG_NAME_LST[-1]:
                    print(f"└── {IMG_NAME}")
                else:
                    print(f"├── {IMG_NAME}")
            IMG_NAME_IDX = int(input(f"(1 - {len(IMG_NAME_LST)}): "))
            IMG_NAME = IMG_NAME_LST[max(1, min(len(IMG_NAME_LST), IMG_NAME_IDX)) - 1]
            print(f"Selected {IMG_NAME}")
        print()
        
        if not os.path.exists(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}')):
                os.makedirs(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'))
        
        if not os.path.exists(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), 'HUE')):
            os.makedirs(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), 'HUE'))
        
        if not os.path.exists(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), 'COL')):
            os.makedirs(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), 'COL'))
        
        if not os.path.exists(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), 'HLT')):
            os.makedirs(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), 'HLT'))
        
        shutil.copy(IMG_NAME, os.path.join(os.path.join(os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}'), IMG_NAME)))
    else:
        IMG_NAME = APOD.GET_APOD()
    
    _HUE_ = 'y'#input("Hue specturm? (Y / N): ")
    if _HUE_.lower() == 'y':
        for _i_ in range (1, 6):
            Edit.HUE_IMG(IMG_NAME, _i_ * 30)
    
    _COL_ = 'y'#input("Toggled color channels? (Y / N): ")
    if _COL_.lower() == 'y':
        Edit.INV_IMG(IMG_NAME)
        Edit.BNW_IMG(IMG_NAME)
        Edit.RED_IMG(IMG_NAME)
        Edit.GRE_IMG(IMG_NAME)
        Edit.BLU_IMG(IMG_NAME)
        Edit.CYA_IMG(IMG_NAME)
        Edit.PUR_IMG(IMG_NAME)
        Edit.YEL_IMG(IMG_NAME)

    _HLT_ = 'y'#input("Highlight color channels? (Y / N): ")
    if _HLT_.lower() == 'y':
        Edit.HLT_RED_IMG(IMG_NAME)
        Edit.HLT_GRE_IMG(IMG_NAME)
        Edit.HLT_BLU_IMG(IMG_NAME)
        Edit.HLT_CYA_IMG(IMG_NAME)
        Edit.HLT_PUR_IMG(IMG_NAME)
        Edit.HLT_YEL_IMG(IMG_NAME)
        
        _BAL_ = 'y'#input("Calculate color balance? (Y / N): ")
        BAL = True if _BAL_.lower() == 'y' else False
        Edit.HLT_ALL_IMG(IMG_NAME, BAL)

    print(f"See output/DIR-{IMG_NAME}/")