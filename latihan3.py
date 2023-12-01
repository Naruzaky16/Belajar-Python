umur = int(input("masukan umur anda :"))
keanggotaan_bioskop = input("apa kamu memiliki kartu keanggotan (yes/no) :")
if (umur > 18) or keanggotaan_bioskop == "yes":
    print("selamat anda dapat memenuhi syarat tiket untuk diskon")
else :
    print("tidak diskon")