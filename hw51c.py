import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

dat=[-1.85142667 ,-2.0862657 , -1.76382996, -1.44755012 ,-2.23350803 ,-1.17419516]
dat2=[ 0.13052159 , 0.26719907 , 0.76923717 , 0.03236004,  0.85683387 ,-0.4863988 ]
stat_val, p_val = stats.ttest_ind(dat, dat2, equal_var=False)
#看看两个分布在均值上有没有显著差异
#注意，这里我们生成的第二组数据样本大小、方差和第一组均不相等，在运用t检验时需要使用Welch's t-test
#即指定ttest_ind中的equal_var=False。
print ('Two-sample t-statistic = %6.3f, p-value = %6.14f' % (stat_val, p_val))


