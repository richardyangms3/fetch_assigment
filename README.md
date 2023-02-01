# fetch_assigment
## How to run?
```
python3 mycode.py {point to spend}
```
## Implementation (detailed explanation and concerns are in mycode.py's comments)
1. calculate the total points for each payer
2. sort transactions based on timestamps
3. iterate sorted transaction and determine how much points should cost per iteration
4. return the answer and output it on std

## Others
Since the problem does not mention how to deal with the situation of "bounce back" after dealing with negative points (transaction2.csv as an example, Dannon balance change: 110->0->200->190 in the current implementation. However, if consider the balance after receiving negative 200 as an earlier transaction and should be spent before further transactions, it would be wrong)
