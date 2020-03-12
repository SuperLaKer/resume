#### 定义变量

- `byte,short,int,long,float,double,char,boolean`
- 整数默认是int类型，定义long类型的数据时，要在数据后面加L
- 浮点数默认是double类型，定义float类型的数据时，要在数据后面加F

```
数据类型 变量名 = 初始化值;
```

#### 类型转换

```java
// 类型提升
byte, shotr, char, --->int--->long--->float--->double

// 强制下降
int a = 10
int b = 20
byte cc = byte(a + b)
```

#### 算术运算

- 整数相除只能得到整数，要想得到小数，就必须有浮点数参与运算

```java
System.out.println(1/2)  // 0
System.out.println(1/2.0)  // 0.5
System.out.println(1.0/2)  // 0.5
```

- 字符参与

```
int a = 'A'
int b = 10
System.out.println(a + b)  //107
System.out.println("hello" + b)  // "hello10"
```

- 自增自减

```java
int a = 10
a++
++a
int b = a++;  //b == 12
int b = ++a;  //b == 13
System.out.println(a) // 12
```

#### 赋值

```
=， +=， *=， /=
+= 隐含了强制类型转换
```

#### 关系

```
==， !=，>，<，>=，<= 
System.out.println(10 > 11) //false
System.out.println(a = b) //赋值，输出
```

#### 逻辑

```
&, |, !, ^   与 或 非 异或
//异或：相同false，不同true
&&  ||
短路与  短路或
前面表达式可以判定结果时：后面的不执行
```

#### 三元运算

```
int a = 10;
int b = 30;
int c = 20;

int temp = (a > b)?a:b
int max = (temp > c)?temp:c
```

