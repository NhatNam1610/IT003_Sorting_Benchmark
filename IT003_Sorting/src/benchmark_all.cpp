#include <iostream>
#include <iomanip>
#include <fstream>
#include <chrono>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;
using namespace std::chrono;

const int SO_LUONG_DAY = 10;
const int N = 1000000;

void hoanDoi(double &x, double &y) {
    double temp = x;
    x = y;
    y = temp;
}

// 1. QUICKSORT
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

// 2. HEAPSORT
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

// 3. MERGESORT
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

// CAC HAM TAO DU LIEU THU NGHIEM
void taoMangTangDan(double a[], int n) {
    double val = -1000000.0;
    for (int i = 0; i < n; i++) {
        val += (double)rand() / RAND_MAX * 2.0;
        a[i] = val;
    }
}

void taoMangGiamDan(double a[], int n) {
    double val = 1000000.0;
    for (int i = 0; i < n; i++) {
        val -= (double)rand() / RAND_MAX * 2.0;
        a[i] = val;
    }
}

void taoMangNgauNhien(double a[], int n) {
    for (int i = 0; i < n; i++) {
        a[i] = ((double)rand() / RAND_MAX * 2000000.0) - 1000000.0;
    }
}

void saoChepMang(double goc[], double dich[], int n) {
    for (int i = 0; i < n; i++) {
        dich[i] = goc[i];
    }
}

int main() {
    srand(12345);
    double *goc = new double[N];
    double *tam = new double[N];
    double *mangPhuMerge = new double[N];

    double bangKetQua[SO_LUONG_DAY][4];

    for (int d = 0; d < SO_LUONG_DAY; d++) {
        cout << "\nDang khoi tao va chay thu nghiem cho Day " << (d + 1) << " ... ";
        if (d == 0) {
            cout << "(Tang dan)" << endl;
            taoMangTangDan(goc, N);
        } else if (d == 1) {
            cout << "(Giam dan)" << endl;
            taoMangGiamDan(goc, N);
        } else {
            cout << "(Ngau nhien)" << endl;
            taoMangNgauNhien(goc, N);
        }

        // 1. Chay QuickSort
        saoChepMang(goc, tam, N);
        auto t1 = high_resolution_clock::now();
        quickSort(tam, 0, N - 1);
        auto t2 = high_resolution_clock::now();
        bangKetQua[d][0] = duration_cast<milliseconds>(t2 - t1).count();
        cout << "  + QuickSort : " << bangKetQua[d][0] << " ms" << endl;

        // 2. Chay HeapSort
        saoChepMang(goc, tam, N);
        t1 = high_resolution_clock::now();
        heapSort(tam, N);
        t2 = high_resolution_clock::now();
        bangKetQua[d][1] = duration_cast<milliseconds>(t2 - t1).count();
        cout << "  + HeapSort  : " << bangKetQua[d][1] << " ms" << endl;

        // 3. Chay MergeSort
        saoChepMang(goc, tam, N);
        t1 = high_resolution_clock::now();
        mergeSort(tam, 0, N - 1, mangPhuMerge);
        t2 = high_resolution_clock::now();
        bangKetQua[d][2] = duration_cast<milliseconds>(t2 - t1).count();
        cout << "  + MergeSort : " << bangKetQua[d][2] << " ms" << endl;

        // 4. Chay sort C++
        saoChepMang(goc, tam, N);
        t1 = high_resolution_clock::now();
        sort(tam, tam + N);
        t2 = high_resolution_clock::now();
        bangKetQua[d][3] = duration_cast<milliseconds>(t2 - t1).count();
        cout << "  + sort (C++): " << bangKetQua[d][3] << " ms" << endl;
    }

    // Tinh thoi gian trung binh
    double trungBinh[4] = {0, 0, 0, 0};
    for (int j = 0; j < 4; j++) {
        double tong = 0;
        for (int i = 0; i < SO_LUONG_DAY; i++) {
            tong += bangKetQua[i][j];
        }
        trungBinh[j] = tong / SO_LUONG_DAY;
    }

    cout << left << setw(12) << "Du lieu"
         << right << setw(14) << "QuickSort"
         << setw(14) << "HeapSort"
         << setw(14) << "MergeSort"
         << setw(14) << "sort (C++)" << endl;
    cout << string(68, '-') << endl;

    for (int d = 0; d < SO_LUONG_DAY; d++) {
        cout << left << setw(12) << (to_string(d + 1))
             << right << fixed << setprecision(1)
             << setw(14) << bangKetQua[d][0]
             << setw(14) << bangKetQua[d][1]
             << setw(14) << bangKetQua[d][2]
             << setw(14) << bangKetQua[d][3] << endl;
    }
    cout << string(68, '-') << endl;
    cout << left << setw(12) << "Trung binh"
         << right << fixed << setprecision(1)
         << setw(14) << trungBinh[0]
         << setw(14) << trungBinh[1]
         << setw(14) << trungBinh[2]
         << setw(14) << trungBinh[3] << endl;

    // Ghi ra file CSV de tien ve bieu do va dan vao bao cao
    ofstream csv("report/results.csv");
    if (csv.is_open()) {
        csv << "Dataset,QuickSort,HeapSort,MergeSort,std_sort\n";
        for (int d = 0; d < SO_LUONG_DAY; d++) {
            csv << (d + 1) << ","
                << bangKetQua[d][0] << ","
                << bangKetQua[d][1] << ","
                << bangKetQua[d][2] << ","
                << bangKetQua[d][3] << "\n";
        }
        csv << "Trung binh,"
            << trungBinh[0] << ","
            << trungBinh[1] << ","
            << trungBinh[2] << ","
            << trungBinh[3] << "\n";
        csv.close();
        cout << "\n-> Da luu ket qua vao file report/results.csv!" << endl;
    }

    // Giai phong bo nho
    delete[] goc;
    delete[] tam;
    delete[] mangPhuMerge;

    return 0;
}
