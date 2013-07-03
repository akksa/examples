#Akksa



def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        else:
            if left:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]        
    return result


def merge_sort(unsorted_list):
    if len(unsorted_list)<=1:
        return unsorted_list
    right = []
    left = []
    middle = len(unsorted_list)/2
    left = unsorted_list[:middle]
    right = unsorted_list[middle:]
    #print left, right
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

if __name__ == '__main__':
    print 'hello, world'
    #print merge([2],[1])
    my_list = [5, 1, 3, 4, 2, 8, 7, 6]
    print merge_sort(my_list)