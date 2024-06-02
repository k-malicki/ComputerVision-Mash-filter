# Computer-Vision-project
Prosty projekt wykorzystujący technologie wizji komputerowej do analizy obrazu płyt filtra zaciernego. Niniejsza praca jest projektem zaliczeniowym.

## Kontakt

Karol Malicki - malickiart@gmail.com

## Biblioteki
- Python
- OpenCV
- Pandas
- Streamlit

## Instalacja
1. Przechodzimy do katalogu, do którego chcemy sklonować repozytorium
   ```sh
   cd /sciezka_do_katalogu
   ```
2. Klonujemy repozytorium
   ```sh
   git clone https://github.com/k-malicki/ComputerVision-Mash-filter.git
   ```
3. Przechodzimy do katalogu projektu
   ```sh
   cd nazwa_projektu
   ```
4. Tworzymy środowisko wirtualne i aktywujemy je
   ```sh
   python -m venv venv
   ```
   ```sh
   .\venv\Scripts\activate
   ```
5. Instalujemy wymagane biblioteki
   ```sh
   pip install -r requirements.txt
   ```

## Uruchomienie
W pliku `app.py` w zmiennej `image_path` musimy podmienić aktualną lokalizację pliku
```py
...
def main():
    """Główna funkcja aplikacji
    
    """
    image_path = r"" <------- nowa lokalizacja pliku
    image_processor = ImageProcessor(image_path)
    my_text = "Przykład aplikacji służącej do wizualizacji płyt filtra zaciernego oraz monitorowanie nieprawidłowości."
...
```


Następnie w terminalu środowiska programistycznego wykonujemy plecenie

```sh
streamlit run app.py
```



<p align="center">
Przykład
</p>

![mashfilter-streamlit](https://github.com/k-malicki/ComputerVision-Mash-filter/assets/141445691/28043a86-5035-46cf-b52f-ebb9c87c8557)
