print("\n\t *Ödünç Kitap Alma Sistemi*\t")
dklasik=[["AD","KOD"],
["Suç ve Ceza","100"],
["Sefiller","101"],
["Anna Karenina","102"],
["Vadideki Zambak","103"],
["Notre Dame'ın Kamburu","104"],
["Aşk ve Gurur","105"],
["İlahi Komedya","106"],
["Romeo ve Juliet","107"]]
fantastik=[["AD","KOD"],
["Yerdeniz Büyücüsü","100"],
["Kara Kule","101"],
["Narnia Günlükleri","102"],
["Harry Potter","103"],
["Ozan Beedle'ın Hikayeleri","104"],
["Zaman Çarkı","105"],
["Hobbit","106"],
["Yüzüklerin Efendisi","107"]]
polisiye=[["AD","KOD"],
["Sherlock Holmes","100"],
["Kızıl Nehirler","101"],
["Nam-ı Diğer Grace","102"],
["Doğu Ekspresi’nde Cinayet","103"],
["Morgue Sokağı Cinayetleri","104"],
["Sisle Gelen Yolcu","105"],
["Beyoğlu Rapsodisi","106"],
["Siyah Kan","107"]]
bkurgu=[["AD","KOD"],
["Olasılıksız","100"],
["Mülksüzler","101"],
["Cesur Yeni Dünya","102"],
["1984","103"],
["Fahrenheit 451","104"],
["Denizler Altında Yirmi Bin Fersah","105"],
["Frankenstein","106"],
["Otostopçunun Galaksi Rehberi","107"],]
anamenu=0
sistem=0
liste=[]
while(True):
    def kaydetme(c):
          for i in range(0,10):
              try:
                  if kod==100+i:
                      print(c[i+1][0],"listenize eklenmiştir.\n")
                      liste.append(c[i+1][0])
                      print(liste)
              except:
                  continue
              else:
                  continue
    kartlar=[["sena","k"],["nisa","k"],["mert","e"],["muhammed","e"],["salih","e"],["hülya","k"],["gürkan","e"],["sude","k"],["emirhan","e"],["yeşim","k"]]
    if sistem==0:
        secim=int(input("kartınızı okutun:\n(1-2-3-4-5-6-7-8-9-10) "))-1
        if kartlar[secim][1]=="k":
            print("\nhoş geldiniz",kartlar[secim][0],"hanım\n")
        if kartlar[secim][1]=="e":
            print("\nhoş geldiniz",kartlar[secim][0],"bey\n")
        anamenu=0
    else:
        break
#ana menü
    while(True):
        if anamenu==0 or anamenu==1:
            islem=int(input("""Yapmak istediğiniz işlem:\n
kitap iade için 1'i 
kitap ödünç almak için 2'yi tuşlayın 
sistemden çıkmak için 3’ü tuslayın: \n"""))
            anamenu=2
        if islem==1:
            try:
                if len(liste)>0:
                    for f in range(0,len(liste)):
                        print(f+1,"-",liste[f])
                    kaldırma=int(input("listenizdeki kitaplar bunlardır iade etmek istediğiniz kitabın numarasını tuşlayınız\n"))
                    print(liste[kaldırma-1],"listenizden iade edilmiştir.\n")
                    liste.pop(kaldırma-1)
            except:
                print("Yazdığınız numarada bir kitap bulunmamaktadır ana menüye aktarılıyorsunuz...\n")
            else:
                print("listenizde kitap bulunmamaktadır ana menüye aktarılıyorsunuz...\n")
                tur=0
            
            
        if islem==3:
            print("Sistemden çıkış yaptınız.\n")
            sistem=1
            break
        if islem==2:
            tur=int(input("""Ödünç almak istediğiniz kitabın türünü tuslayın:\n
Dünya klasikleri için 1'i
Fantastik için 2'yi
Polisiye için 3'ü
Bilim kurgu için 4'ü 
Ana menüye dönmek için 0'ı tuşlayınız: \n"""))
        
        if tur==0:
          anamenu=1 
    


        if tur==1:
            for i in range(0,len(dklasik)):
                print(dklasik[i])
            kod=int(input("Ödünç almak istediğiniz kitabın kodunu tuslayın: \n"))
            kaydetme(dklasik)
                     
        if tur==2:
            for i in range(0,len(fantastik)):
                print(fantastik[i])
            kod=int(input("Ödünç almak istediğiniz kitabın kodunu tuslayın: \n"))
            kaydetme(fantastik)
        if tur==3:
            for i in range(0,len(polisiye)):
                print(polisiye[i])
            kod=int(input("Ödünç almak istediğiniz kitabın kodunu tuslayın: \n"))
            kaydetme(polisiye)
        if tur==4:
            for i in range(0,len(bkurgu)):
                print(bkurgu[i])
            kod=int(input("Ödünç almak istediğiniz kitabın kodunu tuslayın: \n"))
            kaydetme(bkurgu)
        
        