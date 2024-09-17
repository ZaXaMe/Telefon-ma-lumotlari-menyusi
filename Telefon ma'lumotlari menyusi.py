import random
from abc import ABC, abstractmethod

class Telefon(ABC):
    def __init__(self):
        self.nomi = ""
        self.id = None
        self.fayl_nomi = ""
        self.narx = 0  

    @abstractmethod
    def raqam_kiritish(self):
        pass

    @abstractmethod
    def malumotni_saqlash(self):
        pass

    @abstractmethod
    def idni_korish(self):
        pass

    def narx_qoyish(self, narx):
        self.narx = narx
        try:
         print(f"Telefonning narxi {narx} so'mga o'rnatildi.")

        except ValueError:
            print("XATO!")

    def narxini_korish(self):
        print(f"Telefonning narxi: {self.narx} so'm")

class Iphone(Telefon):
    def __init__(self):
        super().__init__()
        self.fayl_nomi = "iphone_ma'lumotlari.txt"
    
    def raqam_kiritish(self):
        self.nomi =Iphone
        self.id = random.randint(1000, 9999)
        self.malumotni_saqlash()

    def malumotni_saqlash(self):
        with open(self.fayl_nomi, 'w') as fayl:
            fayl.write(f"Telefon nomi: {self.nomi}\n")
            fayl.write(f"ID: {self.id}\n")
        print("Iphone ma'lumotlari saqlandi!")

    def idni_korish(self):
        try:
            with open(self.fayl_nomi, 'r') as fayl:
                malumotlar = fayl.read()
                print("Iphone uchun fayldan o'qilgan ma'lumotlar:")
                print(malumotlar)
        except FileNotFoundError:
            print("Iphone ma'lumotlar fayli topilmadi. Avval telefon nomini kiritishingiz kerak.")

class Samsung(Telefon):
    def __init__(self):
        super().__init__()
        self.fayl_nomi = "samsung_ma'lumotlari.txt"
    
    def raqam_kiritish(self):
        self.nomi = Samsung
        self.id = random.randint(1000, 9999)
        self.malumotni_saqlash()

    def malumotni_saqlash(self):
        with open(self.fayl_nomi, 'w') as fayl:
            fayl.write(f"Telefon nomi: {self.nomi}\n")
            fayl.write(f"ID: {self.id}\n")
        print("Samsung ma'lumotlari saqlandi!")

    def idni_korish(self):
        try:
            with open(self.fayl_nomi, 'r') as fayl:
                malumotlar = fayl.read()
                print("Samsung uchun fayldan o'qilgan ma'lumotlar:")
                print(malumotlar)
        except FileNotFoundError:
            print("Samsung ma'lumotlar fayli topilmadi. Avval telefon nomini kiritishingiz kerak.")

def yangi_telefon_yaratish(telefon_nomi):
    fayl_nomi = f"{telefon_nomi.lower()}_ma'lumotlari.txt"
    
    def init(self):
        super(type(self), self).__init__()
        self.fayl_nomi = fayl_nomi

    def raqam_kiritish(self):
        self.nomi = {telefon_nomi}
        self.id = random.randint(1000, 9999)
        self.malumotni_saqlash()

    def malumotni_saqlash(self):
        with open(self.fayl_nomi, 'w') as fayl:
            fayl.write("Telefon nomi: {self.nomi}\n")
            fayl.write(f"ID: {self.id}\n")
        print(f"{telefon_nomi} ma'lumotlari saqlandi!")

    def idni_korish(self):
        try:
            with open(self.fayl_nomi, 'r') as fayl:
                malumotlar = fayl.read()
                print(f"{telefon_nomi} uchun fayldan o'qilgan ma'lumotlar:")
                print(malumotlar)
        except FileNotFoundError:
            print(f"{telefon_nomi} ma'lumotlar fayli topilmadi. Avval telefon nomini kiritishingiz kerak.")
    
    yangi_klass = type(
        telefon_nomi,
        (Telefon,),
        {
            '__init__': init,
            'raqam_kiritish': raqam_kiritish,
            'malumotni_saqlash': malumotni_saqlash,
            'idni_korish': idni_korish,
        }
    )
    
    return yangi_klass

telefonlar = {}

def fayldan_telefon_malumotlarini_korish(fayl_nomi, telefon_turi):
    try:
        with open(fayl_nomi, 'r') as fayl:
            malumotlar = fayl.read()
            print(f"{telefon_turi} uchun fayldan o'qilgan ma'lumotlar:")
            print(malumotlar)

    except FileNotFoundError:
        print(f"{telefon_turi} ma'lumotlar fayli topilmadi.")

def menyu():
    while True:
        print("\nMenyu:")
        print("0. Chiqish")
        print("1. Telefon qo'shish")
        print("2. Telefonlarni ko'rish")
        print("3. Telefon (ID bo'yicha) ustida amallar bajarish")
        tanlov = input("Tanlovingizni kiriting: ")

        if tanlov == '0':
            break
        elif tanlov == '1':
            telefon_nomi = input("Yangi telefon nomini kiriting: ")
            YangiTelefon = yangi_telefon_yaratish(telefon_nomi)
            yangi_telefon = YangiTelefon()
            yangi_telefon.raqam_kiritish()
            telefonlar[yangi_telefon.id] = yangi_telefon
        elif tanlov == '2':

            print("\nTelefonlar ro'yxati:")
            fayldan_telefon_malumotlarini_korish("iphone_ma'lumotlari.txt", "Iphone")
            fayldan_telefon_malumotlarini_korish("samsung_ma'lumotlari.txt", "Samsung")
            if telefonlar:
                print("Telefonlar ro'yxati:")
                for id, telefon in telefonlar.items():
                    print(f"ID: {id}, Telefon nomi: {telefon.__class__.__name__}")
            else:
                print("Telefonlar ro'yxati bo'sh.")
        elif tanlov == '3':
            id_kiritish = int(input("Telefonning ID'sini kiriting: "))
            if id_kiritish in telefonlar:
                tanlangan_telefon = telefonlar[id_kiritish]
                print(f"{tanlangan_telefon.__class__.__name__} uchun quyidagi amallarni tanlang:")
                print("1. ID'sini ko'rish")
                print("2. Narx qo'yish")
                print("3. Narxini ko'rish")
                amal = input("Amalni tanlang: ")

                if amal == '1':
                    tanlangan_telefon.idni_korish()
                elif amal == '2':
                    narx = int(input("Telefonning narxini kiriting: "))
                    tanlangan_telefon.narx_qoyish(narx)
                elif amal == '3':
                    tanlangan_telefon.narxini_korish()
                else:
                    print("Noto'g'ri tanlov!")
            else:
                print("Berilgan ID bo'yicha telefon topilmadi.")
        else:
            print("Noto'g'ri tanlov!")


menyu()
