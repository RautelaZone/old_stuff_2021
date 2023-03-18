value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
rom = "MCMXCIV"
pre = 0
ans = 0
n = len(rom)
for i in range(n - 1, -1, -1):
    if value[rom[i]] >= pre:
        ans += value[rom[i]]
    else:
        ans -= value[rom[i]]
    pre = value[rom[i]]
print(ans)