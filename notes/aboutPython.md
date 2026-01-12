_Python 기본 문법 정리_

## 입력
### 띄어쓰기 기준 나누기
```py 
a, b = map(int, input().split())
```

split() 함수 사용

### list로 받기
``` py
inputs = list(map(int, input().split()))
```

list() 함수 사용

## 수학
### 절대값
``` py
abs()
```

### 버림
```py
import math

math.floor()
```

### 올림
```py
import math

math.ceil()
```

### 진법 변환
```py
bin()   # 10진수 -> 2진수
oct()   # 10진수 -> 8진수
hex()   # 10진수 -> 16진수
```
``` py
format(42, 'b') # 10진수 -> 2진수
format(42, 'o')   # 10진수 -> 8진수
format(42, 'x')   # 10진수 -> 16진수
```

접두어 제외하여 출력

```py
int(k, n)   # n진수 -> 10진수
```