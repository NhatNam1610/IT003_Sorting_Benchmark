#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    const int SO_DAY = 10;
    const int N = 1000000; // 1 trieu so thuc

    srand(12345);
    cout << "Bat dau tao 10 file du lieu (moi file 1 trieu so thuc)..." << endl;

    for (int d = 1; d <= SO_DAY; d++) {
        string tenFile = "data/input_" + to_string(d) + ".txt";
        ofstream f(tenFile);
        if (!f.is_open()) {
            tenFile = "input_" + to_string(d) + ".txt";
            f.open(tenFile);
        }

        f << N << "\n";
        cout << "Dang ghi file " << tenFile << " ... ";

        if (d == 1) {
            // Day 1: Tang dan
            double val = -1000000.0;
            for (int i = 0; i < N; i++) {
                val += (double)rand() / RAND_MAX * 2.0;
                f << fixed << setprecision(3) << val << " ";
            }
            cout << "(Tang dan) Xong!" << endl;
        } else if (d == 2) {
            // Day 2: Giam dan
            double val = 1000000.0;
            for (int i = 0; i < N; i++) {
                val -= (double)rand() / RAND_MAX * 2.0;
                f << fixed << setprecision(3) << val << " ";
            }
            cout << "(Giam dan) Xong!" << endl;
        } else {
            // Day 3 - 10: Ngau nhien
            for (int i = 0; i < N; i++) {
                double val = ((double)rand() / RAND_MAX * 2000000.0) - 1000000.0;
                f << fixed << setprecision(3) << val << " ";
            }
            cout << "(Ngau nhien) Xong!" << endl;
        }

        f << "\n";
        f.close();
    }

    cout << "\nDa tao xong toan bo du lieu!" << endl;
    return 0;
}
