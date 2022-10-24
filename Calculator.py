def add(x,y):
    return x + y
def substract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Select Operasi Hitungan")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    pilih = input("Pilihan (1/2/3/4): ")
    if pilih in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if pilih == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif pilih == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif pilih == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif pilih == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next1 = input("Lanjut (yes/no): ")
        if next1 == "no":
          break
    else:
        print("Ketik ulang")
