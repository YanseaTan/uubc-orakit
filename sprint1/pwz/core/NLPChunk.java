package pwz.core;

public class NLPChunk {
    public static void seyHello(){
        System.out.println("Hi~ what can I do for you?");
    }

    public static String tokenAnalyze(String sentence){
        if(sentence.contains("snake"))return "snake";
        else return "hello";
    }
}