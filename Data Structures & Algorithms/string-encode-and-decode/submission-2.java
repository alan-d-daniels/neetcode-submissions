class Solution {

    public String encode(List<String> strs) {
        StringBuilder s= new StringBuilder();

        for(String word: strs){
            s.append(word.length()).append("#").append(word);
        }
        return s.toString();


    }

    public List<String> decode(String str) {

        List<String> ls= new ArrayList<>();

        char[] words=str.toCharArray();
        System.out.println(str);
        for(int i=0;i<words.length;){
            String num="";
            while(words[i]!='#'){
                num+=words[i];
                i+=1;
            }
           int nol=Integer.parseInt(String.valueOf(num));
            String word="";
           int j;
           for(j=i+1;j<nol+i+1;j++){
            word+=words[j];
            
           }
          
           System.out.print(j);
           ls.add(word);
           i=j;            
        }
        return ls;

    }
}
