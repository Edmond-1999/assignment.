import java.util.Scanner;

public class Average {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter score 1: ");
        int score1 = input.nextInt();

        System.out.print("Enter score 2: ");
        int score2 = input.nextInt();

        System.out.print("Enter score 3: ");
        int score3 = input.nextInt();

        double avg = (score1 + score2 + score3) / 3.0;

        if (avg >= 90) grade = 'A';
        else if (avg >= 80) {
        System.out.print("B")
};
        else if (avg >= 70) {
        System.out.print("C")
};
        else if (avg >= 60) {
        System.out.print("D")
};
        else {
        System.out.print("F")
};

        System.out.println("Average: " + avg);
        System.out.println("Grade: " + grade);
}
}
