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