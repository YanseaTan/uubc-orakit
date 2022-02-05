package pwz.core;

import java.util.Scanner;

public class OriKit {
    //private static NLPChunk nlpc;

    public static void main(String[] args) {

        class Task implements Runnable{
            String token;

            public Task(String token) {
                this.token = token;
            }

            @Override
            public void run() {
                LogicChunk.doLogic(token);
            }
        }

        Scanner in = new Scanner(System.in);
        String input, token;
        NLPChunk.seyHello();
        while(true) {
            input = in.nextLine();
            token = NLPChunk.tokenAnalyze(input);

            Task task = new Task(token);
            Thread t = new Thread(task);
            t.start();
            //System.out.println("Task is running...");
        }
    }
}
