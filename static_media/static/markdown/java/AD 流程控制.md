#### if

- 第一种使用方式

```java
if (表达式) {
    语句
}

if (a == b) {
	System.out.println("a等于b");
}
```

- 带有else

```
if (表达式) {
    语句
}else{
	语句
}
```

- else if

```
if (表达式) {
    语句
}else if (表达式){
	语句
}else {
	语句
}
```

###### if嵌套

```
if () {
	if () {
	
	}
}
```



#### switch语句

- 表达式的取值：`byte,short,int,char`
- 可以是枚举，也可以是String
- case后面跟的是要和表达式进行比较的值
- break  和 default

```
switch(表达式) {
	case 值1:
		语句体1;
		break;
	case 值2:
	case 值3:
	case 值4:
		语句体2;
		break;
	default:
		语句；
		break;

```

#### for

```java
for(初始化语句;判断条件语句;控制条件语句) {
	循环体语句;
}
int title = 0;
for (int i = 1; i <= 100; i++) {
    title += i;
}
System.out.println(title);
```

#### while

```
while(判断条件语句) {
	循环体语句;
	条件控制语句；
}

```

#### do   while

```
do {
	循环体语句；
} while (条件语句)

int i = 1；
do {
	System.out.println(i);
	i++;
} while(x <= 10);

```

#### 三种循环的区别

- do…while循环至少会执行一次循环体
- for循环和while循环只有在条件成立的时候才会去执行循环体
- for中的 `i `变量，在外界不能使用，但while可以
- for循环结束，该变量就从内存中消失，能够提高内存的使用效率