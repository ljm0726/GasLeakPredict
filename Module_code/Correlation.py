

def correlation(data_file): #pearson ěę´ęłě
    print(data_file)
    corr1 = data_file.corr(method = 'pearson')
    # corr2 =  stats.spearmanr(f3)
    print(corr1)
    return corr1

