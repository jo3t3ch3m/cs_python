def MovingTheBall(listOfBalls,position,numCell):
    while 1:
        stop=1
        positionTmp = (position[0]+choice([-1,0,1]),position[1]+choice([-1,0,1]),0)
        for i in range(0,len(listOfBalls)):
            if positionTmp==listOfBalls[i].pos:
                stop=0
        if stop==1:
            if (positionTmp[0]==0 or positionTmp[0]>=numCell or positionTmp[0]<=-numCell or positionTmp[1]>=numCell or positionTmp[1]<=-numCell):
                stop=0
        else:
            return positionTmp
