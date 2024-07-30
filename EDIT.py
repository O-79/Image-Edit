import cv2
import numpy as np

class Edit:
    def HUE_IMG(IMG_NAME, HUE):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        IMG_HSV = cv2.cvtColor(IMG_BGR, cv2.COLOR_BGR2HSV)
        IMG_HSV[..., 0] = (IMG_HSV[..., 0] + HUE) % 180
        IMG_BGR = cv2.cvtColor(IMG_HSV, cv2.COLOR_HSV2BGR)

        HUE_PATH = f'output\\DIR-{IMG_NAME}\\HUE\\HUE-{HUE}-{IMG_NAME}'
        cv2.imwrite(HUE_PATH, IMG_BGR)

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

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        HLT_BLU = (B > G) & (B > R)
        IMG_BGR[HLT_BLU] = [255, 0, 0]

        HLT_BLU_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_BLU-{IMG_NAME}'
        cv2.imwrite(HLT_BLU_PATH, IMG_BGR)

    def HLT_GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        HLT_GRE = (G > B) & (G > R)
        IMG_BGR[HLT_GRE] = [0, 255, 0]
        
        HLT_GRE_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_GRE-{IMG_NAME}'
        cv2.imwrite(HLT_GRE_PATH, IMG_BGR)

    def HLT_RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        HLT_RED = (R > B) & (R > G)
        IMG_BGR[HLT_RED] = [0, 0, 255]

        HLT_RED_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_RED-{IMG_NAME}'
        cv2.imwrite(HLT_RED_PATH, IMG_BGR)

    def HLT_YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        MJR_YEL = (G > B) & (R > B)
        DIF_RED_GRE = np.abs(R - G)
        DIF_GRE_BLU = np.abs(G - B)
        DIF_RED_BLU = np.abs(R - B)

        HLT_YEL = MJR_YEL & (DIF_RED_GRE < DIF_GRE_BLU) & (DIF_RED_GRE < DIF_RED_BLU)
        IMG_BGR[HLT_YEL] = [0, 255, 255]

        HLT_YEL_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_YEL-{IMG_NAME}'
        cv2.imwrite(HLT_YEL_PATH, IMG_BGR)

    def HLT_PUR_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        MJR_PUR = (B > G) & (R > G)
        DIF_RED_GRE = np.abs(R - G)
        DIF_GRE_BLU = np.abs(G - B)
        DIF_RED_BLU = np.abs(R - B)

        HLT_PUR = MJR_PUR & (DIF_RED_BLU < DIF_GRE_BLU) & (DIF_RED_BLU < DIF_RED_GRE)
        IMG_BGR[HLT_PUR] = [255, 0, 255]

        HLT_PUR_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_PUR-{IMG_NAME}'
        cv2.imwrite(HLT_PUR_PATH, IMG_BGR)

    def HLT_CYA_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        MJR_CYA = (B > R) & (G > R)
        DIF_RED_GRE = np.abs(R - G)
        DIF_GRE_BLU = np.abs(G - B)
        DIF_RED_BLU = np.abs(R - B)

        HLT_CYA = MJR_CYA & (DIF_GRE_BLU < DIF_RED_GRE) & (DIF_GRE_BLU < DIF_RED_BLU)
        IMG_BGR[HLT_CYA] = [255, 255, 0]

        HLT_CYA_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_CYA-{IMG_NAME}'
        cv2.imwrite(HLT_CYA_PATH, IMG_BGR)

    def HLT_ALL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)

        B = IMG_BGR[:, :, 0]
        G = IMG_BGR[:, :, 1]
        R = IMG_BGR[:, :, 2]

        HLT_BLU = (B > G) & (B > R)
        HLT_GRE = (G > B) & (G > R)
        HLT_RED = (R > B) & (R > G)
        HLT_EQL = (B == G) & (G == R)

        MJR_YEL = (G > B) & (R > B)
        MJR_CYA = (B > R) & (G > R)
        MJR_PUR = (B > G) & (R > G)
        DIF_RED_GRE = np.abs(R - G)
        DIF_GRE_BLU = np.abs(G - B)
        DIF_RED_BLU = np.abs(R - B)

        HLT_YEL = MJR_YEL & (DIF_RED_GRE < DIF_GRE_BLU) & (DIF_RED_GRE < DIF_RED_BLU)
        HLT_PUR = MJR_PUR & (DIF_RED_BLU < DIF_RED_GRE) & (DIF_RED_BLU < DIF_GRE_BLU)
        HLT_CYA = MJR_CYA & (DIF_GRE_BLU < DIF_RED_GRE) & (DIF_GRE_BLU < DIF_RED_BLU)

        IMG_BGR[HLT_YEL] = [0, 255, 255]
        IMG_BGR[HLT_PUR] = [255, 0, 255]
        IMG_BGR[HLT_CYA] = [255, 255, 0]

        IMG_BGR[HLT_BLU] = [255, 0, 0]
        IMG_BGR[HLT_GRE] = [0, 255, 0]
        IMG_BGR[HLT_RED] = [0, 0, 255]
        IMG_BGR[HLT_EQL] = [255, 255, 255]

        HLT_ALL_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_ALL-{IMG_NAME}'
        cv2.imwrite(HLT_ALL_PATH, IMG_BGR)