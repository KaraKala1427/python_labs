print("Inter the numbers")
sec = int(input())
sec_pm = 60
sec_ph = 3600
sec_pd = 86400

days = int(sec / sec_pd)
sec = sec % sec_pd
days_res= str(days).zfill(2)

hours = int(sec/ sec_ph)
sec = sec % sec_ph
hours_res=str(hours).zfill(2)

minutes = int(sec / sec_pm)
sec = sec % sec_pm
min_str=str(minutes)
min_res=min_str.zfill(2)

print( "Days =",days_res, "\nHours =", hours_res,"\nMinutes =", min_res,"\nSeconds =", sec)

