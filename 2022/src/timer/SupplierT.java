package src.timer;

@FunctionalInterface
public interface SupplierT<T> {
    T get() throws Exception;
}
