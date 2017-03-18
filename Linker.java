import java.io.*;
import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.LinkedHashMap;
import java.util.Scanner;

public class Linker {	
	
	private static Map<String, Integer> definitions = new LinkedHashMap<String, Integer>();
	private static Map<String, ArrayList<Integer>> uses = new LinkedHashMap<String, ArrayList<Integer>>();
	private static ArrayList<ArrayList<Object>> texts = new ArrayList<ArrayList<Object>>();



	private static void secondpass(Map<String, ArrayList<Integer>> uses, ArrayList<ArrayList<Object>> texts){


		
		int usesize = uses.size();
		
		int addval = Integer.parseInt(texts.get(0).get(1).toString()) + 3;

		

		int loop1 = uses.size();

		int finalcount = 0;

		// System.out.println(definitions.size());
		// System.out.println(uses.size());

		for (String key : definitions.keySet()){
			if (!uses.containsKey(key)){
				System.out.println("##WARNING  A symbol is defined, but not used.");
			}
		}
		

		System.out.println("Memory Table: ");

		

		for (String key : uses.keySet()){
			
			int secloop = uses.get(key).size();
			
			for (int k =0; k < secloop; k++){
				
				
				ArrayList<Object> newarr =  new ArrayList<Object> ();

				int indick = uses.get(key).get(k);


				newarr.add(texts.get(indick).get(0));


				int dick = Integer.parseInt(texts.get(indick).get(1).toString());
				dick = dick - dick%1000;
			
				if (newarr.get(0).equals("E")){

						if ( !definitions.containsKey(key)){
							System.out.println("##ERROR  Symbol is not defined, so zero was used instead.");
							newarr.add(dick);
						}
						else{
							int newkey = definitions.get(key);
							newarr.add(dick + newkey);
						}
					
				}
				
			

				texts.set(uses.get(key).get(k), newarr);


			}
		
		}

		//System.out.println(texts);
		
		for (ArrayList<Object> text : texts){
			System.out.println(finalcount + ": ");
			System.out.println(text.get(1));
			System.out.println();
			finalcount+=1;
		}

		
		int count = 0;







	}

	public static void main(String[] args) throws IOException {

    	Scanner firstreader = new Scanner(new BufferedReader(new FileReader(args[0])));
    	char checker = firstreader.next().charAt(0);
    	
    	Scanner reader = new Scanner(new BufferedReader(new FileReader(args[0])));

		try {
			boolean typeNumberDefined = false;
			int countType = 0;
			int relativeToAbsoluteCount = 0;
			int modCount = 0;

			int countArg = 0;
			String name = "";

			boolean use = false;
			int err5 = 0;
			int err5check = 0;
			int err5check2 = 0;
			ArrayList<Integer> recent = new ArrayList<Integer>();

			int countargcheck = 0;

		
			while (reader.hasNext()) {
				String readNext = reader.next();

				switch(countType) {
					case 1:
						Scanner secondreader = new Scanner(new BufferedReader(new FileReader(args[0])));

						


						if (typeNumberDefined == false) {
							countArg = Integer.parseInt(readNext) * 2;
							//System.out.println("NUMone countarg: " + countArg);
							countargcheck = countArg;
							typeNumberDefined = true;
						} else {
							if (countArg > 0) {
								if (countArg % 2 == 0) name = readNext;

								else {
									if (definitions.containsKey(name)){
										System.out.println("##ERRORR  There was a symbol which was multiply defined, first value used.");
									}																	
									else{
									err5 = Integer.parseInt(readNext);
									definitions.put(name, texts.size() + err5);
										if (err5check2 == 0){
											err5check += 1;
											//System.out.println("ERRCHECK: " + err5check);
										}
									}
								}
								countArg --;
							}
						}
						if (countArg == 0) { countType ++; typeNumberDefined = false; }



						break;

					case 2:

					
						if (typeNumberDefined == false) {
							countArg = Integer.parseInt(readNext);
							//System.out.println("This countarg: " + countArg);
							typeNumberDefined = true;
						} else {
							if (countArg > 0) {
								if (use == false) { name = readNext; use = true; }
								else if (Integer.parseInt(readNext) == -1) { use = false; countArg--; }
								else {
									if (!uses.containsKey(name)) uses.put(name, new ArrayList<Integer>());
									uses.get(name).add(texts.size() + Integer.parseInt(readNext));
									
									recent.add(Integer.parseInt(readNext));
									

								}
							}
						}

						
						if (countArg == 0) { countType++; typeNumberDefined = false; use = false; }
						break;

					case 3:
						

						
						if (typeNumberDefined == false) {
							int next = Integer.parseInt(readNext);
							modCount = next;

							int modcheck = next;


							countArg = next * 2;
						//	System.out.println("err5: " + err5);
						//	System.out.println("MODCOUNT: " + modCount);
							if (err5 >= modCount && countargcheck > 0){
								System.out.println("##Error: Address appearing in defnition exceeds the size of module. Address was treated as 0.");
								err5check2 = 1;
								int err5check3 = 0;
								//System.out.println("The index of definition to check: " + (err5-1));
								for (Map.Entry<String, Integer> entry: definitions.entrySet()){
									//System.out.println("WOAH" + entry.getKey());
									err5check3 += 1;
									if (err5check3 == (err5)){
										//System.out.println("The value being subtracted is: " + err5);
										definitions.put(entry.getKey(), entry.getValue() - err5);
									}
								}

								


								//System.out.println(definitions.getValue(err5check - 1));
							}


							for (int rr = 0; rr < recent.size(); rr++){
								if (recent.get(rr) > modCount){
									//System.out.println("recent:" + recent.get(rr));
									System.out.println("##ERRORR  There was a use that exceeded the size of module. This use was ignored.");
									for (Entry<String, ArrayList<Integer>> entry: uses.entrySet()) {
										//System.out.println(entry.getKey() + " : " + entry.getValue());
										entry.getValue().remove(recent.get(rr));
									}
									
								}

							}
							recent.clear();



							typeNumberDefined = true;
						} else {
							if (countArg > 0) {
								if (countArg % 2 == 0) {
									ArrayList<Object> text = new ArrayList<Object>();
									text.add(readNext);
									texts.add(text);
								}
								else {
									if (texts.get(texts.size() - 1).get(0).toString().equals("R")) {

										int relat = Character.getNumericValue(checker);
										int originalText = Integer.parseInt(readNext);
										
										//System.out.println("RELAaaaaaaaaaaT: " + relat);

										if (originalText % 1000 > relat){
											System.out.println("##ERRORR  Relative address exceeds module size.");
											originalText = originalText - originalText%1000;
											int relativeAddress = originalText;
											texts.get(texts.size() - 1).add(relativeAddress);
										}

										else{
											int relativeAddress = originalText + relativeToAbsoluteCount;
											texts.get(texts.size() - 1).add(relativeAddress);

										}


									} else texts.get(texts.size() - 1).add(readNext);
								}
								countArg -= 1;
							}
						}
						if (countArg == 0) { countType = 1; typeNumberDefined = false; relativeToAbsoluteCount += modCount; modCount = 0;}//
						break;
					default:
						countType ++;
				}
			}
		} finally { if (reader != null) reader.close(); }


		//System.out.println(err5check2);
		System.out.println("Symbol Table");
		for (Map.Entry<String, Integer> entry: definitions.entrySet()) {
			System.out.println(entry.getKey() + " : " + entry.getValue());
		}

		
		System.out.println();

	//	System.out.println("USELIST");

		ArrayList<Integer> totaluse = new ArrayList<Integer>();


		//System.out.println("ERR5check2: " +err5check2);

		for (Entry<String, ArrayList<Integer>> entry: uses.entrySet()) {
			//System.out.println(entry.getKey() + " : " + entry.getValue());
			//System.out.println("LIST: " + entry.getValue().size());


			for (int ii = 0; ii < entry.getValue().size();){
			

				if(totaluse.contains(entry.getValue().get(ii))){
					entry.getValue().remove(entry.getValue().get(ii));
					System.out.println("##ERROR  Multiple variable used in instruction; all but first ignored.");
					//System.out.println("!!!!!");
				}
				else{
					totaluse.add(entry.getValue().get(ii));
				}

				//totaluse.add(entry.getValue().get(ii));

				ii+=1;
			}
			System.out.println();

			

		}

		// System.out.println(uses);		

		System.out.println();

		

		for (ArrayList<Object> text : texts) {
			
			
			if (text.get(0).equals("A")){
				
				int absol = Integer.parseInt(text.get(1).toString());
				if (absol%1000 > 200){
					System.out.println("##ERROR  Absolute address exceeds machine size, zero used.");
					absol = absol - absol%1000;

					text.set(1, absol);
				}
			}
			
			
		}

		secondpass(uses, texts);
		
	}
}