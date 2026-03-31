import os
import shutil
import tkinter as tk
from tkinter import filedialog

# フォルダ選択ダイアログ
root = tk.Tk()
root.withdraw()  # メイン画面を表示しない
folder_path = filedialog.askdirectory(title="整理したいフォルダを選択")

# フォルダが選ばれなかった場合
if not folder_path:
    print("フォルダが選択されませんでした")
    exit()

print("選択されたフォルダ:", folder_path)

# 拡張子ごとの分類ルール
file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "pdf": [".pdf"],
    "text": [".txt"],
    "excel": [".xlsx", ".xls"],
    "others": [],
    "presentation":["pptx"]
}

# フォルダ内のファイルを取得
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder_name, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"{filename} → {folder_name}")
                moved = True
                break

        if not moved:
            target_folder = os.path.join(folder_path, "others")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"{filename} → others")

print("整理完了！")