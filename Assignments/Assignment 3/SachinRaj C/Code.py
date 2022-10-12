import time
i=1
while True:
    if(i>0 and i<=15):
        time.sleep(2)
        for j in range(1,16):
            print("Red {} sec".format(j))
            time.sleep(0.5)
            i+=1
            print("**********")
    elif(i>15 and i<=18):
        time.sleep(2)
        for j in range(1,4):
            print("yellow {} sec".format(j))
            i+=1
            time.sleep(0.5)
            print("**********")
    elif(i>18 and i<=33):
        time.sleep(2)
        for j in range(1,16):
            print("Green {} sec".format(j))
            i+=1
            time.sleep(0.5)
            print("***********")
            i=1
J
