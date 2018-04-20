#------------------------------------------------------------- PYTHON PROJECT ------------------------------------------------------------

from tkinter import *
import tkinter
top=tkinter.Tk()
count=0

bookid=StringVar()
bookname=StringVar()
bookprice=StringVar()
bookauthor=StringVar()
bookpublisher=StringVar()

#--------------------------- FUNCTIONS -----------------------------------------------------------------

''' FUNCTION TO ADD BOOK DETAILS TO FILE '''

def Add_Book():
    f=open('C:/Users/Parth/Desktop/books.txt','a')
    bookid=E1.get()
    bookname=E2.get()
    bookprice=E3.get()
    bookauthor=E4.get()
    bookpublisher=E5.get()
    if(bookid=='' or bookname=='' or bookprice=='' or bookauthor=='' or bookpublisher==''):
        print("Details can't be empty!")
        exit()
    f.writelines(bookid.ljust(20)+bookname.ljust(20)+bookprice.ljust(20)+bookauthor.ljust(20)+bookpublisher.ljust(3)+"\n")
    print("Record added to file!")
    f.close()
    

''' FUNCTION TO DELETE BOOK DETAILS FROM FILE BY BOOKID '''

def Delete_Book():
    k=bookid.get()
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    f.close()
    f=open('C:/Users/Parth/Desktop/books.txt','w')
    for book in lines: 
        j=book.split()
        print(j)
        if(j[0]!=k): 
             f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
             print("Record deleted from the file!!")
    bookid.set("") 
    bookname.set("") 
    bookprice.set("") 
    bookauthor.set("") 
    bookpublisher.set("")
    f.close()


''' FUNCTION TO SEARCH BOOK DETAILS FROM FILE BY BOOKID '''
    
def Search_Book():
    k=bookid.get()
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    for book in lines: 
        j=book.split() 
        if(j[0]==k):   
            print(j) 
            bookid.set(j[0]) 
            bookname.set(j[1]) 
            bookprice.set(j[2]) 
            bookauthor.set(j[3]) 
            bookpublisher.set(j[4])
            flag=1
            break
    if(flag==0):
        print("Record not found!")
    else:
        print("Record found!")
    bookid.set("") 
    bookname.set("") 
    bookprice.set("") 
    bookauthor.set("") 
    bookpublisher.set("")
    f.close()


''' FUNCTION TO UPDATE BOOK DETAILS FROM FILE '''   

def Update_Book():
    new_id=bookid.get() 
    new_name=bookname.get() 
    new_price=bookprice.get() 
    new_author=bookauthor.get() 
    new_publisher=bookpublisher.get() 
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    ctr=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines() 
    f.close() 
    f=open('C:/Users/Parth/Desktop/books.txt','w') 
    for book in lines: 
        j=book.split() 
        if(j[0]!=new_id): 
            f.writelines(j[0].ljust(3)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n") 
     
        else: 
            f.writelines(j[0].ljust(3)+new_name.ljust(20)+new_price.ljust(20)+new_author.ljust(20)+new_publisher.ljust(5)+"\n")
    print("Record updated!!")
    bookid.set("") 
    bookname.set("") 
    bookprice.set("") 
    bookauthor.set("") 
    bookpublisher.set("")
    f.close()        


''' FUNCTION TO GET FIRST RECORD OF FILE '''

def Get_First_Record():
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print("\n")
    print(l)
    j=l[0].split()
    bookid.set(j[0])
    bookname.set(j[1]) 
    bookprice.set(j[2]) 
    bookauthor.set(j[3]) 
    bookpublisher.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()
    

''' FUNCTION TO GET LAST RECORD OF FILE '''
 
def Get_Last_Record():
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    ctr=0
    flag=0
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print(l)
    j=l[ctr-1].split()
    bookid.set(j[0])
    bookname.set(j[1]) 
    bookprice.set(j[2]) 
    bookauthor.set(j[3]) 
    bookpublisher.set(j[4])
    print("\n Last Record of file is as:")
    print(l[ctr-1])
    f.close()


''' FUNCTION TO GET EVERY PREVIOUS RECORD OF FILE '''

def Get_Prev_Record():
    global count 
    i=0
    ctr=0
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    try: 
         
        while(i<=count-1): 
            l=f.readline() 
            i=i+1 
 
        m=l.split() 
        bookid.set(m[0]) 
        bookname.set(m[1]) 
        bookprice.set(m[2]) 
        bookauthor.set(m[3]) 
        bookpublisher.set(m[4]) 
        print(m)
        
    except:
        bookid.set("") 
        bookname.set("") 
        bookprice.set("") 
        bookauthor.set("") 
        bookpublisher.set("")
        print("Sorry, no more records!")
    count=count-1 
    f.close()


''' FUNCTION TO GET EVERY NEXT RECORD OF FILE '''

def Get_Next_Record():
    global count 
    i=0
    ctr=0
    f=open('C:/Users/Parth/Desktop/books.txt','r')
    for line in f:
        ctr=ctr+1
    print("No. of lines in file:")    
    print(ctr)
    f.seek(0)
    try: 
         
        while(i<=count): 
            l=f.readline() 
            i=i+1 
 
        m=l.split() 
        bookid.set(m[0]) 
        bookname.set(m[1]) 
        bookprice.set(m[2]) 
        bookauthor.set(m[3]) 
        bookpublisher.set(m[4]) 
        print(m)
        
    except:
        bookid.set("") 
        bookname.set("") 
        bookprice.set("") 
        bookauthor.set("") 
        bookpublisher.set("")
        print("Sorry, no more records!")
    count=count+1 
    f.close()

#------------------------------------------------------------------------- GUI -----------------------------------------------------------------------------------    

top.configure(background="lightgreen")
#------------------------------ LABELS ----------------------------------------------------------
    
w = tkinter.Label(top, text="BOOK DETAILS",bg="yellow",font=('calibri',15,'bold'),underline=12).grid(row=0,column=1)
tkinter.Label(top, text="BOOK ID:",bg="lightyellow",font=('calibri',15,'bold')).grid(row=5,sticky=W)
tkinter.Label(top, text="BOOK NAME:",bg="lightyellow",font=('calibri',15,'bold')).grid(row=6,sticky=W)
tkinter.Label(top, text="BOOK PRICE:",bg="lightyellow",font=('calibri',15,'bold')).grid(row=7,sticky=W)
tkinter.Label(top, text="BOOK AUTHOR:",bg="lightyellow",font=('calibri',15,'bold')).grid(row=8,sticky=W)
tkinter.Label(top, text="BOOK PUBLISHER:",bg="lightyellow",font=('calibri',15,'bold')).grid(row=9,sticky=W)

#------------------------------ ENTRIES ---------------------------------------------------------

E1 = tkinter.Entry(top,textvariable=bookid)
E2 = tkinter.Entry(top,textvariable=bookname)
E3 = tkinter.Entry(top,textvariable=bookprice)
E4 = tkinter.Entry(top,textvariable=bookauthor)
E5 = tkinter.Entry(top,textvariable=bookpublisher)
E1.grid(row=5, column=1)
E2.grid(row=6, column=1)
E3.grid(row=7, column=1)
E4.grid(row=8, column=1)
E5.grid(row=9, column=1)

#------------------------------ BUTTONS -------------------------------------------------------------------

fr=tkinter.Button(top,text="|<",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Get_First_Record).grid(row=10, column=0)
pr=tkinter.Button(top,text="<",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Get_Prev_Record).grid(row=10, column=1)
nr=tkinter.Button(top,text=">",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Get_Next_Record).grid(row=10, column=2)
lr=tkinter.Button(top,text=">|",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Get_Last_Record).grid(row=10, column=3)

rb=tkinter.Button(top,text="ADD",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Add_Book).grid(row=11, column=0)
db=tkinter.Button(top,text="DELETE",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Delete_Book).grid(row=11, column=1)
sb=tkinter.Button(top,text="SEARCH",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Search_Book).grid(row=11, column=2)
ub=tkinter.Button(top,text="UPDATE",width=15,bg="lightblue",font=('Ariel',15,'bold'),command=Update_Book).grid(row=11, column=3)
top.mainloop()
