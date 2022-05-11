import sqlite3 as sqlite
print("** İsim alanı boş bırakılırsa programdan çıkılır **\n")
db = sqlite.connect("kayit.db")
cs = db.cursor() #cursor ==> işlem yapabilmek için kullanılır
#cs.execute("create table Students (id integer primary key autoincrement, name, surname, department, number)")
def tablo():
    cs.execute("select count(*) from Students")
    count = cs.fetchone()
    print("{} tane öğrenci kayıtlı".format(count[0]))
    cs.execute("select * from Students ")
    dataSet = cs.fetchall() # execute metodundan seçilen datayı al ve değişkene ata
    for data in dataSet: # verileri  seçip ekrana yazar 
        print(data,"\n")
tablo()

while True:
    print("Tabloya veri eklemek için ekle, tablodan veri silmek için sil yazabilirsiniz..\n")
    secim = input("Ekle/Sil: ")
    if secim == 'Ekle':
        name = input("Enter your name: ")
        if name == "":
            tablo()
            break
        surname = input("Enter your surname: ")
        department = input("Enter your department: ")
        number = input("Enter your number: ")
        cs.execute("insert into Students values(null,?,?,?,?)",(name,surname,department,number))
    elif secim =='Sil':
        sil = input("Silmek istediğiniz id'yi giriniz: ")
        cs.execute("delete from Students where id = ?",[sil]) 
    db.commit() #commit ==> veriyi veri tabanına işlemeyi sağlar
    tablo()
db.close()

   





