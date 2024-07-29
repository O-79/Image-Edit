import cv2
import numpy as np

class EDIT:
    def HUE_IMG(IMG_NAME, HUE):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        IMG_HSV = cv2.cvtColor(IMG_BGR, cv2.COLOR_BGR2HSV)
        IMG_HSV[..., 0] = (IMG_HSV[..., 0] + HUE) % 180
        IMG_BGR = cv2.cvtColor(IMG_HSV, cv2.COLOR_HSV2BGR)
        HUE_PATH = f'output\\DIR-{IMG_NAME}\\HUE-{HUE}-{IMG_NAME}'
        cv2.imwrite(HUE_PATH, IMG_BGR)

    def BLU_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_BLU = cv2.merge([B, G, R])
        BLU_PATH = f'output\\DIR-{IMG_NAME}\\BLU-{IMG_NAME}'
        cv2.imwrite(BLU_PATH, IMG_BLU)

    def GRE_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_GRE = cv2.merge([B, G, R])
        GRE_PATH = f'output\\DIR-{IMG_NAME}\\GRE-{IMG_NAME}'
        cv2.imwrite(GRE_PATH, IMG_GRE)

    def RED_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_RED = cv2.merge([B, G, R])
        RED_PATH = f'output\\DIR-{IMG_NAME}\\RED-{IMG_NAME}'
        cv2.imwrite(RED_PATH, IMG_RED)

    def CYA_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        R = np.clip(R * 0, 0, 255).astype(np.uint8)
        IMG_CYA = cv2.merge([B, G, R])
        CYA_PATH = f'output\\DIR-{IMG_NAME}\\CYA-{IMG_NAME}'
        cv2.imwrite(CYA_PATH, IMG_CYA)

    def YEL_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        B = np.clip(B * 0, 0, 255).astype(np.uint8)
        IMG_YEL = cv2.merge([B, G, R])
        YEL_PATH = f'output\\DIR-{IMG_NAME}\\YEL-{IMG_NAME}'
        cv2.imwrite(YEL_PATH, IMG_YEL)

    def PUR_IMG(IMG_NAME):
        IMG_PATH = f'output\\DIR-{IMG_NAME}\\{IMG_NAME}'
        IMG_BGR = cv2.imread(IMG_PATH)
        B, G, R = cv2.split(IMG_BGR)
        G = np.clip(G * 0, 0, 255).astype(np.uint8)
        IMG_PUR = cv2.merge([B, G, R])
        PUR_PATH = f'output\\DIR-{IMG_NAME}\\PUR-{IMG_NAME}'
        cv2.imwrite(PUR_PATH, IMG_PUR)