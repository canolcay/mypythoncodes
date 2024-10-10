import os

#PYTHON için temel giriş seviyesi örnekler

#Python da konsola yazı yazdırmak
print("Konsola yazı yazdırıldı")

#Python da değişken tanımlamak
#Python değişken türlerini otomatik olarak algılar ve tür bildirmek zorunda değiliz

name = "Mert" #str/String
age = 25 #int
temp = 36.5 #float
isSleep = False #boolean
isAlive = True #boolen

print(name)
print(age)
print(temp)
print(isSleep)
print(isAlive)
#-----------------------------------------------------------------

#Değişken türlerini nasıl yazdırabiliriz?
print(type(name)) #Değişkeni type() içerisine ekleyerek yazdırabiliriz

#-----------------------------------------------------------------

#Değişkenin türünü nasıl değiştirebiliriz?

str(age) #string olarak değiştirmek için str içerisine yaş değişkenini aldık
int(temp) #integer olarak değiştirmek için temp değişkenini int içerisine aldık
#fakat name değişkenini int(name) şeklinde integer olarak değiştiremeyiz, burada hata alırız
#değiştirmeye uygun olan değişkenleri değiştirebiliriz

puan = "65.5"#String bir değer
float(puan)# String bir değer fakat içerisinde gördüğünüz gibi float türüne uygun bir değer barındırıyor
#Burada başarıyla türü değiştirebiliriz

#------------------------------------------------------------------

#Koşullu ifadeler ve koşullar

age = 15
puan = 100

if age >= 18:
    print("Yaşınız ehliyet almak için uygundur")
else:
    print("Yaşınız ehliyet almak için uygun değildir")
    
#Çoklu koşul kullanımı elif

if age > 18:
    print("Yaşınız 18'den büyüktür")
elif age == 18:
    print("Yaşınız tam 18'dir")
    
else:
    print("Yaşınız 18'den küçüktür")
    
# == işareti eğer eşitse sorgusu için kullanılır
# > işareti eğer büyükse sorgusu için kullanılır
# < işareti eğer küçükse sorgusu için kullanılır
# <= işareti küçükse veya eşitse sorgusu için kullanılır
# >= işareti büyükse veya eşitse sorgusu için kullanılır
# != işareti eğer eşit değilse sorgusu için kullanılır
# or kelmesi {veya} sorgusu için kullanılır örnek: age 18 or age 21
# her ikisi ise sorgusu yapmak için {and} kullanılır and ve demektir
#Mantıksal operatörler and,or,not
if age == 15 and puan == 100: #age eğer 15 se ve puan eğer 100 ise
    print("Her iki koşul da doğrudur")
elif not(age==15):
    print("Yaş 15 değildir")

#veya boolean olarak yazdırabiliriz
print(not(age > 5 and age < 18))

#----------------------------------------------------------------------
#Döngüler while ve for

while True: #True değeri değişmeyeceği için bu döngü sonsuza kadar çalışır
    print("Bu bir sonsuz döngüdür")
    
while age <= 90: #age 90dan küçükse veya eşitse döngü çalışmaya devam eder
    print("Hala hayatta")
    age+=1 # age değişkenini her döngüde 1 arttır
    
fruits = ["Elma","Armut","Karpuz","Kavun","Üzüm","Muz"]
#  fruit'i fruits içinden itemler ile eşitle, her döngüde bir meyve ile eşitler
for fruit in fruits:
    print(fruit)
    

#---------------------------------------------------------------
#Fonksiyonlar
def my_function():
    print("Bu bir basit fonksiyondur")
    
#Veri isteyen fonksiyon
def total(puan1,puan2):
    print(puan1+puan2)#toplama işlemi
    return puan1+puan2 # sonucu döndürür, böylece dışarıdan sonuca ulaşabiliriz

#Eğer kaç adet veri vereceğimiz değişiyorsa
def total_all(*puans):
    print(puan[0]+puan[2])
    return puan[0]+puan[2]
#Eğer anahtar kelime ile erişmek istiyorsak sözlük türü isteyebiliriz
def airport_staff(**data):
    print(data["name"])
    print(data["age"])
    print(data["job"])
    
#----------------------------------------------
#Dosya işlemleri
# w dosyadaki verileri siler ve yeni verileri yazar
# a dosyadaki verileri silemeden üzerine ekleme yapar
# x yeni boş bir dosya oluşturur
# r okuma yapmak için dosyayı okuma modunda açar

file1 = open("new_file.txt","w")
file1.write("Yeni veriler yazıldı")
file1.close()

file2 = open("new_file.txt","a")
file2.write("Yeni veriler ekleme yapıldı")
file2.close()

file3 = open("new_file.txt","r")
read = file3.read() 
file3.close()
print(read)

file4 = open("empty_file.txt","x")
file4.close()
print("Boş dosya oluşturuldu")

#Dosya silme
os.remove("new_file.txt")

#Bir dosyanın varlıgını sorgulama
if os.path.exists("new_file.txt"):
    print("Dosya bulundu")
    os.remove("new_file.txt")#isterseniz silin
    
else:
    print("Böyle bir dosya yok!")
    
#Bir dosyanın başka bir kopyasını oluşturalım

os.system('copy new_file.txt new_file2.txt') # dosyayı kopyaladık

#hata yönetimi için try except bloklarını kullanırız

def new_total(sayi1,sayi2):
    try:
        print(sayi1+sayi2)
        
    except:
        print("Vermiş oldugunuz veriler hatalıdır!")
        
    finally:
        print("Fonksiyon çalıştı")
        
new_total(10,26) #dogru sonucu verecek ve başarılı olacak
new_total(15,"80") # hata verecek çünkü 1 değer string
# bu şekilde eğer hata alırsak bir işlem yapabiliriz, böylece program çökmez ve kapanmaz

#freecodecamp - daha iyi ve tavsiye ederim
#udemy - orta seviyeye kadar ilerleyebilirsiniz
#w3school - diğerlerinden ayrı olarak mutlaka kullanın tester ve örnekler anlaşılır
#btkacademy - başlangıç için iyi olabilir

#Basit proje fikirleri
#Sayı bilmece
#Kim milyoner olmak ister
#hesap makinesi
#txt kaydeden bir nor defteri
#okul ortalaması hesaplayan program
#anaktar kelimeye göre personel bilgisi getiren ve bunları txt ye kaydeden basit otomat
#Basit alarm,saat
#Herkese iyi çalışmalar