# fetch_assigment
## How to run?
```
python3 mycode.py {point to spend}
```
## Implementation (detailed implementation and concerns are in mycode.py's comments)
1. calculate total points for each payer
2. sort transaction base on timestamp
3. iterate sorted transaction and determine how much point should cost per iteration
4. return answer and output it on std

## Others
Since the problem do not mention how to deal with the situation of "bounce back" after dealing with a negative points (transaction2.csv as an example, Dannon balance change: 110->0->200->190 in current implementation. However, if consider balance after recieve negative 200 as old transaction and should be spent before further transaction, it would be wrong)
