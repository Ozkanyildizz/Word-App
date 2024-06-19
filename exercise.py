import customtkinter
import tkinter.messagebox
import random
from CTkListbox import CTkListbox

class Alıstırma_ac(customtkinter.CTkFrame,):
    def __init__(self,parent,ana_frame,liste,):
        super().__init__(parent)
        self.ana_frame = ana_frame
        self.listbox_get=liste
        # frame alıştırma
        self.frame_alıstırma = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame_alıstırma.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)

        self.alıstırma_lbl = customtkinter.CTkLabel(self.frame_alıstırma,font=("Arial",25),corner_radius=50
                                                    ,fg_color="gray",text_color="white",height=40,
                                                    text=("Alıştırma yapmak istediğiniz listeyi seçiniz."))
        self.alıstırma_lbl.place(relx=0.001,rely=0.03,relheight=0.1,relwidth=1)
        self.listbox_alıstırma = CTkListbox(self.frame_alıstırma,multiple_selection=True)
        self.listbox_alıstırma.place(relx=0.001,rely=0.15,relheight=0.7,relwidth=1)
        self.oku()
        self.alıstırma_ac_button = customtkinter.CTkButton(self.frame_alıstırma,text=("Alıştırmaya Başla"),corner_radius=60,command=self.alıstırma)
        self.alıstırma_ac_button.place(relx=0.001,rely=0.87,relheight=0.1,relwidth=1)
    # alıştırma Frami açar 
    def alıstırma(self):     
        if self.kontroll():
            self.frame_alıstırma1 = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
            self.frame_alıstırma1.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)
        
            self.frame_alıstırma2= customtkinter.CTkFrame(self.frame_alıstırma1,width=600,corner_radius=150,height=600)
            self.frame_alıstırma2.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
            lbl= customtkinter.CTkLabel(self.frame_alıstırma2,bg_color="#292929",corner_radius=15,font=("Arial",25),text="Doğru Cevapı İşaretleyin")
            lbl.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)
            self.cvp1_strvar = customtkinter.StringVar() 
            self.cvp2_strvar = customtkinter.StringVar()    
            self.cvp3_strvar = customtkinter.StringVar()    
            self.cvp4_strvar = customtkinter.StringVar()  
            self.lbl_ingkelimevar = customtkinter.StringVar() 
            self.lbl_cvpvar= customtkinter.StringVar()
            self.yeni_soru()
            self.lbl_ing=customtkinter.CTkLabel(self.frame_alıstırma2,corner_radius=50,bg_color="#292929",font=("Arial",30),textvariable=self.lbl_ingkelimevar)
            self.lbl_ing.place(relx=0.18,rely=0.25,relwidth=0.8,relheight=0.1)
            self.cvp= customtkinter.CTkLabel(self.frame_alıstırma2,corner_radius=100,width=450,height=50,bg_color="#292929",textvariable=self.lbl_cvpvar)
            self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
            
            cvp4_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp4_strvar,command=self.cvp4).place(relx=0.1,rely=0.4,relwidth=0.4,relheight=0.1)
            cvp2_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp2_strvar,command=self.cvp2).place(relx=0.52,rely=0.4,relwidth=0.4,relheight=0.1)
            cvp3_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp3_strvar,command=self.cvp3).place(relx=0.1,rely=0.55,relwidth=0.4,relheight=0.1)
            cvp1_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp1_strvar,command=self.cvp1).place(relx=0.52,rely=0.55,relwidth=0.4,relheight=0.1)
            next_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=450,height=50,text="Sonraki",command=self.yeni_soru).place(relx=0.14,rely=0.7,relwidth=0.75,relheight=0.1)
            geri_button=  customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=200,bg_color="#292929",width=50,height=40,font=("Ariel",18),text="<",command=self.geri_alıstırma).place(relx=0.02,rely=0.26,relwidth=0.15,relheight=0.08)
    def oku(self):
        for i in self.listbox_get:
            self.listbox_alıstırma.insert(self.listbox_alıstırma.size(),i)    
    #alıştırma geri tuşu 
    def geri_alıstırma(self):
        self.frame_alıstırma1.place_forget()

    # liste kontrol 
    def kontroll(self):
        try:
            self.result =  self.listbox_alıstırma.get()
            if len(self.result)>1:
                    message = tkinter.messagebox.showwarning("Liste Seçin", "Açmak istediğiniz bir tane listeyi seçin liste boş olmamalı")   
            elif len(self.result)==1:
                self.oku7= open(f"{self.result[0]}.txt","r",encoding='utf-8')
                self.b = self.oku7.readlines()  
                self.degerr = len(self.b)
                if self.degerr<=4:
                    message = tkinter.messagebox.showwarning("Liste Boş", "Seçtiğiniz listede en az 4 kelime bulunmalı")   
                else:
                    return True
        except Exception as a:
            message = tkinter.messagebox.showwarning("Liste Seçin", "Açmak istediğiniz bir tane listeyi seçin liste boş olmamalı")
# yeni soru         
    def yeni_soru(self):
        try:
            # kelimeleri oku    
            self.kontroll()
            self.list1=[]
            self.list2=[]    
            randomm= random.randint(1,self.degerr-1)
            ing = self.b[randomm].split(",")[0]
            tr = self.b[randomm].split(",")[1]
            self.list1.append(ing)
            self.list2.append(tr)

            for i in range(3):
                randomn= random.randint(1,self.degerr-1)
                self.list2.append(self.b[randomn].split(",")[1])
            self.karısık = random.sample(self.list2,4)
            self.cvp1_strvar.set(f"{self.karısık[0]}")
            self.cvp2_strvar.set(f"{self.karısık[1]}")
            self.cvp3_strvar.set(f"{self.karısık[2]}")
            self.cvp4_strvar.set(f"{self.karısık[3]}")
            self.lbl_ingkelimevar.set(f"{self.list1[0]}")         
            self.cvp.place_forget()
        except Exception:
            pass

   # cevapları kontrol eder     
    def cvp1(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[0] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
    def cvp2(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[1] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
    def cvp3(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[2] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
    def cvp4(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[3] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")