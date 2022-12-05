import numpy as np
import scipy as sp
import RemoveErr

def mahala_distance(data_file):
    def mahalanobis(x=None, data=None, cov=None):
        """Compute the Mahalanobis Distance between each row of x and the data
        x    : 데이터의 값
        data : 비교할 특징의 평균값
        cov  : 공분산행렬을 통한 상관관계
        d^2 = (x - m) C^-1 (x _ m) => 거리 구하는 공식을 이용 마할라노비스 거리를 측정 하는 수식. C인 공분산행렬을 통해 곱해준다.
        """
        x_minus_mu = x - np.mean(data) #x-m
        if not cov:
            cov = np.cov(data.values.T) #C
        inv_covmat = sp.linalg.inv(cov) #C^-1
        left_term = np.dot(x_minus_mu, inv_covmat) #x-m * c^-1
        mahal = np.dot(left_term, x_minus_mu.T) #(x-m)^T * left_term
        return mahal.diagonal()

    df_x = data_file[["FRAC_HRS_SINCE_JAN1", "CavityTemp", "DasTemp", "EtalonTemp", "WarmBoxTemp", "OutletValve", "CH4", "WIND_N", "WIND_E", "WIND_DIR_SDEV", "CAR_SPEED"]] #,"MinTemp","MaxTemp","DailyTemp_range"
    df_x['mahala'] = mahalanobis(x=df_x, data=data_file[["FRAC_HRS_SINCE_JAN1", "CavityTemp", "DasTemp", "EtalonTemp", "WarmBoxTemp", "OutletValve", "CH4", "WIND_N", "WIND_E", "WIND_DIR_SDEV", "CAR_SPEED"]])

    result = RemoveErr.removeErr(df_x, data_file) #임시로 5000개로 설정.
    return result

