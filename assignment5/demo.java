import test;

class demo {
    public static void main(String[] args) {
        // test comment
        /*test multiline comment*/
        String string = "this is a test string";
        
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }

        while (true) {
            if (true) {
                System.out.println("test");
            } else {
                System.out.println("test2");
            }
        }
        try {
            open("demo.java");
        } catch (Exception e) {
            System.out.println("caught");
        }


    }
}