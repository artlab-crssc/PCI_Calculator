#Created by Ben on 11/11/2024, ART Lab, CRSSC

import tkinter as tk
from tkinter import ttk,messagebox
from webbrowser import open_new


class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PCI Calculator')
        self.geometry('800x500')
        self.resizable(False,False)
        self.ratio=[]
        self.intv=[]
        self.url='https://sciforum.net/manuscripts/21124/slides.pdf'
        self.logo=tk.PhotoImage(file='./Database/PCI logo3.png')
        self.logo=self.logo.subsample(4,4)
        self.iconbitmap('./Database/PCI-logo2.ico')
        self.bg=tk.PhotoImage(file='./Database/background.png')
        self.bgim=tk.Label(self,image=self.bg)
        self.bgim.place(x=0,y=0)
        for i in range(0,9):
            self.ratio.append(str(i))
        self.linkstyle = ttk.Style()
        self.linkstyle.configure('s.TLabel',foreground="blue",font=('Arial',7,'bold','underline','italic'),background='#E1F2FC')
        self.commonstyle=ttk.Style()
        self.commonstyle.configure('s.TMenubutton',background='#E3F2D5',font=('Arial'))
        self.butstyle=ttk.Style()
        self.butstyle.configure('s.TButton',font=('Arial',15),background='#E3F2D5')
        self.lab=[]
        self.entry=[]
        self.row=4
        self.lab.append(self.label('Tensile'))
        self.entry.append(self.ent())
        self.lab.append(self.label('Print Time'))
        self.entry.append(self.ent())
        self.lab.append(self.label('Elongation'))
        self.entry.append(self.ent())
        self.lab.append(self.label('Nozzle Diameter'))
        self.noz=tk.StringVar()
        options=['any','0.2','0.4','0.6','0.8']
        self.Nozz=ttk.OptionMenu(self,self.noz,options[0],*options,style='s.TMenubutton')
        #option for nozz
        self.Nozz.grid(row=self.row,column=2)
        self.calc=tk.Label(self,text='PC INDEX Calculator',font=('Arial Black',20),bg='#FFFBC1')
        self.calc.grid(row=0,column=3,rowspan=3,columnspan=5,padx=0,sticky='e')
        self.row+=1
        self.logoim=ttk.Label(self,image=self.logo,background='white')
        self.logoim.grid(row=0,column=1,rowspan=3,columnspan=2,sticky='e')
        self.link=ttk.Label(self,text="Publication: YU, K.; Tsoi, K.; Yeung, T.; Ng, R.; Chan, K.; Chan,C. "
                            "Exploring the Trade-off between Printing Time and Mechanical Properties:\n"
                            "Optimization of Three-Dimensional Printing Parameters for Clinical Aids Fabrication, "
                            "in Proceedings of the 5th International Electronic Conference on\n Applied Sciences, "
                            "4–6 December 2024, MDPI: Basel, Switzerland",style='s.TLabel')
        self.link.grid(row=10,column=0,rowspan=3,columnspan=10,sticky='s',pady=40)
        self.link.bind("<Button-1>", self.access_link)
        self.sub=ttk.Button(self,text='Submit',command=self.submit,style='s.TButton')
        self.sub.grid(row=self.row,column=1,columnspan=2)
        self.warn=tk.Label(self,text='*Ratio must be sum of 10!',font=('Arial',10),foreground='red',background='#D5EBF9',pady=0)
        self.warn.grid(row=self.row+1,column=1,columnspan=2)
        self.PCItable()
        

    def access_link(self,e):
        open_new(self.url)
        open_new('https://drive.google.com/file/d/1GyG3Gq8wX-UM82sGwt7UPSXBmm6gB8ZR/view?usp=sharing')

    def label(self,txt):
        s=tk.Label(self,text=txt,font=('Consolas',12),background='white')
        s.grid(row=self.row,column=1,sticky='e',rowspan=1,padx=5)
        return s

    def ent(self):
        self.intv.append(tk.IntVar())
        s=ttk.OptionMenu(self,self.intv[-1],*self.ratio,command=self.ratioconfig,style='s.TMenubutton')
        s.grid(row=self.row,column=2,rowspan=1)
        self.row+=1
        return s
    
    def ratioconfig(self,val):
        self.ratio=[i.get() for i in self.intv]
        
    def submit(self):
        sum=0
        for i in self.ratio:
            sum+=int(i)
        if sum==10:
            pass
        else:
            messagebox.showerror('Error','Invalid Input!\nRatio must be sum of 10!')
    
    def PCItable(self):
        self.tablestyle = ttk.Style()
        self.tablestyle.configure('s.TTree',font=('Arial',12))
        self.tab=ttk.Treeview(self,columns=('1','2','3','4','5'),show='headings')
        self.tab.heading('1',text='Layer Height(mm)')
        self.tab.heading('2',text='Nozzle Diameter(mm)')
        self.tab.heading('3',text='Infill Density(%)')
        self.tab.heading('4',text='Pattern')
        self.tab.heading('5',text='👑PC Index')
        
        self.tab.column('1',width=120,anchor='center')
        self.tab.column('2',width=130,anchor='center')
        self.tab.column('3',width=100,anchor='center')
        self.tab.column('4',width=80,anchor='center')
        self.tab.column('5',width=80,anchor='center')
        
        self.tab.grid(row=4,column=3,columnspan=2,rowspan=5,padx=10,pady=10,sticky='w')
        
    
        

if __name__=='__main__':
    PCI=UI()
    for i in range(50):
        PCI.tab.insert("", "end", values=("Fill {}".format(i), 30 + i,'你好','Bonjour','+-*/'))
    PCI.mainloop()