import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine()); String line = null; String out = "";
		for(int i = 0; i<n; i++) {
			line = in.readLine();
			int length = line.length();
		     
	 		if(length > 10) {
				line = line.charAt(0) + Integer.toString(length-2) + line.charAt(length -1);
			}
			out += line + '\n';
		}
		out.trim();
		System.out.println(out);	
	}
}
