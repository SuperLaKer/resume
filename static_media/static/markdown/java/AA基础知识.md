#### java发展史

-  詹姆斯·高斯林1990年，与xxx等人合作“绿色计划”，后来发展一套语言叫做“Oak”，后改名为Java。
- SUN(Stanford University Network，斯坦福大学网络公司) 

```
JVM（Java Virtual Machine）实现跨平台的依赖
JRE（Java Runtime Environment）= JVM + 类库
JDK（Java Devement kit）JRE+JAVA的开发工具
```

#### windows环境

```
创建新的变量名称：JAVA_HOME  值  ：D:\Program Files\Java
path += D:\Program Files\Java\jdk1.7.0_80\bin

```

#### HelloWorld

```java
public class HelloWorld{
	public static void main (String[] args) {  //main程序执行的入口
		System.out.println("hello world");
	}
}

// 编译,生成字节码文件HelloWorld.class
javac HelloWorld.java
// 解释运行HelloWorld.class
java HelloWorld
```

#### 注释

```java
// 单行注释
/* 多行注释 */
/** 文档注释 **/
```

