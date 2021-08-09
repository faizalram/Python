from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Vending Machine Kelompok 1")
root.config(bg="#2980B9")

saldo = 0
minuman = ['kosong', 'Air Mineral', 'Fruit Tea', 'Pulpy Orange', 'Ultramilk', 'Nescafe', 'Coca-cola']
harga = ['kosong', 5000, 7000, 10000, 10000, 6000, 10000]
stok = [0, 5, 5, 5, 5, 5, 5]
global jmlh
jmlh = [0,0,0,0,0,0,0]
itr = [i for i in range (len(minuman))]

# Frame Kanan
kanan = Frame(root, bg="#2980B9")
kanan.pack(side="right", padx=20, pady=20)

# Bagian Pemilihan Minuman
Label(kanan, font= 'Bubbly 32 bold', bg= "#2980B9", fg= "Orange", text= "Vending Machine\nKelompok 1").pack(side="top", padx = 5, pady= 5)
beli = Frame(kanan, bg="#2980B9", relief="raise")
beli.pack(side="top", padx = 5, pady = 5)
screen = Entry(beli, bg="black", fg="#F1C04F", font="Nunito 16 bold")
screen.pack(padx = 10, pady = 10)

def getlayar(x):
    layar = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(layar) + str(x))

def hpslayar():
    screen.delete(0, END)

beli1 = Frame(beli, bg="#2980B9")
beli1.pack(side="left")
Button(beli1, font="Junegull 24 bold", bg="Orange", text="1", fg="#ECF0F1", cursor="hand2", width = 2, height= 1, command=lambda: getlayar(1)).pack(padx = 5, pady = 5)
Button(beli1, font="Junegull 24 bold", bg="Orange", text="4", fg="#ECF0F1", cursor="hand2", command=lambda: getlayar(4)).pack(padx = 5, pady = 5)

beli2 = Frame(beli, bg="#2980B9")
beli2.pack(side="left")
Button(beli2, font="Junegull 24 bold", bg="Orange", text="2", fg="#ECF0F1", cursor="hand2", command=lambda: getlayar(2)).pack(padx = 5, pady = 5)
Button(beli2, font="Junegull 24 bold", bg="Orange", text="5", fg="#ECF0F1", cursor="hand2", command=lambda: getlayar(5)).pack(padx = 5, pady = 5)

beli3 = Frame(beli, bg="#2980B9")
beli3.pack(side="left")
Button(beli3, font="Junegull 24 bold", bg="Orange", text="3", fg="#ECF0F1", cursor="hand2", command=lambda: getlayar(3)).pack(padx = 5, pady = 5)
Button(beli3, font="Junegull 24 bold", bg="Orange", text="6", fg="#ECF0F1", cursor="hand2", command=lambda: getlayar(6)).pack(padx = 5, pady = 5)

def belii():
    global saldo
    angka = int(screen.get())
    for i in itr:
        if i == angka and saldo>= harga[i] and stok[i] > 0:
            jmlh[i] += 1
            screen.delete(0, END)
            screen.insert(0, "Minuman telah dibeli!")
            stok[i] -= 1
            messagebox.showinfo("Pembelian", "Anda telah membeli " + str(minuman[i] + " x " + str(jmlh[i]) + "\nStok tersisa: " + str(stok[i]) + " pcs"))
            saldo -= harga[i]
            screen.delete(0, END)
        elif i == angka and saldo < harga[i]:
            screen.delete(0, END)
            screen.insert(0, "Uang anda tidak cukup.")
            messagebox.showerror("Pembelian", "Uang anda tidak cukup untuk membeli minuman ini.")
            screen.delete(0, END)
        elif i == angka and stok[i] <= 0:
            screen.delete(0, END)
            screen.insert(0, "Stok kosong.")
            messagebox.showerror("Pembelian", "Minuman yang anda pilih sedang kosong.")
            screen.delete(0, END)

beli4 = Frame(beli, bg="#2980B9")
beli4.pack(side="left")
Button(beli4, font="Bubbly 24 bold", bg="Orange", text="DEL", fg="#ECF0F1", cursor="hand2", width = 4, command=lambda: hpslayar()).pack(padx = 5, pady = 5)
Button(beli4, font="Bubbly 24 bold", bg="Orange", text="✔", fg="#ECF0F1", cursor="hand2", width= 4, command=lambda: belii()).pack(padx = 5, pady = 5)

# Bagian input uang
def saldo1():
    global saldo
    saldo += 1000

def saldo2():
    global saldo
    saldo += 2000

def saldo5():
    global saldo
    saldo += 5000

def saldo10():
    global saldo
    saldo += 10000

def saldo20():
    global saldo
    saldo += 20000

def saldo50():
    global saldo
    saldo += 50000

def saldo100():
    global saldo
    saldo += 100000

Label(kanan, font= 'Bubbly 20 bold', bg= "#2980B9", fg= "Orange", text= "Masukkan uang di sini").pack(side="top", padx = 5, pady= 5)
masuk = Frame(kanan, bg="#2980B9", relief="raise")
masuk.pack(side="bottom", padx = 5, pady = 5)
saldoo = Label(kanan, font="Junegull 16 bold", text="SALDO: Rp" + str(saldo), fg="white", bg= '#023246', anchor=E)
saldoo.pack(side="bottom", padx = 10, pady = 10)

masuk1 = Frame(masuk, bg="#2980B9")
masuk1.pack(side="left")
Button(masuk1, font="Junegull 16 bold", bg="Orange", text="1K", fg="#ECF0F1", cursor="hand2", width=4, height=1, command=lambda: saldo1()).pack(padx = 5, pady = 5)
Button(masuk1, font="Junegull 16 bold", bg="Orange", text="10k", fg="#ECF0F1", cursor="hand2", width=4, height=1, command=lambda: saldo10()).pack(padx = 5, pady = 5)


masuk2 = Frame(masuk, bg="#2980B9")
masuk2.pack(side="left")
Button(masuk2, font="Junegull 16 bold", bg="Orange", text="2K", fg="#ECF0F1", cursor="hand2", width=4, height=1, command=lambda: saldo2()).pack(padx = 5, pady = 5)
Button(masuk2, font="Junegull 16 bold", bg="Orange", text="20K", fg="#ECF0F1", cursor="hand2", width=4, height=1, command=lambda: saldo20()).pack(padx = 5, pady = 5)

masuk3 = Frame(masuk, bg="#2980B9")
masuk3.pack(side="left")
Button(masuk3, font="Junegull 16 bold", bg="Orange", text="5K", fg="#ECF0F1", cursor="hand2", width=4, height=1, command=lambda: saldo5()).pack(padx = 5, pady = 5)
Button(masuk3, font="Junegull 16 bold", bg="Orange", text="50K", fg="#ECF0F1", cursor="hand2", width=4, height=1, command=lambda: saldo50()).pack(padx = 5, pady = 5)

masuk4 = Frame(masuk, bg="#2980B9")
masuk4.pack(side="left")
Button(masuk4, font="Junegull 16 bold", bg="Orange", text="100K", fg="#ECF0F1", cursor="hand2", width=4, height=3, command=lambda: saldo100()).pack(padx = 5, pady = 5)

def tampilsaldo():
    saldoo['text'] = "SALDO: Rp" + str(saldo)
    root.after(150, tampilsaldo)

# Frame Kiri
kiri = Frame(root, bg = 'Orange')
kiri.pack(side = 'left', padx = 20, pady = 20)

vending = Frame(kiri, bg = 'Orange')
vending.pack(padx = 10, pady = 10)

img1 = PhotoImage(file="vend2.png")
vending1 = Button(vending, image = img1, bg= '#023246', cursor="hand2", relief=FLAT)
vending1.pack(padx = 10, pady = 10)

tampilsaldo()
root.mainloop()