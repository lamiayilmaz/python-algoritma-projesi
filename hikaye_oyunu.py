# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:52:09 2024

@author: Lamia Yılmaz
"""
inventory=[]

from time import sleep
import sys

def write(x):
    for i in x:
        print(i)
        sleep(2)
        
def option_1(x):
    write(x)
    return input("KARARIN:").upper()
    option_1()

   
entry=["HİKAYE OLUŞTURMA OYUNUNA HOŞGELDİNİZ",
       "KISACA OYUNDA NE YAPMANIZ GEREKTİĞİNDEN BAHSEDELİM:",
       "OYUNUMUZ ADINI BELİRLEYECEĞİNİZ BİR KARAKTERİ VE KÖPEĞİNİ İÇERMEKTEDİR",
       "SEÇİMLER YAPARAK HİKAYENİN GİDİŞATINI BELİRLERSİNİZ",
       "FAKAT YAPTIĞINIZ SEÇİMDEN GERİ DÖNEMEZSİNİZ",
       "ANCAK BU İSTİSNALAR OLMAYACAĞI ANLAMINA GELMEZ",
       "SEÇİM SİZİ KENDİSİNİ SEÇMEYE ZORLAYABİLİR",
       "YAPTIĞINIZ SEÇİMLER İLE OYUNUN NASIL BİTECEĞİ SİZİN ELİNİZDE",
       "İYİ OYUNLAR DİLERİZ..."] 

write(entry)

personal_information={}
        
story_1=["-Diğer günlerden hiçbir farkı olmayan bir gündü.",
         "-Orman kuş cıvıltıları ile dolup taşıyor",
         "-Güneş ışığı ağaçlar arasından ormana ulaşıyordu..."]

write(story_1)

gender=input("\nKarakterinizin cinsiyetini belirleyiniz:")
personal_information["cinsiyet"]=gender

player_name=input("\nKarakterinizin adını giriniz:")
personal_information["oyuncu adı"]=player_name   

        
story_2=["-"+player_name + " her zamanki gibi ağaçlar arasına kurduğu her zamanki hamağında yatıyor",
        "-Her zamanki yemeğini yemek için yemek vaktini bekliyordu.",
        "-Çok tembeldi,yalnızca yemek yemek için kalkardı",
        "-Ve hayatından çok memnundu..."]
      
write(story_2)

dog_name=input("\nKöpeğinizin adını giriniz:")
personal_information["köpek adı"]=dog_name

        
story_3=["-Yemek vakti geldiği zaman köpeği " + dog_name+" onu uyandırırdı",
        "-Fakat köpeği normal bir köpek değildi.",
        "-Konuşabiliyordu,hiç susmazdı ya ağlar ya da konuşurdu",
        "-Sürekli şikayet edecek bir şey bulurdu",
        "-Özellikle " + player_name+" ile geçirdiği hayatın",
        "-Her zamanki gibi olmasından şikayet ederdi.",
        "-Fakat gidecek hiçbir yeri olmadığı için",
        "-Her zamanki hayata katlanıyordu",
        "-"+player_name + " onu yavruyken bulmuştu",
        "-Her zamanki uykusundan onu bir ağlama sesi uyandırmış",
        "-Kalkıp bu sesin nereden geldiğine bakmıştı.",
        "-Her zamanki uykusuna devam edebilsin diye",
        "-Ona evini açmış ve yemek vermişti.",
        "-Uykusu onun için çok önemliydi..."]           

write(story_3)
    

story_4=["-"+dog_name+" yemeği hazırlayıp "+player_name+"'i uykusundan uyandırdı",
            dog_name+":(Sinirli bir şekilde)Kalk artık!",
            player_name+":------",
            player_name+":Yemekte ne var?",
            dog_name+":Bir de soruyor musun!Her zamanki tavşan eti işte ne olacak başka",
            "(Mokurdanmaya devam eder)",
            player_name+":(Kokuyu içine çeker)Nefis kokuyor",
            dog_name+":Elbette güzel kokacak!",
            dog_name+":(Sinirli bir şekilde)Her gün bunu pişirmek için ne kadar çaba sarf ettiğimi biliyor musun sen?",
            player_name+":(Bıkkın bir şekilde)Alt tarafı ızgara yapıyorsun.",
            dog_name+":Alt tarafı ızgara mı!",
            dog_name+":Bir kere de sen pişir de görelim bakalım kolay mı değil mi?",
            dog_name+":Lanet olsun!Zaten bu tavşanları yakalamak için yeterince çabalıyorum",
            dog_name+":Bir kere de sen uğraşsan ne olur?",
            player_name+":Yemeğini ye soğuyacak",
            dog_name+":Kapa çeneni,bıktım bu hayattan,her şeyden bıktım",
            dog_name+":Sürekli aynı şeyleri yapmaktan bıktım",
            dog_name+":Bu ormandan bıktım,tavşan eti yemekten bıktım",
            dog_name+":Kalacak başka yerim olsa buralarda kalır mıyım sanıyorsun ha?",
            dog_name+":Lanet olsun yalnızca heyecanlı bir hayat istiyorum.",
            dog_name+":(Ağlayarak)Çok mu şey istiyo---",
            "Derken bir anda kırmızı bir ejderha "+player_name+"'i alıp kaçırır"]       
write(story_4)       
        
choise_1=["-----------------SEÇİM VAKTİİİİİ-----------------",
          "A-)Ejderhayı takip edip "+dog_name+"'i kurtar",
          "B-)"+dog_name+" için dua et",
          "C-)Hiçbir şey yapmayıp her zamanki hayatına devam et"]
answer=option_1(choise_1)
  
while True:
    if (answer =='A'):
        answer_A=["-Doğru yoldasın oyuncu",
                  "-Dostuna sadakatin gözlerimi yaşarttı..."]
        write(answer_A)
        break
    elif (answer =='B'):
        answer_B=[player_name+":Oh,elimden geleni yaptığıma göre her zamanki hayatıma geri dönebilirim.",
                 "-Gitmen gerek",
                 player_name+":Ne?",
                 "-(Sinirli bir şekilde)GİTMEN GEREK,GİDİP ONU KURTARMAN GEREK!",
                 player_name+":Bu ses nereden geliyor yaa?",
                 "-Sesin kaynağı önemli değil,şimdi git ve onu kurtar hadi yallah."]
        write(answer_B)
        break
    elif (answer =='C'):
        answer_C=[player_name+":Tüh...",
                  "-Bu mu yani?",
                  player_name+":Ne?",
                  "-Bir hikaye anlatmam gerektiğinin farkındasın öyle değil mi?",
                  player_name+":Bu ses nereden geliyor be?",
                  "-(Sinirli bir şekilde)Sesin kaynağı önemli değil,şimdi git ve bana anlatabileceğim bir hikaye ver!"]
        write(answer_C)
        break
    else:
        print("Hikayeye devam etmek istiyorsan verilen seçeneklerden birini seçmen lazım dostum")
        answer=input("KARARIN:").upper()
        
    
story_5=[player_name+":(Esner)Neyse,yemeğimi yiyip "+dog_name+"'i aramaya koyulayım bari...",
        "-Derken o da ne?Kahramanımız yemeklerin etrafa saçılmış olduğunu fark eder.",
        "-Ne yazık...",
        player_name+":(Sinirli bir şekilde)Kahretsin!O ejderha "+dog_name+"'i kaçırırken yemeğimi de dökmüş.",
        player_name+":Tanrım!En sevdiğim iki şeyi elimden almak zorunda mıydın sanki ha?",
        player_name+":(Üzgün bir şekilde)Yemeğim de gitti,uykum da kaçtı...",
        player_name+":(Karnı guruldar)Her neyse "+dog_name+"'i kurtarmalıyım,evet.",
        player_name+":Onu o pis ejderhanın ellerinden kurtarıp eve getirmeliyim ki ona yemek yaptırıp her zamanki hayatıma devam edebileyim...",
        "-Ve böylece kahramanımız yola çıkar ancak bu yolda onu çeşitli sürprizler beklemektedir.",
        "-Bakalım kahramanımız bu zorluklarla nasıl mücadele edecek",
        "-Ve o çok sevdiği her zamanki hayatına kavuşabilecek mi?",
        player_name+" oflayarak yola çıkar fakat avanak karakterimizin karnı o kadar açtır ki",
        "Kafasını çalıştıramayıp yanına hiçbir şey almamıştır",
        "(Anlatıcı derin bir nefes alır)",
        "Zaten karnı tok olduğunda bile kafası çalışmayan birinin",
        "Aç olduğunda akıllıca hareket etmesini bekleyemeyiz ya",
        "(gülümseyerek devam eder) ama merak etmeyin sevgili dostlar...",
        "Güzel anlatıcınız onun önüne birkaç malzeme yağdırır ♥",
        "Kahramanımızın önüne gökyüzünden 3 tane cisim düşer.",
        player_name+":(irkilerek)Neler oluyor böyle?",
        player_name+":Ne zamandan beri gökten cisim yağmaya başladı?",
        "(anlamaya çalışır)",
        player_name+":Bunlar da ne böyle?",
        "Ve karşısında tadaa büyülü bir ok, satranç oyunu ve bir yastık vardır",
        "-Merhaba oyuncu, ben oyun kurucuyum",
        "-Ve baktım ki yolculuğunda çok kıymetli dostunu kurtarmak için yanına hiçbir şey almamışsın",
        "-Cık cık cık cık...",
        "-Ben de sana acıdığım için yardım etmeye karar verdim",
        "-Ama elbette şartlarım var:",
        "-Birincisi önündekilerden yalnızca bir eşya seçme hakkın var",
        "-Ve ikincisi yani sonuncusu",
        "-Seçim yaptıktan sonra seçiminden geri dönemezsin.",
        "-Şimdi seçimini yap ve bize akıllı olduğunu göster oyuncu..."]
write(story_5)

choise_2=["-----------------SEÇİM VAKTİİİİİ-----------------",
           "A-)Büyülü ok:Ne kadar kötü bir atıcı olursan ol,büyülü oku çekip nereye isabet etmesi gerektiğini söylemen yeterli!",
           "B-)Satranç oyunu:Güzel bir strateji oyunu,onu nasıl kullanacağın sana kalmış...",
           "C-)Yastık:...Bunun burada ne işi var?"]
answer_2=option_1(choise_2)

while True:
    if (answer_2=="A"):
        print("-Güzel seçim oyuncu,şimdi yoluna devam edebilirsin...")
        inventory.append("Büyülü ok")
        break
    elif(answer_2=="B"):
        print("\n-Kötü bir seçim sayılmaz...Umarım en azından taşların adını biliyorsundur.")
        inventory.append("Satranç oyunu")
        break
    elif(answer_2=="C"):
        print("\n-Bir dakika...Benim yastığımın burada ne işi var?Hayır!Ben ne yaptım böyle,bunun bir seçenek olmaması gerekiyordu.Kahretsin!")
        inventory.append("Yastık")
        break
    else:
        print("Hikayeye devam etmek istiyorsan verilen seçeneklerden birini seçmen lazım dostum")
        choice_2=input("KARARIN:").upper()


    
story_6=["Oyuncu, yoluna karnı aç ve uykulu bir şekilde devam eder.",
        "Güneş ağaçların arasından son ışıklarını ormana göndermektedir,",
        "Hava yavaşça kararmaya başlamıştır,",
        "Kuş sesleri git gide azalır ve ormanın sakinleri yuvalarına çekilir",
        "Gece yırtıcılarındır.",
        "Oyuncumuz baykuş sesleri ile gecenin karanlığında yoluna devam eder",
        "ve birisinin karşısına çıkmasını ve ejderhanın nereye gittiğini bilmesini ümit eder",
        "fakat etrafta tüyler ürpertici çalı hışırtılarından başka bir şey yoktur.",
        "Oyuncumuz karanlıkta tek başına ilerlemeye devam ederken aniden çalıların arasından bir silüet kendini gösterir.",
        "Oyuncu ne olduğunu anlamak için dikkatlice bakar.",
        player_name+":Vay canına...Kaç yıldır ormanda yaşamama rağmen hiç bir kurdu bu kadar yakından görme fırsatı yakalamamıştım.",
        "En iyisi gidip benim için yiyeceği olup olmadığını sorayım...",
        "Kurda yavaşça yaklaşır, sürüsünün nerede olduğuna bakmak için gözleriyle etrafı tarar.",
        player_name+":Bu garip, sürüden ayrı olması normal değil.",
        player_name+"Hikayesi ne acaba?Bence biraz dinlenmeyi hak ettim.",
        "Der ve kurt ile konuşmak için yanına gider",
        "Kurdun yanına yaklaştıkça kurdun ondan çekinmediğini",
        "ve herhangi bir saldırganlık ifadesi göstermediğini fark eder",
        "birkaç adım kala durur.",
        "Gözgözedirler...",
        player_name+":Merhaba.",
        "Beyaz diş:Git buradan insan.Beni rahat bırak.",
        player_name+":Tanrım bu kadar yabani olma, sana sormam gerekenler var",
        player_name+":Sonra hemen gideceğim...",
        "Beyaz diş:Beni ilgilendirmez, git buradan.",      
        "Derken ormandan eli tüfekli bir adam çıkagelir",
        "Oldukça sinirlidir ve hırslı bir şekilde etrafını tarıyordur.",
        "-Adam:İşte orada buldum seni!",
        "Kurt hırlar.",
        player_name+":Neler oluyor?",
        "Adam:Sen karışma ve hemen çekil oradan, her yerde o köpeği arıyorum.",
        "Adam:Bir kere işe yarasan ne olursu sanki ha? Benimle birlikte eve geliyorsun!"]   
write(story_6)
            
choise_3=["-----------------SEÇİM VAKTİİİİİ-----------------",
          "A-)Tüfeğini alıp onu ağaca bağla", 
          "B-)Onu ikna etmeye çalış",
          "C-)Köpeğin önünden çekil"]   
answer_3=option_1(choise_3)


while True:
    if answer_3=="A":
        answerA=["Adam:Neler oluyor?",
                 player_name+":Üzgünüm dostum ama kurda benim ihtiyacım var...",
                 "Beyaz Diş:Bunu neden yaptın?",
                 player_name+":Çünkü açım, şimdi beni dinleyecek misin?",
                 "Beyaz Diş:Sana minnettarım insan, bundan sonra gücüm ve sadakatim seninle.",
                 player_name+":Güzel...Sadakatini sevdim, hikayemi paylaşmak isterim ama önce lütfen yemek yiyelim, sabahtan beri ağzıma bir lokma girmedi."]
        write(answerA)
        break
    elif answer_3=="B":
        answerB=[player_name+":Bak dostum, köpekle ne derdin var bilmiyorum ama karnım açken benimle kavga etmek istemezsin.",
                 "Adam:Bana ne lan senin karnının açlığından.",
                 "-Derken kahramanımız adamın suratına sert bir yumruk indirir.",
                 player_name+":Sana beni sinir etme demiştim! Gel köpek ya da kurt her ne isen, bundan sonra benimlesin tabii öncelikle bana yemek bulma şartı ile..."]
        write(answerB)
        break
    elif answer_3=="C":
        print("Oyuncu yavaşça Beyaz Diş'in önünden çekilir ve adam köpekle birlikte gözden kaybolur...")
        bad_choise=["Köpek ile adam oradan uzaklaşırlar",
                    "Köpek inatlaştıkça adam onu tüfeğiyle korkutmaktadır.",
                    player_name+" onların uzaklaşıp gözden kaybolmalarını izler...",
                    player_name+":Doğru bir seçim yaptım.Evet doğru bir seçim...",
                    player_name+" karnı aç bir şekilde güneş doğarken yoluna koyulur",
                    "yol uzadıkça uzar, kimse ile karşılaşmaz, açlıktan bitkin düşmüş haldedir.",
                    "Bir ağacın altına oturur ve düşünür",
                    player_name+":Nerede hata yapıyorum?",
                    "Derken etrafını kurt sürüsü sarar, daha kaçmaya vakit bulamadan player_name'i yakalarlar ve",
                    "Sanırım yanlış seçimdi ha?"]
        write(bad_choise)
        
        last_choise=["-----------------SON ŞANS-----------------",
                     "Peki son bir şans ister misin?",
                     "A-)Evet",
                     "B-)Hayır"]
        last=option_1(last_choise)
        
        if last=='A':
            choise_3=["-----------------SEÇİM VAKTİİİİİ-----------------",
                      "A-)Tüfeğini alıp onu ağaca bağla", 
                      "B-)Onu ikna etmeye çalış",
                      "C-)Köpeğin önünden çekil"]  
            answer_3=option_1(choise_3)
        elif last=='B':
            print("Oyunu kaybettin ve hepsi senin hatan")
            sys.exit()
        else:
            print("---Hikayeye devam etmek istiyorsan verilen seçeneklerden birini seçmen lazım dostum---")
            answer_3=input("KARARIN:")
    else:
        print("---Hikayeye devam etmek istiyorsan verilen seçeneklerden birini seçmen lazım dostum---")
        answer_3=input("KARARIN:")
        
story_7=["Beyaz Diş:Dile benden ne dilersen.",
         "Der ve "+player_name+"'e tavşan yakalar",
         "Birlikte pişirip yedikleri sırada...",
         player_name+":İşte böyle, bu yüzden sabahtan beri yollardayım",
         player_name+"Peki ya senin hikayen ne?",
         "Beyaz Diş:O adam, kendini benim sahibim sanıyor.",
         "Beyaz Diş:Onun himayesi altındayken bir dövüş köpeğiydim",
         "Beyaz Diş:çok zarar görüyordum, inatlaşıyordum ve cezalandırılıyordum",
         "Beyaz Diş:bu yüzden ben de özgürlüğüm için kaçtım...",
         player_name+":Ama sıradan bir köpeğe benzemiyorsun",
         player_name+":Seni ilk gördüğümde bir kurt sanmıştım",
         "Beyaz Diş:Normaldir, çünkü ben kurt köpeğiyim",
         "Beyaz Diş:İki türün de özelliklerini taşıyorum.",
         player_name+":Vay canına, bunu ilk defa duyuyorum.",
         player_name+":Benim köpeğim de köpek kılığına girmiş bir insan gibi",
         player_name+":Ama zamanının çoğunu şikayet ederek ve ağlayarak geçiriyor",
         player_name+":Yine de onunla olan hayatımdan memnunum o pek öyle düşünmese de...",
         player_name+":Aman Allah'ım onun şikayet etmesini bile özlemişim...",
         "Beyaz Diş:E ne duruyoruz o zaman, vakit kaybetmeden yola koyulalım!",
         "-Kahramanlarımız güneş doğarken yollarına devam ederler... "]
write(story_7)

story_8=[player_name+":Bir dakika onu nasıl bulacağız?",
         "Beyaz Diş:Elinde onun kokusuna sahip bir eşyan var mı?",
         player_name+":Evet onun her zaman ağlamak için kullandığı mendili yanımda",
         "Beyaz Diş:Güzel, onun kokusundan yararlanarak yolumuzu bulabiliriz.",
         "Koku kahramanlarımızı ormanın en karanlık yerine götürür.",
         "Kocaman ve karanlık bir mağaranın girişinde dururlar.",
         player_name+":Kokunun buradan geldiğine emin misin?",
         player_name+":(Gergin bir şekilde)Lütfen yanlış almış ol",
         "Beyaz Diş:Hayır, kokunun buradan geldiğine eminim",
         "Beyaz Diş:Korkmanın sırası değil, hadi içeri girelim."
         "Kahramanlarımız içeri girerler.",
         "İçerisi kapkaranlık, sıcak ve boğucudur",
         "Aydınlığın geldiği tarafa doğru ilerlerler.",
         "Ve ejderha karşılarındadır.",
         dog_name+" ise hemen yanında korkudan titremektedir.",
         "Kan ter içinde kalmıştır zavallıcık...",
         dog_name+":(Kızgın bir şekilde)Sen nerelerdesin ha?",
         dog_name+":Dünden beri senin gelmeni bekliyorum",
         dog_name+":Bu yanındaki de kim?",
         dog_name+":Yokluğumda yerime hemen başka hizmetçi buldun ha?",
         dog_name+":Benimkinden daha iyi tavşan eti pişirebiliyor mu bari?",
         player_name+":Ne saçmalıyorsun "+dog_name+" senin yerine birini bulmadım tabiki de",
         player_name+":Buraya gelene kadar bana o yardımcı oldu, teşekkür etmen lazım",
         player_name+":Ama seninkinden daha iyi pişirdiği doğru",
         dog_name+":(Bağırarak)Benim sinirimi bozma!",
         "Ejderha:(Ellerini kavuşturarak)Ben de sizi bekliyordum",
         player_name+":Bizi mi?",
         "Ejderha:Evet, sizi.",
         player_name+":İki kişi geleceğimizi de nereden bildin?",
         "Ejderha:Yalnızca iki kişi olduğunuzu değil senin hakkında her şeyi de biliyorum.",
         player_name+":Nasıl yani?",
         "Ejderha:Bak şöyle"]
write(story_8)

print(personal_information)

story_9=[player_name+":(Şaşırmış bir şekilde)Bunları nereden biliyorsun?",
         "Ejderha:Endişelenmen gereken konu bu değil",
         "Ejderha:Şimdi asıl konumuza gelelim.",
         "Ejderha:"+dog_name+"'i sana kolay kolay vermeyeceğim",
         "Ejderha:Bana onu hak ettiğini kanıtlamalısın.",
         dog_name+":Evet, kanıtlamalısın",
         "Ejderha:Beni nasıl yeneceğini seç bakalım."]
write(story_9)

if answer_2=='A':
    büyülü_ok=[player_name+":Seni bununla yeneceğim.",
               "Ejderha:Onu nereye atman gerektiğini bulamazsın",
               player_name+":Bana kendi ellerinle koz veriyorsun",
               "Kahramanımız tek tek denemektedir",
               "Ama nereye atarsa atsın ejderha etkilenmemektedir",
               "Ve ejderhanın ateşinden kaçmak zorlaşmaktadır",
               player_name+":Kahretsin az daha kalsın yanıyordum",
               "Beyaz Diş:(Bağırır)Onu görüyorum",
               player_name+":Bana nerede olduğunu söyle",
               "Beyaz Diş:(Bağırır)Tam sol göğsünde zırhında bir boşluk var",
               dog_name+":(Bağırır)Evet, tam orada yapabilirsin "+player_name,
               player_name+":(Oku çekip bağırır)Sol göğse git",
               "-Ve BOOOM ejderha yere yığılır",
               "Beyaz Diş:Başardık!",
               dog_name+":(Mutluluktan ağlar,hıçkırarak)Artık eve gidelim",
               player_name+":(Gülümseyerek)Hadi gidelim",
               ]
    write(büyülü_ok)
elif answer_2=='B':
    satranç=[player_name+":Satranca ne dersin?",
             "Ejderha:(Ellerini çırparak)Ay sen ciddi misin?",
             "Ejderha:Bayılırım satranca",
             "Ejderha:(Sırıtarak)Ama kazanırsam köpek benim",
             player_name+":(Yutkunarak)Tamam",
             "Beyaz Diş:Satranç oynamayı bilmen iyi oldu.",
             player_name+":Taşların yerini biliyorum, satranç oynamayı değil.",
             "Beyaz Diş:Ne?O zaman neden en başında teklif ettin?",
             player_name+":Kim bir ejderhanın satranç oynamayı bildiğini düşünebilirdi ki?",
             "Beyaz Diş:Köpeğinin hayatını nasıl tehlikeye attığının farkında mısın?",
             "Beyaz Diş:Neyse tamam, ben sana yardımcı olacağım.",
             player_name+":Nasıl yani, sen oynamayı biliyor musun?",
             "Beyaz Diş:O adam sürekli oynardı, ben de izlerdim.",
             player_name+":Vay canına! Bilmen çok işimize yarayacak.",
             "Ejderha ve player_name sırasıyla satranç taşlarını dizerler",
             "Ejderha hamleleri söylemekte "+dog_name+" ise taşları onun yerine oynatmaktadır",
             "Bizimkilerde ise Beyaz Diş hamleleri fısıldamakta "+player_name+" ise taşları oynatmaktadır.",
             "Oyun çok çekişmeli geçer.",
             "Derken Beyaz Diş yanlış hamle yaptıklarını son anda fark eder.",
             "Ejderha sırıtır.",
             player_name+" ve Beyaz Diş boncuk boncuk terlerler.",
             "Derken aniden "+dog_name+" yerinden fırlar",
             dog_name+":Aaaaaaaa!",
             player_name+":Ne oldu?"
             "Beyaz Diş:""("+player_name+"'e Fısıldayarak)Bekle",
             "Ejderha:(Şaşırarak)Neler oluyor?",
             dog_name+":(Bağırarak)Bir şey var!Üstümde bir şey var!",
             "Ejderha:Ya Rabbi!Kız buraya gel bakıyım",
             "-"+dog_name+" mağara etrafında koşuşturur",
             "Beyaz Diş:Farkında değil misin?",
             "Beyaz Diş:Bizim için yapıyor",
             "Beyaz Diş:Şunların yerlerini değiştirelim...",
             "-Beyaz Diş taşların yerlerini değiştirir.",
             "Ejderha ile "+dog_name+" geri gelirler.",
             dog_name+" değiştirdiklerini umarak "+player_name+" ile Beyaz Diş'e bakar",
             player_name+" onaylar biçimde kafasını sallar.",
             "Ejderha önceden belirlemiş olduğu hamlesini yaptırır.",
             "Ejderha:Ha?Bunun böyle olmaması gerekiyordu",
             player_name+":Şah ve mat",
             dog_name+":(Ağlayarak)Sonundaaaa",
             "Ejderha:(Şaşırarak)Bunun böyle olmaması gerekiyordu",
             "Beyaz Diş:(Rahatlayarak)Ohh",
             player_name+":Hadi evimize gidelim",
             dog_name+":(Duygulu bir şekilde)Gidelim",
             "Ejderha:(Üzgün bir şekilde)Sen kazandın, arkadaşının değerini bil",
             "Ejderha:Görüşürüz köpekçik",
             dog_name+":Hırrrrr"]
    write(satranç)                
elif answer_2=='C':
   yastık=[player_name+":Ben bununla ne yapacağım?",
           dog_name+":(Sinirli bir şekilde bağırır)Beni kurtarmak için bir yastık mı getirdin!?"
           "Beyaz Diş:Sen gerçekten bunu niye getirdin?",
           player_name+":Ben bunu seçtim...",
           "Beyaz Diş:Nasıl yani?",
           player_name+":Gökten üç malzeme düştü ve ben bunu seçtim...",
           "Beyaz Diş:(Derin bir nefes alarak)Bana diğer iki eşyanın ne olduğunu söyle.",
           player_name+":(Yutkunarak)Büyülü ok ve satranç...",
           "Beyaz Diş:(Sinirli bir şekilde)Tanrım senin derdin ne!?",
           dog_name+":("+player_name+"'in ayaklarına vurarak)Bir de seçtin ha?Bir de seçtin haa!?"
           "Beyaz Diş:(Bağırarak)Bunca eşya arasından niye yastık lan!?Niye yastık?",
           player_name+":(Üzgün bir şekilde)Yolda dinlenirken işe yarayacağını düşünmüştüm...",
           "Beyaz Diş:(Bağırarak)Seni avanak!Bu hayatımda gördüğüm en kötü seçim",
           "Yastığı alır ve ejderhaya doğru fırlatır.",
           "Beyaz Diş "+player_name+"'in yakasından tutup onu havaya kaldırmıştır, kavga etmektedirler.",
           "Ejderha yastığa doğru eğilir.",
           "Ve koklar, koku onu geçmişe götürür",
           "Bu ejderhanın bebeklik yastığıdır.",
           "Gözleri dolar",
           "İkisi de Ejderhaya doğru kafalarını çevirirler.",
           "Ejderha:(Gözleri dolarak yastığa sarılır)Benim minik yaştığım şen nerelerdeydin",
           "Ejderha:Ben her yerde şeni aradım hımmmm(Yastığa sarılarak döndürür)",
           "Ejderha:Artık sonsuza dek beraberiiiiz...",
           player_name+":(Sırıtarak)Bak işe yarıyormuş demek ki",
           "Beyaz Diş "+player_name+"'i indirir.",
           "Beyaz Diş:(Boğazını temizleyerek)Bu seferlik işe yaradı.",
           dog_name+"(Ağlayarak)Artık eve gidelim lütfenn",
           "-Ve kahramanlarımız evlerine doğru yola koyulurlar."]
   write(yastık)          
           
story_10=["Güneş bir güne daha merhaba demiştir",
          player_name+" her zamanki hamağındadır",
          "Beyaz Diş ve "+dog_name+" ise yemeği hazırlamaktadırlar",
          dog_name+" ve Beyaz Diş sorunsuz anlaşmaktadırlar.",
          "Kahramanlarımız artık sonsuza dek birliktedirler.",
          player_name+":(Havayı içine çekerek)Her zamanki hayatıma kavuştuğum için çok mutluyum...",
          "-Doğru seçimdi ha oyuncu?",
          "-SON?"
          ]
write(story_10)


story_11=["-İyi iş çıkarttın sıkıcı hayatın renklendi mi iki günlüğüne bile olsa?",
          "Ejderha:(Mutlu bir şekilde)Evet, hepsi senin sayende",
          "-Eh, ikimizin de istediği gerçekleşti",
          "-(Sırıtarak)Hem sana eğlence çıktı hem de bana anlatacak bir hikaye...",
          "Ejderha:(Gülümseyerek)Bu kaçırma fikri iyiydi ama eğlencesi kısa sürdü...",
          "-Sen merak etme bundan sonra senede bir yaparız.",
          "Ejderha:(Gülümseyerek)Bana uyar...",
          "---OYUNUMUZU OYNADIĞINIZ İÇİN TEŞEKKÜR EDERİİİZ---"]      
write(story_11)          
          
