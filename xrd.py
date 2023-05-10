import csv
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

path = r"C:\Users\f1c256b\Desktop\python\data\xrd\20230510\SHT 046(TEXT).txt"
#ファイル読み込む
with open(path) as file:
    lines = file.readlines()
    s_lines = [line.strip() for line in lines]
#行を抽出
taget_line = lines[324:7823]

for i in range(len(taget_line)):
    taget_line[i] = taget_line[i].replace("1.0000", "", ).replace("\n", "")

#CSVに書き出す
with open('SHT046(TEXT)_to_output.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for row in taget_line:
        writer.writerow(row.strip().split())

#CSVを出力
Df = pd.read_csv("SHT046(TEXT)_to_output.csv")
Df.to_csv("SHT046(TEXT)_to.csv", index = False, header = False)

Dataflame = pd.read_csv("SHT046(TEXT)_to.csv")

print(Dataflame)

#excelに出力
Dataflame.to_excel("SHT046(TEXT)_to.xlsx")
print(Dataflame)

Dataflame.plot()
plt.show()
