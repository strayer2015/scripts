#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6



# generate date, days in week week
def genDateWeek(month,firstDay):
    daysInWeekTuple = "Mon","Tue","Wed","Thu","Fri","Sat","Sun"
    monthsLUT = {
                "jan":31,
                "feb":28,
                "mar":31,
                "apr":30,
                "may":31,
                "jun":30,
                "jul":31,
                "aug":31,
                "sep":30,
                "oct":31,
                "nov":30,
                "dec":31}
    f = open(month+'.txt','w')
    days = monthsLUT[month]
    for ii in range(days):
        d_idx = ((days - ii-1) + (int(firstDay)-1)) % 7
        f.write(month.capitalize() + ' ' 
                                   + str(days-ii)
                                   + ' '
                                   + daysInWeekTuple[d_idx]+"\n\n")


month = input('Enter month: ')
firstDay = input('Enter the weekday of 1st day in '+month+': ')
genDateWeek(month.lower(),firstDay.lower())
