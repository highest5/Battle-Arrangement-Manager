import customtkinter, ast
from customtkinter import *
from customtkinter import filedialog
from tkinter import ttk, messagebox
import ctypes

myappid = 'Battle.Arrangement.Manager'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

customtkinter.set_appearance_mode("dark")

master = CTk()                                                               
master.title("Battle Arrangement Manager")        
# master.configure(fg_color="#ADD8E6")                                   
sh = master.winfo_screenheight()                                            
sw = master.winfo_screenwidth()                                             
master.geometry('%dx%d+%d+%d' % (sw/2,sh-80,-8,0))

def open_file():
    global PermaList,turn,turnnum
    filename = filedialog.askopenfilename()
    delete_all()
    file = open(f"{filename}",'r')
    data = file.read()
    DataList = ast.literal_eval(data)
    PList = DataList[0]
    EList = DataList[1]
    for i in range(len(PList)):
        for j in range(len(PList[i])-1):
            PNameList[i][j].insert(customtkinter.END,PList[i][j])
    for i in range(len(EList)):
        for j in range(len(EList[i])-1):      
            ENameList[i][j].insert(customtkinter.END,EList[i][j])
    PermaList = DataList[2]
    turn = DataList[4]
    turnnum = len(PermaList)
    print_names(PermaList)
    StatList = DataList[3]
    StatBox.insert(customtkinter.END,StatList)
    highlight(turn)
    
        
def save_file():
    global PermaList
    PList,EList,CList,SaveList=[],[],[],[]
    for i in PNameList:
        name = i[0].get()
        if len(name)>0:
            ini = i[1].get()
            if len(ini)>0:
                ini = int(ini)
            else: ini = 0
            dex = i[2].get()
            if len(dex)>0:
                dex = int(dex)
            else: dex = 0
            hp = i[3].get()
            if len(hp)>0:
                hp = int(hp)
            else: hp = ''
            PList.append([name,ini,dex,hp,"A"])
    SaveList.append(PList)
    for j in ENameList:
        name = j[0].get()
        if len(name)>0:
            ini = j[1].get()
            if len(ini)>0:
                ini = int(ini)
            else: ini = 0
            dex = j[2].get()
            if len(dex)>0:
                dex = int(dex)
            else: dex = 0
            hp = j[3].get()
            if len(hp)>0:
                hp = int(hp)
            else: hp = ""
            EList.append([name,ini,dex,hp,"A"])
    SaveList.append(EList)
    if "PermaList" in globals():
        SaveList.append(PermaList)
    ConList = StatBox.get("1.0",customtkinter.END)
    SaveList.append(ConList)
    SaveList.append(turn)
    file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    file.write(f"{SaveList}")
    file.close()
    # else:
        # messagebox.showinfo("No Data","There is no data to save")
        
def delete_enemies():
    for i in ENameList:
        for j in i:
            j.delete(0,customtkinter.END)
            
def delete_order():
    NameBox.delete(1.0,'end')
    HPBox.delete(1.0,'end')
    
def delete_conditions():
    global turnnum
    StatBox.delete(1.0,'end')
    for i in range(turnnum-1):
        StatBox.insert("end",'\n')
            
def delete_all():
    if messagebox.askokcancel("Are you sure?","Pressing 'ok' will erase all entries. Proceed?"):
        for i in PNameList:
            for j in i:
                j.delete(0,customtkinter.END)
        delete_enemies()
        delete_order()
        delete_conditions

FilePane = CTkFrame(master)
FilePane.grid(row=0,column=0,sticky=N+E+W+S)

OPEN = CTkButton(FilePane,text='OPEN',width=100,command=open_file)
OPEN.grid(row=0,column=0,padx=15,pady=3,sticky=E+W)

SAVE = CTkButton(FilePane,text='SAVE',width=100,command=save_file)
SAVE.grid(row=0,column=1,padx=15,pady=3,sticky=E+W)

PFrame = CTkFrame(master,width=400,fg_color="#006400")
PFrame.grid(row=1,column=0,padx=2,pady=2,ipadx=4,ipady=10,)

PNameLabel = CTkLabel(PFrame,text="Player Name")
PNameLabel.grid(row=0,column=1,sticky=E+W)

InitLabel=CTkLabel(PFrame,text='Init')
InitLabel.grid(row=0,column=2,sticky=E+W)

DexLabel=CTkLabel(PFrame,text='Dex')
DexLabel.grid(row=0,column=3,sticky=E+W)

HPLabel=CTkLabel(PFrame,text='HP')
HPLabel.grid(row=0,column=4,sticky=E+W)

PNameList=[]
for i in range(1,11):
    CTkLabel(PFrame,text=i).grid(row=i,column=0)
    PName = CTkEntry(PFrame,width=135,height=5)
    PName.grid(row=i,column=1,padx=1,sticky=W)
    Ini = CTkEntry(PFrame,width=30,height=20)
    Ini.grid(row=i,column=2,padx=1,ipady=0)
    Dex = CTkEntry(PFrame,width=30,height=20)
    Dex.grid(row=i,column=3,padx=1,ipady=0)
    HP = CTkEntry(PFrame,width=40,height=20)
    HP.grid(row=i,column=4,padx=1,ipady=0)
    PNameList.append([PName,Ini,Dex,HP])

EFrame = CTkFrame(master,fg_color="#8B0000")
EFrame.grid(row=2,column=0,rowspan=4,columnspan=1,padx=2,pady=(0,2),ipadx=4,ipady=10,sticky=W+E)

ENameLabel = CTkLabel(EFrame,text="Enemy Name")
ENameLabel.grid(row=0,column=1)

ENameList=[]
for i in range(1,11):
    CTkLabel(EFrame,text=i).grid(row=i,column=0)
    EName = CTkEntry(EFrame,width=135,height=5)
    EName.grid(row=i,column=1,padx=1,sticky=E)
    Ini = CTkEntry(EFrame,width=30,height=20)
    Ini.grid(row=i,column=2,padx=1,ipady=0)
    Dex = CTkEntry(EFrame,width=30,height=20)
    Dex.grid(row=i,column=3,padx=1,ipady=0)
    HP = CTkEntry(EFrame,width=40,height=20)
    HP.grid(row=i,column=4,padx=1,ipady=0)
    ENameList.append([EName,Ini,Dex,HP])
    
DispFrame = CTkFrame(master)
DispFrame.grid(row=0,column=1,rowspan=3,sticky=W+N,ipadx=3,ipady=3)

NameLabel = CTkLabel(DispFrame,text="Name")
NameLabel.grid(row=0,column=1)

HPLabel = CTkLabel(DispFrame,text="HP")
HPLabel.grid(row=0,column=2)

StatLabel = CTkLabel(DispFrame,text="Condition")
StatLabel.grid(row=0,column=3)

NameBox = CTkTextbox(DispFrame,wrap="none",corner_radius=1,height=400,width=120)
NameBox.grid(row=1,column=1,padx=(3,0),pady=(3,0))

HPBox = CTkTextbox(DispFrame,wrap="none",corner_radius=1,height=400,width=40)
HPBox.grid(row=1,column=2,pady=(3,0))

StatBox = CTkTextbox(DispFrame,wrap="none",corner_radius=1,height=400,width=200)
StatBox.grid(row=1,column=3,padx=(0,0),pady=(3,0))
StatBox.insert("end",'\n')

def assemble():
    if messagebox.askokcancel("Are you sure?","Pressing 'ok' will erase all entries. Proceed?"):
        TurnList=[]
        for i in PNameList:
            name = i[0].get()
            if len(name)>0:
                ini = i[1].get()
                if len(ini)>0:
                    ini = int(ini)
                else: ini = 0
                dex = i[2].get()
                if len(dex)>0:
                    dex = int(dex)
                else: dex = 0
                hp = i[3].get()
                if len(hp)>0:
                    hp = int(hp)
                else: hp = ''
                TurnList.append([name,ini,dex,hp,"A"])
        for j in ENameList:
            name = j[0].get()
            if len(name)>0:
                ini = j[1].get()
                if len(ini)>0:
                    ini = int(ini)
                else: ini = 0
                dex = j[2].get()
                if len(dex)>0:
                    dex = int(dex)
                else: dex = 0
                hp = j[3].get()
                if len(hp)>0:
                    hp = int(hp)
                else: hp = ""
                TurnList.append([name,ini,dex,hp,"A"])
        TurnList=sorted(TurnList,key=lambda x: (-x[1],-x[2]))
        return TurnList

def add_enemies():
    global PermaList,turn
    for j in ENameList:
        name = j[0].get()
        if len(name)>0:
            ini = j[1].get()
            if len(ini)>0:
                ini = int(ini)
            else: ini = 0
            dex = j[2].get()
            if len(dex)>0:
                dex = int(dex)
            else: dex = 0
            hp = j[3].get()
            if len(hp)>0:
                hp = int(hp)
            else: hp = ""
            if ini > PermaList[turn-1][1]:
                turn+=1
            PermaList.append([name,ini,dex,hp,"A"])
    PermaList=sorted(PermaList,key=lambda x: (-x[1],-x[2]))
    print_names(PermaList)
    highlight(turn)
    
    
def strikethrough(line):
    NameBox.tag_config("strikethrough",overstrike=True,foreground='red')
    NameBox.tag_add("strikethrough", str(line+0.0), str(line)+".end")

def print_names(ConList):
    NameBox.delete("1.0", customtkinter.END)
    HPBox.delete("1.0", customtkinter.END)
    for k in ConList:
        NameBox.insert("end",k[0]+"\n")
        HPBox.insert("end",str(k[3])+"\n")
        if k[4]=="D":
            strikethrough(ConList.index(k)+1)
        
def first_print():
    global turn,turnnum,PermaList
    turn = 1
    FirstList=assemble()
    turnnum = len(FirstList)
    print_names(FirstList)
    highlight(turn)
    PermaList = FirstList
    StatBox.delete('0.0','end')
    for i in range(turnnum-1):
        StatBox.insert("end",'\n')

DataFrame = CTkFrame(master)
DataFrame.grid(row=6,column=0,columnspan=2,sticky=N+E+W+S)    

SORT = CTkButton(DataFrame,text="SORT",width=120,command=first_print)
SORT.grid(row=0,column=0,pady=3,padx=(10,5),sticky=N+E+W+S)

ADD = CTkButton(DataFrame,text="ADD",width=120,command=add_enemies)
ADD.grid(row=0,column=1,pady=3,padx=(5,20),sticky=N+E+W+S)

CLEARENEMIES = CTkButton(DataFrame,text="CLEAR\nENEMIES",width=40,font=("Helvetica", 10),command=delete_enemies)
CLEARENEMIES.grid(row=0,column=2,pady=3,padx=(0,5),sticky=N+E+W+S)

CLEARTURN = CTkButton(DataFrame,text="CLEAR\nORDER",width=40,font=("Helvetica", 10),command=delete_order)
CLEARTURN.grid(row=0,column=3,pady=3,padx=5,sticky=N+E+W+S)

CLEARCON = CTkButton(DataFrame,text="CLEAR\nCONDITIONS",width=40,font=("Helvetica", 10),command=delete_conditions)
CLEARCON.grid(row=0,column=4,pady=3,padx=(5,30),sticky=N+E+W+S)

CLEARALL = CTkButton(DataFrame,text="CLEAR ALL",width=120,command=delete_all)
CLEARALL.grid(row=0,column=5,pady=3,sticky=N+E+W+S)

def highlight(line):
    NameBox.tag_config("highlight_line", background="gold",foreground="black")
    NameBox.tag_add("highlight_line", str(line+0.0), str(line)+".end")
    HPBox.tag_config("highlight_line", background="darkmagenta")
    HPBox.tag_add("highlight_line", str(line+0.0), str(line)+".end")
    
def unhighlight(line):
    NameBox.tag_remove("highlight_line", str(line+0.0), str(line)+".end")
    HPBox.tag_remove("highlight_line", str(line+0.0), str(line)+".end")
    
def get_list():
    global turnnum,PermaList
    GotList=PermaList
    return GotList

def next_turn():
    check=0
    global turn, turnnum, PermaList
    TurnList = PermaList
    unhighlight(turn)
    turn+=1
    turn = (turn-1)%(len(TurnList))+1
    while TurnList[turn-1][4]== "D":
        check+=1
        if check > turnnum:
            break
        turn+=1
        turn = (turn-1)%(len(TurnList))+1
    highlight(turn)
    
def up():
    global turn, turnnum, PermaList
    TurnList = PermaList
    unhighlight(turn)
    turn-=1
    turn = (turn-1)%(len(TurnList))+1
    highlight(turn)
    
def down():
    global turn, turnnum, PermaList
    TurnList = PermaList
    unhighlight(turn)
    turn+=1
    turn = (turn-1)%(len(TurnList))+1
    highlight(turn)

TurnFrame = CTkFrame(master)
TurnFrame.grid(row=5,column=1,sticky=N+E+W+S)

NEXT = CTkButton(TurnFrame,text="NEXT TURN",command=next_turn)
NEXT.grid(row=0,column=0,padx=40,pady=10,sticky=N+E+W+S)

UP = CTkButton(TurnFrame,text="\u2191",width=20,command=up)
UP.grid(row=0,column=1,padx=10,pady=15,sticky=N+E+W+S)

DOWN = CTkButton(TurnFrame,text="\u2193",width=20,command=down)
DOWN.grid(row=0,column=2,padx=10,pady=15,sticky=N+E+W+S)

DamFrame = CTkFrame(master)
DamFrame.grid(row=4,column=1,sticky=N+E+W+S)

DamLabel = CTkLabel(DamFrame,text="HP")
DamLabel.grid(row=0,column=0,columnspan=2)

DamEnt = CTkEntry(DamFrame)
DamEnt.grid(row=1,column=0,columnspan=2)

def kill():
    global PermaList
    PermaList[turn-1][3]=0
    PermaList[turn-1][4]="D"
    print_names(PermaList)
    
def revive():
    global PermaList
    PermaList[turn-1][3]=1
    PermaList[turn-1][4]="A"
    print_names(PermaList)
    
def hurt():
    global turn, PermaList
    dam = DamEnt.get()
    hp = int(get_list()[turn-1][3])-int(dam)
    if hp<=0:
        hp = 0
        PermaList[turn-1][4]="D"
    PermaList[turn-1][3]=hp
    print_names(PermaList)
    highlight(turn)
    
def heal():
    global turn,PermaList
    dam = DamEnt.get()
    hp = int(get_list()[turn-1][3])+int(dam)
    if hp>0:
        PermaList[turn-1][4]="A"
    PermaList[turn-1][3]=hp
    print_names(PermaList)
    highlight(turn)

DamDeal = CTkButton(DamFrame,text="Deal Damage",width=40,command=hurt)
DamDeal.grid(row=1,column=2)

Heal = CTkButton(DamFrame,text="Heal",width=40,command=heal)
Heal.grid(row=1,column=3)

Dead = CTkButton(DamFrame,text="DEAD",command=kill)
Dead.grid(row=2,column=0,padx=(20,20),pady=10,sticky=E+W,columnspan=2)

Alive = CTkButton(DamFrame,text="ALIVE",command=revive)
Alive.grid(row=2,column=2,padx=(20,20),pady=10,sticky=E+W,columnspan=2)

conditions = [["Blind","BL"],["Charmed","CH"],["Deafened","DE"],
              ["Exhaustion","EX"],["Frightened","FR"],["Grappled","GR"],
              ["Incapacitated","INCAP"],["Invisible","INV"],["Paralyyzed","PARA"],
              ["Petrified","PET"],["Poisoned","POIS"],["Prone","PR"],
              ["Restrained","REST"],["Stunned","ST"],["Unconcious","UNCON"]]

ConFrame = CTkFrame(master)
ConFrame.grid(row=3,column=1,sticky=N+E+W+S)

def print_con(n):
    global turn
    constr = StatBox.get(turn+0.0,str(turn)+'.end')
    if len(constr)==0:
        newcon = conditions[n][1]
    else: newcon = ','+conditions[n][1]
    if newcon.strip(',') in constr:
        constr = constr.replace(newcon.strip(','),'').strip(',')
        newcon = ''
    StatBox.delete(turn+0.0,str(turn)+'.end')
    StatBox.insert(turn+0.0,constr)
    StatBox.insert(str(turn)+'.end',newcon)

for i in range(int(len(conditions)/5)):
    for j in range(int(len(conditions)/3)):
        ind = i+j*3
        con = CTkButton(ConFrame,
                        text=conditions[ind][0],
                        textvariable=conditions[ind][0],
                        width=70,height=20,font=("Helvetica", 10),
                        command=lambda x=ind: print_con(x))
        con.grid(row=i,column=j,padx=2,pady=2)
      
master.mainloop()