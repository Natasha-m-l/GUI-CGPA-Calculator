from tkinter import *

main_window = Tk()
main_window.title('CGPA calculator')

# Function to round the buttons
def round_button(widget):
    widget.config(relief='raised', bd=4, bg='lightblue', activebackground='skyblue', padx=10, pady=5)
    return widget

Label(main_window, text='CGPA Calculator',bg='white', font=('Times New Roman', 16, 'bold','italic')).grid(row=0, column=0, columnspan=4, sticky='nsew')
Label(main_window, text='Enter Course Details',bg='beige',font=('Times New Roman', 12)).grid(row=1, column=0,columnspan=4, sticky='nsew')
c1 = DoubleVar()
g1 = IntVar()
credit = []
gradept = []

def add_to_list():
    C = c1.get()
    G = g1.get()
    credit.append(C)
    gradept.append(G)
    c1.set(0)
    g1.set(0)
    for i in range(len(credit)):
        text1 = f'course {i + 1} credit: {credit[i]}      course{i + 1} grade point : {gradept[i]}'
        Label(main_window, text=text1, font=('Times New Roman', 12)).grid(row=4 + i, column=0, columnspan=4, sticky='nsew')
    round_button(Button(main_window, text='Calculate CGPA', command=calc_cgpa)).grid(row=len(credit) + 5, column=0, columnspan=4)

def calc_cgpa():
    num = 0
    den = 0
    for i in range(len(credit)):
        den += credit[i]
        num += credit[i] * gradept[i]
    cgpa = num / den
    Label(main_window,bg='lightblue', text=f'Total credits: {den}', font=('Times New Roman', 12)).grid(row=i + 5, column=0, columnspan=4, sticky='nsew')
    Label(main_window,bg='lightblue', text=f'sum of  course credits x grade point : {num}', font=('Times New Roman', 12)).grid(row=i + 6, column=0, columnspan=4, sticky='nsew')
    Label(main_window,bg='lightblue', text=f'CGPA: {cgpa:.2f}', font=('Times New Roman', 14, 'bold')).grid(row=i + 7, column=0, columnspan=4, sticky='nsew')

Label(main_window, text='Course credits:', font=('Times New Roman', 12)).grid(row=2, column=0, sticky='e')
Label(main_window, text='Course grade point:', font=('Times New Roman', 12)).grid(row=2, column=2, sticky='e')
Entry(main_window, textvariable=c1, font=('Times New Roman', 12)).grid(row=2, column=1, sticky='w')
Entry(main_window, textvariable=g1, font=('Times New Roman', 12)).grid(row=2, column=3, sticky='w')
add_course_button = round_button(Button(main_window, text='Add Course', command=add_to_list))
add_course_button.grid(row=3, column=0, columnspan=4, sticky='nsew')

# Configure grid weights to make the columns expand when window is resized
for i in range(4):
    main_window.grid_columnconfigure(i, weight=1)

# Set background color
main_window.configure(bg='beige')

main_window.mainloop()
