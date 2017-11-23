import string
from tkMessageBox import *
from Tkinter import *
from random import *
master=Tk()
def comic():
    entry=focus.get()
    if (entry!='focus' and entry!='Focus' and entry!='FOCUS'):
        c5.delete('rel')
        c5.create_text(900,240,font=('chiller',20),text="You don't",tags='del')
        c5.create_text(950,265,font=('times new roman',30),text='deserve',tags='del')
        c5.create_text(900,300,font=('chiller',20),text='to be in this',tags='del')
        c5.create_text(1000,300,font=('Arial',25),text='section',tags='del')
    else:
        c5.delete('del')
        c5.create_text(900,240,font=('chiller',40),text="oh!",tags='rel')
        c5.create_text(950,290,font=('times new roman',30),text='really??',tags='rel')
        
    
def image():
    global sign
    global c5
    global focus
    sign=1
    if(sign==1):
        root=Tk()
        c5=Canvas(root,bg='purple',height=700,width=10000)
        c5.pack(side='left')
        snap=PhotoImage(file='bb.gif')
        print snap
        c5.create_image(300,150,image=snap,anchor='nw')
        
        c5.create_text(360,240,font=('chiller',20),text='That')
        c5.create_text(410,240,font=('chiller',20),text='was')
        c5.create_text(470,240,font=('chiller',20),text='awesome!')
        c5.create_text(360,280,font=('times new roman',20),text='Guri,')
        c5.create_text(460,280,font=('chiller',20),text='What do u think?')
        c5.create_text(650,245,font=('chiller',20),text='Of course Vijay!')
        c5.create_text(755,249,font=('chiller',20),text='It was nice')
        c5.create_text(650,280,font=('chiller',20),text='we are so called')
        focus=Entry(c5,fg='red',bg='yellow')
        c5.create_window(650,310,window=focus,height=20,width=60)
        c5.update()
        c5.create_text(720,310,font=('chiller',20),text='group')
        f_button=Button(c5,text='next',command=comic,bitmap='gray12')
        c5.create_window(648,410,window=f_button,height=10,width=20)
        c5.update()
        
        mainloop()

#image()
def calculate():
    global first
    global second
    a=int(first)
    b=int(second)
    global operation
    if(operation=='+'):
        z=a+b
    elif(operation=='-'):
        z=a-b
    elif(operation=='*'):
        z=a*b
    print z
    z=str(z)
    global opr
    print opr.get()
    if(opr.get==''):
        print "#"
    global sync
    if(z!=opr.get()):
        sync.delete(0,END)
        sync.insert(0,'Not The Right Answer')
        phase3()
    else:
        sync.delete(0,END)
        sync.insert(0,'matched')
        showinfo("Perfect","U Are")
        mainloop()
        global sign
        sign=1
        
        

def p3(i=0):
    if(i==0):
        global c4
        c4=Canvas(master,height=400,width=900,bg='SystemButtonFace')
        c4.pack(side='bottom',anchor='s')
p3()
def phase3():
    c4.config(bg='DarkOrchid2')
    global operation
    global first
    global second
    c4.create_rectangle(40,50,400,150,fill='yellow')
    o=['*','+','-']
    operation=o[randint(0,2)]
    first=randint(1,9)
    second=randint(1,9)
    c4.create_text(170,120,font=('algerian',40),text=first)
    c4.create_text(250,100,font=('chiller',25),text=second)
    c4.create_text(220,110,font=('arial',30),text=operation)
    global opr
    opr=Entry(c4,bg='orange')
    c4.create_window(140,200,window=opr,height=27,width=120)
    c4.update()
    opr.insert(0,"answer")
    global sync
    sync=Entry(c4,bg='red',fg='yellow')
    c4.create_window(290,280,window=sync,height=27,width=120)
    c4.update()
    sync.insert(0,'Not the right answer')
    cal=Button(c4,text='submit',command=calculate)
    c4.create_window(150,240,window=cal,height=27,width=90)
    c4.update()
    drop=Button(c4,text='refresh',command=calculate)
    c4.create_window(250,240,window=drop,height=27,width=90)
    c4.update()
        
    
    

    
def p4():
    phase3()    

def circus():
    global acl
    ac=''.join(map(str,acl))
    ac_box=ac_e2.get()
    print ac_box
    print ac
    
    global cl
    c=''.join(map(str,cl))
    c_box=c_e1.get()
    print c
    print c_box
    global flag
    if(c_box==c and ac_box==ac):
        flag.delete(0,END)
        flag.insert(0,"R")
        p4()
        
    else:
        flag.delete(0,END)
        flag.insert(0,"W")
        phase2(1)
            
    
    
    

def phase2(i=0):
    if(i==0):
        global c3
        c3=Canvas(master,bg='beige',height=300,width=440)
        c3.pack(side='left',anchor='n')
    
    c3.create_oval(50,10,400,300,fill='yellow',width=3)
    c3.create_oval(80,40,370,270,fill='red')
    c3.create_oval(110,70,340,240,fill='beige')
    c3.create_line(225,10,225,300,fill='purple')
    c3.create_line(400,160,50,160,fill='blue')
    lib=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    global cl
    cl=[]
    for a in range(0,2):
        cl.append(lib[randint(0,23)])
        cl.append(randint(0,9))
    print cl
    c3.create_text(90,80,font=('arial',12),text=cl[0])
    c3.create_text(80,80,font=('times new roman',70),text=".")
    c3.create_text(80,200,font=('verdana',25),text=cl[3])
    c3.create_text(370,100,font=('times new roman',20),text=cl[1])
    c3.create_text(380,200,font=('chiller',34),text=cl[2])
    global acl
    acl=[]
    for a in range(0,2):
        acl.append(lib[randint(0,23)])
        acl.append(randint(0,9))
    print acl
    c3.create_text(100,140,font=('forte',20),text=acl[0])
    c3.create_text(110,80,font=('times new roman',70),text=".")
    c3.create_text(180,250,font=('arial',19),text=acl[1])
    c3.create_text(270,60,font=('chiller',30),text=acl[3])
    c3.create_text(300,230,font=('times new roman',20),text=acl[2])
    global c_e1
    c_e1=Entry(c3,bg='yellow')
    c3.create_window(230,120,window=c_e1,width=140,height=25)
    c_e1.insert(0,"clockwise")
    c3.update()
    global ac_e2
    ac_e2=Entry(c3,bg='red')
    c3.create_window(230,200,window=ac_e2,width=140,height=25)
    ac_e2.insert(0,"anticlockwise")
    c3.update()

    ver=Button(c3,text='submit',command=circus)
    c3.create_window(190,160,window=ver)
    c3.update()
    ref=Button(c3,text='refresh',command=circus)
    c3.create_window(250,160,window=ref)
    c3.update()
    global flag
    flag=Entry(c3,bg='white')
    c3.create_window(350,30,window=flag,width=20)
    flag.insert(0,'W')
    c3.update()
    
    
    

global count
count=0

def captcha():
    global value
    global list
    global verify
    print list
    v=value.get()
    val=''.join(map(str,list))
    print v
    print val
    if(v==val):
        verify.delete(0,END)    
        verify.insert(0,'Captcha Verified')
        phase2()
    else:
        verify.delete(0,END)
        verify.insert(0,'Match Not Found')
        phase1(1)
    
        
def phase1(choice=0):
    global count
    if(count==1 and choice==0):
        global c2
        c2=Canvas(master,bg='cyan',height='300',width='440')
        c2.pack(side='left',anchor='n')
    o_x1=40
    o_y1=50
    o_x2=400
    o_y2=180
    i_x1=o_x1+20
    i_y1=o_y1+20
    i_x2=o_x2-20
    i_y2=o_y2-20
    l_x1=i_x1
    l_y1=i_y2
    l_x2=i_x2
    l_y2=i_y1
    
    c2.create_rectangle(o_x1, o_y1, o_x2, o_y2, fill='purple')
    c2.create_rectangle(i_x1, i_y1, i_x2, i_y2, fill="yellow")
    c2.create_line(i_x1,i_y1,i_x2,i_y2, fill="green", width=3)
    c2.create_line(l_x1, l_y1, l_x2, l_y2, fill="grey", width=3)
    #c2.create_line(m_x1,m_x2, m_y1, m_y2, fill="#476042", width=3)
    #c2.create_line(150, 80, 200,100,fill="grey",width=3)
    lib=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   # print lib
    global list
    list=[]
    for a in range(0,3):
        list.append(lib[randint(0,23)])
        list.append(randint(0,9))           
    #print list
    
    c2.create_text(i_x1+50,i_y1+30,font=('chiller',50),text=list[0])
    c2.create_text(i_x1+100,i_y1+60,font=('arial',20),text=list[1])
    c2.create_text(i_x1+110,i_y1+55,font=('times new roman',19),text=list[2])
    c2.create_text(i_x1+150,i_y1+55,font=('verdana',34),text=list[3])
    c2.create_text(i_x1+170,i_y1+55,font=('forte',40),text=list[4])
    c2.create_text(i_x1+210,i_y1+20,font=('calibri',24),text=list[5])
    global value
    value=Entry(c2,bg='white')
    c2.create_window(210,200,window=value,height=30,width=150)
    
    check=Button(c2,text='check',bg='pink',command=captcha)
    c2.create_window(180,230,window=check,width=50)
    c2.update()
    refresh=Button(c2,text='another',bg='aqua',command=captcha)
    c2.create_window(240,230,window=refresh,width=50)
    c2.update()
    global verify
    verify=Entry(c2,bg='white',fg='red')
    c2.create_window(210,260,window=verify,height=30,width=150)
    c2.update()
    verify.insert(0,'Match Not Found')
    
            
c1=Canvas(master,bg='dark khaki',height='300',width='440')
c1.pack(side='left',anchor='n')
def verify():
    e3.delete(0,END)
    user=e1.get()
    password=e2.get()
    if(user=='user' and password=='user123'):
        e3.insert(0,'Matched')
        showinfo("Credentials","Matched")
        global count
        count=count+1
       # print count
        phase1()
        #phase2()
    else:
        showwarning("Credentials",'Wrong')
        e3.insert(0,'Not Matched')
        


l1=Label(c1,text='Username(user)',fg='red')
c1.create_window(45,25,window=l1,height=30)
c1.update()
l2=Label(c1,text='Password(user123)',fg='blue')
c1.create_window(50,60,window=l2,height=30)
c1.update()

e1=Entry(c1)
c1.create_window(200,25,window=e1,height=30,width=200)
c1.update()
e2=Entry(c1)
c1.create_window(200,60,window=e2,height=30,width=200)
c1.update()
b=Button(c1,text='Submit',width='10',command=verify)
c1.create_window(182,140,window=b,height=30)
l3=Label(c1,text='Match')
c1.create_window(50,95,window=l3,height=30)
c1.update()
e3=Entry(c1)
e3.insert(0,'Not Matched')
c1.create_window(200,95,window=e3,height=30,width=200)
mainloop()

image()
