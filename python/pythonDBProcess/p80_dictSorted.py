wordInfo = {'laundryMachine':60, 'fanWithoutWings':80, 'autoCleaningRobot':65 ,'fridge':30}

myxticks = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(myxticks)

myxticks = sorted(wordInfo.keys(), reverse=True)
print(myxticks)

myxticks = sorted(wordInfo.values(), reverse=True)
print(myxticks)
