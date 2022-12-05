import AddTemp
import Normalization
import Correlation
import DatafileChage
import MahalaDistance
import PredictTemp
import CollectTemp
import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd

original_data_path = 'C:/Users/ljm/Desktop/data_file/SampleRawData/2.dat' #초기 데이터 파일 2~27까지
data_path = 'C:/Users/ljm/Desktop/data_file/final_Data.csv' #오류제거와 기온추가된 최종 파일
#your datafile path;, original_datafile

data_file = pd.read_csv(data_path)

if __name__ =="__main__":
    """ 원본 파일 형식을 csv형식으로 만듬. 탭구분으로 바꿈 """
    # result = F_Chage.File_change(original_data_path)
    # result.to_csv("C:/Users/ljm/Desktop/gas_test10.csv", index=False)

    """ 데이터 정규화 """
    result = Normalization.transMinMax(data_file) ###사용
    # result = Normalization.transMaxAbs(data_file)
    # result = Normalization.transOrdinal(data_file) ###사용
    # result = Normalization.transStandard(data_file)
    # result = Normalization.transQuantile(data_file) ###사용

    """ data_file = data_file[["CH4"]] 형태로 한개씩 출력 가능 """
    plt.plot(result, linestyle="", marker="o", markersize="1")
    plt.show()

    """ 정규화된 파일 만들기 """
    # wf = pd.DataFrame(result)
    # wf.columns=[list(data_file)]
    # wf.to_csv("C:/Users/ljm/Desktop/gas_test12.csv", index=False, header=True)


    """ 마할라노비스거리를 이용한 오류제거 """
    # result = MahalaDistance.mahala_distance(data_file) #제거까지 마친 리스트를 return
    # result.to_csv("C:/Users/ljm/Desktop/gas_test11.csv", index=False) #오류 값을 제거한 파일을 만듬.


    """ 지역의 기온을 가져와서 요일별 최소기온, 최고기온 데이터 추가 """
    # result = AddTemp.add_Temp(data_file) #기온 추가된 데이터 return
    # result.to_csv("C:/Users/ljm/Desktop/gas_test10.csv", index=False)


    """ 최종데이터의 상관 관계를 구함 """
    # result = Correlation.correlation(data_file) #상관계수 리턴
    # sns.heatmap(result, annot=True, fmt='.2f', cmap='Blues')
    # plt.show()


    """ 최종 데이터를 확인하여 위험 기준을 정하여 온도를 비교해서 출력 """
    while(1):
        val1, val2 = CollectTemp.collectTemp();     #센서 값을 받음
        result = PredictTemp.predictTemp(val1, val2)    #센서 값을 예측 온도와 비교해서 결과 출력

        print(result)
