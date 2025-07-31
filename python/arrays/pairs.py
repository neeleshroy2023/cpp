arr = [10,5,2,3,-6,9,11]
S = 4

mpp = {}
for i in range(len(arr)):
  if arr[i] in mpp:
    print([S - arr[i], arr[i]])
  else:
    mpp[S - arr[i]] = arr[i];