# Python Flask Day 01
---
## REPL
REPL mean read-eval-print-loop 
"`>>>`" this is symbol for REPL

```python
>>> x = 5
>>> x
5
```

## List

```python
nameList = ['Aman', 'Anil', 'Anita']

print(nameList)

# access a value from list
# sorthand is var[index] and longhand is var.__getitem__(index)
print(nameList.__getitem__(2))

# list_variable[index]
print(nameList[2])
```
### Slice
```python
# Slice
nameList = ['Aman', 'Anil', 'Anita', 'Sumit', 'Rakesh']
print(nameList[1:4]) # return and print list from index 0 to 3
# ['Anil', 'Anita', 'Sumit']

```

list[start_index:last_index] 
Here last_index is exclude so we can say 
list[start:end+1] 

```python
x = []
x[start:]       # start to length-1
x[:end]         # 0 to end
x[start:end]    # start to end-1

## start and end can be positive or negative
```

### Nested list

nested list are used for save 2d data structure and colum-row data like :
SNo|Name|Mobile
---|---|---
1|a|9828098780
2|b|1234567890
3|c|1234567891


```python
fData_2D = [[1, 'a', '9828098780'], [2, 'b', '1234567890'], [3, 'c', '1234567891']]
print(fData_2D[1])  # [2, 'b', '1234567890']
```

> Note: List does not support colum wise operation because it perfrom operation in row or liner way. so for perform operation we have to use loop / zip / list comprehension / numpy array.

### numpy array
```python
>>> import numpy
>>> xList = [[1, 'a', '9828098780'], [2, 'b', '1234567890'], [3, 'c', '1234567891']]
>>> type(xList)
<class 'list'>
>>> xArray = numpy.array(xList)
>>> type(xArray)
<class 'numpy.ndarray'>
>>> xArray[:, 1]
array(['a', 'b', 'c'], dtype='<U21')

## col id and mobile
>>> xArray[:, 0:3:2]
array([['1', '9828098780'],
       ['2', '1234567890'],
       ['3', '1234567891']], dtype='<U21')
```