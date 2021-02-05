import sys
try:
    a = open(sys.argv[1],"r")
    c = open(sys.argv[2], "r")
except IOError:
    print("IOError: cannot open", sys.argv[2],".txt")
    print("- Game Over -")
    quit()
except IndexError:
    print("IndexError: number of input files less than expected.")
    print("- Game Over -")
    quit()


def main(x,lines):
    global b
    global truelist
    global div
    global nondiv
    global fromm
    global too
    if b == len(lines):
        print("bitti")
        quit()
    try:
        print("")
        div,nondiv,fromm,too = "","","",""
        div = argumanlist[x][0]
        nondiv = argumanlist[x][1]
        fromm = argumanlist[x][2]
        too = argumanlist[x][3]
        div = round(float(div))
        nondiv = round(float(nondiv))
        fromm = round(float(fromm))
        too = round(float(too))


        k = True
        x = fromm - 1
        while k :
            x +=1
            if x % div == 0 and x % nondiv != 0:
                truelist.append(str(x))
            if x == too:
                assert (" ".join(truelist)) == lines[b].rstrip("\n")
                print(" ----------------------------------","\n","My results: "," ".join(truelist),"\n","Results to compare: ",lines[b].rstrip("\n"),"\n","Goool!!!","\n","----------------------------------")
                break
    except IndexError:
        print("----------------------------------")
        print("IndexError: number of operands less than expected.")
        print("Given input:", div, nondiv, fromm, too)
        print("----------------------------------")


    except ZeroDivisionError:
        print("----------------------------------")
        print("ZeroDivisionError: You can't divide by 0")
        print("Given input:", div, nondiv, fromm, too)
        print("----------------------------------")

    except ValueError:
        print("----------------------------------")
        print("ValueError: only numeric input is accepted.")
        print("Given input:",div,nondiv,fromm,too)
        print("----------------------------------")
    except AssertionError:
        print(" ----------------------------------", "\n", "My results: ", " ".join(truelist), "\n","Results to compare: ", lines[b].rstrip("\n"), "\n","Assertion Error: results don’t match." , "\n","----------------------------------")

    except:
        print("kaBOOM: run for your life!")
    finally:
        b = b+1
        truelist = []
try:
    argumanlist = []
    truelist = []
    lines = c.readlines()
    b = 0
    for f in a.readlines():
        argumanlist.append(f.rstrip("\n").split())
    a.close()
    a = open("operands.txt","r")
    for x in range(len(a.readlines())):
        main(x,lines)
except:
    pass
finally:
    print(" -Game Over-")
