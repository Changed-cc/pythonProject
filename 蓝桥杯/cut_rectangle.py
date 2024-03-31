#切割的最大的正方形以宽来切
Length = 2019
Width = 324
count = 0
while(Width != Length):
    Length = Length - Width
    if Length < Width:
        Width,Length = Length,Width
    count += 1
print(count+1)