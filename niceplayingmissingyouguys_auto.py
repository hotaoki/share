import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt

# Tkinterのルートウィンドウを作成
root = tk.Tk()
root.withdraw()

# ファイル名を入力するダイアログを表示
file_path = filedialog.askopenfilename()
save_path = filedialog.asksaveasfilename(defaultextension='.csv')

# ファイルを開いて行を抽出
with open(file_path, "r") as file:
    lines = file.readlines()

# 数値リストを作成する
data_lst = []
target_line = lines[324:7823]
target_line = ''.join(target_line)  # 改行文字を除去するために、文字列を結合する
data = target_line.strip().split()  # 全ての数値を取得し、空白で分割する

x = data[::3]
y = data[1::3]

# CSVファイルに書き出す
with open(save_path, mode='w', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(x)):
        writer.writerow([x[i], y[i]])


# Tkinterのルートウィンドウを作成
root = tk.Tk()
root.withdraw()

# ファイルダイアログを表示し、ファイルパスを取得
file_path = filedialog.askopenfilename()

# ファイルを開いて行を抽出
with open(file_path, "r") as file:
    lines = file.readlines()

# 数値リストを作成する
data_lst = []
for line in lines:
    data = line.strip().split(',')
    data_lst.append([float(x) for x in data])

# xとyのリストを作成
x = [row[0] for row in data_lst]
y = [row[1] for row in data_lst]

# 折れ線グラフを作成
plt.plot(x, y)

# 軸目盛を内側にする
plt.tick_params(which='both', direction='in')

# x軸ラベルを設定
plt.xlabel('2θ (degree)')

# y軸ラベルを設定
plt.ylabel('Intensity(a.u.)')

# y軸の目盛りを消す
plt.yticks([])

# x軸の目盛りを設定
plt.xticks(range(0, int(max(x))+11, 10))

# 凡例を右上に表示する
legend_text = input("凡例を入力してください：")
plt.legend([legend_text], loc='upper right')

# グラフを表示
plt.show()

# グラフを画像として保存 # ファイルを開くダイアログを表示し、ファイルパスを取得する
root = tk.Tk()
root.withdraw()
file_path = filedialog.asksaveasfilename(defaultextension='.png')
plt.savefig('output.png')
