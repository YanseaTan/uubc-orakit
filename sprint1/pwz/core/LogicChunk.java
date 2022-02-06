package pwz.core;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;

public class LogicChunk {
    static class Task implements Runnable{
        String token;

        public Task(String token) {
            this.token = token;
        }

        @Override
        public void run() {
            ArrayList<String> tokenInfo = ServiceToken.tokenInfo.get(token);
            // output task start greetings
            System.out.println(tokenInfo.get(1));
            // try to run the task
            try {
                String className = tokenInfo.get(0);
                Class cl = Class.forName(className);

                Method mainMethod = cl.getDeclaredMethod("main", String[].class);
                mainMethod.invoke(null, (Object) new String[]{});

            } catch (ClassNotFoundException | NoSuchMethodException | InvocationTargetException | IllegalAccessException e) {
                e.printStackTrace();
            }

            // output task finished greetings
            System.out.println(tokenInfo.get(2));

        }
    }

    public static boolean doLogic(ArrayList<String> tokens){
        try {
            for(String token: tokens){
                Thread t = new Thread(new Task(token));
                t.setDaemon(false);
                t.start();
            }
        }catch (Throwable throwable){
            throwable.printStackTrace();
            return false;
        }
        return true;
    }
}
