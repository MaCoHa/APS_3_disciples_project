#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
    int nDrinks;
    cin >> nDrinks;

    int bestDrinkIndex = -1;
    double bestRatio = 0.0;
    for (int x = 0; x < nDrinks; x++) {
        int OH, price;
        cin >> OH >> price;
        double ratio = static_cast<double>(OH) / price;
        if (ratio > bestRatio) {
            bestRatio = ratio;
            bestDrinkIndex = x;
        }
    }

    cout << bestDrinkIndex << endl;

    return 0;
}
