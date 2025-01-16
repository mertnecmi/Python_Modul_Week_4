import json

import boek_transactions as bt
import members_transactions as mt



def cikis():
    print("Çıkış Yapılıyor...")
    exit()
def members_menu():
    menu =  "-----------------------------------------------------------------\n"
    menu += "|                      ÜYELİK İŞLEMLERİ                         |\n"
    menu +="|                                                               |\n"
    menu +="|    1 - Üye Listesi            6 - Kitap Ödünç Ver             |\n"
    menu +="|    2 - Üye Kaydet             7 - Kitap İade Al               |\n"
    menu +="|    3 - Üye Bul                8 - Üyenin Aldığı Kitaplar      |\n"
    menu +="|    4 - Üye Aktif/Pasif Yap                                    |\n"
    menu +="|    5 - Silinmiş Üyeler        0 - Ana Menüye Dön              |\n"
    menu +="|                                                               |\n"
    menu +="-----------------------------------------------------------------\n"
    print(menu)
    while True:
        try:
            print("Üye Menüsü İçim 9 ")
            choice = input("Üye İşlemleri Seçiniz : ")
           
            if choice == "1":
                mt.members_list()
            elif choice == "2":
                mt.members_add()
            elif choice == "3":
                mt.members_search()
            elif choice == "4":
                mt.members_delete()
            elif choice == "5":
                mt.members_deleted()
            elif choice == "6":
                mt.members_boek_give()
            elif choice == "7":
                mt.members_boek_refund()
            elif choice == "8":
                mt.member_boek_list()
            elif choice == "9":
                members_menu()
            elif choice == "0":
                main_menu()
            else:
                print("0-9 arası bir seçim yapınız....")
        except Exception as error:
                print("Bir hata oldu.:",error)

def boek_menu():
        print ("-----------------------------------------------------------------")
        print ("|                      KİTAP İŞLEMLERİ                          |")
        print ("|                                                               |")
        print ("|    1 - Kitap Listesi            5- Emanetteki Kitaplar        |")
        print ("|    2 - Kitap Kaydet                                           |")
        print ("|    3 - Kitap Ara                                              |")
        print ("|    4 - Kitap Sil                0 - Ana Menuye Dön            |")
        print ("|                                                               |")
        print ("-----------------------------------------------------------------")
        
        while True:
            try:
                print("Kitap Menüsü İçim 9 - Ana Menü İçin 0")
                choice = input("Bir İşlem Seçiniz : ")
                if choice == "1":
                    bt.boek_list()
                elif choice == "2":
                     bt.boek_add()
                elif choice == "3":
                     bt.boek_search()
                elif choice == "4":
                     bt.boek_delete()
                elif choice == "5":
                     mt.members_boek_list()
                elif choice == "9":
                     boek_menu()
                elif choice == "0":
                     main_menu()
                else:
                     print("1-2-3-4-9-0 arası bir seçim yapınız....")
            except Exception as error:
                 print("Kitap Menüsünde Bir hata oldu...: ", error)


def main_menu ():
    while True:
        try:
            print ("-----------------------------------------------------------------")
            print ("|              HALK KÜTÜPHANESİNE HOŞGELDİNİZ                   |")
            print ("|                                                               |")
            print ("|                  1 - Üyelik İşelmleri                         |")
            print ("|                  2 - Kitap İşlemleri                          |")
            print ("|                  0 - Çıkış                                    |")
            print ("|                                                               |")
            print ("-----------------------------------------------------------------")
            choice = input("Seçim Yapınız : ")
            if choice == "1":
                members_menu()
            elif choice == "2":
                boek_menu()
            elif choice == "0":
                cikis()
            else:
                print("Lütfen 1-2-3 Giriniz......")
                print("\n")
        except Exception as error:
            print("Hata :", error)



main_menu()