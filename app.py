"""
Prosty projekt wykorzystujący technologie wizji komputerowej do analizy obrazu płyt filtra zaciernego. 
Niniejsza praca jest projektem zaliczeniowym.
Autor: Karol Malicki
Data: 2024-06-01
"""

import streamlit as st
import pandas as pd
from image_processor import ImageProcessor

def main():
    """Główna funkcja aplikacji
    
    """
    image_path = r"Image\mash_filter.jpg"
    image_processor = ImageProcessor(image_path)
    my_text = "Przykład aplikacji służącej do wizualizacji płyt filtra zaciernego oraz monitorowanie nieprawidłowości."
    
    st.set_page_config(layout="wide")
    st.sidebar.title('Opis')
    st.sidebar.write(my_text)
    
    button_check = st.sidebar.checkbox("Rozpocznij analizę")
    slider_blur = st.sidebar.slider("Rozmycie Gaussa", value=1, min_value=1, max_value=25, step=4)
    slider_thresh = st.sidebar.slider("Progowanie", value=0, min_value=0, max_value=254, step=1)
    
    st.sidebar.divider()
    export_button = st.sidebar.button("Eksportuj do pliku")
    
    col1, col2 = st.columns([2, 1])
    df = None
    
    with col1:
        st.subheader('Kamera #1')
        st.text("Przykładowy podgląd z kamery")
        
        if button_check:
            image_processor.preprocess_image(slider_blur, slider_thresh)
            st.image(image_processor.processed_image)
            st.text(f"Rozmiar obrazu: {image_processor.processed_image.shape}")
            st.text(f"Odstępy między płytami: {image_processor.rect_count}")
            
            df = pd.DataFrame(image_processor.widths, columns=["Odległość w pikselach"])
            df.index.name = "Numer"
            df.index += 1
            
            if export_button:
                image_processor.export_file("processed_image.png", slider_blur, slider_thresh)
        else:
            st.image(image_processor.image)
            st.text(f"Rozmiar obrazu: {image_processor.image.shape}")
    
    with col2:
        st.subheader('Ustawienia')
        st.metric(label="Rozmycie Gaussa", value=slider_blur)
        st.metric(label="Progowanie", value=slider_thresh)
        st.dataframe(df, width=200)

if __name__ == "__main__":
    main()
