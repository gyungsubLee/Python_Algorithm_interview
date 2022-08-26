# ✍️ 문자열 -> ASCII(아스키코드) 변환

> ### ✍️ ord(), chr()
> ```ord()```: 문자 -> 유니코드 정수  변환  ex) ord('a') -> 97<br/>
> ```chr()```: 유니코드 정수 -> 문자 변환  ex)chr(97) -> 'a'

<br/>

```python
text = 'hello'
ascii_values = []
for character in text:
    ascii_values.append(ord(character))

print(ascii_values)
>>> [104, 101, 108, 108, 111]
```

<br/>

## 👉 List-for문으로 축약

> ### ✍️ List 내 for문
> ```[실행문 + for i in (rang or list) + 조건문]```
>
>```python
>num = [1, 2, 3, 4, 5]
>
># l=[]
># for i in num:
>#    if i%2 == 0:
>#       l.append(i)
> -> [i for i in num if i%2 == 0]
> >>> [2, 4]
>```



```python
def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values

print(to_ascii('hello'))
>>> [104, 101, 108, 108, 111]
```

<br/> 

----

Reference)<br/> 
https://goez.tistory.com/12<br/>
https://www.delftstack.com/ko/howto/python/convert-string-to-ascii-python/
