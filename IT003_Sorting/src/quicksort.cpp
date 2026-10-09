#include <iostream>
#include <fstream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

void hoanDoi(double &x, double &y) {
    double temp = x;
    x = y;
    y = temp;
}

void quickSort(double a[], int left, int right) {
    double pivot = a[(left + right) / 2];
    int i = left;
    int j = right;

    while (i <= j) {
        while (a[i] < pivot) i++;
        while (a[j] > pivot) j--;
        if (i <= j) {
            hoanDoi(a[i], a[j]);
            i++;
            j--;
        }
    }

    if (left < j) quickSort(a, left, j);
    if (i < right) quickSort(a, i, right);
}

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

    cout << "Dang chay QuickSort voi n = " << n << "..." << endl;
    auto start = high_resolution_clock::now();
    quickSort(a, 0, n - 1);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Thoi gian chay QuickSort: " << duration.count() << " ms" << endl;

    delete[] a;
    return 0;
}
