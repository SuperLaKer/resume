#### 理解java中方法区的常量池

- python中的字符串为不可变类型
- java中String类对象，不可变类型
- java中StringBuilder对象，可变类型

```
普通String类对象使用：+= 浪费空间
使用StringBuilder类差个年间的对象，直接拼接
```

###### StringBuilder的几个方法

```java
package com.itheima_01;
/*
 * 成员方法：
 * 		public int capacity():返回当前容量
 * 		public int length():返回长度（字符数）
 * 		容量：理论值
 * 		长度：实际值
 */
public class StringBuilderDemo {
	public static void main(String[] args) {
		//创建对象
		StringBuilder sb = new StringBuilder();
		System.out.println("sb:"+sb);
		System.out.println("sb.capacity():"+sb.capacity());
		System.out.println("sb.length():"+sb.length());
	}
}

package com.itheima_02;
/*
 * 添加功能
 *		public StringBuilder append(任意类型):添加数据，并返回自身对象
 * 反转功能
 *		public StringBuilder reverse()
 */
public class StringBuilderDemo {
	public static void main(String[] args) {
		//创建对象
		StringBuilder sb = new StringBuilder();
		
		//public StringBuilder append(任意类型)
		//StringBuilder sb2 = sb.append("hello");
		
		/*
		System.out.println("sb:"+sb);
		System.out.println("sb2:"+sb2);
		System.out.println(sb == sb2); //true
		*/
		
		/*
		sb.append("hello");
		sb.append("world");
		sb.append(true);
		sb.append(100);
		*/
		
		//链式编程
		sb.append("hello").append("world").append(true).append(100);
		
		System.out.println("sb:"+sb);
		
		//public StringBuilder reverse()
		sb.reverse();
		System.out.println("sb:"+sb);
		
	}
}
```

###### 相互转化

```java
/*
 * StringBuilder和String的相互转换
 * 
 * StringBuilder -- String
 * 		public String toString():通过toString()就可以实现把StringBuilder转成String
 * 
 * String -- StringBuilder
 * 		StringBuilder(String str):通过构造方法就可以实现把String转成StringBuilder
 */

public class StringBuilderTest {
	public static void main(String[] args) {
		//StringBuilder -- String
		/*
		StringBuilder sb = new StringBuilder();
		sb.append("hello").append("world");
		
		String s = sb.toString();
		System.out.println(s);
		*/
		
		//String -- StringBuilder
		String s = "helloworld";
		StringBuilder sb = new StringBuilder(s);
		System.out.println(sb);
	}
}
```

