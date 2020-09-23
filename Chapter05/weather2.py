from source import daily, weekly

print("Daily forcast:", daily.forecast())
print("Weekly forcast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)