import os
import shutil
import glob
from APOD import APOD
from Edit import Edit

class Manager:
    def __init__(self, HUE_SIZ, PXL_SIZ, BLR_SIZ):
        self.HUE_SIZ = HUE_SIZ
        self.PXL_SIZ = PXL_SIZ
        self.BLR_SIZ = BLR_SIZ

    def EXP(self, OLD_PATH):
        PATH = 'output'#os.path.join(os.path.normpath(os.path.expanduser('~/Desktop')), 'output-Image-Edit')
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        
        IMG_PATH = os.path.join(PATH, f'DIR-{os.path.basename(OLD_PATH)}')
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
        
        shutil.copy(OLD_PATH, os.path.join(IMG_PATH, os.path.basename(OLD_PATH)))
        
        ################################################################
        
        Edit.DST_PXL_IMG(IMG_PATH, OLD_PATH, self.PXL_SIZ)
        Edit.DST_HOR_IMG(IMG_PATH, OLD_PATH, self.BLR_SIZ)
        Edit.DST_VER_IMG(IMG_PATH, OLD_PATH, self.BLR_SIZ)
        Edit.DST_MIX_IMG(IMG_PATH, OLD_PATH)
        
        for MAG in range(1, self.HUE_SIZ):
            Edit.HUE_IMG(IMG_PATH, OLD_PATH, MAG * (180 / self.HUE_SIZ))
        
        Edit.COL_DUL_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_SAT_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_BNW_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_INV_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_BLU_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_GRE_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_RED_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_CYA_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_PUR_IMG(IMG_PATH, OLD_PATH)
        Edit.COL_YEL_IMG(IMG_PATH, OLD_PATH)

        Edit.HLT_RED_IMG(IMG_PATH, OLD_PATH)
        Edit.HLT_GRE_IMG(IMG_PATH, OLD_PATH)
        Edit.HLT_BLU_IMG(IMG_PATH, OLD_PATH)
        Edit.HLT_CYA_IMG(IMG_PATH, OLD_PATH)
        Edit.HLT_PUR_IMG(IMG_PATH, OLD_PATH)
        Edit.HLT_YEL_IMG(IMG_PATH, OLD_PATH)
        
        Edit.HLT_ALL_IMG(IMG_PATH, OLD_PATH, True)