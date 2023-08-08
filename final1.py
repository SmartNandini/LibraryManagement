import tkinter as tk
from tkinter import messagebox
def show_frame(frame):
   frame.tkraise() 
window=tk.Tk()
window.state('zoomed')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
frame1=tk.Frame(window,bg='Turquoise')
frame4=tk.Frame(window,bg='spring green')
frame5=tk.Frame(window,bg='spring green')
frame6=tk.Frame(window,bg='spring green')
frame7=tk.Frame(window,bg='Turquoise')
frame8=tk.Frame(window,bg='spring green')
frame9=tk.Frame(window,bg='spring green')
frame10=tk.Frame(window,bg='spring green')
frame11=tk.Frame(window,bg='spring green')
frame12=tk.Frame(window,bg='spring green')
frame13=tk.Frame(window,bg='spring green')
frame14=tk.Frame(window,bg='spring green')
frame15=tk.Frame(window,bg='spring green')
frame16=tk.Frame(window,bg='spring green')
frame17=tk.Frame(window,bg='spring green')
frame18=tk.Frame(window,bg='spring green')
frame19=tk.Frame(window,bg='spring green')
frame20=tk.Frame(window,bg='spring green')
frame21=tk.Frame(window,bg='spring green')
frame22=tk.Frame(window,bg='spring green')
frame23=tk.Frame(window,bg='spring green')
for frame in (frame1,frame4,frame5,frame6,frame7,frame8,frame9,frame10,frame11,frame12,frame13,frame14,frame15,frame16,frame17,frame18,frame19,frame20,frame21,frame22,frame23):
    frame.grid(row=0,column=0,sticky='nsew')
    
#==========Frame 1 code==========login and registration/sign-in
frame1_title=tk.Label(frame1,text='Home page',bg='deeppink2')
frame1_title.pack(fill='x')
frame1_btn=tk.Button(frame1,text='Login',command=lambda:show_frame(frame4))
frame12_btn=tk.Button(frame1,text='Sign-in',command=lambda:show_frame(frame5))
frame14_btn= tk.Button(frame1, text="QUIT", fg="red",command=quit)
frame1_btn.pack()
frame12_btn.pack()
frame14_btn.pack()


#==========Frame 4 code==========login page
frame4_title=tk.Label(frame4,text='Login-Page',bg='deeppink')
frame4_title.pack(fill='x')
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
   import tkinter as tk
   cu=frame42_btn.get()
   du=frame44_btn.get()
   tup=(cu,du)
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   st="SELECT user_name,password FROM users"
   cursor=con_obj.cursor()
   cursor.execute(st)
   data=cursor.fetchall()
   for namepass in data:
      if namepass==tup:
         show_frame(frame7)
   if tup not in data:
      show_frame(frame1)
      messagebox.showinfo("Message", "You have not registered !\n Sign in to register.")
   con_obj.close()
frame41_label=tk.Label(frame4,text='Username')
frame42_btn=tk.Entry(frame4,text='name_var')
frame43_label=tk.Label(frame4,text='Password')
frame44_btn=tk.Entry(frame4,text='passw_var', show = '*')
sub_btn=tk.Button(frame4,text = 'Submit', command =lambda:submit())
frame45_btn=tk.Button(frame4,text='Back to home page',command=lambda:show_frame(frame1))
frame41_label.pack()
frame42_btn.pack()
frame43_label.pack()
frame44_btn.pack()
sub_btn.pack()
frame45_btn.pack()

#==========Frame 5 code==========signin page
frame5_title=tk.Label(frame5,text='Sign-in Page',bg='deeppink')
frame5_title.pack(fill='x')
frame5_btn=tk.Button(frame5,text='Back to home page',command=lambda:show_frame(frame1))
import mysql.connector as sqltor
con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
sb=tk.StringVar()
sc=tk.StringVar()
se=tk.StringVar()
sf=tk.StringVar()
sg=tk.StringVar()
si=tk.StringVar()

def submit1():
   import tkinter as tk
   sa=frame52_btn.get()
   sb=frame54_btn.get()
   sc=frame56_btn.get()
   sd=frame58_btn.get()
   se=frame510_btn.get()
   sf=frame512_btn.get()
   sg=frame514_btn.get()
   sh=frame516_btn.get()
   si=frame518_btn.get()
   st="INSERT INTO users(user_ID,user_type,user_name,phone_no,address,email,identification_type,identification_no,password) VALUES({},'{}','{}',{},'{}','{}','{}',{},'{}')".format(sa,sb,sc,sd,se,sf,sg,sh,si)
   cursor=con_obj.cursor()
   cursor.execute(st)
   con_obj.commit()
   con_obj.close()

frame51_label=tk.Label(frame5,text='user_ID')
frame52_btn=tk.Entry(frame5,text='sa')
frame53_label=tk.Label(frame5,text='user_type')
frame54_btn=tk.Entry(frame5,text='sb')
frame55_label=tk.Label(frame5,text='user_name')
frame56_btn=tk.Entry(frame5,text='sc')
frame57_label=tk.Label(frame5,text='phone_no')
frame58_btn=tk.Entry(frame5,text='sd')
frame59_label=tk.Label(frame5,text='address')
frame510_btn=tk.Entry(frame5,text='se')
frame511_label=tk.Label(frame5,text='email')
frame512_btn=tk.Entry(frame5,text='sf')
frame513_label=tk.Label(frame5,text='identification_type')
frame514_btn=tk.Entry(frame5,text='sg')
frame515_label=tk.Label(frame5,text='identification_no')
frame516_btn=tk.Entry(frame5,text='sh')
frame517_label=tk.Label(frame5,text='password')
frame518_btn=tk.Entry(frame5,text='si')
sub1_btn=tk.Button(frame5,text = 'Submit1', command = submit1)
sub0_btn=tk.Button(frame5,text = 'Login-in', command=lambda:show_frame(frame4))

frame5_btn.pack()
frame51_label.pack()
frame52_btn.pack()
frame53_label.pack()
frame54_btn.pack()
frame55_label.pack()
frame56_btn.pack()
frame57_label.pack()
frame58_btn.pack()
frame59_label.pack()
frame510_btn.pack()
frame511_label.pack()
frame512_btn.pack()
frame513_label.pack()
frame514_btn.pack()
frame515_label.pack()
frame516_btn.pack()
frame517_label.pack()
frame518_btn.pack()
sub1_btn.pack()
sub0_btn.pack()

#========== Frame 6 ==========Add Book Page
frame6_title=tk.Label(frame6,text='Add Book !',bg='deeppink')
frame6_title.pack(fill='x')
import mysql.connector as sqltor
con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()
d=tk.StringVar()
e=tk.StringVar()
f=tk.StringVar()
g=tk.StringVar()
h=tk.StringVar()
i=tk.StringVar()
j=tk.StringVar()
k=tk.StringVar()
def submit2():
   import tkinter as tk
   a=ne1.get()
   b=ne2.get()
   c=ne3.get()
   d=ne4.get()
   e=ne5.get()
   f=ne6.get()
   g=ne7.get()
   h=ne8.get()
   i=ne9.get()
   j=ne10.get()
   k=ne11.get()
   st="INSERT INTO BOOK_DETAILS(BOOK_CODE,TITLE,CATEGORY,AUTHOR,PUBLICATION,PUBLISH_DATE,EDITION,PRICE,RACK_NO,ARRIVAL_DATE,SUPPLIER_ID) VALUES('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".format(a,b,c,d,e,f,g,h,i,j,k)
   cursor=con_obj.cursor()
   cursor.execute(st)
   con_obj.commit()
   con_obj.close()
   messagebox.showinfo("Message","Book Added !")
frf1=tk.Button(frame6,text='Back to home page',command=lambda:show_frame(frame1))
frg1=tk.Button(frame6,text='Back',command=lambda:show_frame(frame8))
nl1 = tk.Label(frame6, text = 'Book Code', font=('calibre',10, 'bold'))
ne1 = tk.Entry(frame6,textvariable = a, font=('calibre',10,'normal'))
nl2 = tk.Label(frame6, text = 'Title', font=('calibre',10, 'bold'))
ne2 = tk.Entry(frame6,textvariable = b, font=('calibre',10,'normal'))
nl3 = tk.Label(frame6, text = 'Category', font=('calibre',10, 'bold'))
ne3 = tk.Entry(frame6,textvariable = c, font=('calibre',10,'normal'))
nl4 = tk.Label(frame6, text = 'Author', font=('calibre',10, 'bold'))
ne4 = tk.Entry(frame6,textvariable = d, font=('calibre',10,'normal'))
nl5 = tk.Label(frame6, text = 'Publication', font=('calibre',10, 'bold'))
ne5 = tk.Entry(frame6,textvariable = e, font=('calibre',10,'normal'))
nl6 = tk.Label(frame6, text = 'Publish Date', font=('calibre',10, 'bold'))
ne6 = tk.Entry(frame6,textvariable = f, font=('calibre',10,'normal'))
nl7 = tk.Label(frame6, text = 'Edition', font=('calibre',10, 'bold'))
ne7 = tk.Entry(frame6,textvariable = g, font=('calibre',10,'normal'))
nl8 = tk.Label(frame6, text = 'Price', font=('calibre',10, 'bold'))
ne8 = tk.Entry(frame6,textvariable = h, font=('calibre',10,'normal'))
nl9 = tk.Label(frame6, text = 'Rack no', font=('calibre',10, 'bold'))
ne9 = tk.Entry(frame6,textvariable = i, font=('calibre',10,'normal'))
nl10 = tk.Label(frame6, text = 'Arrival Date', font=('calibre',10, 'bold'))
ne10 = tk.Entry(frame6,textvariable = j, font=('calibre',10,'normal'))
nl11 = tk.Label(frame6, text = 'Supplier ID', font=('calibre',10, 'bold'))
ne11= tk.Entry(frame6,textvariable = k, font=('calibre',10,'normal'))
sub_btn=tk.Button(frame6,text = 'Submit', command = submit2)
frf1.pack()
frg1.pack()
nl1.pack()
ne1.pack()
nl2.pack()
ne2.pack()
nl3.pack()
ne3.pack()
nl4.pack()
ne4.pack()
nl5.pack()
ne5.pack()
nl6.pack()
ne6.pack()
nl7.pack()
ne7.pack()
nl8.pack()
ne8.pack()
nl9.pack()
ne9.pack()
nl10.pack()
ne10.pack()
nl11.pack()
ne11.pack()
sub_btn.pack()

#==========Frame 7 code==========Button which is ia program runned along with submit in the login page
frame7_title=tk.Label(frame7,text='Types of functions',bg='Orange')
frame7_title.pack(fill='x')
frame7_btn=tk.Button(frame7,text='Book Data',command=lambda:show_frame(frame8))
frame71_btn=tk.Button(frame7,text='Members',command=lambda:show_frame(frame9))
frame72_btn=tk.Button(frame7,text='Issue/Return Book',command=lambda:show_frame(frame10))
frame73_btn=tk.Button(frame7,text='Users(only for admin)',command=lambda:show_frame(frame11))
frf2=tk.Button(frame7,text='Back to home page',command=lambda:show_frame(frame1))
frame7_btn.pack()
frame71_btn.pack()
frame72_btn.pack()
frame73_btn.pack()
frf2.pack()

#==========Frame 8 code==========Button which is ia program runned along with submit in the login page
frame8_title=tk.Label(frame8,text='Book Data',bg='chocolate2')
frame8_title.pack(fill='x')
frame8_btn=tk.Button(frame8,text='Add Book',command=lambda:show_frame(frame6))
frame81_btn=tk.Button(frame8,text='Update Book',command=lambda:show_frame(frame14))
frame82_btn=tk.Button(frame8,text='Delete Book',command=lambda:show_frame(frame13))
frame83_btn=tk.Button(frame8,text='Search Book',command=lambda:show_frame(frame12))
frf3=tk.Button(frame8,text='Back to home page',command=lambda:show_frame(frame1))
frw1=tk.Button(frame8,text='Back',command=lambda:show_frame(frame7))
frame8_btn.pack()
frame81_btn.pack()
frame82_btn.pack()
frame83_btn.pack()
frf3.pack()
frw1.pack()

#==========Frame 9 code==========Button which is ia program runned along with submit in the login page
frame9_title=tk.Label(frame9,text='Members',bg='chocolate2')
frame9_title.pack(fill='x')
frame9_btn=tk.Button(frame9,text='Add Member',command=lambda:show_frame(frame15))
frame91_btn=tk.Button(frame9,text='Remove member',command=lambda:show_frame(frame16))
frf4=tk.Button(frame9,text='Back to home page',command=lambda:show_frame(frame1))
frw2=tk.Button(frame9,text='Back',command=lambda:show_frame(frame7))
frame9_btn.pack()
frame91_btn.pack()
frf4.pack()
frw2.pack()

#==========Frame 10 code==========Button which is ia program runned along with submit in the login page
frame10_title=tk.Label(frame10,text='Issue/Return Book',bg='chocolate2')
frame10_title.pack(fill='x')
frame10_btn=tk.Button(frame10,text='Issue',command=lambda:show_frame(frame17))
frame101_btn=tk.Button(frame10,text='Return',command=lambda:show_frame(frame18))
frf5=tk.Button(frame10,text='Back to home page',command=lambda:show_frame(frame1))
frw3=tk.Button(frame10,text='Back',command=lambda:show_frame(frame7))
frame10_btn.pack()
frame101_btn.pack()
frf5.pack()
frw3.pack()

#==========Frame 11 code==========users(only for admin)
frame11_title=tk.Label(frame11,text='Users(only for admin)',bg='chocolate2')
frame11_title.pack(fill='x')
frame11_btn=tk.Button(frame11,text='User data',command=lambda:show_frame(frame19))
frame111_btn=tk.Button(frame11,text='Search user',command=lambda:show_frame(frame20))
frf6=tk.Button(frame11,text='Back to home page',command=lambda:show_frame(frame1))
frw4=tk.Button(frame11,text='Back',command=lambda:show_frame(frame7))
frame11_btn.pack()
frame111_btn.pack()
frf6.pack()
frw4.pack()

#==========Frame 12 code==========search book
frame12_title=tk.Label(frame12,text='Search Book',bg='deeppink')
frame12_title.pack(fill='x')
frf7=tk.Button(frame12,text='Back to home page',command=lambda:show_frame(frame1))
frf7.pack()
frg2=tk.Button(frame12,text='Back',command=lambda:show_frame(frame8))
frg2.pack()
choice=0
def search1(x):
   global choice
   choice=x
   def subit1():
      btt=m2.get()
      length=len(btt)
      import mysql.connector as sqltor
      con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
      cursor=con_obj.cursor()
      st2="SELECT * FROM BOOK_DETAILS WHERE TITLE LIKE '{}'".format(btt+'%')
      cursor.execute(st2)
      data=cursor.fetchall()
      for record in data:
         if record[1][0:length]==btt:
            searchlabel1=tk.Label(frame12,text=record)
            searchlabel1.pack()
      else:
         from tkinter import messagebox
         messagebox.showinfo("Message", "No such data !")
         #searchlabel1=tk.Label(frame12,text="No such data")
         #searchlabel1.pack()
   def subit2():
      bta=m4.get()
      length=len(bta)
      import mysql.connector as sqltor
      con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
      cursor=con_obj.cursor()
      st2="SELECT * FROM BOOK_DETAILS WHERE AUTHOR LIKE '{}'".format(bta+'%')
      cursor.execute(st2)
      data=cursor.fetchall()
      for record in data:
         if record[3][0:length]==bta:
            searchlabel1=tk.Label(frame12,text=record)
            searchlabel1.pack()
      else:
         from tkinter import messagebox
         messagebox.showinfo("Message", "No such data !")
         #searchlabel1=tk.Label(frame12,text="No such data")
         #searchlabel1.pack()
      
      
   if choice==1:
      qa=tk.StringVar()
      m1 = tk.Label(frame12, text = 'Book Title', font=('calibre',10, 'bold'))
      m2 = tk.Entry(frame12,textvariable =qa, font=('calibre',10,'normal'))
      sub_btn=tk.Button(frame12,text = 'Submit', command = subit1)
      m1.pack()
      m2.pack()
      sub_btn.pack()
   if choice==2:
      qb=tk.StringVar()
      m3 = tk.Label(frame12, text = 'Book Author', font=('calibre',10, 'bold'))
      m4 = tk.Entry(frame12,textvariable = qb, font=('calibre',10,'normal'))
      sub_btn=tk.Button(frame12,text = 'Submit', command = subit2)
      cursor=con_obj.cursor()
      m3.pack()
      m4.pack()
      sub_btn.pack()
frame121_btn=tk.Button(frame12,text='SearchbyBook_Title',command=lambda:search1(1))
frame122_btn=tk.Button(frame12,text='Search by Book_Author',command=lambda:search1(2))
frame121_btn.pack()
frame122_btn.pack()


#==========Frame 13 code==========delete book
frame13_title=tk.Label(frame13,text='Delete Book',bg='deeppink')
frame13_title.pack(fill='x')
frf8=tk.Button(frame13,text='Back to home page',command=lambda:show_frame(frame1))
frf8.pack()
frg3=tk.Button(frame13,text='Back',command=lambda:show_frame(frame8))
frg3.pack()
Book_code3=tk.StringVar()
def submit3():
   token=m41.get()
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   cursor=con_obj.cursor()
   st="DELETE FROM BOOK_DETAILS WHERE BOOK_CODE='{}'".format(token)
   cursor.execute(st)
   con_obj.commit()
   con_obj.close()
   messagebox.showinfo("Message", "Book deleted !")
m31 = tk.Label(frame13, text = 'Bookcode', font=('calibre',10, 'bold'))
m41 = tk.Entry(frame13,textvariable = Book_code3, font=('calibre',10,'normal'))
m31.pack()
m41.pack()
sub_btn=tk.Button(frame13,text = 'Submit', command = submit3)
sub_btn.pack()

#==========Frame 14 code==========update book
frame14_title=tk.Label(frame14,text='Update Book',bg='deeppink')
frame14_title.pack(fill='x')
frf9=tk.Button(frame14,text='Back to home page',command=lambda:show_frame(frame1))
frf9.pack()
frg4=tk.Button(frame14,text='Back',command=lambda:show_frame(frame8))
frg4.pack()
dic={1:'TITLE',2:'CATEGORY',3:'AUTHOR',4:'PUBLICATION',5:'PUBLISH_DATE',6:'EDITION',7:'PRICE',8:'RACK_NO',9:'ARRIVAL_DATE',10:'SUPPLIER_ID'}
loop_const=True
while loop_const==True:
   import tkinter as tk
   num=0
   dicc=dic.keys()
   for i in dicc:
      num=num+1
      frame142_label=tk.Label(frame14,text=(str(num)+'.'+' '+dic[i]))
      frame142_label.pack()
   loop_const=False
   
hy=tk.StringVar()
frame141_label=tk.Label(frame14,text='Book Code')
frame141_btn=tk.Entry(frame14,text='hy')
frame141_label.pack()
frame141_btn.pack()
   
def updatenewdata1():
   xw=frame141_btn.get()
   xww=frame143_btn.get()
   xww=int(xww)
   vvc=dic[xww]
   bww=frame145_btn.get()
   if xww==6 or xww==7:
      bww=int(bww)
      st="UPDATE BOOK_DETAILS SET {}={} WHERE BOOK_CODE='{}'".format(vvc,bww,xw)
   else:
      st="UPDATE BOOK_DETAILS SET {}='{}' WHERE BOOK_CODE='{}'".format(vvc,bww,xw)
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="SkyBlue@2021",database="comproj12")
   cursor=con_obj.cursor()
   cursor.execute(st)
   con_obj.commit()
   con_obj.close()
   messagebox.showinfo("Message", "Data updated !")

xww=0
frame143_label=tk.Label(frame14,text='Enter your choice(numerical)')
frame143_btn=tk.Entry(frame14,text='xww')
frame143_label.pack()
frame143_btn.pack()
bww=tk.StringVar()
frame145_label=tk.Label(frame14,text='Enter New Data')
frame145_btn=tk.Entry(frame14,text='bww')
sub_btn=tk.Button(frame14,text = 'Submit', command = updatenewdata1)
frame145_label.pack()
frame145_btn.pack()
sub_btn.pack()

#==========Frame 15 code==========add member
frame15_title=tk.Label(frame15,text='Add Member',bg='deeppink')
frame15_title.pack(fill='x')
frf10=tk.Button(frame15,text='Back to home page',command=lambda:show_frame(frame1))
frf10.pack()
frg5=tk.Button(frame15,text='Back',command=lambda:show_frame(frame9))
frg5.pack()
import mysql.connector as sqltor
con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
pa=tk.StringVar()
pb=tk.StringVar()
pd=tk.StringVar()
pe=tk.StringVar()
pf=tk.StringVar()

def submit4():
    #import datetime module
   import tkinter as tk
   pa=frame152_btn.get()
   pb=frame154_btn.get()
   pc=frame156_btn.get()
   pd=frame158_btn.get()
   pe=frame1510_btn.get()
   pf=frame1512_btn.get()
   pg=frame1514_btn.get()
   #cudate= grt current date like this
   #now = datetime.now()
   #nd=now.strftime('%Y-%m-%d %H:%M:%S')
   #ne=datetime.strptime(nd,"%Y-%m-%d %H:%M:%S")
   #ne=ne+timedelta(days=365)
   #ne=ne.strftime('%Y-%m-%d %H:%M:%S')
   #add the variables into the following string st
   st="INSERT INTO MEMBER(MEMBER_ID,NAME,PHONE_NO,ADDRESS,EMAIL,IDENTIFICATION_TYPE,IDENTIFICATION_NO) VALUES('{}','{}',{},'{}','{}','{}',{})".format(pa,pb,pc,pd,pe,pf,pg)
   cursor=con_obj.cursor()
   cursor.execute(st)
   con_obj.commit()
   con_obj.close()
   messagebox.showinfo("Message", "Member Added !")

frame151_label=tk.Label(frame15,text='MEMBER_ID')
frame152_btn=tk.Entry(frame15,text='pa')
frame153_label=tk.Label(frame15,text='NAME')
frame154_btn=tk.Entry(frame15,text='pb')
frame155_label=tk.Label(frame15,text='PHONE_NO')
frame156_btn=tk.Entry(frame15,text='pc')
frame157_label=tk.Label(frame15,text='ADDRESS')
frame158_btn=tk.Entry(frame15,text='pd')
frame159_label=tk.Label(frame15,text='EMAIL')
frame1510_btn=tk.Entry(frame15,text='pe')
frame1511_label=tk.Label(frame15,text='IDENTIFICATION_TYPE')
frame1512_btn=tk.Entry(frame15,text='pf')
frame1513_label=tk.Label(frame15,text='IDENTIFICATION_NO')
frame1514_btn=tk.Entry(frame15,text='pg')
sub_btn=tk.Button(frame15,text = 'Submit', command = submit4)

frame151_label.pack()
frame152_btn.pack()
frame153_label.pack()
frame154_btn.pack()
frame155_label.pack()
frame156_btn.pack()
frame157_label.pack()
frame158_btn.pack()
frame159_label.pack()
frame1510_btn.pack()
frame1511_label.pack()
frame1512_btn.pack()
frame1513_label.pack()
frame1514_btn.pack()
sub_btn.pack()




#==========Frame 16 code==========remove member
frame16_title=tk.Label(frame16,text='Remove Member',bg='deeppink')
frame16_title.pack(fill='x')
frf11=tk.Button(frame16,text='Back to home page',command=lambda:show_frame(frame1))
frf11.pack()
frg6=tk.Button(frame16,text='Back',command=lambda:show_frame(frame9))
frg6.pack()
memid=tk.StringVar()
def submit5():
   jd=m162.get()
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   cursor=con_obj.cursor()
   st="DELETE FROM MEMBER WHERE Member_ID='{}'".format(jd)
   cursor.execute(st)
   con_obj.commit()
   con_obj.close()
   messagebox.showinfo("Message", "Member Removed !")
m161 = tk.Label(frame16, text = 'Member ID', font=('calibre',10, 'bold'))
m162 = tk.Entry(frame16,textvariable = memid, font=('calibre',10,'normal'))
m161.pack()
m162.pack()
sub_btn=tk.Button(frame16,text = 'Submit', command = submit5)
sub_btn.pack()

#==========Frame 17 code==========issue book
frame17_title=tk.Label(frame17,text='Issue Book',bg='deeppink')
frame17_title.pack(fill='x')
frf12=tk.Button(frame17,text='Back to home page',command=lambda:show_frame(frame1))
frf12.pack()
frg7=tk.Button(frame17,text='Back',command=lambda:show_frame(frame10))
frg7.pack()
iss1=tk.StringVar()
iss2=tk.StringVar()
iss3=tk.StringVar()
def submit6():
    #st3=expiry_date from member where member_id=yb
    #cursor.execute(st3)
    #data2=cursor.execute
    #if today's date > expiry date in data2
    #i.e. ne>data2
    #do not run the program, show a message and go back to frame
    #elserun the following program
   yb=nbe.get()
   yc=nce.get()
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   cursor=con_obj.cursor()
   st2="SELECT Return_Date FROM issue_return WHERE Book_ID='{}'".format(yc)
   cursor.execute(st2)
   data1=cursor.fetchall()
   if data1==[]:  
      con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
      st="INSERT INTO ISSUE_RETURN(Membership_ID,Book_ID,Issue_date,Due_date,Return_date,Charges,Fine) VALUES('{}','{}','{}','{}','{}',{},{})".format(yb,yc,nd,ne,nf,ng,nh)
      cursor=con_obj.cursor()
      cursor.execute(st)
      con_obj.commit()
      con_obj.close()
      messagebox.showinfo("Message", "Book issued ! \n This book is issued for first time.")
   else:
      for i in data1:
         if i==(None,):
            messagebox.showinfo("Message", "Book cannot be issued!")
            break
         if (None,) not in data1:
            con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
            st="INSERT INTO ISSUE_RETURN(Membership_ID,Book_ID,Issue_date,Due_date,Return_date,Charges,Fine) VALUES('{}','{}','{}','{}','{}',{},{})".format(yb,yc,nd,ne,nf,ng,nh)
            cursor=con_obj.cursor()
            cursor.execute(st)
            con_obj.commit()
            con_obj.close()
            messagebox.showinfo("Message", "Book Issued !")
            break

from datetime import datetime,timedelta
nbl=tk.Label(frame17, text = 'Membership ID', font=('calibre',10, 'bold'))
nbe=tk.Entry(frame17,textvariable = iss2, font=('calibre',10,'normal'))
ncl=tk.Label(frame17, text = 'Book ID', font=('calibre',10, 'bold'))
nce=tk.Entry(frame17,textvariable = iss3, font=('calibre',10,'normal'))
now = datetime.now()
nd=now.strftime('%Y-%m-%d %H:%M:%S')
ne=datetime.strptime(nd,"%Y-%m-%d %H:%M:%S")
ne=ne+timedelta(days=14)
ne=ne.strftime('%Y-%m-%d %H:%M:%S')
nf='0000-00-00 00:00:00'
ng=0
nh=0.0
sub_btn=tk.Button(frame17,text = 'Submit', command = submit6)
nbl.pack()
nbe.pack()
ncl.pack()
nce.pack()
sub_btn.pack()
#==========Frame 18 code==========return book
frame18_title=tk.Label(frame18,text='Return Book',bg='deeppink')
frame18_title.pack(fill='x')
frf13=tk.Button(frame18,text='Back to home page',command=lambda:show_frame(frame1))
frf13.pack()
frg8=tk.Button(frame18,text='Back',command=lambda:show_frame(frame10))
frg8.pack()
frame18_btn=tk.Button(frame18,text='Return',command=lambda:show_frame(frame3))
frame18_btn.pack()
cat=tk.StringVar()
def submit7():
   yd=cae.get()
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   if con_obj.is_connected():
      print("Succesfully connected to MySql dtabase")
   cursor=con_obj.cursor()
   from datetime import datetime
   now = datetime.now()
   d = now.strftime('%Y-%m-%d %H:%M:%S')
   st="UPDATE issue_return SET Return_date='{}' WHERE (BOOK_ID='{}' AND Return_date='{}') ".format(d,yd,'0000-00-00 00:00:00')
   cursor.execute(st)
   con_obj.commit()
   cursor=con_obj.cursor()
   st="SELECT Due_date from issue_return WHERE Book_ID='{}'".format(yd)
   cursor.execute(st)
   data=cursor.fetchone()
   #data=(data)
   for i in data:
      due_dt=i
      due_dt1=due_dt.date()
   return_dt=datetime.strptime(d,"%Y-%m-%d %H:%M:%S")
   return_dt1=return_dt.date()
   x=return_dt1-due_dt1
   from datetime import datetime,timedelta
   e=x+timedelta(days=-14)
   x=x.days
   if x>0:
      fine=x*1
      st="UPDATE issue_return SET Fine='{}' WHERE (BOOK_ID='{}' AND Return_date='{}') ".format(fine,yd,return_dt)
      cursor=con_obj.cursor()
      cursor.execute(st)
      con_obj.commit()
      print("Rs ",fine,"/- Fine Added !")
      con_obj.close()
   con_obj.close()
   messagebox.showinfo("Message", "Book Returned !")

cal=tk.Label(frame18, text = 'Book ID', font=('calibre',10, 'bold'))
cae=tk.Entry(frame18,textvariable = cat, font=('calibre',10,'normal'))
sub_btn=tk.Button(frame18,text = 'Submit', command = submit7)
cal.pack()
cae.pack()
sub_btn.pack()

#==========Frame 19 code==========users data
frame19_title=tk.Label(frame19,text='User Data',bg='deeppink')
frame19_title.pack(fill='x')
frf14=tk.Button(frame19,text='Back to home page',command=lambda:show_frame(frame1))
frf14.pack()
frg9=tk.Button(frame19,text='Back',command=lambda:show_frame(frame11))
frg9.pack()
frame19_btn=tk.Button(frame19,text='Display each row/data from the users table',command=lambda:show_frame(frame3))
frame19_btn.pack()
def check(username,password):
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   cursor=con_obj.cursor()
   st="SELECT user_type from users WHERE user_name= '{}' and password ='{}'".format(username,password)
   cursor.execute(st)
   data=cursor.fetchone()
   for usertype in data:
      if usertype=='admin':
         messagebox.showinfo("Message", "You are the admin. \n Access allowed.")
         return True
      else:
         return False

   con_obj.close()


name_var1=tk.StringVar()
passw_var1=tk.StringVar()
def submit8():
   import tkinter as tk
   cu=frame191_btn.get()
   du=frame192_btn.get()
   tup=(cu,du)
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   st="SELECT user_name,password FROM users"
   cursor=con_obj.cursor()
   cursor.execute(st)
   data=cursor.fetchall()
   for namepass in data:
      if namepass==tup:
         p=check(cu,du)
         if p==True:
            cursor=con_obj.cursor()
            st1="SELECT * FROM users"
            cursor.execute(st1)
            data=cursor.fetchall()
            for row in data:
               gk=tk.Label(frame19,text=row)
               gk.pack()
         else:
            show_frame(frame1)
            messagebox.showinfo("Message", "You are not the admin. \n Access denied.")
   con_obj.close()
   
frame191_label=tk.Label(frame19,text='Username')
frame191_btn=tk.Entry(frame19,text='name_var1')
frame192_label=tk.Label(frame19,text='Password')
frame192_btn=tk.Entry(frame19,text='passw_var1', show = '*')
sub_btn=tk.Button(frame19,text = 'Submit', command =lambda:submit8())
frame191_label.pack()
frame191_btn.pack()
frame192_label.pack()
frame192_btn.pack()
sub_btn.pack()
#==========Frame 20 code==========search user
frame20_title=tk.Label(frame20,text='Search User',bg='deeppink')
frame20_title.pack(fill='x')
frf15=tk.Button(frame20,text='Back to home page',command=lambda:show_frame(frame1))
frf15.pack()
frg10=tk.Button(frame20,text='Back',command=lambda:show_frame(frame11))
frg10.pack()
frame20_btn=tk.Button(frame20,text='Search User by category-admin,librarian,customer',command=lambda:show_frame(frame3))
frame20_btn.pack()

def search_user(n):
   if n==1:
      import tkinter as tk
      vt=frame211_btn.get()
      import mysql.connector as sqltor
      con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
      st="SELECT * FROM users WHERE user_type= '{}'".format(vt)
      cursor=con_obj.cursor()
      cursor.execute(st)
      data=cursor.fetchall()
      for row in data:
         ok=tk.Label(frame21,text=row)
         ok.pack()
         con_obj.close()
   if n==2:
      import tkinter as tk
      vr=frame221_btn.get()
      import mysql.connector as sqltor
      con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
      st="SELECT * FROM users WHERE user_name= '{}'".format(vr)
      cursor=con_obj.cursor()
      cursor.execute(st)
      data=cursor.fetchall()
      for row in data:
         ok=tk.Label(frame22,text=row)
         ok.pack()
         con_obj.close()
name_var2=tk.StringVar()
passw_var2=tk.StringVar()
frame201_label=tk.Label(frame20,text='Username')
frame201_btn=tk.Entry(frame20,text='name_var2')
frame202_label=tk.Label(frame20,text='Password')
frame202_btn=tk.Entry(frame20,text='passw_var2', show = '*')
         
def newcheck():
   qq=frame201_btn.get()
   ii=frame202_btn.get()
   import mysql.connector as sqltor
   con_obj=sqltor.connect(host="localhost",user="root",passwd="Your password",database="comproj12")
   cursor=con_obj.cursor()
   st="SELECT user_type from users WHERE user_name= '{}' and password ='{}'".format(qq,ii)
   cursor.execute(st)
   data=cursor.fetchone()
   for usertype in data:
      if usertype=='admin':
         messagebox.showinfo("Message", "You are the admin. \n Access allowed.")
         show_frame(frame23)
      else:
         show_frame(frame1)
         messagebox.showinfo("Message", "You are not the admin. \n Access denied.")

   con_obj.close()

frame201_label.pack()
frame201_btn.pack()
frame202_label.pack()
frame202_btn.pack()
sub_btn=tk.Button(frame20,text = 'Submit', command =lambda:newcheck())
sub_btn.pack()

#==========Frame 23 code==========search user by user type
label=tk.Label(frame23,text='Search by:')
but1=tk.Button(frame23,text = 'User type', command =lambda:show_frame(frame21))
but2=tk.Button(frame23,text = 'User Name', command =lambda:show_frame(frame22))
frg11=tk.Button(frame23,text='Back',command=lambda:show_frame(frame20))
frf16=tk.Button(frame23,text='Back to home page',command=lambda:show_frame(frame1))
label.pack()
but1.pack()
but2.pack()
frg11.pack()
frf16.pack()
#==========Frame 21 code==========search user by user type
usertypez=tk.StringVar()
frf17=tk.Button(frame21,text='Back to home page',command=lambda:show_frame(frame1))
frf17.pack()
frg12=tk.Button(frame21,text='Back',command=lambda:show_frame(frame23))
frg12.pack()
frame211_label=tk.Label(frame21,text='User Type')
frame211_btn=tk.Entry(frame21,text='usertypez')
sub_btn=tk.Button(frame21,text = 'Submit', command =lambda:search_user(1))
frame211_label.pack()
frame211_btn.pack()
sub_btn.pack()
#==========Frame 22 code==========search user by user name
usernamez=tk.StringVar()
frf18=tk.Button(frame22,text='Back to home page',command=lambda:show_frame(frame1))
frf18.pack()
frg13=tk.Button(frame22,text='Back',command=lambda:show_frame(frame23))
frg13.pack()
frame221_label=tk.Label(frame22,text='User Name')
frame221_btn=tk.Entry(frame22,text='usernamez')
sub_btn=tk.Button(frame22,text = 'Submit', command =lambda:search_user(2))
frame221_label.pack()
frame221_btn.pack()
sub_btn.pack()

# run the program
show_frame(frame1)
window.mainloop()
