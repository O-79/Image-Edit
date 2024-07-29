from APOD import APOD
from Edit import Edit

if __name__ == "__main__":
    IMG_NAME = APOD.GET_APOD()
    
    _HUE_ = input("Hue specturm? (Y / N): ")
    if _HUE_.lower() == 'y':
        for _i_ in range (1, 6):
            Edit.HUE_IMG(IMG_NAME, _i_ * 30)
    
    _COL_ = input("Toggled color channels? (Y / N): ")
    if _COL_.lower() == 'y':
        Edit.BLU_IMG(IMG_NAME)
        Edit.GRE_IMG(IMG_NAME)
        Edit.RED_IMG(IMG_NAME)
        Edit.CYA_IMG(IMG_NAME)
        Edit.YEL_IMG(IMG_NAME)
        Edit.PUR_IMG(IMG_NAME)