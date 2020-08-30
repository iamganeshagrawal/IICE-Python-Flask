# Day-02

---

## Conditional statements

```python
i = int(input())
if i < 10:
    print('Less then 10')
elif i < 100:
    print("Less then 100")
else:
    print("Greater then 99")
```

## Escape char

```python
print("hello\nworld")   #hello
                        #world

# without escape with escape chars
print(r'hello\nworld')  #hello\nworld
```
Code (Escape char)  |       Result
---                 |       ---
`\'`	            |       Single Quote	
`\\`	            |       Backslash	
`\n`	            |       New Line	
`\r`	            |       Carriage Return	
`\t`	            |       Tab	
`\b`	            |       Backspace	
`\f`	            |       Form Feed	
`\ooo`	            |       Octal value	
`\xhh`	            |       Hex value

