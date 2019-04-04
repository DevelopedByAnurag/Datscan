
try:
    from os import system, name 
    import os
except:
    print("\033[31m \033[1m Error importing OS Module !! \033[0m")

def cls():
    if name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    
def ERR0R(T3MP):
    cls()
    print("\033[31m \033[1m"+T3MP+"\033[0m")

def T4KE_1NPUT(T3MP):
    T3MP1 = input(T3MP)
    return T3MP1
    
def B0LD_T3XT(T3MP):
    print("\033[1m"+ T3MP +"\033[0m")

def PR1NT_T3XT(T3MP):
    print(T3MP)
       
    
def L04D_M0DUL3(T3MP):
    try:
       exec(T3MP, globals())
    except:
        ERR0R("Failed to run "+ T3MP)
        PR1NT_T3XT("Please install the desired module and press any key to Continue...")
        t = T4KE_1NPUT("You can also press # to exit DatScan ")
        if t == "#":
            exit()
        else:
            L04D_M0DUL3(T3MP)   



def ACCESS_CH3CK(L0C,L0C_N):
    CH3CK = os.access(L0C, os.F_OK)
    if CH3CK == False:
        ERR0R("Access check could not be performed at "+L0C_N+" folder")
    else:
        CH3CK = os.access(L0C, os.R_OK)
        if CH3CK == False:
            ERR0R("Error Access Program does not have Read Acess to "+L0C_N)
            PR1NT_T3XT("Please check the desired permissions and press any key to Continue...")
            t = T4KE_1NPUT("You can also press # to exit DatScan ")
            if t == "#":
                exit()
            else:
                ACCESS_CH3CK(L0C,L0C_N)
        else:
            CH3CK = os.access(L0C, os.W_OK)
            if CH3CK == False:
                ERR0R("Error Access Program does not have Write Acess to "+L0C_N)
                PR1NT_T3XT("Please check the desired permissions and press any key to Continue...")
                t = T4KE_1NPUT("You can also press # to exit DatScan ")
                if t == "#":
                    exit()
                else:
                    ACCESS_CH3CK(L0C,L0C_N)

ACCESS_CH3CK("accesscheck","core")
ACCESS_CH3CK("data/accesscheck","Data")
ACCESS_CH3CK("Modules/accesscheck","Modules folder")
##libraries
B0LD_T3XT("INitializing....")
cls()
L04D_M0DUL3("from header import HE4D3R")
L04D_M0DUL3("import csv")
L04D_M0DUL3("import pandas as pd")

def G3T_US3R_CH0IC3_S0L0(T3MP):
    T3MPR4RY = 0
    with open(T3MP, newline='') as f:
        reader = csv.reader(f)
        head = next(reader)
        B0LD_T3XT("Select one head you want us to process:")
    for T3MP1 in head:
        T3MPR4RY = T3MPR4RY + 1
        PR1NT_T3XT("\t "+str(T3MPR4RY)+" "+str(T3MP1))
    TM = T4KE_1NPUT("Enter the row numbers: ")
    try:
        TM = head[int(TM)-1]
    except:
        cls()
        ERR0R("Error try again !!")
        G3T_US3R_CH0IC3_S0L0(T3MP)
    return TM

def give_head():
    row = [likes, comment, id, tim, image_src ]
    with open('insta.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    
    
def ST4ND4R7IS3_CSV(S4V3):
    T3MP = S4V3+"/"+S4V3.replace('data/', '')+".csv"
    return T3MP


#basic functions

def R34D3R(M0DLESL1ST):
    global M0DUL3_L1ST
    M0DUL3_L1ST = []
    M0DUL3_F1l3 = open(M0DLESL1ST,'r')
    L1N3 = M0DUL3_F1l3.readline()
    while L1N3:
        M0DUL3_L1ST.append(L1N3.rstrip())
        L1N3 = M0DUL3_F1l3.readline()
    M0DUL3_F1l3.close()
    
def D1SPL4Y_M0DUL3(T3MP):
    R34D3R(T3MP)
    T3MPR4RY = 0
    for T3MP in M0DUL3_L1ST:
        T3MPR4RY = T3MPR4RY + 1
        PR1NT_T3XT("\t "+str(T3MPR4RY)+" "+str(T3MP))
        
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

def M4N4G3_D474():
    if ENTRY_0PTI0N =="3":
        B0LD_T3XT("Here is the List Of Existing DataSet")
        PR1NT_T3XT("press the number which dataset to delete")
        D1SPL4Y_M0DUL3('D474S37.txt')
        PR1NT_T3XT("to go back press # : ")
        OPTI0N = T4KE_1NPUT("Enter your Choice:- ")
        cls()
        D47A_M4N4G3R(M0DUL3_L1ST[int(OPTI0N)-1])




#base setup
def ST4ND4R7IS3_CSV(S4V3):
    T3MP = S4V3+"/"+S4V3.replace('data/', '')+".csv"
    return T3MP

def G37_1NPUT():
    T3MP = T4KE_1NPUT("Enter the tags you want to scrape and diffrencitate with help of spaces")
    T3MP0 = T3MP.split(" ")
    return T3MP0

def G3T_R0WN4M3(T3MP):
    with open('T3MP', newline='') as f:
        reader = csv.reader(f)
        head = next(reader)


def M3NU():
    HE4D3R()
    global ENTRY_0PTI0N
    ENTRY_0PTI0N = 0
    B0LD_T3XT("select one of the following task")
    PR1NT_T3XT("\t 1. Get New Data")
    PR1NT_T3XT("\t 2. Process Existing Data")
    PR1NT_T3XT("\t 3. Install/Uninstall Module")
    #dis={1:["Get New Data"],2:["Get New Data2"]}
    ENTRY_0PTI0N = T4KE_1NPUT("Enter Your Choice:- ")
    cls()
    M3NU2()


def M3NU2():
    global OPTI0N
    OPTI0N = 0
    if ENTRY_0PTI0N =="1":
        B0LD_T3XT("Which Data feching module to use")
        D1SPL4Y_M0DUL3('FM0DLESL1ST.txt')
        CH0IC3 = T4KE_1NPUT("Enter your Choice:- ")
        try:
            G3T_M0DULE(M0DUL3_L1ST[int(CH0IC3)-1])
        except:
            ERR0R("Invalid choice Try again !!!")
            M3NU2()

    elif ENTRY_0PTI0N =="2":
        B0LD_T3XT("What you want to do with Dataset")
        PR1NT_T3XT("\t 1. Pre-Process Data")
        PR1NT_T3XT("\t 2. Sentiment analysis")
        PR1NT_T3XT("\t 3. Data Translation")
        OPTI0N = input("Enter your Choice:- ")
        cls()
        AN4LYSE_M3NU()

    elif ENTRY_0PTI0N =="3":
        B0LD_T3XT("Select one of the following")
        PR1NT_T3XT("\t 1. Import a module ")
        PR1NT_T3XT("\t 2. Uninstall a module ")
        OPTI0N = T4KE_1NPUT("Enter your Choice:- ")
        cls()
        M0DULE_M3NU()

    else:
        ERR0R("Invalid choice try again \n")
        M3NU()


def AN4LYSE_M3NU():
    CH0IC3 = "0"
    if OPTI0N =='1':
        B0LD_T3XT("Choose the module for Data Prepocessing:")
        D1SPL4Y_M0DUL3("PR3PR0C3SSL1ST.txt")
        CH0IC3 = T4KE_1NPUT("Enter your Choice:- ")
        try:
            G3T_M0DULE(M0DUL3_L1ST[int(CH0IC3)-1])
        except:
            ERR0R("Invalid choice Try again !!!")
            AN4LYSE_M3NU()
            
    if OPTI0N =='2':
        B0LD_T3XT("Choose the module for Sentimental Analysis: ")
        D1SPL4Y_M0DUL3("4N4M0DLESL1ST.txt")
        CH0IC3 = T4KE_1NPUT("Enter your Choice:- ")
        try:
            G3T_M0DULE(M0DUL3_L1ST[int(CH0IC3)-1])
        except:
            ERR0R("Invalid choice Try again !!!")
            AN4LYSE_M3NU()

    elif OPTI0N =='3':
        B0LD_T3XT(" Choose the module for translating data:")
        D1SPL4Y_M0DUL3("TR4NSL4TI0NL1ST.txt")
        CH0IC3 = T4KE_1NPUT("Enter your Choice:- ")
        try:
            G3T_M0DULE(M0DUL3_L1ST[int(CH0IC3)-1])
        except:
            ERR0R("Invalid choice Try again !!!")
            AN4LYSE_M3NU()
    else:
        ERR0R("Invalid choice try again \n")
        M3NU2()



def G3T_M0DULE(T3MP):
    cls()
    B0LD_T3XT("Enter the Name of Folder to Store Data")
    T3MP0 = T4KE_1NPUT("Enter your Choice:- ")
    if os.path.isdir("data/"+T3MP0):
        ERR0R("DataSet With Same Name Might Exist")
        PR1NT_T3XT("1. Enter New Name")
        PR1NT_T3XT("2. Append New Data")
        PR1NT_T3XT("3. Delete Old Data and Continue")
        T3MP1 = T4KE_1NPUT("Enter your Choice:- ")
        if T3MP1 == "1":
            G3T_M0DULE(T3MP)
        elif T3MP1 == "2":
            D474_S37UP(T3MP0)
            M0DUL3_C4LL3R(T3MP ,T3MP0)
        elif T3MP1 == "3":
            R34D3R('D474S37.txt')
            D47A_M4N4G3R(T3MP0)
            D474_S37UP(T3MP0)
            M0DUL3_C4LL3R(T3MP ,T3MP0)
        else:
            ERR0R("Invalid Choice")
    else:
        D474_S37UP(T3MP0)
        B0LD_T3XT("Feching Module Further Everything will be handled by " + T3MP)
        M0DUL3_C4LL3R(T3MP ,T3MP0)


def D474_S37UP(T3MP):
    F1L3_M0D = open("D474S37.txt","a")
    F1L3_M0D.write("\n")
    F1L3_M0D.write(T3MP)
    F1L3_M0D.close()
    os.system("mkdir data/"+T3MP)


def M0DUL3_C4LL3R(T3MP ,T3MP0):
    try:
        exec("from Modules."+T3MP + " import RUNN3R")
    except:
        ERR0R("Error Importing the Module Try Reinstalling it...")
        M3NU()
    T3MP1 = "data/"+T3MP0
    try:
        RUNN3R(T3MP1)
    except:
        ERR0R("Error starting module might be Corrupt...")
        M3NU()
    PR1NT_T3XT("Data Scrapping Completed !!")
    M3NU()


def UN1NST4LL(T3MP):
    PR1NT_T3XT("uninstalling the module please wait...")
    os.system("rm -rf "+ T3MP)
    IN = 0
    L1S7 = ["MODULE_L1" , "MODULE_L2" ,"MODULE_L3" ,"MODULE_L4"]
    for UN1 in L1S7:
        UN1_F1N4L1Z3(T3MP,UN1,IN)
        IN = IN+1
    M3NU()


def M0DULE_M3NU():
    if OPTI0N =='1':
        B0LD_T3XT("Enter the link to import module (under development): ")
    
    elif OPTI0N =='2':
        B0LD_T3XT("Enter the name of module to be uninstalled: ")
        T3MP = T4KE_1NPUT("Enter your Choice:- ")
        #G37_M0DUL3S()
        T3MP0 = M0DUL3_CH3CK3R(T3MP)
        if T3MP0 == True:
            UN1NST4LL(T3MP)
        else:
            cls()
            ERR0R("Module not found please check it again")
    else:
        ERR0R("Invalid choice try again \n")
        M3NU2()

def D47A_M4N4G3R(T3MP):
    if OPTI0N == "#":
        cls()
        M3NU()
    else:
        os.system("rm -rf data/"+T3MP)
        R34D3R('D474S37.txt')
        M0DUL3_L1ST.remove(T3MP)
        L3N7 = len(M0DUL3_L1ST)
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

