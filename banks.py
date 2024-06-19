print("Crew Bank'a Hoş Geldiniz!")

password = 1234
bakiye = 1000
cüzdan = 5000
gonderilecek_iban = int(input("Lütfen veriye kayıt edilecek IBAN belirtin: "))
iban_para = 1000

giris = int(input("Şifre: "))
if giris == password:
    print("İşlemler:\n1: Para Yatırma\n2: Para Çekme\n3: Bakiye Sorgulama\n4: IBAN'a Transfer")
    islem = int(input("İşlem: "))
    
    if islem == 1:
        yatiralacak_miktar = int(input("Yatırılacak Miktar: "))
        
        if yatiralacak_miktar >= cüzdan:
            print("Cüzdan da bu kadar para yok!")
        else:
            bakiyeniz = bakiye + yatiralacak_miktar
            cuzdaniniz = cüzdan - yatiralacak_miktar
            print("Başarılı bir şekilde para yatırıldı.")
            print("Güncel bakiyeniz: {0} | Yatırılan Para: {1} | Cüzdanınız: {2}".format(bakiyeniz, yatiralacak_miktar, cuzdaniniz))
    elif islem == 2:
        cekilecek_miktar = int(input("Çekilecek Miktar: "))
        
        if cekilecek_miktar >= bakiye:
            print("Hesap bakiyeniz'de bu miktarda para bulunamamaktadır.")
        else:
            bakiyeniz = bakiye - cekilecek_miktar
            cuzdaniniz = cüzdan + cekilecek_miktar
            print("Başarılı bir şekilde para çekildi!")
            print("Güncel Bakiyeniz: {0} | Çekilen Para: {1} | Cüzdanınız: {2}".format(bakiyeniz, cekilecek_miktar, cuzdaniniz))    
    elif islem == 3:
        bakiyeniz = bakiye
        print("Bakiyeniz: {0}".format(bakiyeniz))
    elif islem == 4:
        iban = int(input("IBAN: "))
        
        if iban == gonderilecek_iban:
            gonderilecek_miktar = int(input("Ne kadar göndermek istiyorsunuz: "))
            
            if gonderilecek_miktar >= bakiye:
                print("Maalesef, hesabınızda bu kadar para bulunmamaktadır.")
            else:
                gonderildi_para = gonderilecek_miktar + iban_para
                guncel_paraniz = bakiye - gonderilecek_miktar
                print("Başarılı bir şekilde iban'a para gönderildi!\nGönderilen IBAN: TR{0}".format(gonderilecek_iban))
                print("Hesap Bakiyeniz: {0} | Gönderilen Para: {1} | Hesap Parası: {2}".format(guncel_paraniz, gonderilecek_miktar, gonderildi_para))
        else:
            print("Geçersiz iban belirtiniz.")
else:
    print("Geçersiz işlem belirtiniz.")
