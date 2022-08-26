# ✍️ divmod()

첫번째 인자를 두번째 인자로 나눈 ```나머지``` 와 ```몫```을 tuple 형태로 반환함.
 ### -> divmod(a, b) = (a//b, a%b) 

```python
tuple_val = divmod(100, 3)

print(tuple_val)
>>> (33, 1)

print(tuple_val[0])
>>> 33
print(tuple_val[1])
>>> 1
```

### 주의) 0으로 나눌 시 ERROR


<br/>

----
Reference)<br/>
https://ddolcat.tistory.com/685<br/>
https://codingdog.tistory.com/entry/몫과-나머지를-구할-수-있는-파이썬-divmod-함수를-알아봅시다