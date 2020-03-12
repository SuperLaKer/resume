#### IO流

- IO流用来处理设备之间的数据传输
- Java对数据的操作是通过流的方式
- Java用于操作流的类都在IO包中
- 流按流向分为两种：输入流（读取文件），输出流（写入文件）

### FileWriter向文件中写数据

- `flush()`：刷新缓冲区。流对象还可以继续使用。
- `close()`：先刷新缓冲区，然后通知系统释放资源。流对象不可以再被使用了。

```java
import java.io.FileWriter;
import java.io.IOException;

/*
 * 输出流写数据的步骤：
 * 		A:创建输出流对象
 * 		B:调用输出流对象的写数据的方法
 * 		C:释放资源
 */
public class FileWriterDemo {
	public static void main(String[] args) throws IOException {
		//创建输出流对象
		FileWriter fw = new FileWriter("d:\\a.txt");
		//A:创建文件 B:创建句柄（流对象）C:句柄指向文件

		fw.write("IO流你好");
		fw.flush();  //数据没有直接写到文件，其实是写到了内存缓冲区
		fw.close();
	}
}
```

###### Fw对象的其他方法

```java
/*
 * void write(String str):写一个字符串数据
 * void write(String str,int index,int len):写一个字符串中的一部分数据
 * void write(int ch):写一个字符数据,这里写int类型的好处是既可以写char类型的数据，也可以写char对应的int类型的值。'a',97
 * void write(char[] chs):写一个字符数组数据
 * void write(char[] chs,int index,int len):写一个字符数组的一部分数据
 */
```

###### 追加和换行

```
// FileWriter(String fileName, boolean append)
// windows:\r\n
// linux:\n
// mac:\r

FileWriter fw = new FileWriter("c.txt",true);
fw.write("\r\n");
```

#### FileReader类

- 读取数据的返回值是-1的时候，就说明没有数据了

```
FileReader fr = new FileReader("fr.txt");
int ch = fr.read();  // 一次读取一个字符
```

