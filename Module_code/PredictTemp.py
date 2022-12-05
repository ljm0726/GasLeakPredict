def predictTemp(minTemp, maxTemp):
    """ 온도 예측
    * avg(min) > sesnsor_val1 && avg(min) + avg(range) > sensor_val2
    * minTemp = ch4농도가 비교적 높을 때의 avg(min)
    * maxTemp = ch4농도가 비교적 높을 때 avg(min)과 avg(min) + avg(range)의 합
    * 상관계수를 통해 데이터를 확인 하였을 때 range(일교차)와 관련 있음.
    * avg(range)(일교차) < 14.61 일 때
    """
    if(minTemp <= 36.95 and maxTemp <= 51.56):
        return "\n주의 필요!"

    return "\n확률 낮음!"