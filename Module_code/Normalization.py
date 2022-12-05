from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import quantile_transform
from sklearn.preprocessing import OrdinalEncoder

def transMinMax(data_file):
    minMaxScaler = MinMaxScaler()
    trans_minMaxScaler = minMaxScaler.fit_transform(data_file)
    return trans_minMaxScaler

def transMaxAbs(data_file):
    maxAbsScaler = MaxAbsScaler()
    trans_maxAbsScaler = maxAbsScaler.fit_transform(data_file)
    return trans_maxAbsScaler

def transQuantile(data_file):
    quantile = quantile_transform()
    trans_quantileScaler = quantile.fit_transform(data_file)
    return trans_quantileScaler

def transOrdinal(data_file):
    ordinal = OrdinalEncoder()
    trans_ordinal = ordinal.fit_transform(data_file)
    return trans_ordinal

def transStandard(data_file):
    standardScaler = StandardScaler()
    trans_standard = standardScaler.fit_transform(data_file)
    return trans_standard