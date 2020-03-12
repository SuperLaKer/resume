#### random包

- 左闭右开

```
// 导包：import java.util.Random;
// 创建对象：Random r = new Random();
// 获取随机数：int num = r.nextInt(10);  // 左闭右开
```

```
package com.company;
import java.util.Random;

public class RandNum {
    public static void main(String[] args) {
        Random r = new Random();

        for (int i = 0; i < 10; i++) {
            int num = r.nextInt(10);
            System.out.println(num);
        }
    }
}
```

