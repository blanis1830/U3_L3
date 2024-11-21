#Blayne Hoy
#U3 Lab 3

def merge_sort(array):
  if len(array) <= 1:
    return array
  
  mid = len(array) // 2
  left_array = merge_sort(array[:mid])
  right_array = merge_sort(array[mid:])
  
  merged = []
  numL = 0
  numR = 0

  while numL < len(left_array) and numR < len(right_array):
    if left_array[numL] <= right_array[numR]:
      merged.append(left_array[numL])
      numL += 1
    else:
      merged.append(right_array[numR])
      numR += 1
  
  merged.extend(left_array[numL:])
  merged.extend(right_array[numR:])

  return merged
    




def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()