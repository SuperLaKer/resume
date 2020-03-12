#### 方法分类一判断功能

```java
package com.itheima_03;
/*
 * Object:是类层次结构中的根类，所有的类都直接或者间接的继承自该类。
 * 如果一个方法的形式参数是Object，那么这里我们就可以传递它的任意的子类对象。 
 */
 
public class StringDemo {
	public static void main(String[] args) {
		//创建字符串对象
		String s1 = "hello";
		String s2 = "hello";
		String s3 = "Hello";
		
		//boolean equals(Object obj):比较字符串的内容是否相同
		System.out.println(s1.equals(s2));
		System.out.println(s1.equals(s3));
		System.out.println("-----------");
		
		//boolean equalsIgnoreCase(String str):比较字符串的内容是否相同,忽略大小写
		System.out.println(s1.equalsIgnoreCase(s2));
		System.out.println(s1.equalsIgnoreCase(s3));
		System.out.println("-----------");
		
		//boolean startsWith(String str):判断字符串对象是否以指定的str开头
         //boolean endsWith(String str):判断字符串对象是否以指定的str结尾
		System.out.println(s1.startsWith("he"));
		System.out.println(s1.startsWith("ll"));
	}
}
```

#### 方法分类二获取功能

```java
package com.itheima_04;

public class StringDemo {
	public static void main(String[] args) {
		//创建字符串对象
		String s = "helloworld";
		
		//int length():获取字符串的长度，其实也就是字符个数
        arry.length
		System.out.println(s.length());
		System.out.println("--------");
		
		//char charAt(int index):获取指定索引处的字符
		System.out.println(s.charAt(0));
		System.out.println(s.charAt(1));
		System.out.println("--------");
		
		//int indexOf(String str):获取str在字符串对象中第一次出现的索引
		System.out.println(s.indexOf("l"));
		System.out.println(s.indexOf("owo"));
		System.out.println(s.indexOf("ak"));
		System.out.println("--------");
		
		//String substring(int start):从start开始截取字符串
		System.out.println(s.substring(0));
		System.out.println(s.substring(5));
		System.out.println("--------");
		
		//String substring(int start,int end):从start开始，到end结束截取字符串
		System.out.println(s.substring(0, s.length()));
		System.out.println(s.substring(3,8));  //[)  左闭右开
	}
}
```

#### 方法分类三转换功能

```java
package com.itheima_05;
/*
 * String类的转换功能：
 * char[] toCharArray():把字符串转换为字符数组
 * String toLowerCase():把字符串转换为小写字符串
 * String toUpperCase():把字符串转换为大写字符串
 * 
 * 字符串的遍历：
 * 		A:length()加上charAt()
 * 		B:把字符串转换为字符数组，然后遍历数组
 */
public class StringDemo {
	public static void main(String[] args) {
		//创建字符串对象
		String s = "abcde";
		
		//char[] toCharArray():把字符串转换为字符数组
		char[] chs = s.toCharArray();
		for(int x=0; x<chs.length; x++) {
			System.out.println(chs[x]);
		}
		System.out.println("-----------");
		
		//String toLowerCase():把字符串转换为小写字符串
		System.out.println("HelloWorld".toLowerCase());
		//String toUpperCase():把字符串转换为大写字符串
		System.out.println("HelloWorld".toUpperCase());
	}
}
```

#### 方法分类四

```java
package com.itheima_06;

public class StringDemo {
	public static void main(String[] args) {
        //String trim()
		String s1 = "  hello  world  ";
		System.out.println("---"+s1+"---");
		System.out.println("---"+s1.trim()+"---");  // 去除字符串两端空格
                                           
		//String[] split(String str)
		String s4 = "aa,bb,cc";
		String[] strArray = s4.split(",");  // 按照指定的字符分割，返回数组
		for(int x=0; x<strArray.length; x++) {
			System.out.println(strArray[x]);
		}
	}
}
```

#### 字符串遍历

```
for(int i = 0; i < str.length(); i++) {
	System.out.println(str.charAt(i));
}
```

```
for i in str:
	print(i)
```

