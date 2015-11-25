import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class StringChanger {
	//TODO change this to the directory we are actually using to store data
	private static final String startingDirectory = "C:\\Users\\Stephanie\\Desktop\\TESTING";
	
	public static void main(String[] args){
		File rootDir = new File(startingDirectory);
		File[] directories = rootDir.listFiles(File::isDirectory);
		PrintWriter input;
		PrintWriter results;
		try {
			input = new PrintWriter(startingDirectory+"\\input.txt");
		} catch (FileNotFoundException e) {
			System.err.println("Could not create new input file. "+e.getMessage());
			return;
		}
		
		try {
			results = new PrintWriter(startingDirectory+"\\results.txt");
		} catch (FileNotFoundException e) {
			System.err.println("Could not create new results file");
			input.close();
			return;
		}
		
		for(File dir : directories){
			//get a list of files
			File[] files = dir.listFiles(File::isFile);
			for(File f : files){
				//each file is a single input
				try {
					Scanner scanner = new Scanner(f);
					String tmp = toSeperated(scanner.nextLine());
					if(tmp.isEmpty()){
						continue;
					}
					scanner.close();
					
					//write to the output files
					input.println(tmp);
					results.println(dir.getName());
					
				} catch (FileNotFoundException e) {
					System.err.println("Could not use the file"+f.getName()+". "+e.getMessage());
				}
			}
		}
		
		input.close();
		results.close();
		
	}
	
	/**
	 * expects a string like num,num,num;num,num,num;
	 * @param org
	 * @return
	 */
	static String toSeperated(String org){
		String[] split = org.split(";");
		String ret="";
		for(String s : split){
			if(s != ""){
				ret += " " + concatinate(s);
			}
		}
		return ret;
	}
	
	/**
	 * expects a string like: num, num, num
	 * @param org
	 * @return
	 */
	static String concatinate(String org){
		String[] split = org.split(",");
		String ret = "";
		for(String s : split){
			if(s.contains(".")){
				s.replace(".", "");
			}
			ret += s;
		}
		
		return ret;
	}
}
