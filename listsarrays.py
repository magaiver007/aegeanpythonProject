import numpy as np
import pandas as pd

labels = ["First", "Second", "Third"]
values = [10, 20, 30]
array = np.arange(10, 31, 10)
dico = {"First": 10, "Second": 20, "Third": 30}
email = "testuser@hotmail.com"

A = pd.Series(values)
B = pd.Series(values, labels)
C = pd.Series(array, labels)
D = pd.Series(dico)
mail_list = email.split("@")