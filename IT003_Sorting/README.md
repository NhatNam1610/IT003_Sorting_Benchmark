# IT003 - Thử Nghiệm Hiệu Năng Các Thuật Toán Sắp Xếp (Sorting Benchmark)

## 📌 Giới thiệu đề tài
Bài tập lớn môn Cấu trúc Dữ liệu và Giải thuật (IT003): Thực nghiệm đánh giá thời gian thực thi của 4 thuật toán sắp xếp:
1. **QuickSort** (Cài đặt theo slide bài giảng, chọn pivot ở giữa mảng)
2. **HeapSort** (Vun đống đệ quy theo giáo trình)
3. **MergeSort** (Chia để trị dùng mảng tạm)
4. **C++ `std::sort`** (Hàm sort trong thư viện `<algorithm>`)

Thử nghiệm được thực hiện trên **10 bộ dữ liệu**, mỗi bộ gồm **1.000.000 số thực** (`double`):
- **Dãy 1:** Đã sắp xếp tăng dần.
- **Dãy 2:** Đã sắp xếp giảm dần.
- **Dãy 3 -> 10:** Trật tự ngẫu nhiên.

---

## 📂 Cấu trúc Repository

```text
IT003_Sorting_Benchmark/
├── src/                         # Thư mục mã nguồn C++
│   ├── quicksort.cpp            # Thuật toán QuickSort độc lập
│   ├── heapsort.cpp             # Thuật toán HeapSort độc lập
│   ├── mergesort.cpp            # Thuật toán MergeSort độc lập
│   ├── std_sort.cpp             # Gọi hàm sort() của C++
│   └── benchmark_all.cpp        # File tổng hợp chạy cả 4 thuật toán và xuất bảng kết quả
├── data/                        # Sinh dữ liệu
│   └── generate_data.cpp        # Code tạo 10 file dữ liệu txt
├── scripts/                     # Script vẽ biểu đồ
│   └── plot_chart.py            # Script Python vẽ biểu đồ cột kết quả
├── report/                      # Báo cáo kết quả
│   ├── BaoCao_ThucNghiem_Sorting.pdf # File báo cáo PDF nộp bài
│   ├── report.html              # Báo cáo dạng HTML
│   ├── chart.png                # Biểu đồ cột kết quả thử nghiệm
│   └── results.csv              # Bảng số liệu thời gian thực hiện (ms)
├── .gitignore
└── README.md
```

---

## 🚀 Hướng dẫn biên dịch và chạy

### 1. Biên dịch và chạy toàn bộ thử nghiệm:
Bạn có thể mở bằng Dev-C++, Code::Blocks, Visual Studio hoặc gõ lệnh terminal:

#### Dùng GCC (MinGW / CodeBlocks / Dev-C++):
```bash
g++ -O2 src/benchmark_all.cpp -o benchmark_all
./benchmark_all
```

#### Dùng MSVC (Visual Studio):
```cmd
cl /O2 /EHsc src/benchmark_all.cpp /Fe:benchmark_all.exe
benchmark_all.exe
```

Chương trình sẽ tự động tạo dữ liệu trong bộ nhớ, chạy từng thuật toán, đo thời gian thực thi (ms) và in ra bảng kết quả.

---

## 📊 Bảng kết quả thực nghiệm (ms)

| Bộ dữ liệu | QuickSort (ms) | HeapSort (ms) | MergeSort (ms) | sort (C++) (ms) |
| :--- | :---: | :---: | :---: | :---: |
| **1 (Tăng dần)** | 13.0 | 112.0 | 25.0 | 16.0 |
| **2 (Giảm dần)** | 14.0 | 111.0 | 33.0 | 14.0 |
| **3 (Ngẫu nhiên)** | 64.0 | 280.0 | 96.0 | 68.0 |
| **4 (Ngẫu nhiên)** | 73.0 | 300.0 | 111.0 | 63.0 |
| **5 (Ngẫu nhiên)** | 65.0 | 312.0 | 98.0 | 64.0 |
| **6 (Ngẫu nhiên)** | 70.0 | 305.0 | 96.0 | 64.0 |
| **7 (Ngẫu nhiên)** | 67.0 | 309.0 | 95.0 | 61.0 |
| **8 (Ngẫu nhiên)** | 69.0 | 304.0 | 93.0 | 63.0 |
| **9 (Ngẫu nhiên)** | 67.0 | 335.0 | 96.0 | 70.0 |
| **10 (Ngẫu nhiên)** | 65.0 | 299.0 | 90.0 | 64.0 |
| **Trung bình** | **56.7** | **266.7** | **83.3** | **54.7** |

---

## 📝 Nhận xét tóm tắt
1. **`std::sort` (C++):** Nhanh nhất tổng thể (trung bình 54.7 ms) do thư viện C++ sử dụng Introsort kết hợp tối ưu hóa compiler.
2. **QuickSort:** Rất nhanh (trung bình 56.7 ms). Khi chọn pivot ở giữa mảng `pivot = a[(left + right) / 2]`, thuật toán tránh được trường hợp xấu nhất trên mảng tăng dần và giảm dần, chạy mượt mà không bị tràn stack.
3. **MergeSort:** Đạt tốc độ tốt (trung bình 83.3 ms), ổn định nhưng cần thêm mảng tạm $O(N)$ để trộn.
4. **HeapSort:** Chậm nhất (trung bình 266.7 ms) do việc truy xuất cây nhị phân trên mảng lớn bị nhiều Cache Miss.
