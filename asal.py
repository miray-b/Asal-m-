control_sayi = int(input("Asallığını kontrol etmek istediğiniz sayı: "))

def asal_control(control_sayi):
    if control_sayi < 2:
        return False
    for i in range(2, int(control_sayi ** 0.5) + 1):
        if control_sayi % i == 0:
            return False
    return True

if asal_control(control_sayi):
    print("Asal sayıdır.")

else:
    print("Asal sayı değildir.")
