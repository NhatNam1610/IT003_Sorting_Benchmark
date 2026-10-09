#include <iostream>
#include <fstream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

void merge(double a[], int left, int mid, int right, double temp[]) {
    int i = left;
    int j = mid + 1;
    int k = left;

    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
        }
    }

    while (i <= mid) {
        temp[k++] = a[i++];
    }

    while (j <= right) {
        temp[k++] = a[j++];
    }

    for (int p = left; p <= right; p++) {
        a[p] = temp[p];
    }
}

void mergeSort(double a[], int left, int right, double temp[]) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(a, left, mid, temp);
        mergeSort(a, mid + 1, right, temp);
        merge(a, left, mid, right, temp);
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

    double *temp = new double[n];

    cout << "Dang chay MergeSort voi n = " << n << "..." << endl;
    auto start = high_resolution_clock::now();
    mergeSort(a, 0, n - 1, temp);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Thoi gian chay MergeSort: " << duration.count() << " ms" << endl;

    delete[] a;
    delete[] temp;
    return 0;
}
