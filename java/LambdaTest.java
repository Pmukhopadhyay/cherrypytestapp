import java.util.List;
import java.util.ArrayList;

class Employee{
	int id;
	String fname;
	String lname;
	String email;
	float salary;
	int age;
	
	Employee(int id,String fname, String lname, String email,float salary,int age){
		this.id=id;
		this.fname=fname;
		this.lname=lname;
		this.email=email;
		this.salary=salary;
		this.age=age;
	}

	int getId(){
		return this.id;
	}

	float getSalary(){
		return this.salary; 
	}

	int getAge(){
		return this.age;
	}

	String getEmail(){
		return this.email;
	}
	
	public String toString(){
		return "id="+id+"|fname="+fname+"|lname="+lname+"|email="+email+"|salary="+salary+"|age="+age;
	}
}


public class LambdaTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Employee> employees = new ArrayList<Employee>();
		employees.add(new Employee(1,"aa","aa","aa@aa.com",10000,33));
		employees.add(new Employee(2,"bb","bb","bb@bb.com",20000,22));
		employees.add(new Employee(3,"cc","cc","cc@cc.com",21000,44));
		employees.add(new Employee(4,"dd","dd","dd@dd.com",11000,25));
		employees.add(new Employee(5,"ee","ee","ee@ee.com",20200,27));
		employees.add(new Employee(6,"ff","ff","ff@ff.com",11100,34));
		employees.add(new Employee(7,"gg","gg","gg@gg.com",20022,29));

		employees.stream().filter(
								e -> e.getAge()>20 && e.getAge()<35
								)
						  //.map( e -> e.getId())
						  .forEach( e -> System.out.println(e));
	}

}
