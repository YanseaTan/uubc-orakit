package pwz.service;

import java.util.Scanner;

public class WeatherQueryUtil {
    public static void queryWeather(String[] args){
        System.out.println("where do you want to check the weather?");
        Scanner in = new Scanner(System.in);
        String location = in.nextLine();
        //todo: query the weather...
        System.out.println(location);
    }
    public static void main(String[] args) throws InterruptedException {
        queryWeather(null);
    }
}
