def split_minutes(minutes):
   if minutes<0:
     return None
   hours= minutes // 60 
   minutes = minutes % 60
   return hours,minutes
minutes=int(input(" enter  total time "))
print(split_minutes(minutes))
