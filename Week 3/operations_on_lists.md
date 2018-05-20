# OPERATION ON LISTS

### Adding items to list
___
- **add** elements to end of list with L.append(element)
- this **mutates** the list

L = [2,1,3]  
L.append(5) --> **L is now** [2,1,3,5]

### What is the dot?
___
- lists are python objects, everything in python is an object
- objects have data
- objects have method and fuctions
- access this information by `object_name.do_something()`
- will learn more about these later

### Concatenation 

- concatenation of two lists is as simple as adding them together using the + operator
```python
L1 = [1,2,3]  
L2 - [4,5,6]  
L3 = L1 + L2  

L3  = [1,2,3,4,5,6]
```
 *but does not mutate L1 or L2*

```python
L.extend([1])


