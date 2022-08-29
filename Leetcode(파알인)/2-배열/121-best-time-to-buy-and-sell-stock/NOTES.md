​# ✍️ 풀이1(min, max)

```min()``` 를 통해 가장 작은 price를 구하고 
```max()``` 를 통해 가장 큰 이익을 구한다. 

```python
profit = 0
min_price = prices[0]
for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)
```

```min_price = 0``` 으로 생각없이 작성하여 오답이 나왔다. 
최솟값을 구하는데 이미 가장 작은 값을 할당하여 min_price 로직이 제대로 작동되지 않았다.
주어진 list의 첫번째 값(value)으로 지정하여 업데이트 되도록 수정하였더니 정상 작동 되었다. 
