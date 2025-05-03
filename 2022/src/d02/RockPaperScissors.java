package src.d02;

import src.timer.Timer;

import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class RockPaperScissors {

    private static final Path file = Paths.get("src/files/02-RockPaperScissors.txt");

    public static void main(String[] args) throws Exception {
        Timer.measure(RockPaperScissors::aaa);
    }

    static int aaa() throws IOException {
        String data = Files.readString(file);
        List<String[]> plays = Arrays.stream(data.split(System.lineSeparator())).map(playRaw -> playRaw.split(" ")).toList();

        int totalPoints = plays.stream().mapToInt(RockPaperScissors::calcPoints).reduce(Integer::sum).orElseThrow();

        System.out.println(plays);

        return 1;
    }

    private static int calcPoints(String[] play) {
        String opponentPlay = play[0];
        String yourPlay;

        switch (play[1]) {
            case "X": yourPlay = "A";
            case "Y": yourPlay = "B";
            case "Z": yourPlay = "C";
        }

        return 1;
    }

    enum Play {
        A, B, C;
    }

    record Combo(Play opponentPlay, Play yourPlay) {}
}
