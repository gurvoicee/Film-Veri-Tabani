from Film import Film
from Veritabani import Veritabani
def menu():
    print("1- Film Ekle")
    print("2- Film Güncelle")
    print("3- Film Sil")
    print("4- Tüm Filmleri Listele")
    print("5- Çıkış")

    secim = input("Seçiminiz: ")
    return secim

def film_ekle(veritabani):
    ad = input("Film Adı: 5")
    yonetmen = input("Yönetmen: ")
    oyuncular = input("Oyuncular: ")
    yil = input("Yayın Yılı: ")
    tur = input("Tür: ")
    puan = input("Puan: ")
    ozet = input("Özet: ")

    film = Film(ad, yonetmen, oyuncular, yil, tur, puan, ozet)
    veritabani.film_ekle(film)

def film_guncelle(veritabani):
    ad = input("Güncellenecek film adı: ")
    yonetmen = input("Yönetmen: ")
    oyuncular = input("Oyuncular: ")
    yil = input("Yayın Yılı: ")
    tur = input("Tür: ")
    puan = input("Puan: ")
    ozet = input("Özet: ")

    film = Film(ad, yonetmen, oyuncular, yil, tur, puan, ozet)
    veritabani.film_guncelle(film)

def film_sil(veritabani):
    ad = input("Silinecek film adı: ")
    veritabani.film_sil(ad)

def filmleri_listele(veritabani):
    filmler = veritabani.filmleri_listele()
    for film in filmler:
        print(f"Ad: {film[0]}")
        print(f"Yönetmen: {film[1]}")
        print(f"Oyuncular: {film[2]}")
        print(f"Yayın Yılı: {film[3]}")
        print(f"Tür: {film[4]}")
        print(f"Puan: {film[5]}")
        print(f"Özet: {film[6]}")
        print("\n")

def main():
    veritabani = Veritabani("film_veritabani.db")

    while True:
        secim = menu()

        if secim == "1":
            film_ekle(veritabani)

        elif secim == "2":
            film_guncelle(veritabani)

        elif secim == "3":
            film_sil(veritabani)

        elif secim == "4":
            filmleri_listele(veritabani)

        elif secim == "5":
            print("Program sonlandırıldı.")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

main()