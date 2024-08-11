import os
import shutil
import glob
from APOD import APOD
from OLD_Edit import OLD_Edit

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
        
        IMG_PATH = os.path.join(DEBUG_PATH, f'DIR-{IMG_NAME}')
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
        
        shutil.copy(IMG_NAME, os.path.join(IMG_PATH, IMG_NAME))
    else:
        DEBUG_PATH = APOD.OUTPUT_PATH
        IMG_NAME = APOD.GET_APOD()
    
    ################################################################
    
    try:
        _SIZ_ = int(input("Pixelation size? (e.g. 16 = 16px squares): "))
        Edit.DST_PXL_IMG(IMG_NAME, _SIZ_)
    except ValueError:
        print("[LOG] PIXELLATION -> IGNORE -> Chosen pixelation size is not an integer!")
    try:
        _SIZ_ = int(input("Horizontal and vertical stretch? (e.g. 64 = 64px stretch): "))
        Edit.DST_HOR_IMG(IMG_NAME, _SIZ_)
        Edit.DST_VER_IMG(IMG_NAME, _SIZ_)
    except ValueError:
        print("[LOG] HORIZONTAL / VERTICAL STRETCH -> IGNORE -> Chosen pixelation / stretch size is not an integer!")
    Edit.DST_MIX_IMG(IMG_NAME)
    
    for MAG in range(1, 6):
        Edit.HUE_IMG(IMG_NAME, MAG * 30)
    
    Edit.COL_DUL_IMG(IMG_NAME)
    Edit.COL_SAT_IMG(IMG_NAME)
    Edit.COL_BNW_IMG(IMG_NAME)
    Edit.COL_INV_IMG(IMG_NAME)
    Edit.COL_BLU_IMG(IMG_NAME)
    Edit.COL_GRE_IMG(IMG_NAME)
    Edit.COL_RED_IMG(IMG_NAME)
    Edit.COL_CYA_IMG(IMG_NAME)
    Edit.COL_PUR_IMG(IMG_NAME)
    Edit.COL_YEL_IMG(IMG_NAME)

    Edit.HLT_RED_IMG(IMG_NAME)
    Edit.HLT_GRE_IMG(IMG_NAME)
    Edit.HLT_BLU_IMG(IMG_NAME)
    Edit.HLT_CYA_IMG(IMG_NAME)
    Edit.HLT_PUR_IMG(IMG_NAME)
    Edit.HLT_YEL_IMG(IMG_NAME)
    
    Edit.HLT_ALL_IMG(IMG_NAME, True)

    print(f"\nSee {DEBUG_PATH}/DIR-{IMG_NAME}/")