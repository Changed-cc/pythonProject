#1.日期增加
import datetime
import calendar

t1 = datetime.date(2024,3,31)
t2 = datetime.timedelta(days=100)
t3 = datetime.timedelta(2000,2024)
print(t1,t2,t3,t1+t2,t1+t2+t3,sep="\n")

#2.给定日期求星期
print(t1.weekday())#星期一从0开始的
print(t1.isoweekday())#星期一从1开始的
#3.标准化
print(t1.isoformat())
#4.返回公元公历到现在的天数
print(t1.toordinal())
#5.输出
print(t1.__format__('%Y/%m/%d'))
#6.判断是否为闰年
print(calendar.isleap(2024))
#7.返回两年之间的闰年总数
print(calendar.leapdays(2000,2024))