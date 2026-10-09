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

void heapify(double a[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest])
        largest = left;

    if (right < n && a[right] > a[largest])
        largest = right;

    if (largest != i) {
        hoanDoi(a[i], a[largest]);
        heapify(a, n, largest);
    }
}

void heapSort(double a[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(a, n, i);
    }
    for (int i = n - 1; i > 0; i--) {
        hoanDoi(a[0], a[i]);
        heapify(a, i, 0);
    }
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

    cout << "Dang chay HeapSort voi n = " << n << "..." << endl;
    auto start = high_resolution_clock::now();
    heapSort(a, n);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Thoi gian chay HeapSort: " << duration.count() << " ms" << endl;

    delete[] a;
    return 0;
}
