import cv2
import numpy as np

class Edit:
    def HUE_IMG(IMG_NAME, HUE):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        IMG_HSV = cv2.cvtColor(IMG_BGR, cv2.COLOR_BGR2HSV)
        IMG_HSV[..., 0] = (IMG_HSV[..., 0] + HUE) % 180
        IMG_BGR = cv2.cvtColor(IMG_HSV, cv2.COLOR_HSV2BGR)

        HUE_PATH = f'output\\DIR-{IMG_NAME}\\HUE\\HUE_{HUE}-{IMG_NAME}'
        cv2.imwrite(HUE_PATH, IMG_BGR)

    def INV_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(255 - B, 0, 255).astype(np.uint8)
        G = np.clip(255 - G, 0, 255).astype(np.uint8)
        R = np.clip(255 - R, 0, 255).astype(np.uint8)
        IMG_INV = cv2.merge([B, G, R])

        INV_PATH = f'output\\DIR-{IMG_NAME}\\COL\\INV-{IMG_NAME}'
        cv2.imwrite(INV_PATH, IMG_INV)

    def BNW_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BNW = IMG_BGR.astype(np.int16)

        HGT, WID, COL = IMG_BNW.shape
        for _y_ in range(HGT):
            for _x_ in range(WID):
                P = IMG_BNW[_y_, _x_]
                B, G, R = P
                X = max(B, G, R)
                B = X
                G = X
                R = X
                IMG_BNW[_y_, _x_] = np.array([B, G, R])

        IMG_BNW = IMG_BNW.astype(np.uint8)
        BNW_PATH = f'output\\DIR-{IMG_NAME}\\COL\\BNW-{IMG_NAME}'
        cv2.imwrite(BNW_PATH, IMG_BNW)

    def RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_RED = cv2.merge([B, G, R])

        RED_PATH = f'output\\DIR-{IMG_NAME}\\COL\\RED-{IMG_NAME}'
        cv2.imwrite(RED_PATH, IMG_RED)

    def GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_GRE = cv2.merge([B, G, R])

        GRE_PATH = f'output\\DIR-{IMG_NAME}\\COL\\GRE-{IMG_NAME}'
        cv2.imwrite(GRE_PATH, IMG_GRE)

    def BLU_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_BLU = cv2.merge([B, G, R])

        BLU_PATH = f'output\\DIR-{IMG_NAME}\\COL\\BLU-{IMG_NAME}'
        cv2.imwrite(BLU_PATH, IMG_BLU)

    def YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        IMG_YEL = cv2.merge([B, G, R])

        YEL_PATH = f'output\\DIR-{IMG_NAME}\\COL\\YEL-{IMG_NAME}'
        cv2.imwrite(YEL_PATH, IMG_YEL)

    def PUR_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_PUR = cv2.merge([B, G, R])

        PUR_PATH = f'output\\DIR-{IMG_NAME}\\COL\\PUR-{IMG_NAME}'
        cv2.imwrite(PUR_PATH, IMG_PUR)

    def CYA_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B, G, R = cv2.split(IMG_BGR)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_CYA = cv2.merge([B, G, R])

        CYA_PATH = f'output\\DIR-{IMG_NAME}\\COL\\CYA-{IMG_NAME}'
        cv2.imwrite(CYA_PATH, IMG_CYA)

    def HLT_BLU_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_BLU = (B > G) & (B > R)
        IMG_BGR[HLT_BLU] = [255, 0, 0]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_BLU_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_BLU-{IMG_NAME}'
        cv2.imwrite(HLT_BLU_PATH, IMG_BGR)

    def HLT_GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_GRE = (G > B) & (G > R)
        IMG_BGR[HLT_GRE] = [0, 255, 0]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_GRE_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_GRE-{IMG_NAME}'
        cv2.imwrite(HLT_GRE_PATH, IMG_BGR)

    def HLT_RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

        B, G, R = cv2.split(IMG_BGR)

        HLT_RED = (R > B) & (R > G)
        IMG_BGR[HLT_RED] = [0, 0, 255]

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_RED_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_RED-{IMG_NAME}'
        cv2.imwrite(HLT_RED_PATH, IMG_BGR)

    def HLT_YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

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
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

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
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

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
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_BGR = IMG_BGR.astype(np.int16)

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
            TOT = HGT * WID
            
            RED = np.array([0, 0, 255])
            YEL = np.array([0, 255, 255])
            GRE = np.array([0, 255, 0])
            CYA = np.array([255, 255, 0])
            BLU = np.array([255, 0, 0])
            PUR = np.array([255, 0, 255])

            FND_RED = np.all(IMG_BGR == RED, axis=-1)
            FND_YEL = np.all(IMG_BGR == YEL, axis=-1)
            FND_GRE = np.all(IMG_BGR == GRE, axis=-1)
            FND_CYA = np.all(IMG_BGR == CYA, axis=-1)
            FND_BLU = np.all(IMG_BGR == BLU, axis=-1)
            FND_PUR = np.all(IMG_BGR == PUR, axis=-1)

            NUM_RED = np.sum(FND_RED)
            NUM_YEL = np.sum(FND_YEL)
            NUM_GRE = np.sum(FND_GRE)
            NUM_CYA = np.sum(FND_CYA)
            NUM_BLU = np.sum(FND_BLU)
            NUM_PUR = np.sum(FND_PUR)
            
            BAL_RED = round(float(100 * (NUM_RED / TOT)), 1)
            BAL_YEL = round(float(100 * (NUM_YEL / TOT)), 1)
            BAL_GRE = round(float(100 * (NUM_GRE / TOT)), 1)
            BAL_CYA = round(float(100 * (NUM_CYA / TOT)), 1)
            BAL_BLU = round(float(100 * (NUM_BLU / TOT)), 1)
            BAL_PUR = round(float(100 * (NUM_PUR / TOT)), 1)
            
            BAL_COL_LST = [BAL_RED, BAL_YEL, BAL_GRE, BAL_CYA, BAL_BLU, BAL_PUR]
            BAL_COL_VAR = round(np.std(BAL_COL_LST), 1)
            if BAL_COL_VAR < 8:
                BAL_COL_VAR_TYP = 'GOOD'
            elif BAL_COL_VAR < 16:
                BAL_COL_VAR_TYP = 'OKAY'
            else:
                BAL_COL_VAR_TYP = 'POOR'

            BAL_PATH = f'output\\DIR-{IMG_NAME}\\BAL-{IMG_NAME}.txt'
            with open(BAL_PATH, 'w') as F:
                F.write("Color Balance\n")
                F.write("----------------\n")
                F.write(f"RED: %{BAL_RED}\n")
                F.write(f"YEL: %{BAL_YEL}\n")
                F.write(f"GRE: %{BAL_GRE}\n")
                F.write(f"CYA: %{BAL_CYA}\n")
                F.write(f"BLU: %{BAL_BLU}\n")
                F.write(f"PUR: %{BAL_PUR}\n")
                F.write("----------------\n")
                F.write(f"COLOR VARIATION: {BAL_COL_VAR} [{BAL_COL_VAR_TYP}]\n")
                

        IMG_BGR = IMG_BGR.astype(np.uint8)
        HLT_ALL_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_ALL-{IMG_NAME}'
        cv2.imwrite(HLT_ALL_PATH, IMG_BGR)