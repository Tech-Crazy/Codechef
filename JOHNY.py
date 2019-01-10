for _ in range(int(input())):
    n = int(input())
    songs = list(map(int,input().split()))
    k = int(input())
    johny = songs[k-1]
    maxsong = max(songs)
    while maxsong != johny:
        songs.remove(maxsong)
        maxsong = max(songs)
        n-=1
    print(n)