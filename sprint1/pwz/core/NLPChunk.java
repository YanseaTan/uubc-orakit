package pwz.core;

import pwz.core.ServiceToken;

import java.util.ArrayList;

public class NLPChunk {
    public static void sayHello(){
        System.out.println("Hi~ what can I do for you?");
    }

    public static void say404(){
        System.out.println("Sorry, I don't understand.");
    }

    public static ArrayList<String> tokenAnalyze(String sentence){
        ArrayList<String> tokens = new ArrayList<>();
        for (String token: ServiceToken.tokenInfo.keySet()){
            if (sentence.contains(token)){
                tokens.add(token);
            }
        }
        if (tokens.size() == 0) say404();
        return tokens;
    }
}