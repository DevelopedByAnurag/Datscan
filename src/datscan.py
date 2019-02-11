import os
from header import HE4D3R

def cls():
    os.system("clear")

def D1SPL4Y_M0DUL3():
    T3MPR4RY = 0
    for T3MP in M0DUL3_L1ST:
        T3MPR4RY = T3MPR4RY + 1
        print("\t "+str(T3MPR4RY)+" "+str(T3MP))

def M0DUL3_CH3CK3R(M0DUL3):
    global MODULE_L1 , MODULE_L2 ,MODULE_L3 ,MODULE_L4
    R34D3R("4N4M0DLESL1ST.txt")
    MODULE_L1 = M0DUL3_L1ST
    R34D3R("FM0DLESL1ST.txt")
    MODULE_L2 = M0DUL3_L1ST
    R34D3R("PR3M0DLESL1ST.txt")
    MODULE_L3 = M0DUL3_L1ST
    R34D3R("S3RM0DLESL1ST.txt")
    MODULE_L4 = M0DUL3_L1ST
    
    return M0DUL3 in MODULE_L1+MODULE_L2+MODULE_L3+MODULE_L4

def UN1_F1N4L1Z3(T3MP,UN1,IN):
    F1L7 = ["4N4M0DLESL1ST.txt","FM0DLESL1ST.txt","PR3M0DLESL1ST.txt","S3RM0DLESL1ST.txt"]
    if T3MP in eval(UN1):
        eval(UN1).remove(T3MP)
        L3N7 = len(eval(UN1))
        INCR3=1
        F1L3_M0D = open(F1L7[IN], "w")
        for L1N3 in eval(UN1):
            F1L3_M0D.write(L1N3)
            if INCR3 < L3N7:
                INCR3=INCR3+1
                F1L3_M0D.write("\n")
        F1L3_M0D.close()


def UN1NST4LL(T3MP):
    print("uninstalling the module please wait...")
    os.system("rm -rf "+ T3MP)
    IN = 0
    L1S7 = ["MODULE_L1" , "MODULE_L2" ,"MODULE_L3" ,"MODULE_L4"]
    for UN1 in L1S7:
        UN1_F1N4L1Z3(T3MP,UN1,IN)
        IN = IN+1

def R34D3R(M0DLESL1ST):
    global M0DUL3_L1ST
    M0DUL3_L1ST = []
    M0DUL3_F1l3 = open(M0DLESL1ST,'r')
    L1N3 = M0DUL3_F1l3.readline()
    while L1N3:
        M0DUL3_L1ST.append(L1N3.rstrip())
        L1N3 = M0DUL3_F1l3.readline()
    M0DUL3_F1l3.close()

def M3NU():
    HE4D3R()
    global ENTRY_0PTI0N
    print("\033[1m select one of the following task \033[0m")
    print("\t 1. Get New Data")
    print("\t 2. Analyse Existing Data")
    print("\t 3. Install/Uninstall Module")
    ENTRY_0PTI0N = input("Enter Your Choice")
    cls()
    M3NU2()

def M3NU2():
    global OPTI0N
    if ENTRY_0PTI0N =="1":
        print("\033[1m Which Data feching module to use \033[0m")
        R34D3R('FM0DLESL1ST.txt')
        D1SPL4Y_M0DUL3()
        OPTI0N = input("Enter your Choice")
        cls()
        F3CHING_M0DULE(M0DUL3_L1ST[int(OPTI0N)-1])

    elif ENTRY_0PTI0N =="2":
        print("\033[1m What you want to do with Dataset \033[0m")
        print("\t 1. Sentiment analysis")
        print("\t 2. Future Prediction")
        print("\t 3. Searching")
        OPTI0N = input("Enter your Choice")
        cls()
        AN4LYSE_M3NU()

    elif ENTRY_0PTI0N =="3":
        print("\033[1m Select one of the following \033[0m")
        print("\t 1. Import a module ")
        print("\t 2. Uninstall a module ")
        OPTI0N = input("Enter your Choice")
        cls()
        M0DULE_M3NU()

    else:
        print("\033[1m Invalid choice try again \033[0m \n")
        M3NU()

def M0DULE_M3NU():
    if OPTI0N =='1':
        print("\033[1m Enter the link to import module (under development): \033[0m")
    
    elif OPTI0N =='2':
        print("\033[1m Enter the name of module to be uninstalled: \033[0m")
        T3MP = input("Enter your Choice")

        T3MP0 = M0DUL3_CH3CK3R(T3MP)
        if T3MP0 == True:
            UN1NST4LL(T3MP)
        else:
            cls()
            print("\033[1m module not found please check it again \033[0m \n \n \n")
    else:
        print("\033[1m Invalid choice try again \033[0m \n")
        M3NU2()

def AN4LYSE_M3NU():
    if OPTI0N =='1':
        print("\033[1m Choose the module for Sentimental Analysis: \033[0m")
        R34D3R("4N4M0DLESL1ST.txt")
        D1SPL4Y_M0DUL3()
    
    elif OPTI0N =='2':
        print("\033[1m Choose the module for Prediction: \033[0m")
        R34D3R("PR3M0DLESL1ST.txt")
        D1SPL4Y_M0DUL3()
    
    elif OPTI0N =='3':
        print("\033[1m Choose the module for Searching: \033[0m")
        R34D3R("S3RM0DLESL1ST.txt")
        D1SPL4Y_M0DUL3()
    
    else:
        print("\033[1m Invalid choice try again \033[0m \n")
        M3NU2()

def F3CHING_M0DULE(T3MP):
    cls()
    if T3MP in M0DUL3_L1ST:
        print("Enter the Name of Folder to Store Data")
        T3MP0 = input("Enter your Choice")
        if os.path.isdir("data/"+T3MP0):
            print("DataSet With Same Name Might Exist")
            print("1. Enter New Name")
            print("2. Append New Data")
            print("3. Delete Old Data and Continue")
            T3MP1 = input("Enter your Choice")
            if T3MP1 == "1":
                F3CHING_M0DULE(T3MP)
            elif T3MP1 == "2":
                D474_S37UP(T3MP)
                M0DUL3_C4LL3R(T3MP ,T3MP0)
            elif T3MP1 == "3":
                R34D3R('D474S37.txt')
                D47A_M4N4G3R(T3MP)
                D474_S37UP(T3MP)
                M0DUL3_C4LL3R(T3MP ,T3MP0)
            else:
                print("Invalid Choice")
        else:
            D474_S37UP(T3MP)
            print("\033[1m Feching Module Further Everything will be handled by " + T3MP +" \033[0m")
            M0DUL3_C4LL3R(T3MP ,T3MP0)
    else:
        print("Error invalid choice Try Again ")
        M3NU2()

def D474_S37UP(T3MP):
    F1L3_M0D = open("D474S37.txt", "a")
    F1L3_M0D.write("\n")
    F1L3_M0D.write(T3MP)
    F1L3_M0D.close()
    os.system("mkdir data/"+T3MP)

def M0DUL3_C4LL3R(T3MP ,T3MP0):
    eval("from Modules."+T3MP + " import RUNN3R")
    T3MP1 = "data/"+T3MP0
    RUNN3R(T3MP1)

def ST4ND4R7IS3_CSV(S4V3):
    T3MP = S4V3+".csv"
    return T3MP

def M4N4G3_D474():
    if ENTRY_0PTI0N =="3":
        print("\033[1m Here is the List Of Existing DataSet \033[0m")
        print("press the number which dataset to delete")
        R34D3R('D474S37.txt')
        D1SPL4Y_M0DUL3()
        print("to go back press # : ")
        OPTI0N = input("Enter your Choice")
        cls()
        D47A_M4N4G3R(M0DUL3_L1ST[int(OPTI0N)-1])
        

def D47A_M4N4G3R(T3MP):
    if OPTI0N == "#":
        cls()
        M3NU()
    else:
        os.system("rm -rf data/"+T3MP)
        M0DUL3_L1ST.remove(T3MP)
        L3N7 = len(eval(UN1))
        INCR3=1
        F1L3_M0D = open("D474S37.txt", "w")
        for L1N3 in M0DUL3_L1ST:
            F1L3_M0D.write(L1N3)
            if INCR3 < L3N7:
                INCR3=INCR3+1
                F1L3_M0D.write("\n")
        F1L3_M0D.close()
        M4N4G3_D474()

cls()
M3NU()

