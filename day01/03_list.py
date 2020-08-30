nameList = ['Aman', 'Anil', 'Anita', 'Sumit', 'Rakesh']

print(nameList)

# list_variable[index]
print(nameList[2])
# actual code and sorthand is var[index] === var.__getitem__(index)
print(nameList.__getitem__(2))

#length of list
print(len(nameList))

### Slice

print(nameList[1:4])

slicedList = nameList[0:4]
print(slicedList)

## 2D data in 1D list
fData_1D = [1, 'a', '9828098780', 2, 'b', '1234567890', 3, 'c', '1234567891']
print(fData_1D[3:6])

## 2D data in 2D list
fData_2D = [[1, 'a', '9828098780'], [2, 'b', '1234567890'], [3, 'c', '1234567891']]
print(fData_2D[1])
