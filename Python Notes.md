# Python Notes

## String Operations

```python
print('Single Quotes', ' AND ' , "Double Quotes", " are allowed ... with phostrophe like ->i don't do that..")
```
> Single Quotes  AND  Double Quotes  are allowed ... with phostrophe like ->i don't do that..

```python
myString = 'abcdefghijklmnopqrstuvwxyz'
print("my String for further processing is: ", myString)
```
>my String for further processing is:  abcdefghijklmnopqrstuvwxyz

### String starts with 0
### String functions
```python
print("length of the above string :",len(myString))
```
>length of the above string : 26

### Indexing and slicing
```python
print("First character of myString:\t",myString[0])
```
>First character of myString:	 a

```python
print("Last character of myString:\t",myString[-1])
```
>Last character of myString:	 z

```python
print("Last character of myString:\t",myString[6])
```
>Last character of myString:	 g

```python
print("Sequence of myString[2 to remaining]:\t",myString[2:])
```
>Sequence of myString[2 to remaining]:	 cdefghijklmnopqrstuvwxyz

### Upto but not including
```python
print("Sequence of myString[2 to 6]:\t",myString[2:6])
```
>Sequence of myString[2 to 6]:	 cdef

```python
print("Sequence of myString[Upto 5]:\t",myString[:5])
```
>Sequence of myString[Upto 5]:	 abcde

```python
print("Sequence of myString[All the way of beginning to end ]:\t",myString[::])
```
>Sequence of myString[All the way of beginning to end ]:	 abcdefghijklmnopqrstuvwxyz

```python
print("Sequence of myString[All the way from beginning to upto end by jump of 3]:\t",myString[::3])
```
>Sequence of myString[All the way from beginning to upto end by jump of 3]:	 adgjmpsvy

```python
print("Sequence of myString[FROM-2, UPTO-23, BY JUMP OF 3]:\t",myString[2:23:3])
```
>Sequence of myString[FROM-2, UPTO-23, BY JUMP OF 3]:	 cfiloru

```python
print("Reverse String:\t",myString[::-1])
```
>Reverse String:	 zyxwvutsrqponmlkjihgfedcba
