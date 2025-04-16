​

# ✍️ 풀이1-3(함수 합침)
method 내부 함수에 self를 작성하여 에러남.<br/>
-> 
### method 내부에 함수를 작성하는 경우 self 인자 필요없음 

<br/>

## 🤔 why?
> ```self``` 는 인스턴스 그 자체를 말하며 객체 자기 자신을 참조하는 매개변수이다.

클래스 내부에 정의된 method는 첫번째 인자가 반드시 ```self```여야 한다.

```self```를 작성하지 않는 경우 method 호출 시 아래와 같이 error가 발생한다. 
```python
class Hello:
    def func1(self):
        print("Hello")
    def func2():
          print("World")

# 정상 실행
hello = Hello()
hello.func1()
>> Hello

# Error 
hello.func2()
>>Traceback (most recent call last):
  File "main.py", line 10, in <module>
    hello.func2()
TypeError: func2() takes 0 positional arguments but 1 was given
```

참조: https://hyun0k.tistory.com/entry/TIL-17-self%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC 

