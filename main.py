import sys
import customtkinter as CTk

sys.path.append('/path/to/customtkinter/module')

def calculate_result():
    a = float(entry_a.get())
    result = 45 / (a * 3)
    label_result.configure(text=f"Result: {result}")


root = CTk.CTk()
root.title('Calculator')
root.geometry('250x250')

label_a = CTk.CTkLabel(root, text='Enter a value for a:')
label_a.pack()

# Entry under 'a'
entry_a = CTk.CTkEntry(root)
entry_a.pack()

label_result = CTk.CTkLabel(root, text='Result x')
label_result.pack()

btn_calculate = CTk.CTkButton(root, text='Calculate', command=calculate_result)
btn_calculate.pack()

label_formula = CTk.CTkLabel(root, text="Formula: x = 45 / (a * 3)")
label_formula.pack()

root.mainloop()