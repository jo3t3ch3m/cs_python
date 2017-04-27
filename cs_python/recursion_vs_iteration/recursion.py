def MovingTheBall(listOfBalls,position,numCell,flagOfExecution):
    flag = 0
    if flagOfExecution==0:
        positionTmp = position
    else:
        positionTmp = (position[0]+choice([-1,0,1]),position[1]+choice([-1,0,1]),0)
    for i in range( 0, len(listOfBalls) ):
        if positionTmp==listOfBalls[i].pos:
            flag=1


    if flag==1:
        return MovingTheBall(lista,(position[0]+choice([-1,0,1]),position[1]+choice([-1,0,1]),0),numCell,1)
    else:
        if positionTmp[0]==0 or positionTmp[0]>=numCell or positionTmp[0]<=-numCell or positionTmp[1]>=numCell or positionTmp[1]<=-numCell:
            return MovingTheBall(lista,(position[0]+choice([-1,0,1]),position[1]+choice([-1,0,1]),0),numCell,1)

        return positionTmp
