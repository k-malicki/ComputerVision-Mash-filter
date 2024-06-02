import cv2
from datetime import datetime
import time
import streamlit as st

class ImageProcessor:
    """
    Klasa używana do przetwarzania obrazu oraz jego eksportu.
    
    """
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.processed_image = None
        self.rect_count = 0
        self.widths = []
        self.idx_list = []
        self.number_of_deviations = 0

    def preprocess_image(self, blur_val, thresh_val):
        """Metoda do przetworzenia obrazu. Zastosowane metody:
            - Konwersja do skali szarości
            - Zastosowanie rozmycia Gaussowskiego
            - Zastosowanie Progowania

        Args:
            blur_val (int): Wartość slidera Blur
            thresh_val (int): Wartość slidera Threshold
        """
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_image, (blur_val, blur_val), 0)
        _, thresholded = cv2.threshold(blurred, thresh_val, 255, cv2.THRESH_BINARY_INV)
        roi = thresholded[600:700, 0:1200] # Wybór ROI
        contours, _ = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        self.rect_count = 0
        self.widths = []
        self.idx_list = []
        self.number_of_deviations = 0
        self.processed_image = self.image.copy()
        idx = 0

        for c in contours:
            area = cv2.contourArea(c)
            if area > 100:
                x, y, w, h = cv2.boundingRect(c)
                y += 600
                idx += 1
                color = (0, 255, 0) if w <= 8 else (255, 0, 0)
                if w > 8:
                    self.number_of_deviations += 1
                cv2.rectangle(self.processed_image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(self.processed_image, f"Nr: {idx}", (x, y + 130), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 0), 2)
                cv2.putText(self.processed_image, f"{w}", (x, y - 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 0), 2)
                
                self.idx_list.append(idx)
                self.rect_count += 1
                self.widths.append(w)

    def export_file(self, file_path, option1, option2):
        """Metoda do eksportowania pliku

        Args:
            file_path (str): Ścieżka zapisu eksportowanego obrazu
            option1 (int): Wartość slidera Blur
            option2 (int): Wartość slidera Threshold
        """
        img = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2RGB)
        img = cv2.putText(img, f"Data eksportu: {datetime.now()}", (10, 870), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 255), 1)
        img = cv2.putText(img, f"Ustawienia: Rozmycie: {option1}, Progowanie: {option2}, Nieprawidlowosci: {self.number_of_deviations}", (10, 890), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 255), 1)
        cv2.imwrite(file_path, img)
        warning = st.sidebar.success("Obraz został poprawnie wyeksportowany.")
        time.sleep(3)
        warning.empty()
