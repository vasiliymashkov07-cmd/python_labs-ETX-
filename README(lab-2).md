# python_labs-ETX-

# Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
     return ValueError('Список пуст')
    return tuple([min(nums), max(nums)])

print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(set(nums))

print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0, 1, 2.5,2.5,0]))


def flatten(mat: list[list | tuple]) -> list:
    I = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                I.append(j)
        else:
            return TypeError('Строка не строка строк матрицы')
    return I

print(flatten([[1,2],[3,4]]))
print(flatten([[1,2],(3,4,5)]))
print(flatten([[1],[],[2,3]]))
print(flatten([[1,2],"ab"]))
```
![](/images/lab%2002/arrays.png)