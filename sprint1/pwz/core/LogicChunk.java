package pwz.core;

public class LogicChunk {
    public static void doLogic(String token){
        if(token.equals("hello")){
            System.out.println("Hello World.");
            // do logic...
        }
        if(token.equals("snake")){
            new pwz.service.Snake.Scene();
        }
    }
}
