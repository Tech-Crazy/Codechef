n = int(input())
arr = list(map(int,input().split()))
even_numbers = len(list(filter(lambda x: x%2 == 0, arr)))
if even_numbers > n - even_numbers:
    print("READY FOR BATTLE")
else:
    print("NOT READY")