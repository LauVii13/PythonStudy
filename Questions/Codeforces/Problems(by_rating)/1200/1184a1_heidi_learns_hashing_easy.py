r = int(input())

if r % 2 == 0 or r == 1 or r == 3:
    print("NO")
else:
    print(f"1 {(r - 3) // 2}")
