import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys

print("目前使用的 Python 路徑：", sys.executable)

# Java 11 路徑（Gephi 附帶的）
JAVA_HOME = r"C:\Program Files\Gephi-0.10.1\jre-x64\jdk-11.0.17+8-jre"
PYTHON_EXE = r"C:\Users\Leon\AppData\Local\Programs\Python\Python310\python.exe"

selected_script = None

def select_file():
    global selected_script
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if path:
        selected_script = path
        status_label.config(text=f"選擇檔案：{os.path.basename(path)}")

def run_pyspark():
    if not selected_script:
        messagebox.showwarning("提醒", "請先選擇一個 .py 檔案")
        return

    env = os.environ.copy()
    env['JAVA_HOME'] = JAVA_HOME
    env['PATH'] = JAVA_HOME + r"\bin;" + env['PATH']
    env["PYSPARK_PYTHON"] = PYTHON_EXE  # 強制 Spark 使用正確的 Python
    env.pop("PYTHONHOME", None)
    env.pop("PYTHONPATH", None)

    try:
        java_cmd = os.path.join(JAVA_HOME, "bin", "java.exe")
        java_version = subprocess.run([java_cmd, "-version"], env=env, capture_output=True, text=True)

        print("[Java Version Info]")
        print(java_version.stderr)

        # 執行選擇的 PySpark 檔案，並即時顯示在終端機中
        print("[Script Output]")
        process = subprocess.Popen([PYTHON_EXE, selected_script], env=env)
        process.communicate()

    except Exception as e:
        messagebox.showerror("錯誤", f"執行失敗：{e}")

root = tk.Tk()
root.title("Leon 的 PySpark 啟動器")
root.geometry("500x250")

label = tk.Label(root, text="選擇你要執行的 .py 檔案（用 Java11）")
label.pack(pady=10)

select_btn = tk.Button(root, text="選擇檔案", command=select_file, bg="lightblue")
select_btn.pack(pady=5)

btn = tk.Button(root, text="執行 PySpark", command=run_pyspark, bg="lightgreen")
btn.pack(pady=10)

status_label = tk.Label(root, text="尚未選擇檔案", fg="gray")
status_label.pack()

root.mainloop()
