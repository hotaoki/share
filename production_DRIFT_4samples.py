import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルが格納されているフォルダのパス
folder_path = r"C:\Users\f1c256b\Desktop\研究\解析\DRIFT\union"
# フォルダ内の全てのCSVファイルを取得し、更新日時の昇順にソートする
file_paths = sorted(glob.glob(os.path.join(folder_path, '*.csv')), key=os.path.getmtime)

# グラフの大きさを変更するためのパラメータ
fig_width = 8  # グラフの幅（インチ）
fig_height = 6  # グラフの高さ（インチ）

# グラフを作成する
plt.figure(figsize=(fig_width, fig_height))
# 各CSVファイルのデータを追加する
legends = ["Pt/TiO₂-δ", "Pt/Ti₄O₇(A)", "Pt/Ti₄O₇(B)"]  # 下付き文字を追加した凡例
for i, file_path in enumerate(file_paths):
    # CSVファイルを読み込む
    data = pd.read_csv(file_path)

    # グラフにデータを追加
    plt.plot(data.iloc[:, 0], data.iloc[:, 1], label=legends[i], linewidth=0.5)

# 凡例を表示する
plt.xlabel('Wavenumber (cm\u207B\u00B9)')  # "cm^-1"を上付き文字に変更
plt.ylabel('Transmittance (-)')
plt.gca().invert_xaxis()
plt.tick_params(which='both', direction='in')
plt.xlim(1000, 4000)
plt.ylim(-0.02, 0.045)
plt.legend(loc='center left', bbox_to_anchor=(0.9, 0.9))
# x軸の方向を逆にする
plt.gca().invert_xaxis()

# グラフを表示する
plt.show()
