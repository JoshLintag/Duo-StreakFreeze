import duolingo
username = 'joshlintag'
password = ''

print('Duolingo Streak Freeze')

lingo  = duolingo.Duolingo(username, password)
streakInfo = lingo.get_streak_info() #pulls streak info such as streak, daily goal, extended (boolean)
userInfo = lingo.get_user_info() #pulls full name
name = userInfo.get('fullname')
numberOfStreaks = streakInfo.get('site_streak')
isStreakFrozen = streakInfo.get('streak_extended_today')


print('Hey,', name)
print('Your current streak is', numberOfStreaks, 'days')

if(isStreakFrozen == True): #checks if Streak is extended, otherwise buy streak freeze
    print('You currently have streak freeze on')
else:
    print('Your streak is not frozen') 
    lingo.buy_streak_freeze() #returns an exception if not enough Lingots
    print('You bought streak freeze') #prints this if streak freeze is successfully bought

k=input("press close to exit") #so it wont close automatically lmao


