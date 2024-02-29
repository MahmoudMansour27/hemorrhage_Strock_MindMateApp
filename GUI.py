# import libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import numpy as np
import cv2
import webbrowser
import predict_function

main_bg = '#ffffff'

root = tk.Tk()
root.geometry('1600x900')
root.title('MindMate Application')
root.configure(bg=main_bg)

# ********************************************************************
# styles
main_bx_bg = '#7AC5CD'
btn_style = ttk.Style()
btn_style.configure('my.TButton', font=('Arial', 16))

# ********************************************************************

# main text
main_lbl = tk.Label(root, text="MindMate System", bg = main_bg, font=('Arial', 50, 'bold'))
main_lbl.pack(pady=20)

# main frame
main_frame = Frame(root)
main_frame.config(bg = main_bx_bg)
main_frame.pack()

# left side frame
left_frame = Frame(main_frame)
left_frame.config(bg = main_bx_bg)
left_frame.grid(row=0, column=0, ipadx= 20)

# select image
image_one_label = tk.Label(left_frame, width= 80, height=30, bg='#CDB79E')
image_one_label.pack(pady=10)


def display_image_one(file_path):
    image = Image.open(file_path)
    image = image.resize((550, 400))
    photo = ImageTk.PhotoImage(image)
    image_one_label.config(image=photo, width=550, height=400)
    image_one_label.photo = photo
    
def open_image_one():
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        global selected_photo_path_1
        selected_photo_path_1 = file_path
        img1 = cv2.imread(selected_photo_path_1, cv2.IMREAD_GRAYSCALE)
        display_image_one(file_path) 
        
def view_report():
    webbrowser.open_new(r'file:///home/mahmoud/Documents/programming%20%F0%9F%A4%A4%EF%B8%8F%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB%EF%B8%8F/projects/python/MindMate%20Project/Project/temp_saves/report.pdf')

        

select_button_img_one = tk.Button(left_frame, text="Select Image", command=open_image_one)
select_button_img_one.configure(font=('Arial', 16, 'bold'), bg = '#FF6103', foreground='white', width= 55, height= 2)
select_button_img_one.pack(pady=10, padx=30)

# view result btn
view_frame = Frame(left_frame)
view_frame.config(bg = main_bx_bg)
view_frame.pack()

view_res = tk.Button(view_frame, text="View Report")
view_res.configure(font=('Arial', 16, 'bold'), bg = '#66CD00', foreground='white', width= 26, height= 2, command=view_report)
view_res.grid(row=0, column=0, pady=10, padx=5) 

view_res = tk.Button(view_frame, text="View Result")
view_res.configure(font=('Arial', 16, 'bold'), bg = '#66CD00', foreground='white', width= 26, height= 2)
view_res.grid(row=0, column=1, pady=10, padx=5)    

# ----------------------------------------

# right side frame
right_frame = Frame(main_frame)
right_frame.config(bg = main_bx_bg)
right_frame.grid(row=0, column=1)

# patient id entry
# entry type frame
radio_frame = Frame(right_frame)
radio_frame.config(bg = main_bx_bg)
radio_frame.pack(pady=30) #increasable

entry_btn_width = 30

# entry state btns
app_entry_btn = tk.Button(radio_frame, text="App Entry")
app_entry_btn.configure(font=('Arial', 16, 'bold'), bg = '#3D9140', foreground='white', width= entry_btn_width)
app_entry_btn.pack(pady=5)

database_entry_btn = tk.Button(radio_frame, text="Database Entry")
database_entry_btn.configure(font=('Arial', 16, 'bold'), bg = 'chartreuse3', foreground='white', width= entry_btn_width)
database_entry_btn.pack(pady=5)


# patietn id 
id_frame = Frame(radio_frame)
id_frame.config(bg = main_bx_bg)
id_frame.pack()

id_lbl = tk.Label(id_frame, text= "ID    ", font=('Arial', 20, 'bold'), bg=main_bx_bg)
id_lbl.grid(row=0, column=0)
id_values = list(np.arange(0, 51)) # retrieve from database
id_combom = ttk.Combobox(id_frame, values=id_values, state="readonly", font=(('Arial', 20, 'bold')))
id_combom.configure(width=5)
id_combom.grid(row=0, column=1)


# --------------------------------------------------------
# app data entry

combom_width = 20 

# bottom data entry
btm_right_frame = Frame(right_frame)
btm_right_frame.config(bg = main_bx_bg)
btm_right_frame.pack()

# bottom right side data entry
rs_dataEnty_frame = Frame(btm_right_frame)
rs_dataEnty_frame.config(bg = main_bx_bg)
rs_dataEnty_frame.grid(row=0, column=0, ipadx=10, ipady=10)

# gender
gender_frame = Frame(rs_dataEnty_frame)
gender_frame.config(bg=main_bx_bg)
gender_frame.pack(pady=10)
gender_lbl = tk.Label(gender_frame, text="Gender", font=('Arial', 22, 'bold'), bg = main_bx_bg)
gender_lbl.pack()
gender_values = ['Male', 'Female']
gender_combom = ttk.Combobox(gender_frame, values=gender_values, state="readonly", font=(('Arial', 20)), width=combom_width)
gender_combom.pack()

# smoking 
smk_frame = Frame(rs_dataEnty_frame)
smk_frame.config(bg=main_bx_bg)
smk_frame.pack(pady=10)
smoking_lbl = tk.Label(smk_frame, text="Smoking Status", font=('Arial', 22, 'bold'), bg=main_bx_bg)
smoking_lbl.pack()
smoking_values = ['Formerly Smoke', 'Never Smoked', 'Smokes', 'Unkown']
smoking_combom = ttk.Combobox(smk_frame, values=smoking_values, state="readonly", font=(('Arial', 20)), width=combom_width)
smoking_combom.pack()

# hypertension
hyper_frame = Frame(rs_dataEnty_frame)
hyper_frame.config(bg=main_bx_bg)
hyper_frame.pack(pady=10)
hyper_lbl = tk.Label(hyper_frame, text="Hypertension", font=('Arial', 22, 'bold'), bg=main_bx_bg)
hyper_lbl.pack()
hyper_values = ['Yes', 'No']
hyper_combom = ttk.Combobox(hyper_frame, values=hyper_values, state="readonly", font=(('Arial', 20)), width=combom_width)
hyper_combom.pack()

# bottom right side data entry -----------------------------------------------------
ls_dataEnty_frame = Frame(btm_right_frame)
ls_dataEnty_frame.config(bg=main_bx_bg)
ls_dataEnty_frame.grid(row=0, column=1, ipadx=10, ipady=10)

# heart disease
hrt_frame = Frame(ls_dataEnty_frame)
hrt_frame.config(bg=main_bx_bg)
hrt_frame.pack(pady=10)
heart_lbl = tk.Label(hrt_frame, text="Heart Disease", font=('Arial', 22, 'bold'), bg=main_bx_bg)
heart_lbl.pack()
heart_values = ['Yes', 'No']
heart_combom = ttk.Combobox(hrt_frame, values=heart_values, state="readonly", font=(('Arial', 20)), width=combom_width)
heart_combom.pack() 

# Obesity 
ob_frame = Frame(ls_dataEnty_frame)
ob_frame.config(bg=main_bx_bg)
ob_frame.pack(pady=10)
obesity_lbl = tk.Label(ob_frame, text="Obesity", font=('Arial', 22, 'bold'), bg=main_bx_bg)
obesity_lbl.pack()
obesity_values = ['Yes', 'No']
obesity_combom = ttk.Combobox(ob_frame, values=obesity_values, state="readonly", font=(('Arial', 20)), width=combom_width)
obesity_combom.pack()

# avg Glucose level
gluc_frame = Frame(ls_dataEnty_frame)
gluc_frame.config(bg=main_bx_bg)
gluc_frame.pack(pady=10)
glucose_lbl = tk.Label(gluc_frame, text="Avg Glucose Level", font=('Arial', 22, 'bold'), bg=main_bx_bg)
glucose_lbl.pack()
glucose_entry = Entry(gluc_frame, width=21, font=('Arial', 20))
glucose_entry.pack()

# GCS levels
out_gcs_frame = Frame(right_frame)
out_gcs_frame.config(bg=main_bx_bg)
out_gcs_frame.pack(pady=10)

gcs_frame = Frame(out_gcs_frame)
gcs_frame.config(bg=main_bx_bg)
gcs_frame.pack()
gcs_values = list(np.arange(0, 5)) # retrieve from database

# age
age_lbl = tk.Label(gcs_frame, text= "Age", font=('Arial', 20, 'bold'), bg=main_bx_bg)
age_lbl.grid(row=0, column=0)
age_entry = Entry(gcs_frame, width=5, font=('Arial', 20))
age_entry.grid(row=0, column=1)

# eye
eye_lbl = tk.Label(gcs_frame, text= "Eye", font=('Arial', 20, 'bold'), bg=main_bx_bg)
eye_lbl.grid(row=0, column=2, padx=5)
eye_combom = ttk.Combobox(gcs_frame, values=gcs_values, state="readonly", font=(('Arial', 20, 'bold')))
eye_combom.configure(width=2)
eye_combom.grid(row=0, column=3)

# verbal
verbal_lbl = tk.Label(gcs_frame, text= "  Verbal", font=('Arial', 20, 'bold'), bg=main_bx_bg)
verbal_lbl.grid(row=0, column=4)
verbal_combom = ttk.Combobox(gcs_frame, values=gcs_values, state="readonly", font=(('Arial', 20, 'bold')))
verbal_combom.configure(width=2)
verbal_combom.grid(row=0, column=5)

# motor
mot_lbl = tk.Label(gcs_frame, text= "  Motor", font=('Arial', 20, 'bold'), bg=main_bx_bg)
mot_lbl.grid(row=0, column=6)
mot_combom = ttk.Combobox(gcs_frame, values=gcs_values, state="readonly", font=(('Arial', 20, 'bold')))
mot_combom.configure(width=2)
mot_combom.grid(row=0, column=7)



# ------------------------------------------------------------------------------------------
# Result label
result_frame = Frame(right_frame, highlightbackground="black", highlightthickness=1)
result_frame.pack(pady=30)
result_lbl = tk.Label(result_frame, text="Result Will Appear Here", font=('Arial', 25, 'bold'), width=30)
result_lbl.pack(pady=15, padx=15)

# ----------------------------- database entry check ---------------------------------------------------
def app_entry_fun():
    gender_combom.config(state='readonly')
    smoking_combom.config(state='readonly')
    hyper_combom.config(state='readonly')
    heart_combom.config(state='readonly')
    obesity_combom.config(state='readonly')
    glucose_entry.config(state='normal')
    eye_combom.config(state='readonly')
    verbal_combom.config(state='readonly')
    mot_combom.config(state='readonly')
    age_entry.config(state='normal')
    
def database_entry_fun():
    gender_combom.config(state='disable')
    smoking_combom.config(state='disable')
    hyper_combom.config(state='disable')
    heart_combom.config(state='disable')
    obesity_combom.config(state='disable')
    glucose_entry.config(state='disable')
    eye_combom.config(state='disable')
    verbal_combom.config(state='disable')
    mot_combom.config(state='disable')
    age_entry.config(state='disable')

def view_result_btn():
    g = gender_combom.get()
    hyp = hyper_combom.get()
    hrt = heart_combom.get()
    ob = obesity_combom.get()
    smoking = smoking_combom.get()
    
    if smoking == "Formerly Smoke":
        smk = 1
    elif smoking == "Never Smoked":
        smk = 2 
    elif smoking == "Smokes":
        smk = 3
    else:
        smk = 4
    
    g = 1 if g == "Male" else 0
    hyp = 1 if hyp == "Yes" else 0
    hrt = 1 if hyp == "Yes" else 0
    ob = 1 if ob == "Yes" else 0
    
    res_txt = predict_function.prediction(int(id_combom.get()), selected_photo_path_1, g, float(age_entry.get()), hyp, hrt, float(glucose_entry.get()), ob, smk, eye_combom.get(), verbal_combom.get(), mot_combom.get())
        
    result_lbl.configure(text=res_txt)

app_entry_btn.config(command=app_entry_fun)
database_entry_btn.config(command=database_entry_fun)
view_res.config(command=view_result_btn)


root.mainloop()

g = "Female"
g = 1 if g == "Male" else 0
