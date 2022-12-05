import pandas as pd

def add_Temp(data_file2):
    for i in range(len(data_file2.FRAC_HRS_SINCE_JAN1)):
        print(i)
        if data_file2.FRAC_HRS_SINCE_JAN1[i] < 1745:
            data_file2.MinTemp[i] = 37.0
            data_file2.MaxTemp[i] = 46.0
            data_file2.DailyTemp_range[i] = 9.0
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1770:
            data_file2.MinTemp[i] = 27.0
            data_file2.MaxTemp[i] = 45.0
            data_file2.DailyTemp_range[i] = 18.0
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1790:
            data_file2.MinTemp[i] = 26.1
            data_file2.MaxTemp[i] = 50.0
            data_file2.DailyTemp_range[i]= 23.9
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1820:
            data_file2.MinTemp[i] = 43.0
            data_file2.MaxTemp[i] = 69.1
            data_file2.DailyTemp_range[i] = 26.1
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1919:
            data_file2.MinTemp[i] = 60.1
            data_file2.MaxTemp[i] = 89.1
            data_file2.DailyTemp_range[i] = 29.0
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1935:
            data_file2.MinTemp[i] = 55.0
            data_file2.MaxTemp[i] = 82.9
            data_file2.DailyTemp_range[i] = 27.9
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1960:
            data_file2.MinTemp[i] = 51.1
            data_file2.MaxTemp[i] = 77.0
            data_file2.DailyTemp_range[i] = 25.9
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 1985:
            data_file2.MinTemp[i]= 62.1
            data_file2.MaxTemp[i] = 75.0
            data_file2.DailyTemp_range[i] = 12.9
        elif data_file2.FRAC_HRS_SINCE_JAN1[i] < 2005:
            data_file2.MinTemp[i] = 60.1
            data_file2.MaxTemp[i] = 79.0
            data_file2.DailyTemp_range[i] = 18.9

    wf = pd.DataFrame(data_file2)

    return wf
