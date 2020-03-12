- 构造方法（有参、无参）
- `get和set`控制成员变量

#### static

- 类属性

```java
public class Student {
	private String name;
	private string gender;
	private int age;
	
	//无参构造
	public Student() {}
	//有参构造
	public Student(String name, String gender, int age) {  
		this.name = name;
		this.gender = gender;
		this.age = age;
	}
	// get 和 set
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name
	}
	
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	
	public String getAge() {
		return age;
	}
	public void setAge(String name) {
		this.age = age;
	}
	public void show() {
		System.out.println(name + "," + gender + "," + age);
	}
}
```

