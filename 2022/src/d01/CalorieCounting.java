package src.d01;

import src.timer.Timer;

import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class CalorieCounting {

    private static final Path file = Paths.get("src/files/01-CalorieCounting.txt");

    public static void main(String[] args) throws Exception {
        int result = Timer.measure(CalorieCounting::part1);
        System.out.println("Max calories: " + result);

        int result2 = Timer.measure(CalorieCounting::part2);
        System.out.println("Top 3 calories: " + result2);
    }

    static int part1() throws IOException {
        String data = Files.readString(file);
        String[] elvesFood = data.split(System.lineSeparator() + System.lineSeparator());
        ArrayList<Integer> elvesCalorieCount = new ArrayList<>();

        for (String elfFoods : elvesFood) {
            int elfCalorieCount = Arrays.stream(elfFoods.split(System.lineSeparator()))
                    .mapToInt(Integer::valueOf).sum();

            elvesCalorieCount.add(elfCalorieCount);
        }

        return Collections.max(elvesCalorieCount);
    }

    static int part2() throws IOException {
        String data = Files.readString(file);
        String[] elvesFood = data.split(System.lineSeparator() + System.lineSeparator());
        ArrayList<Integer> elvesCalorieCount = new ArrayList<>();

        for (String elfFoods : elvesFood) {
            int elfCalorieCount = Arrays.stream(elfFoods.split(System.lineSeparator()))
                    .mapToInt(Integer::valueOf).sum();

            elvesCalorieCount.add(elfCalorieCount);
        }

        int top1 = Collections.max(elvesCalorieCount);
        elvesCalorieCount.remove(Integer.valueOf(top1));

        int top2 = Collections.max(elvesCalorieCount);
        elvesCalorieCount.remove(Integer.valueOf(top2));

        int top3 = Collections.max(elvesCalorieCount);
        elvesCalorieCount.remove(Integer.valueOf(top3));

        return top1 + top2 + top3;
    }
}
