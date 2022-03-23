from tkinter import *

root= Tk()
root.title("Student Driving Licence")
root.geometry('400x400')

lbl_id= Label(root)
lbl_name= Label(root)
lbl_dob= Label(root)
lbl_pin= Label(root)
lbl_address= Label(root)
lbl_vehicle_type= Label(root)

def id_display():
    label_id = "1265439087"
    label_name = "Atharv Vaish"
    label_dob = "30 April, 2010"
    label_pin = "110024"
    label_address = "E-68 Amar Colony, 2nd Floor, Lajpat Nagar-4"
    label_vehicle_type = "Two Four"
    
    lbl_id['text']=label_id
    lbl_name['text']=label_name
    lbl_dob['text']=label_dob
    lbl_pin['text']=label_pin
    lbl_address['text']= label_address
    lbl_vehicle_type['text']=label_vehicle_type
    
    print("ID : " +lbl_id)
    print("Name : " +lbl_name)
    print("Date Of Birth : " +lbl_dob)
    print("Pin no. : " +lbl_pin)
    print("Address : " +lbl_address)
    print("VEHICLE TYPE : " +lbl_vehicle_type)
    
Btn1= Button(root, text= "Driving Licence : ", command = id_display)
Btn1.place(relx= 0.2, rely= 0.1, anchor= CENTER)
    
root.mainloop()