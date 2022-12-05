import pandas as pd
from scipy.stats import chi2

def removeErr(x, f): #잡음을 제거
    x['p_value'] = 1 - chi2.cdf(x['mahala'], 12) #p_value 값을 구한다.
    cnt = 0
    print(x.loc[x.p_value > 0.001])
    for i in x.p_value:
        if i < 0.0001:    #p_value 값이 0.0001 보다 적은 값이면
            f = f.drop([f.index[cnt]]) #이상치라고 여기고 제거
            cnt -= 1
        cnt += 1

    wf = pd.DataFrame(f)
    print(wf)
    return wf
     #오류 값을 제거한 파일을 만듬.
