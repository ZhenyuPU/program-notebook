# Python Learning

## 字符串
kkki福建按
制表符：\t;
换行符：\n;
字符串连接："+"
删除字符串末尾空白：rstrip();字符串.rstrip()
删除字符串开头空白：lstrip();
删除字符串两端空白：strip()
输出小数，小数点后的位数是不确定的，可能最后几位不一样，可以忽略，这是每个语言都有的问题
str()字符化；

## 列表
列表索引从0开始
访问列表最后一位：`a[-1]`；访问倒数第二位：`a[-2]`......
当列表为空时，即`a=[]`，访问`a[position]`错误
### 在列表中添加元素：
1.末尾——ListName.append('element')
动态创建列表：
```python
namelist=[]
namelist.append('name1')
namelist.append('name2')
print(namelist)
//输出
['name1', 'name2']
```

2.插入元素
`ListName.insert(position,'element')`

3.删除元素
·使用del
```python
	namelist=['name1','name2']
	del namelist[position]
```
·使用pop()
	删除最后一个，但保留元素值
```python
namelist=['name1','name2']
poped_namelist=namelist.pop()
print(namelist)
print(poped_namelist)
#输出
['name1']
name2
```
使用pop()删除任意元素
`pop(position)`

·根据值删除
不知道元素在哪，只知道值，使用`remove()`
```python
namelist=['name1','name2']
namelist.remove('name1')
print(namelist)
#输出
['name2']
```
remove只能删除第一次出现的值，如果值出现很多次，需通过循环来判断是否删除完全。
### 组织列表
#### 使用sort()排序
从小到大，字母也是(转换为同一大小写),永久性改变
```python
namelist=['name1','name2','name3']
namelist.sort()
```
从大到小，`namelist.sort(reverse=True)`(True必须大写T)
#### 使用sortED()临时排序
可以保留原来顺序
```python
namelist=['name1','name2','name3']
print(sorted(namelist))
```
改变顺序：`sorted(namelist,reverse=True)`
#### 倒着打印列表
反转：`reverse()`——反转列表顺序，并不排大小
永久性改变，但可通过再次reverse来回到原来的顺序
#### 确定列表长度
使用`len(namelist)`

### 操作列表
#### for循环
——遍历操作
`for name in namelist: `
表示从namelist列表里一个一个取存进name里面，冒号必不可少。
for后面的语句要缩进
#### 创建数值列表
1.使用`range()`
使用`range()`生成一系列数字，`range(1,6)`打印出1-5；还可以指定步长。`range(2,11,2)`从2到11，步长为2。打印：[2,4,6,8,10]
使用`list()`把`range()`结果转化为列表。
e.g.
```python
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)
```
输出：
```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
2.对数字列表进行统计计算
`min`，`max`，`sum`
3.列表解析
将for循环与创建新元素代码合并为一行
```python
squares=[value**2 for value in range(1,11)]
print(squares)
```
#### 使用列表的一部分
1.切片
```python
players=['c', 'm'. 'i', 'f', 'e']
print(players[1:4])
#输出
['m'. 'i', 'f']
```
负数：
```python
players=['c', 'm'. 'i', 'f', 'e']
print(players[-3:1])
#输出
[ 'i', 'f', 'e']
```
2.遍历切片
利用for循环和切片方法
3.复制列表
`listname[:]`取listname列表的全部元素，即复制一遍但是只是一次复制，在随后操作更改listname不改变复制过后的列表，但是若用`=`，那么这不是简单的复制，而是让新的列表指向原来的namelist，随后改变namelist，新列表也会更改；更改新列表，原来列表亦会更改(互相指向)
#### 元组
1.定义：使用`()`来标识，定义元组后，就可以使用索引来访问其元素。即不可改变的列表。
```python
dimensions=(200, 50)
print(dimensions[0])
#输出
200
```
2.遍历元组中所有值：跟列表一样
3.修改元组变量
虽然无法修改，但可以给存储元组的变量赋值，即重新给原元组赋值。
```python
dimensions=(200, 50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print("\nmodified dimensions:")
for dimension in dimensions:
    print(dimension)

 #输出
 original dimensions:
200
50

modified dimensions:
400
100
```

#### 设置代码格式
1.提出修改建议：编写Python改进提案(PEP)
2.缩进：建议缩进四个空格，制表符和空格最好不要混合使用
3.行长：每行最好不要超过80字符
4.空行：不影响代码运行，只影响可读性
5.其他
## if语句
### 条件测试


