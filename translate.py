import customtkinter
from googletrans import Translator
import tkinter.messagebox
from tkinter import EXTENDED
from CTkListbox import CTkListbox

class Ceviri_ac(customtkinter.CTkFrame,):
    def __init__(self,parent,ana_frame,liste):
        super().__init__(parent)
        self.ana_frame = ana_frame
        self.listbox_get=liste
        self.toplevel_window= None
        self.toplevel_window2= None    
        
        self.frame_ceviri = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame_ceviri.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)
        
        self.textboks1 = customtkinter.CTkTextbox(self.frame_ceviri,width=300,height=150,corner_radius=15)
        self.textboks1.place(relx=0.1,rely=0.15,relwidth=0.4,relheight=0.3)
        self.textboks2 = customtkinter.CTkTextbox(self.frame_ceviri,width=300,height=150,corner_radius=15)
        self.textboks2.place(relx=0.1,rely=0.6,relwidth=0.4,relheight=0.3)
        
        self.textboks1.insert("0.0"," ")
        self.textboks2.insert("0.0"," ")

        self.text_en_tr_sonuc = customtkinter.CTkTextbox(self.frame_ceviri,
                                                   width=300,height=150,corner_radius=15)
        self.text_en_tr_sonuc.place(relx=0.57,rely=0.15,relwidth=0.4,relheight=0.3)
        self.text_tr_en_sonuc = customtkinter.CTkTextbox(self.frame_ceviri,
                                                   width=300,height=150,corner_radius=15)
        self.text_tr_en_sonuc.place(relx=0.57,rely=0.6,relwidth=0.4,relheight=0.3)
        
        btn_cevir_en_tr = customtkinter.CTkButton(self.frame_ceviri,text="Çevir",height=35,width=300,command=self.cevir_en_tr).place(relx=0.1,rely=0.47,relwidth=0.4,relheight=0.05)
        btn_cevir_tr_en = customtkinter.CTkButton(self.frame_ceviri,text="Çevir",height=35,width=300,command=self.cevir_tr_en).place(relx=0.1,rely=0.93,relwidth=0.4,relheight=0.05)
        btn_temizle = customtkinter.CTkButton(self.frame_ceviri,text="Hepsini Sil",height=35,width=300,command=self.sil).place(relx=0.57,rely=0.93,relwidth=0.4,relheight=0.05)
        btn_listeye_ekle_ing = customtkinter.CTkButton(self.frame_ceviri,text="Listey Ekle",width=80,height=30,command=self.toplevel_ing_ac).place(relx=0.66,rely=0.085,relwidth=0.25,relheight=0.05)
        btn_listeye_ekle_tr = customtkinter.CTkButton(self.frame_ceviri,text="Listey Ekle",width=80,height=30,command=self.toplevel_tr_ac).place(relx=0.66,rely=0.535,relwidth=0.25,relheight=0.05)
        
        label_ceviri = customtkinter.CTkLabel(self.frame_ceviri,font=("Arial",30),text="Çeviri").place(relx=0.02,rely=0.02,relwidth=0.4,relheight=0.08)
        label_en_tr = customtkinter.CTkLabel(self.frame_ceviri,text="ingilice > Türkçe").place(relx=0.1,rely=0.1,relwidth=0.4,relheight=0.05)
        label_tr_en = customtkinter.CTkLabel(self.frame_ceviri,text="Türkçe > İngilizce").place(relx=0.1,rely=0.53,relwidth=0.4,relheight=0.05)
  
# cevirme işlemi yapar
    def cevir_tr_en(self):  
        translator = Translator()  
        try: 
            self.text_tr_en_sonuc.delete("0.0","end")
            input2= self.textboks2.get(1.0, "end")
            result=translator.translate(input2,src="tr",dest="en").text
            self.text_tr_en_sonuc.insert("0.0",str(result))
        except Exception as a:
            tkinter.messagebox.showwarning("HATA","Çevrilemedi tekrar deneyin\n(internete bağlı olduğunuzdan emin olun).")
                
    def cevir_en_tr(self):  
        translator = Translator()  
        try: 
            self.text_en_tr_sonuc.delete("0.0","end")
            input= self.textboks1.get(1.0, "end")
            result=translator.translate(input,src="en",dest="tr").text
            self.text_en_tr_sonuc.insert("0.0",str(result))
        except Exception as a:
            tkinter.messagebox.showwarning("HATA","Çevrilemedi tekrar deneyin\n(internete bağlı olduğunuzdan emin olun).")
# cevirideki bütün textboksları temizler
    def sil(self):
        self.textboks1.delete("0.0","end")
        self.textboks2.delete("0.0","end")
        self.text_en_tr_sonuc.delete("0.0","end")
        self.text_tr_en_sonuc.delete("0.0","end")
        
    def toplevel_ing_ac(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_ing() # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
# çeviri kelimelerini listeye ekler
    def toplevel_ing(self):
        self.toplevel_window = customtkinter.CTkToplevel(master=self)
        self.toplevel_window.state("normal")
        self.toplevel_window.title("Listeye Ekle")
        self.toplevel_window.resizable(False,False)
        button_ceviri_listeye_ekle = customtkinter.CTkButton(self.toplevel_window,width=80,height=30,text="Listeye ekle",command=self.Add_to_list_ing).grid(row=2,pady=10)
        self.listbox_ceviri = CTkListbox(self.toplevel_window,multiple_selection=False,height=250,width=220)
        self.listbox_ceviri.grid(row=1,padx=7,pady=5)
        for i in self.listbox_get:
            self.listbox_ceviri.insert(self.listbox_ceviri.size(),i)
 
    def Add_to_list_ing(self):
        yaz = f"{self.textboks1.get(1.0, "end-1c")}, {self.text_en_tr_sonuc.get(1.0, "end-1c")},\n"
        oku6 =open(f"{self.listbox_ceviri.get(self.listbox_ceviri.curselection())}.txt","a",encoding='utf-8')
        oku6.write(yaz)
        oku6.close()
        self.toplevel_window.destroy()
    
    def toplevel_tr_ac(self):
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_tr() # create window if its None or destroyed
        else:
            self.toplevel_window2.focus()  # if window exists focus it
    def toplevel_tr(self):
        self.toplevel_window2= customtkinter.CTkToplevel(self)
        self.toplevel_window2.title("Listeye Ekle")
        self.toplevel_window2.resizable(False,False)
                
        button_ceviri_listeye_ekle = customtkinter.CTkButton(self.toplevel_window2,width=80,height=30,text="Listeye ekle",command=self.Add_to_list_tr).grid(row=2,pady=5)
        self.listbox_ceviri2 = CTkListbox(self.toplevel_window2,multiple_selection=False,height=250,width=220)
        self.listbox_ceviri2.grid(row=1,padx=7,pady=5)
        for i in self.listbox_get:
            self.listbox_ceviri2.insert(self.listbox_ceviri2.size(),i)
    def Add_to_list_tr(self):
        yaz = f"{self.text_tr_en_sonuc.get(1.0, "end-1c")}, {self.textboks2.get(1.0, "end-1c")},\n"
        oku6 =open(f"{self.listbox_ceviri2.get(self.listbox_ceviri2.curselection())}.txt","a",encoding='utf-8')
        oku6.write(yaz)
        oku6.close()
        self.toplevel_window2.destroy()
        
        