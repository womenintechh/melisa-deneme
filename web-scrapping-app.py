import requests
from bs4 import BeautifulSoup

def web_scraping(url):
    # Web sitesinden sayfayı çeker
    response = requests.get(url)
    
    if response.status_code == 200:
        # HTML içeriğini BeautifulSoup ile analiz eder
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Sayfa içeriğinden istenilen veriyi çeker
        # Tüm metin içeriğini alır
        haber_basliklari = soup.find_all('h2', class_='news-title')  # Sayfanın HTML yapısına göre uygun etiket ve sınıfı belirler
        
        # Sonuclari ekrana basar.
        for baslik in haber_basliklari:
            print(baslik.get_text().strip())
    else:
        print(f"Hata: {response.status_code} - Sayfa çekilemedi.")

if __name__ == "__main__":
    websitesi_url = "url buraya yapıştır"
    web_scraping(websitesi_url)
