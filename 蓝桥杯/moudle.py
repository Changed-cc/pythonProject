import statistics
num = [1,2,3,4,5,6,8,8,9,7]
print(statistics.mean(num))#算术平均数
print(statistics.median(num))#中位数
print(statistics.median_low(num))#低中位数
print(statistics.median_high(num))#高中位数
print(statistics.mode(num))#众数
print(statistics.pvariance(num))#计算数据的总体方差
