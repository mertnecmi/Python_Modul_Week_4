import pandas
import json

def mesaj_yaz(mesaj=False):
    if not mesaj:
        print("-"* 100)
    else:
        print("-"* 100) 
        print(mesaj)
        print("-"* 100)
    
def write_boek(boeklist):
     try:
          with open("boeks.json", "w", encoding="utf-8") as f:
               json.dump(boeklist, f, ensure_ascii=False, indent=4)
               mesaj_yaz("Veriler başarıyla JSON dosyasına kaydedildi.")
               return True
     except Exception as e:
          mesaj_yaz("Bir hata oldu : ", e)
          return False

def read_boek_file():
     try:
        with open('boeks.json', 'r', encoding='utf-8') as f:
            boek_list = json.load(f) 
            return boek_list
     except (FileNotFoundError, json.JSONDecodeError):
        mesaj_yaz("Kitap verileri bulunamadı veya dosya boş.")  
        return False
def boek_list():
     boek_listesi = read_boek_file()
     df = pandas.DataFrame(boek_listesi)
     print("Sıralama Türü : 1-Kitap Adı    2-Yayıncı    3-Yazar     4-Dil")
     siralama = input("Sıralam Türü : ")
     if siralama == "1":
          df = df.sort_values(by="kitap_adi")
     elif siralama == "2":
          df = df.sort_values(by="yayinci")
     elif siralama == "3":
          df = df.sort_values(by="yazar")
     else:
          df = df.sort_values(by="dil") 
     print("-" * 80)
     print(df.to_string(index=False))
     print("-" * 80)
def boek_add():
    boek_listesi = read_boek_file()
  
    try:
        boek_name    = input("Kitap Adı    :")
        boek_barcode = input("Barkod No    :")
        boek_publish = input("Yayıncı      :")
        boek_year    = input("Yayın Yılı   :")
        boek_author  = input("Yazar        :")
        boek_lang    = input("Dil          :")
        boek_price   = input("Fiyat        :")
        
        if not boek_listesi :
          new_id =  1
          boek_listesi=[]
        else:
          new_id = len(boek_listesi) + 1

        boek_data = {
        "kitap_id": new_id,     
        "kitap_adi": boek_name.capitalize(),
        "barkod_no": boek_barcode,
        "yayinci": boek_publish.capitalize(),
        "yayin_yili": boek_year,
        "yazar": boek_author.capitalize(),
        "dil": boek_lang.capitalize(),
        "fiyat": boek_price,
        "status": "Rafta"
        }
        boek_listesi.append(boek_data)
        write_boek(boek_listesi)
    except Exception as e:
         print(e)
def boek_search():
     while True:
          mesaj_yaz("KİTAP ARAMA")
          try:
               secim = int(input("1-Kitap Adına Göre   2-Yazara Göre   3-Yayıncıya Göre   0-Kitap İşlemleri  : "))
               if secim == 1:
                    nearanacak = input("Kitap Adı Giriniz : ")
                    boek_find("kitap_adi", nearanacak)
                    
               elif secim == 2:
                    nearanacak = input("Kitap Yazarı Giriniz : ")
                    boek_find("yazar", nearanacak)
                    
               elif secim == 3:
                    nearanacak = input("Kitap Yayıncısı Giriniz : ")
                    boek_find("yayinci", nearanacak)
                    
               elif secim == 0:
                    return
          except ValueError as e:
               print("Lütfen 1-2-3 veya 0 Seçiniz ")

def boek_find(nerede,ne):
     listemiz = read_boek_file()
     found = [boek for boek in listemiz if ne.lower() in boek[nerede].lower()]
     if not found:
          mesaj_yaz(f"'{nerede}' İçinde geçen '{ne}' bulunamadı ")
          return
     else:
          df = pandas.DataFrame(found)
          df = df.sort_values(by="kitap_adi")
          mesaj_yaz(f"'{nerede}' Alanı İçinde '{ne}' Geçen  Kitaplar ")
          print(df.to_string(index=False))
          return
def boek_delete():
     boek_list = read_boek_file()
     while True:
          mesaj_yaz("KİTAP DURUM AKTİF/PASİF OLARAK DEĞİŞTİRME")
          try:
               
               print("Çıkış İçin 0 ")
               delete_id = int(input("Durumu Değişecek Kitap ID : "))
               if delete_id == 0:
                   return
               else:
                    varmi = False
                    for boek in boek_list:
                         if boek["kitap_id"] == delete_id:
                              df = pandas.DataFrame(boek, index=[0])
                              print("-"*80)
                              print(df.to_string(index=False))
                              print("-"*80)                  
                              if boek["status"] == "Rafta":
                                   boek["status"] = "Pasif"
                                   neyazilacak = "Pasif"
                                   varmi = True
                                   break
                              elif boek["status"] == "Pasif":
                                   boek["status"] =  "Rafta"
                                   neyazilacak="Rafta"
                                   varmi = True
                                   break
                              else:
                                   mesaj_yaz("Bu Kitap Emanette Olduğu İçin Değiştiremezsin")
                                   return
               if varmi:
                    yesno = input(f"Bu Kitabın Durumunu {neyazilacak} olarak değiştirmek İstiyormusunuz y/n : ")
                    if yesno == "y" or yesno == "Y":
                         
                         write_boek(boek_list)
                         break
                    else:
                         break
               else:
                    return
                    
          except ValueError as e:
               print("Bu Kitap İle İlgili Hata : ", e)

