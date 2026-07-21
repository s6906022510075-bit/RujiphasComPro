for i in range(60,140,10):
    cal_kph = i * 0.6214

print("KPH\tMPH")
print("-----------------")
for i in range(60,140,10):
    cal_kph = i * 0.6214
    print(f"{i}\t{cal_kph:.1f}")