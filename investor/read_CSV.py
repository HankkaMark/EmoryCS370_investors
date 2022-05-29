import pandas as pd

return_list=[]

rec_list = pd.read_csv('stock_rec.csv')

for i in rec_list.values.tolist():
    print(i)
    if i[2] >20 and i[2]<40:
        return_list.append(i[1])

print(return_list)