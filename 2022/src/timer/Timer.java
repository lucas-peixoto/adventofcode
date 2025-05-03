package src.timer;

public class Timer {

    public static <T> T measure(SupplierT<T> supplier) throws Exception {
        long start = System.currentTimeMillis();

        T value = supplier.get();

        long finish = System.currentTimeMillis();
        long timeElapsed = finish - start;

        System.out.println(timeElapsed + "ms");

        return value;
    }
}
