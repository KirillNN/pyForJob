from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import pandas as pd

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

new_df = pd.read_csv(filename)
print(new_df)
# f = open(filename, 'r', encoding='utf-8')
# count = 0
#
# for line in f:
#     print(count, line)
#     count += 1
#
# f.close()
