from  tkinter import filedialog, Tk, simpledialog
import pandas as pd
import re

def is_email(cell):
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return (re.search(regex, cell))

root = Tk()
root.filename =  filedialog.askopenfilename(title = "choose your excel file",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
root.withdraw()

xl = pd.ExcelFile(root.filename)

sheet_index = 0
if (len(xl.sheet_names) > 1):
    question = "Choose a sheet by index:\n"
    for i in range(len(xl.sheet_names)):
        question += str(i) + ": " + xl.sheet_names[i] + "\n"
    answer = simpledialog.askinteger("Input", question ,parent=root,minvalue=0, maxvalue=len(xl.sheet_names)-1)
sheet = xl.sheet_names[sheet_index]

email_list = set()

df = xl.parse(sheet)
columns = list(df)
for i in columns:
    for cell in df[i]:
        if is_email(str(cell)):
            email_list.add(cell)

print(*email_list, sep=",")
print()
print(*email_list, sep=";")
print()
print(*email_list, sep=" ")
print()
print(*email_list, sep="\t")
print()
print(*email_list, sep="\n")

