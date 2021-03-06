from message3 import message3

def hyperna_msg3():
    print("Sodium content in fluids: ")
    print("+-------------------+")
    print("| G-ORS : 75 mmol/l |")
    print("| 1/2 NS: 77 mmol/l |")
    print("| 1/2 AC: 66 mmol/l |")
    print("+-------------------+\n")

def hyperna_calc3():
    print("FLUID VOLUME CALCULATION:")
    wt = float(input(" Weight (kg): "))
    serum = input(" Serum Sodium (mmol/l): ")
    fluid = int(input(" Fluid choice\
\n (1) G-ORS\
\n (2) 1/2 NS\
\n (3) 1/2 Acetate\
\nEnter code: "))
    if fluid == 1:
        fluid = 75
    elif fluid == 2:
        fluid = 77
    elif fluid == 3:
        fluid = 66
    corr = ((10/((float(serum)-float(fluid))/((float(wt)*0.6)+1)))*1000)/24
    print("\nCorrection volume:", round(corr, 2), "ml/hr\n")

    print("25% DIET CURTAIL")
    kwash = str(input(" Marasmus(1) | Kwash(2): "))
    if kwash == "1":
        curt = (wt*10)*0.75
    elif kwash == "2":
        curt = (wt*9)*0.75
    print("\nCurtailed diet:", round(curt, 2), "ml/2h + Salt added.")
    ques = str(input("Want to do anything else? (y/n): "))
    if ques == "y" or ques == "Y":
        from main3 import main3
    else:
        print("Thanks for using auto-calc!")
        exit()

hyperna_msg3()
hyperna_calc3()
#input("Press `Enter' to exit.")
