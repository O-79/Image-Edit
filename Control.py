from APOD import APOD
from EDIT import EDIT

if __name__ == "__main__":
    IMG_NAME = APOD.GET_APOD()
    
    _HUE_ = input("Hue specturm? (Y / N): ")
    if _HUE_.lower() == 'y':
        for _i_ in range (1, 6):
            EDIT.HUE_IMG(IMG_NAME, _i_ * 30)
    
    _COL_ = input("Toggled color channels? (Y / N): ")
    if _COL_.lower() == 'y':
        EDIT.BLU_IMG(IMG_NAME)
        EDIT.GRE_IMG(IMG_NAME)
        EDIT.RED_IMG(IMG_NAME)
        EDIT.CYA_IMG(IMG_NAME)
        EDIT.YEL_IMG(IMG_NAME)
        EDIT.PUR_IMG(IMG_NAME)