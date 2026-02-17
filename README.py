paynet_mal = {}
xazna = 0
menyu = """
    Paynetimizga xush kelipsiz!
    
    1) Paynetda foydalanish
    2) Paynet tarixini korish
    3) Paynet xaznasini korish
    0) Chiqish"""
operatorlar = ["99", "98", "97", "95", "94", "93", "91",
               "90", "88", "77", "70", "55", "50", "33", "20"]
while True:
    print(menyu)
    menyu_tanlash = int(input("\n\tMenyulardan birini tanlang: "))
    if menyu_tanlash == 1:
        while True:
            raqam = int(input("\tRaqamingizni kiriting: +998 "))
            if len(str(raqam)) == 9 in operatorlar:
                pul = int(input("\tQancha miqdorda pul tashamoqchisiz: "))
                if pul >= 200:
                    uslug = pul // 50
                    pul -= uslug
                    xazna += uslug
                    paynet_mal[raqam] = pul
                    print(f"\t{pul} so`m tushdi, 0.5% {uslug} so`m ushlab qolindi!")
                    break
                else:
                    print("Paynet uchun bu pul yetarli emas")
            else:
                print("\tRaqam noto`g`ri")
    elif menyu_tanlash == 2:
        print(f"\t{paynet_mal}")
    elif menyu_tanlash == 3:
        print(f"\t{xazna}")
    elif menyu_tanlash == 0:
        print("\tTashrifingiz uchun rahmat!")
        break
    else:
        print("\n\tBunday menyu yoq")
