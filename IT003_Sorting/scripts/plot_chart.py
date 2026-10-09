import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Đường dẫn file dữ liệu
csv_path = os.path.join(os.path.dirname(__file__), "..", "report", "results.csv")
output_path = os.path.join(os.path.dirname(__file__), "..", "report", "chart.png")

df = pd.read_csv(csv_path)

# Lọc 10 dataset và hàng Trung bình
datasets = df['Dataset'].astype(str).tolist()
quicksort_times = df['QuickSort'].round(1).tolist()
heapsort_times = df['HeapSort'].round(1).tolist()
mergesort_times = df['MergeSort'].round(1).tolist()
std_sort_times = df['std_sort'].round(1).tolist()

x = np.arange(len(datasets))
width = 0.20

plt.figure(figsize=(15, 7.5), dpi=300)

# Cấu hình màu sắc giống mẫu đề bài:
# QuickSort: Xanh dương (#4F81BD)
# HeapSort: Cam (#ED7D31)
# MergeSort: Xám (#A5A5A5)
# sort (C++): Vàng (#FFC000)
rects1 = plt.bar(x - 1.5 * width, quicksort_times, width, label='QuickSort', color='#4F81BD', edgecolor='none')
rects2 = plt.bar(x - 0.5 * width, heapsort_times, width, label='HeapSort', color='#ED7D31', edgecolor='none')
rects3 = plt.bar(x + 0.5 * width, mergesort_times, width, label='MergeSort', color='#A5A5A5', edgecolor='none')
rects4 = plt.bar(x + 1.5 * width, std_sort_times, width, label='sort (C++)', color='#FFC000', edgecolor='none')

plt.title('Kết quả thử nghiệm trên bộ dữ liệu', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Bộ dữ liệu', fontsize=13, labelpad=10)
plt.ylabel('Thời gian thực hiện (ms)', fontsize=13, labelpad=10)
plt.xticks(x, datasets, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=12, loc='upper left')

# Hàm hiển thị giá trị lên trên mỗi cột
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate(f'{height:.0f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, rotation=45)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

max_y = max(max(heapsort_times), max(mergesort_times), max(quicksort_times), max(std_sort_times))
plt.ylim(0, max_y * 1.15)
plt.tight_layout()

plt.savefig(output_path, dpi=300)
print(f"Da xuat bieu do thanh cong tai: {output_path}")
