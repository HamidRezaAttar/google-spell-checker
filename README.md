<h1 align="center">Google Spell Checker 🖊️</h1>
 
## A simple script for retrieving Google's <font color = "cyan">Did You Mean? </font> result

<br>

# How to use


## Pre Requirements (Python 3.8.16)

```bash
regex == 2022.6.2
urllib3 == 1.24.3
html5lib == 1.0.1
```

## How to retrieve result

```python
s = Spell()
text = "gianis antetukompo"
res = s.correct(text)
print(s.decode(res))
>>> 'giannis antetokounmpo'
```
