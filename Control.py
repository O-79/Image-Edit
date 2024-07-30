import os
import shutil
from APOD import APOD
from Edit import Edit

if __name__ == "__main__":
    IMG_NAME = 'TEST_IMAGE_1.png'
    DEBUG_PATH = 'output'
    _DBG_ = input("Debug? (Y / N): ")
    if _DBG_.lower() == 'y':
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
    
    _HUE_ = input("Hue specturm? (Y / N): ")
    if _HUE_.lower() == 'y':
        for _i_ in range (1, 6):
            Edit.HUE_IMG(IMG_NAME, _i_ * 30)
    
    _COL_ = input("Toggled color channels? (Y / N): ")
    if _COL_.lower() == 'y':
        Edit.RED_IMG(IMG_NAME)
        Edit.GRE_IMG(IMG_NAME)
        Edit.BLU_IMG(IMG_NAME)
        Edit.CYA_IMG(IMG_NAME)
        Edit.PUR_IMG(IMG_NAME)
        Edit.YEL_IMG(IMG_NAME)

    _HLT_ = input("Highlight color channels? (Y / N): ")
    if _HLT_.lower() == 'y':
        Edit.HLT_RED_IMG(IMG_NAME)
        Edit.HLT_GRE_IMG(IMG_NAME)
        Edit.HLT_BLU_IMG(IMG_NAME)
        Edit.HLT_CYA_IMG(IMG_NAME)
        Edit.HLT_PUR_IMG(IMG_NAME)
        Edit.HLT_YEL_IMG(IMG_NAME)
        Edit.HLT_ALL_IMG(IMG_NAME)

        _BAL_ = input("Calculate color balance? (Y / N): ")
        # if _BAL_.lower() == 'y':
        

# hlt cya(),pur,yel)
# - check abs(g-b) > abs(b-r) & abs(r-g)
# - override existing r, g, b hlt pixels

# hlt all
# - check r = g = b

# inv all
# - [255 - r, 255 - g, 255 - b]

# bal
# - txt: lower better, find ranges for good/okay/poor: std dev of # of r, y, g, c, b, p (not n/a) pixels after hlt
# - txt: % each color (including %n/a)