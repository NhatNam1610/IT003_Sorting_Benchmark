#include <iostream>
#include <fstream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

int main() {
    ifstream fin("input.txt");
    if (!fin.is_open()) {
        cout << "Khong the mo file input.txt!" << endl;
        return 1;
    }

    int n;
    fin >> n;
    double *a = new double[n];
    for (int i = 0; i < n; i++) {
        fin >> a[i];
    }
    fin.close();

    cout << "Dang chay ham sort() cua C++ voi n = " << n << "..." << endl;
    auto start = high_resolution_clock::now();
    sort(a, a + n);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Thoi gian chay sort(C++): " << duration.count() << " ms" << endl;

    delete[] a;
    return 0;
}
