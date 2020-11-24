import tkinter as tk

master = tk.Tk()
master.geometry("1000x200")
tk.Label(master, text="Student Name").grid(row=0)

input_field = tk.Entry(master)
input_field.grid(row=0, column=1)

enter_button = tk.Button(master, text="Enter")
enter_button.grid(row=1, column=1)


list_box = tk.Listbox(master)
list_box.grid(row=0, column=2)
i = 1
#  drills is temporarily seeded. It will use the get drills function when implemented
drills = ["this", "that", "the othddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddder"]
for drill in drills:
    list_box.insert(i, drill)


master.mainloop()
#
# top = tk.Tk()
#
# Lb1 = tk.Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")

# i=1
#
# drill_list = get_drills(student_name)
# for each(drill in drill_list):
#
#     Lb1.insert(i, drill)
#     i++
#
# Lb1.pack()
# top.mainloop()