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

    def PUR_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_PUR = cv2.merge([B, G, R])
        PUR_PATH = f'output\\DIR-{IMG_NAME}\\COL\\PUR-{IMG_NAME}'
        cv2.imwrite(PUR_PATH, IMG_PUR)

    def YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        IMG_YEL = cv2.merge([B, G, R])
        YEL_PATH = f'output\\DIR-{IMG_NAME}\\COL\\YEL-{IMG_NAME}'
        cv2.imwrite(YEL_PATH, IMG_YEL)

    def CYA_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_CYA = cv2.merge([B, G, R])
        CYA_PATH = f'output\\DIR-{IMG_NAME}\\COL\\CYA-{IMG_NAME}'
        cv2.imwrite(CYA_PATH, IMG_CYA)

    def HLT_RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        HLT_RED = (IMG_BGR[:, :, 0] > IMG_BGR[:, :, 1]) & (IMG_BGR[:, :, 0] > IMG_BGR[:, :, 2])
        IMG_BGR[HLT_RED] = [255, 0, 0]
        HLT_RED_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_RED-{IMG_NAME}'
        cv2.imwrite(HLT_RED_PATH, IMG_BGR)

    def HLT_GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        HLT_GRE = (IMG_BGR[:, :, 1] > IMG_BGR[:, :, 0]) & (IMG_BGR[:, :, 1] > IMG_BGR[:, :, 2])
        IMG_BGR[HLT_GRE] = [0, 255, 0]
        HLT_GRE_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_GRE-{IMG_NAME}'
        cv2.imwrite(HLT_GRE_PATH, IMG_BGR)

    def HLT_BLU_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        HLT_BLU = (IMG_BGR[:, :, 2] > IMG_BGR[:, :, 0]) & (IMG_BGR[:, :, 2] > IMG_BGR[:, :, 1])
        IMG_BGR[HLT_BLU] = [0, 0, 255]
        HLT_BLU_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_BLU-{IMG_NAME}'
        cv2.imwrite(HLT_BLU_PATH, IMG_BGR)

    def HLT_ALL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        HLT_RED = (IMG_BGR[:, :, 0] > IMG_BGR[:, :, 1]) & (IMG_BGR[:, :, 0] > IMG_BGR[:, :, 2])
        HLT_GRE = (IMG_BGR[:, :, 1] > IMG_BGR[:, :, 0]) & (IMG_BGR[:, :, 1] > IMG_BGR[:, :, 2])
        HLT_BLU = (IMG_BGR[:, :, 2] > IMG_BGR[:, :, 0]) & (IMG_BGR[:, :, 2] > IMG_BGR[:, :, 1])
        HLT_EQL = (IMG_BGR[:, :, 0] == IMG_BGR[:, :, 1]) | (IMG_BGR[:, :, 1] == IMG_BGR[:, :, 2]) | (IMG_BGR[:, :, 2] == IMG_BGR[:, :, 0])
        IMG_BGR[HLT_RED] = [255, 0, 0]
        IMG_BGR[HLT_GRE] = [0, 255, 0]
        IMG_BGR[HLT_BLU] = [0, 0, 255]
        IMG_BGR[HLT_EQL] = [255, 255, 255]
        HLT_ALL_PATH = f'output\\DIR-{IMG_NAME}\\HLT\\HLT_ALL-{IMG_NAME}'
        cv2.imwrite(HLT_ALL_PATH, IMG_BGR)