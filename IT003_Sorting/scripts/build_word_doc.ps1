# PowerShell script to create native formatted Word Document (.docx) via Word COM
$chartPath = "C:\Users\LENOVO\.gemini\antigravity\scratch\IT003_Sorting_Benchmark\report\chart.png"
$docxPathDownloads = "C:\Users\LENOVO\Downloads\BaoCao_ThucNghiem_Sorting.docx"
$docxPathProject = "C:\Users\LENOVO\.gemini\antigravity\scratch\IT003_Sorting_Benchmark\report\BaoCao_ThucNghiem_Sorting.docx"

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Add()

    # Set page margins A4
    $doc.PageSetup.TopMargin = 56.7    # 2 cm
    $doc.PageSetup.BottomMargin = 56.7 # 2 cm
    $doc.PageSetup.LeftMargin = 56.7   # 2 cm
    $doc.PageSetup.RightMargin = 56.7  # 2 cm

    $selection = $word.Selection

    # 1. Title & Header
    $selection.ParagraphFormat.Alignment = 1 # Center
    $selection.Font.Name = "Times New Roman"
    $selection.Font.Size = 13
    $selection.Font.Bold = $true
    $selection.Font.ColorIndex = 1 # Black
    $selection.TypeText("TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM`n")
    $selection.TypeText("MÔN HỌC: CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT (IT003) - LỚP: IT003.R17`n`n")

    $selection.Font.Size = 18
    $selection.Font.Color = 192 # Dark Red
    $selection.TypeText("BÁO CÁO KẾT QUẢ THỬ NGHIỆM`n")

    $selection.Font.Size = 12
    $selection.Font.Bold = $false
    $selection.Font.Italic = $true
    $selection.Font.ColorIndex = 1
    $selection.TypeText("Thời gian thực hiện: 01/10 – 10/10/2026`n`n")

    # 2. Student Info Box
    $selection.ParagraphFormat.Alignment = 0 # Left
    $selection.Font.Italic = $false
    $selection.Font.Size = 12
    
    $selection.Font.Bold = $true
    $selection.TypeText("Sinh viên thực hiện: ")
    $selection.Font.Bold = $false
    $selection.TypeText("[Điền Họ và tên sinh viên]`n")

    $selection.Font.Bold = $true
    $selection.TypeText("Mã số sinh viên (MSSV): ")
    $selection.Font.Bold = $false
    $selection.TypeText("[Điền MSSV]`n")

    $selection.Font.Bold = $true
    $selection.TypeText("Môi trường thử nghiệm: ")
    $selection.Font.Bold = $false
    $selection.TypeText("C++17 (Compiler MSVC/GCC - O2), CPU Intel Core, 16GB RAM, Windows 11`n`n")

    # 3. Section I
    $selection.Font.Size = 14
    $selection.Font.Bold = $true
    $selection.Font.Color = 8274731 # Dark Navy Blue
    $selection.TypeText("I. NỘI DUNG VÀ MỤC TIÊU THỰC NGHIỆM`n")
    $selection.Font.ColorIndex = 1
    $selection.Font.Size = 12.5
    $selection.Font.Bold = $false
    $selection.TypeText("Thực nghiệm nhằm đo đạc và so sánh thời gian thực thi của 4 giải thuật sắp xếp: ")
    $selection.Font.Bold = $true
    $selection.TypeText("QuickSort, HeapSort, MergeSort")
    $selection.Font.Bold = $false
    $selection.TypeText(" và hàm ")
    $selection.Font.Bold = $true
    $selection.TypeText("sort của C++ (std::sort)")
    $selection.Font.Bold = $false
    $selection.TypeText(" trên 10 bộ dữ liệu số thực, mỗi bộ gồm ")
    $selection.Font.Bold = $true
    $selection.TypeText("1.000.000 phần tử")
    $selection.Font.Bold = $false
    $selection.TypeText(" (kiểu double):`n")

    $selection.TypeText("• Dãy 1: Đã có thứ tự tăng dần.`n")
    $selection.TypeText("• Dãy 2: Đã có thứ tự giảm dần.`n")
    $selection.TypeText("• Dãy 3 đến Dãy 10: Dữ liệu có thứ tự ngẫu nhiên.`n`n")

    # 4. Section II
    $selection.Font.Size = 14
    $selection.Font.Bold = $true
    $selection.Font.Color = 8274731
    $selection.TypeText("II. KẾT QUẢ THỬ NGHIỆM`n")
    $selection.Font.ColorIndex = 1
    $selection.Font.Size = 13
    $selection.TypeText("1. Bảng thời gian thực hiện (đơn vị: ms)`n`n")

    # Insert Table: 13 rows x 5 columns
    $table = $doc.Tables.Add($selection.Range, 13, 5)
    $table.Borders.Enable = $true
    $table.Range.Font.Name = "Times New Roman"
    $table.Range.Font.Size = 11

    # Table Header Data
    $data = @(
        @("Bộ Dữ liệu", "QuickSort", "HeapSort", "MergeSort", "sort (C++)"),
        @("1 (Tăng dần)", "13.0", "112.0", "25.0", "16.0"),
        @("2 (Giảm dần)", "14.0", "111.0", "33.0", "14.0"),
        @("3 (Ngẫu nhiên)", "64.0", "280.0", "96.0", "68.0"),
        @("4 (Ngẫu nhiên)", "73.0", "300.0", "111.0", "63.0"),
        @("5 (Ngẫu nhiên)", "65.0", "312.0", "98.0", "64.0"),
        @("6 (Ngẫu nhiên)", "70.0", "305.0", "96.0", "64.0"),
        @("7 (Ngẫu nhiên)", "67.0", "309.0", "95.0", "61.0"),
        @("8 (Ngẫu nhiên)", "69.0", "304.0", "93.0", "63.0"),
        @("9 (Ngẫu nhiên)", "67.0", "335.0", "96.0", "70.0"),
        @("10 (Ngẫu nhiên)", "65.0", "299.0", "90.0", "64.0"),
        @("Trung bình", "56.7", "266.7", "83.3", "54.7")
    )

    # Populate Table
    for ($r = 0; $r -lt 12; $r++) {
        for ($c = 0; $c -lt 5; $c++) {
            $cell = $table.Cell($r + 1, $c + 1)
            $cell.Range.Text = $data[$r][$c]
            $cell.Range.ParagraphFormat.Alignment = 1 # Center
            if ($r -eq 0) {
                $cell.Range.Font.Bold = $true
                $cell.Shading.BackgroundPatternColor = 14535354 # Light blue-gray
            }
            if ($r -eq 11) {
                $cell.Range.Font.Bold = $true
                $cell.Shading.BackgroundPatternColor = 15395562 # Soft highlight
            }
        }
    }
    # Auto-fit table
    $table.AutoFitBehavior(2) # wdAutoFitWindow

    # Move after table
    $doc.Characters.Last.Select()
    $selection.Collapse(0)
    $selection.TypeText("`n`n")

    # 5. Chart
    $selection.Font.Size = 13
    $selection.Font.Bold = $true
    $selection.Font.Color = 8274731
    $selection.TypeText("2. Biểu đồ cột thời gian thực hiện`n`n")
    $selection.Font.ColorIndex = 1

    # Insert Picture with embedding (LinkToFile = False, SaveWithDocument = True)
    if (Test-Path $chartPath) {
        $shape = $selection.InlineShapes.AddPicture($chartPath, $false, $true)
        $shape.Width = 460 # Fit nicely within page width
        $shape.Height = 230
        $selection.ParagraphFormat.Alignment = 1
        $selection.TypeText("`nHình 1: Biểu đồ cột thời gian thực hiện (ms) trên 10 bộ dữ liệu và giá trị trung bình`n`n")
    }

    # 6. Section III: Analysis
    $selection.ParagraphFormat.Alignment = 0 # Left
    $selection.Font.Size = 14
    $selection.Font.Bold = $true
    $selection.Font.Color = 8274731
    $selection.TypeText("III. NHẬN XÉT VÀ GIẢI THÍCH KẾT QUẢ`n")
    $selection.Font.ColorIndex = 1
    $selection.Font.Size = 12.5
    $selection.Font.Bold = $false

    $selection.TypeText("Dựa trên bảng số liệu và biểu đồ thu được từ thực nghiệm trên 1.000.000 số thực, em rút ra các nhận xét sau:`n`n")

    # QuickSort
    $selection.Font.Bold = $true
    $selection.TypeText("1. Thuật toán QuickSort:`n")
    $selection.Font.Bold = $false
    $selection.TypeText("• Độ phức tạp: Trung bình là O(N log N), xấu nhất là O(N^2).`n")
    $selection.TypeText("• Kết quả trên dãy 1 (Tăng dần - 13.0 ms) và dãy 2 (Giảm dần - 14.0 ms): Khi cài đặt QuickSort theo bài giảng, chọn pivot là phần tử chính giữa mảng (pivot = a[(left + right) / 2]), trên mảng đã có thứ tự tăng dần hoặc giảm dần, phần tử chính giữa này chính là giá trị trung vị của dãy. Nhờ đó mảng được chia đôi rất cân bằng, không bị rơi vào trường hợp xấu nhất O(N^2) và không bị tràn ngăn xếp (Stack Overflow). Do các phần tử đã gần đúng vị trí nên số lần hoán đổi ít, giúp QuickSort chạy cực nhanh.`n")
    $selection.TypeText("• Trên 8 dãy ngẫu nhiên: Thời gian dao động từ 64 ms đến 73 ms (trung bình 56.7 ms). Thuật toán hoạt động rất hiệu quả, tốc độ tương đương với hàm sort của C++.`n`n")

    # HeapSort
    $selection.Font.Bold = $true
    $selection.TypeText("2. Thuật toán HeapSort:`n")
    $selection.Font.Bold = $false
    $selection.TypeText("• Độ phức tạp: Luôn là O(N log N) trong mọi trường hợp, không dùng bộ nhớ phụ (O(1)).`n")
    $selection.TypeText("• Hiệu năng thực tế: Chạy chậm nhất trong cả 4 thuật toán, trung bình mất 266.7 ms.`n")
    $selection.TypeText("• Giải thích nguyên nhân: Cấu trúc cây Heap lưu trên mảng khiến các bước truy cập phần tử cha - con bị nhảy cách quãng xa (i -> 2i+1, 2i+2). Với mảng lớn 1 triệu phần tử, việc này gây ra nhiều hiện tượng Cache Miss (bộ nhớ đệm CPU không chứa sẵn dữ liệu), CPU phải tốn thời gian lấy dữ liệu từ RAM nên tốc độ thực tế bị chậm hơn.`n`n")

    # MergeSort
    $selection.Font.Bold = $true
    $selection.TypeText("3. Thuật toán MergeSort:`n")
    $selection.Font.Bold = $false
    $selection.TypeText("• Độ phức tạp: Luôn là O(N log N) trong mọi trường hợp, có tính ổn định (Stable Sort).`n")
    $selection.TypeText("• Hiệu năng thực tế: Thời gian trung bình là 83.3 ms, đứng thứ 3 sau sort C++ và QuickSort. Trên dãy tăng dần (25.0 ms) và giảm dần (33.0 ms), MergeSort chạy nhanh hơn mảng ngẫu nhiên (khoảng 90 - 111 ms).`n")
    $selection.TypeText("• Đặc điểm: MergeSort cần mảng tạm kích thước O(N) để trộn hai nửa mảng lại với nhau.`n`n")

    # std::sort
    $selection.Font.Bold = $true
    $selection.TypeText("4. Hàm sort của C++ (std::sort):`n")
    $selection.Font.Bold = $false
    $selection.TypeText("• Hiệu năng thực tế: Chạy nhanh nhất tổng thể với thời gian trung bình 54.7 ms.`n")
    $selection.TypeText("• Giải thích: Hàm sort trong thư viện <algorithm> của C++ sử dụng thuật toán Introsort (kết hợp thông minh giữa QuickSort, HeapSort khi đệ quy quá sâu để tránh O(N^2), và InsertionSort cho các đoạn mảng nhỏ). Ngoài ra, trình biên dịch C++ tối ưu hóa mã nguồn rất tốt nên đạt hiệu năng cao nhất.`n`n")

    # Section IV
    $selection.Font.Size = 14
    $selection.Font.Bold = $true
    $selection.Font.Color = 8274731
    $selection.TypeText("IV. KẾT LUẬN`n")
    $selection.Font.ColorIndex = 1
    $selection.Font.Size = 12.5
    $selection.Font.Bold = $false
    $selection.TypeText("1. Hàm sort của C++ là lựa chọn tốt nhất và tiện lợi nhất khi làm việc thực tế nhờ được tối ưu toàn diện.`n")
    $selection.TypeText("2. QuickSort nếu chọn pivot hợp lý (ở giữa mảng) là thuật toán tự cài đặt nhanh nhất trong các thuật toán thông dụng.`n")
    $selection.TypeText("3. MergeSort chạy ổn định, phù hợp khi cần bảo toàn trật tự ban đầu của các phần tử bằng nhau.`n")
    $selection.TypeText("4. HeapSort đảm bảo O(N log N) lý thuyết và tiết kiệm bộ nhớ, nhưng thực tế chạy chậm hơn trên mảng lớn do hạn chế về truy xuất bộ nhớ.`n`n")

    # Section V
    $selection.Font.Size = 14
    $selection.Font.Bold = $true
    $selection.Font.Color = 8274731
    $selection.TypeText("V. THÔNG TIN CHI TIẾT – LIÊN KẾT GITHUB`n")
    $selection.Font.ColorIndex = 1
    $selection.Font.Size = 12.5
    $selection.Font.Bold = $false
    $selection.TypeText("Toàn bộ mã nguồn, dữ liệu thử nghiệm và file báo cáo được lưu trữ công khai tại GitHub:`n")
    
    $selection.Font.Bold = $true
    $selection.Font.Underline = 1
    $selection.Font.Color = 16737792 # Blue
    $selection.TypeText("Link GitHub: https://github.com/username/IT003-Sorting-Benchmark`n")
    $selection.Font.Underline = 0
    $selection.Font.ColorIndex = 1
    $selection.Font.Bold = $false
    $selection.Font.Italic = $true
    $selection.TypeText("(Sinh viên thay thế đường dẫn trên bằng link GitHub cá nhân sau khi tạo repo)`n`n")
    $selection.Font.Italic = $false

    $selection.TypeText("Cấu trúc repository trên GitHub:`n")
    $selection.TypeText("• BaoCao_ThucNghiem_Sorting.pdf / .docx: Báo cáo kết quả thử nghiệm.`n")
    $selection.TypeText("• src/: Chứa mã nguồn các thuật toán (quicksort.cpp, heapsort.cpp, mergesort.cpp, std_sort.cpp, benchmark_all.cpp).`n")
    $selection.TypeText("• data/: Chứa mã nguồn sinh 10 bộ dữ liệu (generate_data.cpp).`n")
    $selection.TypeText("• scripts/: Script Python vẽ biểu đồ (plot_chart.py).`n")
    $selection.TypeText("• report/: File ảnh biểu đồ và bảng kết quả (chart.png, results.csv).`n")

    # Save to both locations
    $doc.SaveAs2($docxPathDownloads, 16) # 16 = wdFormatXMLDocument (.docx)
    $doc.SaveAs2($docxPathProject, 16)
    $doc.Close()
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null

    Write-Host "XUAT FILE WORD THANH CONG:"
    Write-Host "- " $docxPathDownloads
    Write-Host "- " $docxPathProject
} catch {
    Write-Host "Loi tao Word: " $_.Exception.Message
}
