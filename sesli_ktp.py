import pypdf
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdf_metni_cikar(pdf_yolu):
    metin=""
    pdf_okuyucu=pypdf.PdfReader(open(pdf_yolu,'rb'))
    for sayfa_num in range (len(pdf_okuyucu.pages)):
        metin+=pdf_okuyucu.pages[sayfa_num].extract_text()
    return metin
#ses bölümü
def metni_ses_cevir(metin,cikti_dosya):
    sesli_cevir=gTTS(text=metin, lang='tr')
    sesli_cevir.save(cikti_dosya)
#dosya secme 
def dosya_sec():
    dosya_yolu=filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*.pdf")])
    if dosya_yolu:
        pdf_metin=pdf_metni_cikar(dosya_yolu)
        metni_ses_cevir(pdf_metin, "ses.mp3")
        os.system("afplay ses.mp3") #mac için varsayılan seslendirici ve oynatıcı start komutu windowslar için veya open .... ses.mp3
#tkinter arayüzü
pencre=tk.Tk()
pencre.title("sesli kitap")
pencre.geometry("250x150")

buton=tk.Button(pencre, text="PDF SEÇ", padx=10, pady=10, command=dosya_sec)
buton.pack(pady=20)

pencre.mainloop()
