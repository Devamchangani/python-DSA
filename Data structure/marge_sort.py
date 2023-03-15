import random
import time


def random_list():
  n = int(input("Enter a Number size: "))
  for i in range(n):
    l1.append(random.randrange(0,n))
    
  print(f"MAIN LIST :- {l1}")
  return l1

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	
	L = [0] * (n1)
	R = [0] * (n2)

	
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	
	i = 0	 
	j = 0	 
	k = l	 

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1


	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1




def mergeSort(arr, l, r):
	if l < r:

		
		m = l+(r-l)//2

	
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)



if __name__ == "__main__":
  l1 = []
  l1 = random_list()

  # avrage case
  st = time.time()
  mergeSort(l1, 0, len(l1)-1)
  et = time.time()
  tt = et - st
  print(l1)


  # best case
  st1 = time.time()
  mergeSort(l1, 0, len(l1)-1)
  et1 = time.time()
  tt1  = et1 - st1
  print(l1)


  # worst case
  l1 = l1[::-1]  #reverse the list
  print(l1)

  st2 = time.time()
  mergeSort(l1, 0, len(l1)-1)
  et2 = time.time()
  tt2  = et2 - st2
  print(l1)
  
  print(f"best cassetime: {tt1}")
  print(f"avrage cassetime: {tt}")
  print(f"wrost cassetime: {tt2}")