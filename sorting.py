#AOA Project
#Date November 18,2024
#: Khadejah Benjamin-2208656 
# Ramon Johnston -2008317
#Daniel Lewis- 2202361 
# Rushane Green – 2006930 
# Chamarie Taylor – 2100037

def merge_sort(arr, key_func=lambda x: x):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key_func)
        merge_sort(right_half, key_func)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if key_func(left_half[i]) < key_func(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
