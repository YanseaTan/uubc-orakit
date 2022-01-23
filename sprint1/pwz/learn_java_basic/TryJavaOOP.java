import java.util.Date;

/**
 * Core Java --> Chapter4~6 reading notes
 * @author pengwei.zhang
 * @version 2022.01.24
 * @see <a href="www.horstmann.com/corejava.html">Core Java</a>
 */
public class TryJavaOOP {


    /**
     * the first method of this Class
     */
    public void aboutObjectVariable(){
        Date deadline;
        // using an object variable which does not refer to an object would cause a compile-time error
        // deadline.toString(); // compile-time error
        deadline = new Date();
        System.out.println("Hello, now is " + deadline.toString()); // fine

        // !An object variable doesn’t actually contain an object. It only refers to an object.
        Date deadline2 = deadline; // deadline & deadline2 ~ all refer to that Date ob.
        System.out.println(System.identityHashCode(deadline)); // print address in flash
        System.out.println(System.identityHashCode(deadline2));

        deadline = null; // this makes
        // System.out.println(deadline.toString()); // NullPointerException
    }


}

class TestTryJavaOOP{
    public static void main(String[] args) {
        TryJavaOOP tjo = new TryJavaOOP();
        tjo.aboutObjectVariable();
    }
}