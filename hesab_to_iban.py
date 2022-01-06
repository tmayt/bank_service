import tkinter as tk
from azbankintro import *
from functools import partial


hint = '''
    'BMI' # meli
    'SEP' #saman
    'EBANK_BANK' # eghtesad novin
    'PEC_BANK' # parsian
    'BPI_BANK' # pasargad
    'POST_BANK' # post bank iranian
    'TEJARAT_BANK' # tejarat
    'EDBI_BANK' # tose ee saderat
    'REFAH_BANK' # refah
    'SEPAH_BANK' # sepah
    'SARMAYE_BANK' # sarmaye
    'BSI_BANK' # saderat
    'BIM_BANK' # sanat madan tejarat
    'KARAFARIN_BANK' # karafarin
    'BKI_BANK' # keshavarzi
    'MASKAN_BANK' # maskan
    'MELLAT_BANK' # melat
    'CID' # moasese etebari tose e
    'TT_BANK' # tose e ta aavon
    'AYANDEH_BANK' # ayandeh
'''

print(hint)

bank_type = BankEnum(input('bank type ==> '))


root = tk.Tk()
# specify size of window.
root.geometry("500x300")



# Create text widget and specify size.
T = tk.Text(root, height = 1, width = 52,padx = 10, pady = 10)

# Create label
l = tk.Label(root, text = "Iban Generator",width=100, height=5)

l.config(font =("Courier", 14))


def hesab_to_iban():
    number = int(T.get("1.0",'end'))
    iban = IBAN.calculate_iban(bank_type, number)
    l.config(text = iban)

# Create button for next text.
b1 = tk.Button(root, text = "submit",command = hesab_to_iban ,width=30, height=2 )



l.pack()
T.pack()
b1.pack()
tk.mainloop()
