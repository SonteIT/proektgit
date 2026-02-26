import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

tdp_cpu = {
    "Intel Core i9-12900K": 241,
    "Intel Core i9-12900KF": 241,
    "Intel Core i7-12700K": 190,
    "Intel Core i7-12700KF": 190,
    "Intel Core i5-12600K": 150,
    "Intel Core i5-12600KF": 150,
    "Intel Core i5-12400": 117,
    "Intel Core i5-12400F": 117,
    "Intel Core i3-12100": 88,
    "Intel Core i3-12100F": 88,
    "Intel Core i9-13900K": 253,
    "Intel Core i9-13900KF": 253,
    "Intel Core i9-13900KS": 253,
    "Intel Core i7-13700K": 253,
    "Intel Core i7-13700KF": 253,
    "Intel Core i7-13700F": 219,
    "Intel Core i5-13600K": 253,
    "Intel Core i5-13600KF": 253,
    "Intel Core i5-13400": 148,
    "Intel Core i5-13400F": 148,
    "Intel Core i3-13100": 110,
    "Intel Core i3-13100F": 110,
    "Intel Core i9-14900K": 253,
    "Intel Core i9-14900KF": 253,
    "Intel Core i7-14700K": 253,
    "Intel Core i7-14700KF": 253,
    "Intel Core i5-14600K": 253,
    "Intel Core i5-14600KF": 253,
    "Intel Core i5-14400": 148,
    "Intel Core i5-14400F": 114,
    "Intel Core i3-14100": 110,
    "Intel Core i3-14100F": 110,
    "Ryzen 9 9950X": 250,
    "Ryzen 9 9950X3D": 250,
    "Ryzen 9 7950X": 210,
    "Ryzen 9 7950X3D": 220,
    "Ryzen 9 7900X": 230,
    "Ryzen 9 7900X3D": 230,
    "Ryzen 9 7900": 220,
    "Ryzen 7 9700X": 105,
    "Ryzen 7 7700X": 105,
    "Ryzen 7 7700": 105,
    "Ryzen 7 9800X3D": 250,
    "Ryzen 7 7800X3D": 162,
    "Ryzen 7 8700F": 87,
    "Ryzen 5 9600X": 105,
    "Ryzen 5 9600": 105,
    "Ryzen 5 7600X": 105,
    "Ryzen 5 7600": 65,
    "Ryzen 5 7500F": 120,
    "Ryzen 5 8600G": 65,
    "Ryzen 5 8400F": 65,
    "Ryzen 5 7600X3D": 120,
    "Ryzen 5 7400F": 65,
    "Ryzen 9 5950X": 105,
    "Ryzen 9 5900X": 105,
    "Ryzen 7 5800X": 105,
    "Ryzen 5 5600X": 65,
    "Ryzen 5 5600G": 65,
    "Ryzen 5 5500": 65,
    "Ryzen 5 3600": 65,
    "Ryzen 5 3600X": 95,
    "Ryzen 5 2600": 65,
    "Ryzen 5 2600X": 95,
    "Ryzen 3 3100": 65,
    "Ryzen 3 3300X": 95,
    "Ryzen 3 3200G": 65,
    "Ryzen 3 5300G": 65,
}

tdp_gpu = {
    "GeForce GTX 1650": 100,
    "GeForce GTX 1650 Super": 100,
    "GeForce GTX 1660": 120,
    "GeForce GTX 1660 Super": 125,
    "GeForce GTX 1660 Ti": 120,
    "GeForce RTX 2060": 160,
    "GeForce RTX 2060 Super": 175,
    "GeForce RTX 2070": 175,
    "GeForce RTX 2070 Super": 215,
    "GeForce RTX 2080": 225,
    "GeForce RTX 2080 Super": 250,
    "GeForce RTX 2080 Ti": 250,
    "GeForce RTX 3060": 170,
    "GeForce RTX 3060 Ti": 200,
    "GeForce RTX 3070": 220,
    "GeForce RTX 3070 Ti": 250,
    "GeForce RTX 3080": 320,
    "GeForce RTX 3080 Ti": 350,
    "GeForce RTX 3090": 350,
    "GeForce RTX 4060": 160,
    "GeForce RTX 4060 Ti": 160,
    "GeForce RTX 4070": 300,
    "GeForce RTX 4070 Ti": 310,
    "GeForce RTX 4070 Super": 240,
    "GeForce RTX 4080": 320,
    "GeForce RTX 4080 Super": 320,
    "GeForce RTX 4090": 450,
    "Radeon RX 5300": 100,
    "Radeon RX 5500": 150,
    "Radeon RX 5500 XT": 150,
    "Radeon RX 5600": 160,
    "Radeon RX 5600 XT": 180,
    "Radeon RX 5700": 180,
    "Radeon RX 5700 XT": 225,
    "Radeon RX 5700 Super": 225,
    "Radeon RX 6400": 72,
    "Radeon RX 6500 XT": 107,
    "Radeon RX 6600": 132,
    "Radeon RX 6600 XT": 160,
    "Radeon RX 6700": 180,
    "Radeon RX 6700 XT": 230,
    "Radeon RX 6800": 250,
    "Radeon RX 6800 XT": 300,
    "Radeon RX 6900 XT": 300,
    "Radeon RX 6750 XT": 250,
    "Radeon RX 6950 XT": 300,
    "Radeon RX 7600": 165,
    "Radeon RX 7700 XT": 250,
    "Radeon RX 7800 XT": 300,
    "Radeon RX 7900 XT": 300,
    "Radeon RX 7900 XTX": 350,
}


def PSC():
    cpu = choice_cpu.get()
    gpu = choice_gpu.get()

    proc_tdp = tdp_cpu.get(cpu)
    gpu_tdp = tdp_gpu.get(gpu)

    res1 = (proc_tdp + gpu_tdp) * 1.3
    res=round(res1,0)
    messagebox.showinfo("Результат", f"Мощность блока питания для вашей конфигурации: {res} Вт")


okno = tk.Tk()
okno.title("Расчет мощности блока питания")
okno.geometry("500x300+700+200")
okno.config(bg="#d2f9f8")

processor = tk.Label(okno, text='Выберите процессор:',
                    font=('Arial', 8, 'bold'),
                    bg="#d2f9f8")

gpu = tk.Label(okno, text='Выберите видеокарту:',
               font=('Arial', 8, 'bold'),
               bg="#d2f9f8")

processor.place(x=80, y=66)
gpu.place(x=270, y=66)

name_cpu = list(tdp_cpu.keys())
choice_cpu = ttk.Combobox(okno, values=name_cpu, width=20, font=('Arial', 8, 'bold'))
choice_cpu.place(x=80, y=85)

name_gpu = list(tdp_gpu.keys())
choice_gpu = ttk.Combobox(okno, values=name_gpu, width=20, font=('Arial', 8, 'bold'))
choice_gpu.place(x=270, y=85)

PCbtn = tk.Button(okno, text='Рассчитать мощность блока питания', command=PSC, font=('Arial', 8, 'bold'))
PCbtn.place(x=135, y=160)
okno.mainloop()
