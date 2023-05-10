import csv
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

path = r"C:\Users\f1c256b\Desktop\python\data\xrd\20220825\SHT 012(S)(text).txt"

#ファイル読み込む
with open(path) as file:
    lines = file.readlines()
    s_lines = [line.strip() for line in lines]

#行を抽出
target_line = lines[324:7823]

for i in range(len(target_line)):
    target_line[i] = target_line[i].replace("1.0000", "").replace("\n", "")

#CSVに書き出す
with open('SHT012(TEXT)_to_output.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for row in target_line:
        writer.writerow(row.strip().split())

#CSVを読み込む
df = pd.read_csv("SHT012(TEXT)_to_output.csv", header=None)

#Excelに出力
df.to_excel("SHT012(TEXT)_to.xlsx", index=False, header=False)

DB=pd.read_excel("SHT012(TEXT)_to.xlsx")
