# Excel file format cannot be determined, you must specify an engine manually 

import glob
import pandas as pd

for file in glob.glob('./*.xlsx'):
    if '~$' in file:
        continue
    else:
        df = pd.read_excel(
            file,
            engine='openpyxl'
        )

        print(df)