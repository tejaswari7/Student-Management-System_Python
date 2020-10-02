from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
import matplotlib.pyplot as plt
import socket
import bs4
import requests

res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'lxml')
quote = soup.find('img',{"class":"p-qotd"})
Quote = quote['alt']

try:
	cities=['thane']
	for city in cities:
		socket.create_connection(("www.google.com",80))
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q="+city
		a3="&appid=c6e315d09197cec231495138183954bd"
		api_address=a1+a2+a3
		res1=requests.get(api_address)
		data=res1.json()
		main=data['main']
		temp=main['temp']

except OSError:
	messagebox.showerror("Error", "Check Network")

root = Tk()
root.title("Student Management System")
root.geometry("750x500+300+50")
root.resizable(False,False)

def f1():
	root.withdraw()
	addst.deiconify()	
def f2():
	addst.withdraw()
	root.deiconify()	
def f3():
	root.withdraw()
	viewst.deiconify()
	stData.delete('1.0',END)
	import cx_Oracle
	con = None 
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "select distinct * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "R: " + str(d[0]) + " N: " + str(d[1]) + " Marks: " + str(d[2]) +  "\n"
		stData.insert(INSERT , msg)
	except cx_Oracle.DatabaseError as e:
		print("some issue ",e)
	finally:	
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f4():
	viewst.withdraw()
	root.deiconify()	
def f5():
	import cx_Oracle
	con = None 
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		rno = int(entARno.get())
		name = entAName.get()
		marks = int(entAMarks.get())
		 	
		if(rno <= 0):
			entARno.delete(0, END)
			entARno.focus()
			raise Exception("Roll No should be > 0")
			rno = int(entARno.get())

		if(name.isalnum() or name.isalnum() != True):
			if(len(name)<2):
				entAName.delete(0, END)
				entAName.focus()
				raise Exception("Name cannot be less < 2 ")

			elif(name.isalpha() != True ):
				entAName.delete(0, END)
				entAName.focus()
				raise Exception("Name should not be consiting digit or special character")
			
			name = entAName.get()
			
		if( (marks < 0 or marks > 100) ):
				entAMarks.delete(0, END)
				entAMarks.focus()
				raise Exception("Marks should be in the range of 0-100")
				marks = int(entAMarks.get())
			

		cursor = con.cursor()
		sql = "insert into student values('%d' , '%s' , '%d')"
		args = (rno, name,marks)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + " records inserted "
		messagebox.showinfo("Done ",msg)
		entARno.delete(0, END)
		entAName.delete(0, END)
		entAMarks.delete(0, END)
		entARno.focus()
	except ValueError:
		msg="Only Intergers and it should not Empty!!"
		messagebox.showerror("",msg)
	except Exception as exp :
		messagebox.showerror("",exp)
		
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror(" ", e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f6():
	root.withdraw()
	updatest.deiconify()
	stData.delete('1.0',END)
	
def f7():
	import cx_Oracle
	stData.delete('1.0',END)
	con = None 
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		rno = int(entURno.get())
		name = entUName.get()
		marks = int(entUMarks.get())
		
		Rno = (rno,)
		check = False
		cur= con.cursor()
		cur.execute("select rno from student")
		data = cur.fetchall()
		for i in data:
			if(i == Rno):
				check=True	
				 
		if(check == True):
			if(name.isalnum() or name.isalnum() != True):
				if(len(name)<2):
					entUName.delete(0, END)
					entUName.focus()
					raise Exception("Name cannot be less < 2 ")

				elif(name.isalpha() != True ):
					entUName.delete(0, END)
					entUName.focus()
					raise Exception("Name should not be consiting digit or special character")
			
				name = entUName.get()
			
			if( (marks < 0 or marks > 100) ):
				entUMarks.delete(0, END)
				entUMarks.focus()
				raise Exception("Marks should be in the range of 0-100")
				marks = int(entUMarks.get())
				
			cursor = con.cursor()
			sql = "update student set name= '%s',marks ='%d' where rno = '%d' "
			args = (name,marks,rno)
			cursor.execute(sql % args)
			con.commit()
			msg = str(cursor.rowcount) + " Records Updated "
			messagebox.showinfo("Done ",msg)
			entURno.delete(0, END)
			entUName.delete(0, END)
			entUMarks.delete(0, END)
			entURno.focus()
		else:
			msg="Roll Number doesn't Exists!!"
			messagebox.showerror("",msg)
			entURno.delete(0, END)
			entUName.delete(0, END)
			entUMarks.delete(0, END)
			entURno.focus()
	except ValueError:
		msg="Only Intergers and it should not Empty!!"
		messagebox.showerror("",msg)
	except Exception as exp :
		messagebox.showerror("",exp)
		
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror(" ", e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f8():
	updatest.withdraw()
	root.deiconify()
def f9():
	root.withdraw()
	deletest.deiconify()
def f10():
	import cx_Oracle
	con = None 
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		rno = int(entDRno.get())
		Rno = (rno,)
		check = False
		cur= con.cursor()
		cur.execute("select rno from student")
		data = cur.fetchall()
		for i in data:
			if(i == Rno):
				check=True	
				 
		if(check == True):
			cursor = con.cursor()
			sql = "delete from student  where rno = '%d' "
			args = (rno)
			cursor.execute(sql % args)
			con.commit()
			msg = str(cursor.rowcount) + " Records Deleted "
			messagebox.showinfo("Done ",msg)
			entDRno.delete(0, END)
			entDRno.focus()
		else:
			msg="Roll Number doesn't Exists!!"
			messagebox.showerror("",msg)
			entDRno.delete(0, END)
			entDRno.focus()
	except ValueError:
		msg="Only Intergers and it should not Empty!!"
		messagebox.showerror("",msg)
		entDRno.delete(0, END)
		entDRno.focus()
	except Exception as exp :
		messagebox.showerror("",exp)
def f11():
	deletest.withdraw()
	root.deiconify()
def graph():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		stData.delete('1.0',END)
		sql="select name,marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		Names=[]
		Marks=[]
		for d in data:
			Names.append(d[0])
			Marks.append(d[1])
		plt.bar(Names,Marks,width=0.4)
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.title("Student's Performance")
		plt.show()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	

btnAdd = Button(root, text="Add",font=("arial", 18,"bold"), width = 10, command=f1)
btnView = Button(root, text="View",font=("arial", 18,"bold"), width = 10, command=f3)
btnUpdate = Button(root, text="Update",font=("arial", 18,"bold"), width = 10, command=f6)
btnDelete = Button(root, text="Delete",font=("arial", 18,"bold"), width = 10,command=f9)
btnGraph = Button(root, text="Graph",font=("arial", 18,"bold"), width = 10,command=graph)
lblquote = Label(root, text=Quote,font=("arial", 18,"bold"))
lbltemp = Label(root, text="Temperature : "+str(temp)+chr(176)+"C",font=("arial", 18,"bold"))

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10) 	
btnGraph.pack(pady=10)
lblquote.pack(pady=10)
lbltemp.pack(pady=10)

addst = Toplevel(root)
addst.title("Add Student")
addst.geometry("400x500+500+40")
addst.withdraw()
lblARno = Label(addst, text="Enter Roll Number ",font=("arial", 18,"bold"))
entARno = Entry(addst, bd=5,font=("arial", 18,"bold"))
lblAName = Label(addst, text="Enter Name ",font=("arial", 18,"bold"))
entAName= Entry(addst, bd=5,font=("arial", 18,"bold"))
lblAMarks = Label(addst, text="Enter Marks ",font=("arial", 18,"bold"))
entAMarks= Entry(addst, bd=5,font=("arial", 18,"bold"))
btnAddSave = Button(addst, text="Save",font=("arial", 18,"bold"),command=f5)
btnAddBack = Button(addst, text="Back",font=("arial", 18,"bold"),command=f2)


lblARno.pack(pady=5)
entARno.pack(pady=5)
lblAName.pack(pady=5)
entAName.pack(pady=5)
lblAMarks.pack(pady=5)
entAMarks.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

viewst = Toplevel(root)
viewst.title("View Student")
viewst.geometry("400x300+500+100")  #400x500+500+40
viewst.withdraw()

stData = scrolledtext.ScrolledText(viewst, width=60,height=10)
btnViewBack = Button(viewst, text="Back",font=("arial", 18,"bold"),command=f4)

stData.pack(pady=5)
btnViewBack.pack()


updatest = Toplevel(root)
updatest.title("Update Student")
updatest.geometry("400x500+500+40")
updatest.withdraw()
lblURno = Label(updatest, text="Enter Roll Number ",font=("arial", 18,"bold"))
entURno = Entry(updatest, bd=5,font=("arial", 18,"bold"))
lblUName = Label(updatest, text="Enter Name",font=("arial", 18,"bold"))
entUName= Entry(updatest, bd=5,font=("arial", 18,"bold"))
lblUMarks = Label(updatest, text="Enter Marks ",font=("arial", 18,"bold"))
entUMarks= Entry(updatest, bd=5,font=("arial", 18,"bold"))
btnUpdateSave = Button(updatest, text="Save",font=("arial", 18,"bold"),command=f7)
btnUpdateBack = Button(updatest, text="Back",font=("arial", 18,"bold"),command=f8)

lblURno.pack(pady=5)
entURno.pack(pady=5)
lblUName.pack(pady=5)
entUName.pack(pady=5)
lblUMarks.pack(pady=5)
entUMarks.pack(pady=5)
btnUpdateSave.pack(pady=5)
btnUpdateBack.pack(pady=5)

deletest = Toplevel(root)
deletest.title("Delete Student")
deletest.geometry("400x400+500+40")
deletest.withdraw()
lblDRno = Label(deletest, text="Enter Roll Number ",font=("arial", 18,"bold"))
entDRno = Entry(deletest, bd=5,font=("arial", 18,"bold"))
btnDeleteSave = Button(deletest, text="Save",font=("arial", 18,"bold"),command=f10)
btnDeleteBack = Button(deletest, text="Back",font=("arial", 18,"bold"),command=f11)

lblDRno.pack(pady=5)
entDRno.pack(pady=5)
btnDeleteSave.pack(pady=5)
btnDeleteBack.pack(pady=5)



root.mainloop()