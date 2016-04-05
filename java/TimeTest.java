import java.util.Calendar;
import java.text.SimpleDateFormat;
public class TimeTest{
	public static void main(String args[]){
		Calendar cal = Calendar.getInstance();
		SimpleDateFormat df = new SimpleDateFormat("dd_MM_YYYY_hh_mm_ss");
		System.out.println("Current Time >>" + df.format(cal.getTime()));
		System.out.println(System.currentTimeMillis());
	}

	public static String getCustomTimeStamp(){
		Calendar cal = Calendar.getInstance();
		SimpleDateFormat df = new SimpleDateFormat("dd_MM_YYYY_hh_mm_ss");
		return df.format(cal.getTime());	
	}
}