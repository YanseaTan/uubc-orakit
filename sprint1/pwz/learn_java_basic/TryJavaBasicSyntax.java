import static java.lang.Math.*;

/**
 * this is Documentation Comments
 * used to generate documentation automatically
 */
public class TryJavaBasicSyntax {

    /**
     * documentation comment contains free-form text followed by tags.
     * A tag starts with an @, such as @since or @param.
     *
     * 8 primitive type in java: integer*4 + floating-point*2 + char + boolean
     *
     * @author pengwei.zhang
     * @date 2022.01.20
     * @return well, always -1
     */
    public int tryPrimitiveType(){
        // JAVA is a kind of strongly type programming language, that means every variable
        // ~~should~~ must be declared a type

        // Java is a strongly typed language. This means that every variable must have a
        // declared type.

        // integer types
        int a = abs(-4); //int ~ 4 bytes ~ –2,147,483,648 to 2,147,483,647
        short b = 2; // short int ~ 2 bytes ~ –32,768 to 32,767
        long c = 8; // long int ~ 8 bytes ~ –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
        byte d = 1; // byte is just a byte ~ –128 to 127
        // note: no unsigned int in java
        // tips: you can write big int in this way: 100_0000_0000
        long people_on_earth = 9_000_000_000L; // note: add suffix 'L' after a long type integer

        // Floating-Point Types
        float ff = 4.0f;
        double dd = 8.0; // a floating point number will be process as double type in default
        double ddd = 8.0d; // add a 'd' after a double number to make it more clear, however that's unnecessary
        // clearer ~ more clear ~ both ok

        // char is just char
        char aaa = ' '; // ' ' = 32, first visible ascii character
        char zzz = 'z';
        for (int i = aaa;; i++){
            if(i > (int)zzz)break;
            System.out.printf("%d  =  %c\n",i,(char)i);
        }

        // boolean
        boolean t = true;
        boolean f = false;
        // you can't do this: boolean x = 0 or 1;
        // boolean x = 0; won't work...

        return -1;
    }

    public static void main(String[] args) {
        TryJavaBasicSyntax tjbs = new TryJavaBasicSyntax();
        tjbs.tryPrimitiveType();
    }

}
