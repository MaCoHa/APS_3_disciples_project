import java.util.Scanner;

public class BestDrink {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int nDrinks = scanner.nextInt();

        int bestDrinkIndex = -1;
        double bestRatio = 0.0;
        for (int x = 0; x < nDrinks; x++) {
            int OH = scanner.nextInt();
            int price = scanner.nextInt();
            double ratio = (double) OH / price;
            if (ratio > bestRatio) {
                bestRatio = ratio;
                bestDrinkIndex = x;
            }
        }

        System.out.println(bestDrinkIndex);
        scanner.close();
    }
}

