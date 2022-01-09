import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.filtering;
import static java.util.stream.Collectors.joining;

public class Pionki {

    static class Field {
        boolean black;
        int howManyTimesFlipped = 0;

        Field(boolean black) {
            this.black = black;
        }

        int flip() {
            this.black = !black;
            howManyTimesFlipped++;
            return black ? 1 : -1;
        }

        @Override
        public String toString() {
            return (black ? "." : " ") + howManyTimesFlipped + " ";
        }
    }

    static class Board {
        int blackCount = 0;
        Field[] fields;

        Board() {
            this.fields = new Field[64];
            for (int i = 0; i < 64; i++) {
                fields[i] = new Field(false);
            }
        }

        static Board of(String configuration) {
            Board board = new Board();
            List<Integer> flipped = Arrays.stream(configuration.split(" ")).map(Integer::valueOf).toList();
            flipped.forEach(f -> board.fields[f].black = true);
            board.blackCount = flipped.size();
            return board;
        }

        static Board copy(Board b) {
            Board board = new Board();
            board.fields = Arrays.copyOf(b.fields, b.fields.length);
            board.blackCount = b.blackCount;
            return board;
        }

        boolean isSolved() {
            return blackCount == 0 || blackCount == 64;
        }

        void flip(int index) {
            adjacent(index).forEach(i -> {
                int n = fields[i].flip();
                blackCount += n;
            });
        }

        Set<Integer> adjacent(int index) {
           Set<Integer> result = new HashSet<>();
           int row = index / 8;
           int col = index % 8;
           for (int i  = row - 1; i <= row + 1; i++) {
               for (int j  = col - 1; j <= col + 1; j++) {
                   int coords = i * 8 + j;
                   if (i >= 0 && i < 8 && j >= 0 && j < 8) {
                       result.add(coords);
                   }
               }
           }
           result.remove(index);
           return result;
        }

        /*
        Finds the maximum flip number if this flip is executed
         */
        int rank(int index) {
            Set<Integer> adjacent = adjacent(index);
            int max = adjacent.stream().map(i -> fields[i].howManyTimesFlipped).max(Comparator.naturalOrder()).orElse(-1);
            return max + 1;
        }

        void print() {
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    int index = i * 8 + j;
                    System.out.print(fields[index].toString());
                }
                System.out.println();
            }
        }
    }

    static class Node {
        Node prev;
        Board b;
    }

    static class Solver {

        List<Integer> minimal(Board board) {
            Map<Integer, List<Integer>> rankMap = IntStream.range(0, 64)
                    .boxed()
                    .collect(Collectors.groupingBy(board::rank));
            int min = rankMap.keySet().stream().min(Comparator.naturalOrder()).orElse(-1);
            return rankMap.get(min);
        }

        Set<Integer> solve(Board b) {

        }



    }

    public static void main(String[] args) {
        Board board = Board.of("8 9 10 11 12 13 14 15");
//        board.flip(56);
//        board.flip(58);
//        board.flip(61);
//        board.flip(63);
//        board.flip(49);
//        board.flip(54);
//        board.flip(41);
//        board.flip(46);
//        board.flip(32);
//        board.flip(34);
//        board.flip(37);
//        board.flip(39);
//        board.flip(24);
//        board.flip(25);
//        board.flip(27);
//        board.flip(28);
//        board.flip(30);
//        board.flip(31);
//        board.flip(17);
//        board.flip(18);
//        board.flip(21);
//        board.flip(22);
//        board.flip(1);
//        board.flip(2);
//        board.flip(5);
//        board.flip(6);
        board.print();

        Solver solver = new Solver();
        System.out.println(solver.minimal(board).stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }

}
