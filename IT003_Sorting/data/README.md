# Dữ liệu thử nghiệm (Datasets)

Thư mục này chứa mã nguồn **`generate_data.cpp`** dùng để sinh 10 bộ dữ liệu số thực thử nghiệm theo yêu cầu đề bài:
- **Dãy 1:** 1.000.000 số thực có thứ tự **tăng dần** (`input_1.txt`).
- **Dãy 2:** 1.000.000 số thực có thứ tự **giảm dần** (`input_2.txt`).
- **Dãy 3 đến 10:** Mỗi dãy gồm 1.000.000 số thực **ngẫu nhiên** (`input_3.txt` -> `input_10.txt`).

---

## 🛠 Hướng dẫn sinh dữ liệu:
Do 10 file dữ liệu văn bản chứa tổng cộng 10 triệu số thực có kích thước rất lớn (~125 MB), vượt quá giới hạn tải lên của GitHub, bạn có thể tự sinh lại dữ liệu bất cứ lúc nào bằng lệnh:

```bash
g++ -O2 generate_data.cpp -o generate_data
./generate_data
```

Hoặc khi chạy chương trình **`src/benchmark_all.cpp`**, chương trình đã tích hợp sẵn cơ chế tự động sinh dữ liệu trực tiếp trong bộ nhớ RAM để đo đạc mà không cần đọc ghi file dung lượng lớn.
