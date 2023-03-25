import sqlite3
import Film
class Veritabani:
    def __init__(self, veritabani):
        self.baglanti = sqlite3.connect(veritabani)
        self.cursor = self.baglanti.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS filmler(ad TEXT, yonetmen TEXT, oyuncular TEXT, yil INT, tur TEXT, puan INT, ozet TEXT)")
        self.baglanti.commit()

    def film_ekle(self, film):
        self.cursor.execute("INSERT INTO filmler VALUES (?, ?, ?, ?, ?, ?, ?)", (film.ad, film.yonetmen, film.oyuncular, film.yil, film.tur, film.puan, film.ozet))
        self.baglanti.commit()

    def film_guncelle(self, film):
        self.cursor.execute("UPDATE filmler SET yonetmen=?, oyuncular=?, yil=?, tur=?, puan=?, ozet=? WHERE ad=?", (film.yonetmen, film.oyuncular, film.yil, film.tur, film.puan, film.ozet, film.ad))
        self.baglanti.commit()

    def film_sil(self, film_ad):
        self.cursor.execute("DELETE FROM filmler WHERE ad=?", (film_ad,))
        self.baglanti.commit()

    def filmleri_listele(self):
        self.cursor.execute("SELECT * FROM filmler")
        filmler = self.cursor.fetchall()
        return filmler
    
