#### 键盘录入三步骤

- 导包：`import java.util.Scanner`
- 创建对象：`Scanner sc = new Scanner(System.in);`
- 接收数据：`int i = sc.nextInt();`

```
package com.company;
import java.util.Scanner  //导包

public class HelloWorld {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);  //创建对象
		
		System.out.println("请输入数据：")
		int i = sc.nextInt();  //接收值
		
		System.out.println(i)
    }
}
```

