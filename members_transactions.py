import json
from datetime import datetime
import time_transactions as tt
import pandas as pd


def mesaj_yaz(mesaj=False):
    if not mesaj:
        print("-"* 100)
    else:
        print("-"* 100) 
        print(mesaj)
        print("-"* 100)
    
def member_name_given(id):
    boeklist = read_members_file()
    for boek in boeklist:
        if boek["üye_id"] == id:
            found = boek["üye_adi"] + " " + boek["üye_soyadi"]
            return found
def boek_name_given(id):
    boeklist = read_boek_file()
    for boek in boeklist:
        if boek["kitap_id"] == id:
            found = boek["kitap_adi"] 
            return found
def read_lend_file():
    try:
        with open('lend.json', 'r', encoding='utf-8') as f:
            lend_list = json.load(f) 
            return lend_list
    except (FileNotFoundError, json.JSONDecodeError):
        print("Lend verileri bulunamadı veya dosya boş.") 
        return False
def write_lend_file(lendlist):
     try:
          with open("lend.json", "w", encoding="utf-8") as f:
               json.dump(lendlist, f, ensure_ascii=False, indent=4)
               print("Veriler başarıyla LEND.JSON dosyasına kaydedildi.")
               return True
     except Exception as e:
          print("Bir hata oldu : ", e)
          return False
def write_boek_file(boeklist):
     try:
          with open("boeks.json", "w", encoding="utf-8") as f:
               json.dump(boeklist, f, ensure_ascii=False, indent=4)
               print("Veriler başarıyla BOEK.JSON dosyasına kaydedildi.")
               return True
     except Exception as e:
          print("Bir hata oldu : ", e)
          return False

def read_boek_file():
    try:
        with open('boeks.json', 'r', encoding='utf-8') as f:
            boek_list = json.load(f) 
            return boek_list
    except (FileNotFoundError, json.JSONDecodeError):
        print("Kitap verileri bulunamadı veya dosya boş.") 

def write_members_file(members):
    try:
        with open("members.json", "w", encoding="utf-8") as f:
            json.dump(members, f, ensure_ascii=False, indent=4)
            print("Veriler başarıyla MEMBERS.JSON dosyasına kaydedildi.")
            return True
    except Exception as e:
        print("Bir hata oldu : ", e)
        return False

def read_members_file():
    try:
        with open('members.json', 'r', encoding='utf-8') as f:
            members_lists = json.load(f) 
            return members_lists
    except (FileNotFoundError, json.JSONDecodeError):
        print("Üye verileri bulunamadı veya dosya boş.")  

def members_list():
    try:
        members_list = read_members_file()
        mesaj_yaz("ÜYE LİSTESİ")
        df = pd.DataFrame(members_list)
        if members_list:
            df = df.sort_values(by="üye_adi")
            print(df.to_string(index=False))
        else:
            mesaj_yaz("Üye Listesi Boş")
        mesaj_yaz()
        return
    except Exception as e:
        print(e)
      
def members_add():
    members_lists = read_members_file()
    mesaj_yaz("ÜYE KAYIT BÖLÜMÜ")
    new_id = 1
    try:
        member_name      = input("Üye Adı      : ")
        member_surname   = input("Üye Soyadı   : ")
        member_phone     = input("Üye Telefon  : ")
        member_adres     = input("Üye Adres    : ")
        member_city      = input("Üye Şehir    : ")
        while True:
            member_birth_day = input("Doğum Tarihi ('gg.aa.yyyy' olarak giriniz): ")
            if tt.dogum_tarihi_dogrulama(member_birth_day):
                break  
            else:
                print("Geçersiz doğum tarihi formatı! Lütfen DD.MM.YYYY formatında giriniz.")
        bugun = datetime.today().date()
        if members_lists:
            new_id = len(members_lists) + 1
        else:
            members_lists = []
        member_data = {
        "üye_id": new_id,
        "üye_adi": member_name.capitalize(),
        "üye_soyadi": member_surname.capitalize(),
        "üye_telefon": member_phone,
        "üye_adres": member_adres.capitalize(),
        "üye_şehir": member_city.capitalize(),
        "üye_doğum_tarihi": member_birth_day,
        "date": bugun.strftime("%d.%m.%Y"),
        "üye_durum": "Aktif"
        }
        members_lists.append(member_data)
        write_members_file(members_lists)
        return True
    except Exception as e:
         print(e)
 
def members_search():
    mesaj_yaz("ÜYE ARA")
    uyearamenu = " 1. İsimle Ara \n"
    uyearamenu += " 2. Soyisimle Ara\n"
    uyearamenu += " 3. Şehirle Ara\n"
    uyearamenu += " 0. Üye Menüsüne Dön\n"
    print(uyearamenu)
    while True:
        uyechoice = input("Arama Şeklini Seçiniz : ")
        if uyechoice == "1":
            aranacak = input("İsim Girimiz :")
            uyeara("üye_adi", aranacak)
            break
        elif uyechoice == "2":
            aranacak = input("Soyisim Girimiz :")
            uyeara("üye_soyadi", aranacak)
            break
        elif uyechoice == "3":
            aranacak = input("Şehir Girimiz :")
            uyeara("üye_şehir", aranacak)
            break
        elif uyechoice == "0":
            break            
        else: 
            print("lütfen doğru seçim yapınız...")
def uyeara(neyle, nearanacak):
    """ üyeler listesinde isim, soyisim veya şehre göre arama yapar. tamamını girmek zorunda değilsiniz"""
    listemiz = read_members_file()
    found = [member for member in listemiz if nearanacak.lower() in member[neyle].lower()]
    if not found:
        mesaj_yaz(f"'{neyle}' İçinde geçen '{nearanacak}' bulunamadı ")
        return
    df = pd.DataFrame(found)
    df = df.sort_values(by="üye_adi")
    mesaj_yaz(f"'{neyle}' Alanı İçinde '{nearanacak}' Geçen  Üyeler ")
    print(df.to_string(index=False))
    return

def members_delete():
    mesaj_yaz("ÜYE STATUSU DEĞİŞTİRME")
    while True:
        try:
            print("Çıkış İçin 0")
            delete_id = int(input("Durumu Değişecek Üye ID : "))
            if delete_id == 0:
                return
            try:
                members_list = read_members_file()
                pasif_durum = False
                for member in members_list:
                    if member["üye_id"] == delete_id:
                        if member["üye_durum"] == "Aktif":
                            member["üye_durum"] = "Pasif" 
                            neyapildi = "Pasif"
                        else:
                            member["üye_durum"] = "Aktif" 
                            neyapildi = "Aktif"
                        pasif_durum = True
                        break
                if not pasif_durum:
                    mesaj_yaz(f"{delete_id} ID Bulunamadı ....")
              
                else:
                    write_members_file(members_list)
                    mesaj_yaz(f"ID {delete_id} numarasına sahip üyenin durumu {neyapildi} olarak değiştirildi")
                    return
            except Exception as e:
                mesaj_yaz("hata", e)   
        except ValueError as e:
            print(e)
def members_boek_give():
    mesaj_yaz("KİTAP EMANETE VERME")
    kitaplistesi = read_boek_file()
    members_list = read_members_file()
    lend_list = read_lend_file()
    try:
        uye_id = int(input("Üye ID Giriniz : "))
        if uye_id == 0:
            return
        for member in members_list:
            if member["üye_id"] == uye_id and member["üye_durum"] == "Aktif" :
                print("Üye Adı \t Üye Soyadı \t Telefon")
                print("--------- \t ---------- \t --------")
                print(f"{member["üye_adi"]} \t\t {member["üye_soyadi"]} \t\t {member["üye_telefon"]}")
                raftakilar = [boek for boek in kitaplistesi if boek["status"] != "Emanette"]
                if not raftakilar:
                    print("Emanet Verilebilecek Kitap Yok")
                    return
                df = pd.DataFrame(raftakilar)
                df = df.sort_values(by="kitap_adi")
                mesaj_yaz("RAFTAKİ KİTAP LİSTESİ")
                print(df.to_string(index=False))
                try:
                    emanetverilecekid = int(input("Emanet Verilecek Kitap ID : "))
                    if(emanetverilecekid) == 0:
                        return
                    emanet = False
                    for kitap in kitaplistesi:
                        if kitap["kitap_id"] == emanetverilecekid:
                            kitap["status"] = "Emanette"
                            emanet = True
                    if not emanet:
                        print("Emanet Verilecek Kitap ID Bulunamadı ")
                    else:
                        write_boek_file(kitaplistesi)
                        if not lend_list:
                            lend_list = []
                            lend_id = 1
                        else:
                            lend_id = len(lend_list)+1
                        lend_data = {
                            "lend_id" : lend_id,
                            "boek_id" : emanetverilecekid,
                            "member_id" :uye_id,
                            "verilme_tarihi": tt.bugun(),
                            "iade_tarihi" : tt.due_date(),
                            "iade_oldugu_tarih" : ""
                        }
                        lend_list.append(lend_data)
                        write_lend_file(lend_list)
                        print(f"{emanetverilecekid} ID nolu kitap {uye_id} nolu üyeye emanet verildi")
                        return
                except ValueError as e:
                    print(e)
                break
        mesaj_yaz("Bu ID'ye Kayıtlı AKTİF Üye Yok")        
    except ValueError as e:
        print(e)
def members_boek_refund():
    sayac = members_boek_list()
    found = False 
    if sayac == 0 :
         return    
    lend_listesi = read_lend_file()
    boek_listesi = read_boek_file()
    try:
        print("Menüye Dönüş İçin 0")
        choice = int(input("İade Alınacak LEND ID : "))
        if choice == 0:
            return
        for lend in lend_listesi:
            if lend["lend_id"] == choice and lend["iade_oldugu_tarih"] =="":
                lend["iade_oldugu_tarih"] = tt.bugun()
                found = True
                for boek in boek_listesi:
                    if boek["kitap_id"] == lend["boek_id"]:
                        boek["status"] = "Rafta"
                        break
                break
        if not found:
            print(f"lend_id {choice} bulunamadı veya daha önce teslim edilmiş.")
        else:
            write_lend_file(lend_listesi)
            write_boek_file(boek_listesi) 
    except ValueError as e:
        print("Lütfen Doğru Seçenek Girin...:", e)

def member_boek_found(x):
    lend_listesi = read_lend_file()
    yenilendlist = []
    sayac = 0
    toplamgun = 0
    bekleyen = 0
    ortalama = 0
    if not lend_listesi:
        return sayac
    for lend in lend_listesi:
        if lend["member_id"] ==x:
            fark = tt.ikitarihfarki(lend["iade_oldugu_tarih"], lend["iade_tarihi"])
            if fark != 0:
                sayac +=1
                toplamgun += fark
            else :
                bekleyen +=1
            boek_name = boek_name_given(lend["boek_id"])
            member_name = member_name_given(lend["member_id"])
            yenidata = {
            "Id" : lend["lend_id"],
            "Kitap" : boek_name,
            "Üye" : member_name,
            "Verilme_Tarihi" : tt.parse_date(lend["verilme_tarihi"]),
            "İade_Olacağı_Tarihi" : tt.parse_date(lend["iade_tarihi"]),
            "İade_Olduğu_Tarihi" : tt.parse_date(lend["iade_oldugu_tarih"]),
            "Fark" : fark
            }
            yenilendlist.append(yenidata)
            try:
                ortalama = toplamgun / sayac
            except Exception as e:
                pass
            else:
                mesaj_yaz("Henüz Kayıt Yok")
    df = pd.DataFrame(yenilendlist)
    df = df.sort_values(by="Fark")
    print(df.to_string(index=False))   
    mesaj_yaz(f"Bu üye {sayac} kitabı Ortalama {round(ortalama,1)} günde iade etmiş ve {bekleyen} bekleyen kitap var")
    return
def members_boek_list():
    mesaj_yaz("EMANETE VERİLMİŞ KİTAP LİSTESİ")
    lend_listesi = read_lend_file()
    yenilendlist = []
    sayac = 0
    if not lend_listesi:
        return sayac
    for lend in lend_listesi:
        if lend["iade_oldugu_tarih"] =="":
            sayac +=1
        boek_name = boek_name_given(lend["boek_id"])
        member_name = member_name_given(lend["member_id"])
        yenidata = {
            "Id" : lend["lend_id"],
            "Kitap" : boek_name,
            "Üye" : member_name,
            "Verilme_Tarihi" : tt.parse_date(lend["verilme_tarihi"]),
            "İade_Olacağı_Tarihi" : tt.parse_date(lend["iade_tarihi"]),
            "İade_Olduğu_Tarihi" : tt.parse_date(lend["iade_oldugu_tarih"]),
            "Fark" : tt.ikitarihfarki(lend["iade_oldugu_tarih"], lend["iade_tarihi"])
        }
        yenilendlist.append(yenidata)
    df = pd.DataFrame(yenilendlist)
    df = df.sort_values(by="Fark")
    print(df.to_string(index=False))    
    mesaj_yaz(f"İade Edilmeyi Bekleyen Kitap Sayısı : {sayac}")
    return sayac
def members_deleted():
    try:
        members_list = read_members_file()
        mesaj_yaz("Silinmiş Üyeler Listesi:")
        df = pd.DataFrame(members_list)
        df = df[df['üye_durum'] == 'Pasif']
        if len(df) == 0:
            print("Pasif Üye Yok")
        else:
            print(df.to_string(index=False))
            mesaj_yaz()
    except:
        print("Üye verileri bulunamadı veya dosya boş.")

def member_boek_list():
    mesaj_yaz("ÜYENİN ALDIĞI KİTAPLAR")
    while True:
        try:
            uye_id = int(input("Üye ID Giriniz : "))
            if uye_id == 0:
                return
            else:
                #lend_list = read_lend_file()
                #found = [lend for lend in lend_list if uye_id == lend["member_id"]]
                member_boek_found(uye_id)
                # if not found:
                #     mesaj_yaz("Bu Üye Hiç Emanet Kitap Almamış")
                # else:
                #     df = pd.DataFrame(found)
                #     print(df.to_string(index=False))
                #     mesaj_yaz()
                #     return
        except ValueError as e:
            print("Sayısal Veri Giriniz ")