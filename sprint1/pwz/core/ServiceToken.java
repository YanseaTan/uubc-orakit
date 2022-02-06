package pwz.core;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class ServiceToken {
    /**
     * service info map
     *
     * key = token
     * value = ArrayList<String>
     *     list[0] = service entrance
     *     list[1] = task started greetings
     *     list[2] = task finished greetings
     */
    public static final HashMap<String, ArrayList<String>> tokenInfo = new HashMap<String, ArrayList<String>>() {
        {
            put("snake", new ArrayList<>(
                    Arrays.asList(
                            "pwz.service.Snake.Scene",
                            "enjoy the game~",
                            "boring...")));
        }
    };
}
