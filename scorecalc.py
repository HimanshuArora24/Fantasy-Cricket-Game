def batpoints(runs,four,six,balls):
    strike_rate = (runs/balls)*100
    batscore = runs/2
    batscore += four+(six*2)

    if(runs>=100):
        batscore += 10
    elif(runs>=50):
        batscore += 5
    else:
        batscore = batscore

    if((strike_rate>=80)and(strike_rate<=100)):
        batscore += 2
    elif(strike_rate>100):
        batscore += 4
    else:
        batscore = batscore

    return batscore
        
def bowlpoints(wkts,overs,runs):
    economy = runs/overs
    bowlscore = wkts*10

    if(wkts>=5):
        bowlscore += 10
    elif(wkts>=3):
        bowlscore += 5

    if(economy<2):
        bowlscore += 10
    elif(economy<3.5):
        bowlscore += 7
    elif(economy<4.5):
        bowlscore += 4
    else:
        bowlscore = bowlscore

    return bowlscore

def fieldpoints(catches,stumping,runout):
    field = catches+stumping+runout
    fieldscore = field*10

    return fieldscore

     
