import numpy as np
import pandas as pd 

students = {"std_id": [1, 2, 3, 4], 
            "std_name": ["mohamed", "moayad", "meshal", "mohanad"], 
            "age": [17, 16, 13, 12], 
            "betyg": [80, 65, 45, 40]}

df = pd.DataFrame(students)
print (df)
