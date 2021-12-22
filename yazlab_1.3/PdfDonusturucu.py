from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.converter import TextConverter
import io


def donustur(path):

    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(path, 'rb') as fh:

        for page in PDFPage.get_pages(fh,
                                    caching=True,
                                    check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()





        
    x = text.splitlines()
    print(len(x))
    adsoyad=""
    donem=""

    isim=""
    soy_isim=""
    ogrenci_no=""
    ogrenim_tur=""
    ders_adi=""
    proje_ozeti=""
    proje_teslim_tarih=""
    
    proje_baslıgı=""
    anahtar_kelimeler=""
    danisman_bilgileri=""
    juri_bilgileri=""
    j=0

    for i in range(len(x)):
        
        
        if "Anahtar" in x[i]  and  "kelimeler:" in x[i] :
            j=0
            while not (x[i+2+j].strip() and x[i+1+j].strip()):
                anahtar_kelimeler+=x[i+j]
                j=j+1
            anahtar_kelimeler=anahtar_kelimeler.split()
            anahtar_kelimeler=anahtar_kelimeler[2:]
            anahtar_kelimeler=' '.join(anahtar_kelimeler)
        if "Soyadı:" in x[i]:
            j=0
            while not  x[i+1+j].strip():
                adsoyad+=x[i+j]
                j=j+1
            adsoyad= adsoyad.split()
            print(adsoyad)
            isim=adsoyad[2]
            soy_isim=adsoyad[3]
            print
        if "Öğrenci" in x[i]  and  "No:" in x[i] :
            ogrenci_no=x[i]
            ogrenci_no=ogrenci_no.split()
            ogrenci_no=ogrenci_no[2]
        if ("ARAŞTIRMA" in x[i] and "PROBLEMLERİ" in x[i]) or ("BİTİRME"in x[i] and "PROJESİ" in x[i]) :
            ders_adi=x[i]
        if ("TEZİ" in x[i] ) :
            ogrenim_tur=x[i]
            ogrenim_tur=ogrenim_tur.split()
            ogrenim_tur=ogrenim_tur[0]
            
        if "ÖZET" in x[i]:
            j=0
            while not ("Anahtar" in x[i+j]  and  "kelimeler:" in x[i+j]):
                if "ÖZET" in x[i+j] and j!=0:
                    proje_ozeti=""
                    break
                proje_ozeti+=x[i+j]
                j=j+1
        if "Tarih" in x[i]  :
            proje_teslim_tarih=x[i]
            proje_teslim_tarih=proje_teslim_tarih.split()
            proje_teslim_tarih=proje_teslim_tarih[3]
            donem=proje_teslim_tarih.split(".")
            donem=int(donem[1])
            print(donem)
            print(type(donem))
            if (donem>=8 and donem<=12) or donem==1:
                donem="GÜZ"
                print(type(donem))
            if (donem>=2 and donem<=7):
                donem="BAHAR"
                print(type(donem))
        if ("ARAŞTIRMA" in x[i] and "PROBLEMLERİ" in x[i]) or ("BİTİRME"in x[i] and "PROJESİ" in x[i]) :
                
                j=i
            
                bos_alan=0
                while x[j].strip():
                    j+=1
                j=j+3
                dolu_bas=j
                
            
                proje_baslıgı=x[dolu_bas]+x[dolu_bas+2]
                
        if "Danışman" in x[i]  :
            danisman_bilgileri=x[i-2]
        
        if "Jüri" in x[i]and "Üyesi," in x[i]  :
            juri_bilgileri+=x[i-2]



    list = []
    list.append(isim)
    list.append(soy_isim)
    list.append(ogrenci_no)
    list.append(ogrenim_tur)
    list.append(ders_adi)
    list.append(proje_ozeti)
    list.append(proje_teslim_tarih)
    list.append(donem)
    list.append(proje_baslıgı)
    list.append(anahtar_kelimeler)
    list.append(danisman_bilgileri)
    list.append(juri_bilgileri)

    return list
