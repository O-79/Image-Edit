import cv2
import numpy as np
import random

class Edit:
    def HUE_IMG(IMG_NAME, HUE):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        IMG_HSV = cv2.cvtColor(IMG_BGR, cv2.COLOR_BGR2HSV)
        IMG_HSV[..., 0] = (IMG_HSV[..., 0] + HUE) % 180
        IMG_BGR = cv2.cvtColor(IMG_HSV, cv2.COLOR_HSV2BGR)

        HUE_PATH = f'output\\DIR-{IMG_NAME}\\HUE\\HUE_{HUE}-{IMG_NAME}'
        cv2.imwrite(HUE_PATH, IMG_BGR)

    def DST_PXL_IMG(IMG_NAME, SIZ):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR.shape
        
        if SIZ == 1:
            IMG_BGR = IMG_BGR.astype(np.uint8)
            DST_PXL_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_PXL-{IMG_NAME}'
            cv2.imwrite(DST_PXL_PATH, IMG_BGR)
            return
        if HGT < SIZ or WID < SIZ:
            print("[LOG] PIXELLATION -> IGNORE -> Chosen pixellation size is too large for selected image!")
            return
        
        for ROW in range(HGT):
            PXL = None
            for COL in range(WID):
                if COL % SIZ == 0:
                    PXL = IMG_BGR[ROW, COL].copy()
                elif PXL is not None:
                    IMG_BGR[ROW, COL] = PXL
        
        for COL in range(WID):
            PXL = None
            for ROW in range(HGT):
                if ROW % SIZ == 0:
                    PXL = IMG_BGR[ROW, COL].copy()
                elif PXL is not None:
                    IMG_BGR[ROW, COL] = PXL

        IMG_BGR = IMG_BGR.astype(np.uint8)
        DST_PXL_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_PXL-{IMG_NAME}'
        cv2.imwrite(DST_PXL_PATH, IMG_BGR)

    def DST_HOR_IMG(IMG_NAME, SIZ):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR.shape
        
        if SIZ == 1:
            IMG_BGR = IMG_BGR.astype(np.uint8)
            DST_PXL_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_PXL-{IMG_NAME}'
            cv2.imwrite(DST_PXL_PATH, IMG_BGR)
            return
        if WID < SIZ:
            print("[LOG] HORIZONTAL STRETCH -> IGNORE -> Chosen horizontal stretch size is too large for selected image!")
            return
        
        for ROW in range(HGT):
            PXL = None
            for COL in range(WID):
                if COL % SIZ == 0:
                    PXL = IMG_BGR[ROW, COL].copy()
                elif PXL is not None:
                    IMG_BGR[ROW, COL] = PXL

        IMG_BGR = IMG_BGR.astype(np.uint8)
        DST_HOR_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_HOR-{IMG_NAME}'
        cv2.imwrite(DST_HOR_PATH, IMG_BGR)

    def DST_VER_IMG(IMG_NAME, SIZ):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR.shape
        
        if SIZ == 1:
            IMG_BGR = IMG_BGR.astype(np.uint8)
            DST_PXL_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_PXL-{IMG_NAME}'
            cv2.imwrite(DST_PXL_PATH, IMG_BGR)
            return
        if HGT < SIZ:
            print("[LOG] VERTICAL STRETCH -> IGNORE -> Chosen vertical stretch size is too large for selected image!")
            return
        
        for COL in range(WID):
            PXL = None
            for ROW in range(HGT):
                if ROW % SIZ == 0:
                    PXL = IMG_BGR[ROW, COL].copy()
                elif PXL is not None:
                    IMG_BGR[ROW, COL] = PXL

        IMG_BGR = IMG_BGR.astype(np.uint8)
        DST_VER_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_VER-{IMG_NAME}'
        cv2.imwrite(DST_VER_PATH, IMG_BGR)

    def DST_MIX_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR_0 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_1 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_2 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_3 = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR_3.shape
        
        for ROW in range(HGT):
            for COL in range(WID):
                IMG_BGR_0[ROW, COL] = IMG_BGR_3[random.randint(0, HGT - 1), random.randint(0, WID - 1)]
                IMG_BGR_1[ROW, COL] = IMG_BGR_3[random.randint(0, HGT - 1), random.randint(0, WID - 1)]
                IMG_BGR_2[ROW, COL] = IMG_BGR_3[random.randint(0, HGT - 1), random.randint(0, WID - 1)]
                IMG_BGR_3[ROW, COL] = IMG_BGR_3[random.randint(0, HGT - 1), random.randint(0, WID - 1)]

        IMG_BGR_0 = IMG_BGR_0.astype(np.uint8)
        IMG_BGR_1 = IMG_BGR_1.astype(np.uint8)
        IMG_BGR_2 = IMG_BGR_2.astype(np.uint8)
        IMG_BGR_3 = IMG_BGR_3.astype(np.uint8)
        DST_MIX_0_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_MIX_0-{IMG_NAME}'
        DST_MIX_1_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_MIX_1-{IMG_NAME}'
        DST_MIX_2_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_MIX_2-{IMG_NAME}'
        DST_MIX_3_PATH = f'output\\DIR-{IMG_NAME}\\DST\\DST_MIX_3-{IMG_NAME}'
        cv2.imwrite(DST_MIX_0_PATH, IMG_BGR_0)
        cv2.imwrite(DST_MIX_1_PATH, IMG_BGR_1)
        cv2.imwrite(DST_MIX_2_PATH, IMG_BGR_2)
        cv2.imwrite(DST_MIX_3_PATH, IMG_BGR_3)

    def COL_DUL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR_0 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_1 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_2 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_3 = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR_3.shape
        
        for ROW in range(HGT):
            for COL in range(WID):
                B, G, R = IMG_BGR_3[ROW, COL]
                AVG = int((B + G + R) / 3)
                B_0 = int((B + AVG) / 2)
                B_1 = int((B_0 + AVG) / 2)
                B_2 = int((B_1 + AVG) / 2)
                B_3 = int((B_2 + AVG) / 2)
                G_0 = int((G + AVG) / 2)
                G_1 = int((G_0 + AVG) / 2)
                G_2 = int((G_1 + AVG) / 2)
                G_3 = int((G_2 + AVG) / 2)
                R_0 = int((R + AVG) / 2)
                R_1 = int((R_0 + AVG) / 2)
                R_2 = int((R_1 + AVG) / 2)
                R_3 = int((R_2 + AVG) / 2)
                IMG_BGR_0[ROW, COL] = np.array([B_0, G_0, R_0])
                IMG_BGR_1[ROW, COL] = np.array([B_1, G_1, R_1])
                IMG_BGR_2[ROW, COL] = np.array([B_2, G_2, R_2])
                IMG_BGR_3[ROW, COL] = np.array([B_3, G_3, R_3])

        IMG_BGR_0 = IMG_BGR_0.astype(np.uint8)
        IMG_BGR_1 = IMG_BGR_1.astype(np.uint8)
        IMG_BGR_2 = IMG_BGR_2.astype(np.uint8)
        IMG_BGR_3 = IMG_BGR_3.astype(np.uint8)
        COL_DUL_0_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_DUL_0-{IMG_NAME}'
        COL_DUL_1_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_DUL_1-{IMG_NAME}'
        COL_DUL_2_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_DUL_2-{IMG_NAME}'
        COL_DUL_3_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_DUL_3-{IMG_NAME}'
        cv2.imwrite(COL_DUL_0_PATH, IMG_BGR_0)
        cv2.imwrite(COL_DUL_1_PATH, IMG_BGR_1)
        cv2.imwrite(COL_DUL_2_PATH, IMG_BGR_2)
        cv2.imwrite(COL_DUL_3_PATH, IMG_BGR_3)

    def COL_SAT_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR_0 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_1 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_2 = cv2.imread(IMG_PATH).astype(np.int16)
        IMG_BGR_3 = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR_3.shape
        
        for ROW in range(HGT):
            for COL in range(WID):
                B, G, R = IMG_BGR_3[ROW, COL]
                AVG = int((B + G + R) / 3)
                B_VAL = 255 if B > AVG else 0 if B < AVG else B
                G_VAL = 255 if G > AVG else 0 if G < AVG else G
                R_VAL = 255 if R > AVG else 0 if R < AVG else R
                B_0 = int((B + B_VAL) / 2)
                B_1 = int((B_0 + B_VAL) / 2)
                B_2 = int((B_1 + B_VAL) / 2)
                B_3 = int((B_2 + B_VAL) / 2)
                G_0 = int((G + G_VAL) / 2)
                G_1 = int((G_0 + G_VAL) / 2)
                G_2 = int((G_1 + G_VAL) / 2)
                G_3 = int((G_2 + G_VAL) / 2)
                R_0 = int((R + R_VAL) / 2)
                R_1 = int((R_0 + R_VAL) / 2)
                R_2 = int((R_1 + R_VAL) / 2)
                R_3 = int((R_2 + R_VAL) / 2)
                IMG_BGR_0[ROW, COL] = np.array([B_0, G_0, R_0])
                IMG_BGR_1[ROW, COL] = np.array([B_1, G_1, R_1])
                IMG_BGR_2[ROW, COL] = np.array([B_2, G_2, R_2])
                IMG_BGR_3[ROW, COL] = np.array([B_3, G_3, R_3])

        IMG_BGR_0 = IMG_BGR_0.astype(np.uint8)
        IMG_BGR_1 = IMG_BGR_1.astype(np.uint8)
        IMG_BGR_2 = IMG_BGR_2.astype(np.uint8)
        IMG_BGR_3 = IMG_BGR_3.astype(np.uint8)
        COL_SAT_0_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_SAT_0-{IMG_NAME}'
        COL_SAT_1_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_SAT_1-{IMG_NAME}'
        COL_SAT_2_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_SAT_2-{IMG_NAME}'
        COL_SAT_3_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_SAT_3-{IMG_NAME}'
        cv2.imwrite(COL_SAT_0_PATH, IMG_BGR_0)
        cv2.imwrite(COL_SAT_1_PATH, IMG_BGR_1)
        cv2.imwrite(COL_SAT_2_PATH, IMG_BGR_2)
        cv2.imwrite(COL_SAT_3_PATH, IMG_BGR_3)

    def COL_BNW_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        HGT, WID, COL = IMG_BGR.shape
        
        for ROW in range(HGT):
            for COL in range(WID):
                B, G, R = IMG_BGR[ROW, COL]
                X = max(B, G, R)
                B = X
                G = X
                R = X
                IMG_BGR[ROW, COL] = np.array([B, G, R])

        IMG_BGR = IMG_BGR.astype(np.uint8)
        BNW_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_BNW-{IMG_NAME}'
        cv2.imwrite(BNW_PATH, IMG_BGR)

    def COL_INV_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(255 - B, 0, 255).astype(np.uint8)
        G = np.clip(255 - G, 0, 255).astype(np.uint8)
        R = np.clip(255 - R, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        IMG_BGR = IMG_BGR.astype(np.uint8)
        INV_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_INV-{IMG_NAME}'
        cv2.imwrite(INV_PATH, IMG_BGR)

    def COL_BLU_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        BLU_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_BLU-{IMG_NAME}'
        cv2.imwrite(BLU_PATH, IMG_BGR)

    def COL_GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        GRE_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_GRE-{IMG_NAME}'
        cv2.imwrite(GRE_PATH, IMG_BGR)

    def COL_RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        RED_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_RED-{IMG_NAME}'
        cv2.imwrite(RED_PATH, IMG_BGR)

    def COL_YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        YEL_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_YEL-{IMG_NAME}'
        cv2.imwrite(YEL_PATH, IMG_BGR)

    def COL_PUR_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        PUR_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_PUR-{IMG_NAME}'
        cv2.imwrite(PUR_PATH, IMG_BGR)

    def COL_CYA_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_BGR = cv2.merge([B, G, R])

        CYA_PATH = f'output\\DIR-{IMG_NAME}\\COL\\COL_CYA-{IMG_NAME}'
        cv2.imwrite(CYA_PATH, IMG_BGR)

    def HLT_BLU_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_BLU = (B > G) & (B > R)
        IMG_BGR[HLT_BLU] = [255, 0, 0]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_BLU_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_BLU-{IMG_NAME}'
        cv2.imwrite(HLT_BLU_PATH, IMG_BGR)

    def HLT_GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_GRE = (G > B) & (G > R)
        IMG_BGR[HLT_GRE] = [0, 255, 0]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_GRE_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_GRE-{IMG_NAME}'
        cv2.imwrite(HLT_GRE_PATH, IMG_BGR)

    def HLT_RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_RED = (R > B) & (R > G)
        IMG_BGR[HLT_RED] = [0, 0, 255]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_RED_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_RED-{IMG_NAME}'
        cv2.imwrite(HLT_RED_PATH, IMG_BGR)

    def HLT_YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        MJR_YEL = (G > B) & (R > B)
        DIF_G_R = np.abs(G - R)
        DIF_B_R = np.abs(B - R)
        DIF_B_G = np.abs(B - G)

        HLT_YEL = MJR_YEL & (DIF_G_R < DIF_B_G) & (DIF_G_R < DIF_B_R)
        IMG_BGR[HLT_YEL] = [0, 255, 255]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_YEL_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_YEL-{IMG_NAME}'
        cv2.imwrite(HLT_YEL_PATH, IMG_BGR)

    def HLT_PUR_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        MJR_PUR = (B > G) & (R > G)
        DIF_G_R = np.abs(G - R)
        DIF_B_R = np.abs(B - R)
        DIF_B_G = np.abs(B - G)

        HLT_PUR = MJR_PUR & (DIF_B_R < DIF_B_G) & (DIF_B_R < DIF_G_R)
        IMG_BGR[HLT_PUR] = [255, 0, 255]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_PUR_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_PUR-{IMG_NAME}'
        cv2.imwrite(HLT_PUR_PATH, IMG_BGR)

    def HLT_CYA_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        MJR_CYA = (B > R) & (G > R)
        DIF_G_R = np.abs(G - R)
        DIF_B_R = np.abs(B - R)
        DIF_B_G = np.abs(B - G)

        HLT_CYA = MJR_CYA & (DIF_B_G < DIF_G_R) & (DIF_B_G < DIF_B_R)
        IMG_BGR[HLT_CYA] = [255, 255, 0]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_CYA_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_CYA-{IMG_NAME}'
        cv2.imwrite(HLT_CYA_PATH, IMG_BGR)

    def HLT_ALL_IMG(IMG_NAME, BAL):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH).astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_BLU = (B > G) & (B > R)
        HLT_GRE = (G > B) & (G > R)
        HLT_RED = (R > B) & (R > G)
        HLT_EQL = (B == G) & (G == R)

        MJR_YEL = (G > B) & (R > B)
        MJR_CYA = (B > R) & (G > R)
        MJR_PUR = (B > G) & (R > G)
        DIF_G_R = np.abs(G - R)
        DIF_B_R = np.abs(B - R)
        DIF_B_G = np.abs(B - G)

        HLT_YEL = MJR_YEL & (DIF_G_R < DIF_B_G) & (DIF_G_R < DIF_B_R)
        HLT_PUR = MJR_PUR & (DIF_B_R < DIF_B_G) & (DIF_B_R < DIF_G_R)
        HLT_CYA = MJR_CYA & (DIF_B_G < DIF_G_R) & (DIF_B_G < DIF_B_R)

        IMG_BGR[HLT_BLU] = [255, 0, 0]
        IMG_BGR[HLT_GRE] = [0, 255, 0]
        IMG_BGR[HLT_RED] = [0, 0, 255]
        IMG_BGR[HLT_EQL] = [255, 255, 255]

        IMG_BGR[HLT_YEL] = [0, 255, 255]
        IMG_BGR[HLT_PUR] = [255, 0, 255]
        IMG_BGR[HLT_CYA] = [255, 255, 0]
        
        if BAL:
            HGT, WID, COL = IMG_BGR.shape
            
            RED = np.array([0, 0, 255])
            YEL = np.array([0, 255, 255])
            GRE = np.array([0, 255, 0])
            CYA = np.array([255, 255, 0])
            BLU = np.array([255, 0, 0])
            PUR = np.array([255, 0, 255])
            EQL = np.array([255, 255, 255])

            FND_RED = np.all(IMG_BGR == RED, axis=-1)
            FND_YEL = np.all(IMG_BGR == YEL, axis=-1)
            FND_GRE = np.all(IMG_BGR == GRE, axis=-1)
            FND_CYA = np.all(IMG_BGR == CYA, axis=-1)
            FND_BLU = np.all(IMG_BGR == BLU, axis=-1)
            FND_PUR = np.all(IMG_BGR == PUR, axis=-1)
            FND_EQL = np.all(IMG_BGR == EQL, axis=-1)

            NUM_RED = np.sum(FND_RED)
            NUM_YEL = np.sum(FND_YEL)
            NUM_GRE = np.sum(FND_GRE)
            NUM_CYA = np.sum(FND_CYA)
            NUM_BLU = np.sum(FND_BLU)
            NUM_PUR = np.sum(FND_PUR)
            NUM_EQL = np.sum(FND_EQL)
            
            TOT = (HGT * WID) - NUM_EQL
            
            BAL_RED = round(float(100 * (NUM_RED / TOT)), 1)
            BAL_YEL = round(float(100 * (NUM_YEL / TOT)), 1)
            BAL_GRE = round(float(100 * (NUM_GRE / TOT)), 1)
            BAL_CYA = round(float(100 * (NUM_CYA / TOT)), 1)
            BAL_BLU = round(float(100 * (NUM_BLU / TOT)), 1)
            BAL_PUR = round(float(100 * (NUM_PUR / TOT)), 1)
            
            BAL_COL_LST = [BAL_RED, BAL_YEL, BAL_GRE, BAL_CYA, BAL_BLU, BAL_PUR]
            BAL_COL_VAR = round(16 - np.std(BAL_COL_LST), 1)
            if BAL_COL_VAR > 8:
                BAL_COL_VAR_TYP = 'GOOD'
            elif BAL_COL_VAR > 4:
                BAL_COL_VAR_TYP = 'OKAY'
            else:
                BAL_COL_VAR_TYP = 'POOR'

            BAL_PATH = f'output\\DIR-{IMG_NAME}\\BAL-{IMG_NAME}.txt'
            with open(BAL_PATH, 'w') as F:
                F.write("Color Balance Report\n")
                F.write("--------------------------------\n")
                F.write(f"RED: %{BAL_RED}\n")
                F.write(f"YEL: %{BAL_YEL}\n")
                F.write(f"GRE: %{BAL_GRE}\n")
                F.write(f"CYA: %{BAL_CYA}\n")
                F.write(f"BLU: %{BAL_BLU}\n")
                F.write(f"PUR: %{BAL_PUR}\n")
                F.write("--------------------------------\n")
                F.write(f"COLOR VARIATION: {BAL_COL_VAR} [{BAL_COL_VAR_TYP}]\n")
                F.write("--------------------------------\n")
                F.write("Grading:\n")
                F.write("8 ---[GOOD]--- 16\n")
                F.write("4 ---[OKAY]--- 8\n")
                F.write("X ---[POOR]--- 4\n")
                F.write("--------------------------------\n")

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_ALL_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_ALL-{IMG_NAME}'
        cv2.imwrite(HLT_ALL_PATH, IMG_BGR)