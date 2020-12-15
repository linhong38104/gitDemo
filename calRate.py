#F=P*(1+i)N(次方) F:复利终dao值；P: 本金；i:利率源；N：利率获取时bai间的整数倍

def invest(amount,rate,time): #amount资金，rate利率，time投资时间
    print('princial amount:'+str(amount))
    for t in range(1,time+1):
        frate = amount*((1+rate/100)**t)
        print('year'+str(t)+':'+'$'+str(frate))

invest(100,5,10)
