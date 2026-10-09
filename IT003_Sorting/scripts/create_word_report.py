import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Đặt màu nền cho cell"""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Đặt khoảng cách đệm (padding) trong cell"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_report():
    doc = docx.Document()

    # Cấu hình lề trang A4 (2cm = 0.787 inch)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Đặt font chữ mặc định Times New Roman
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    # 1. HEADER
    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run1 = p_header.add_run("TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM\n")
    run1.font.size = Pt(13)
    run1.font.bold = True
    run1.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    run2 = p_header.add_run("MÔN HỌC: CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT (IT003) - LỚP: IT003.R17\n\n")
    run2.font.size = Pt(13)
    run2.font.bold = True
    run2.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    run3 = p_header.add_run("BÁO CÁO KẾT QUẢ THỬ NGHIỆM\n")
    run3.font.size = Pt(18)
    run3.font.bold = True
    run3.font.color.rgb = RGBColor(0xB3, 0x00, 0x00)

    run4 = p_header.add_run("Thời gian thực hiện: 01/10 – 10/10/2026\n")
    run4.font.size = Pt(11.5)
    run4.font.italic = True
    run4.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # 2. THÔNG TIN SINH VIÊN
    p_info = doc.add_paragraph()
    p_info.paragraph_format.space_before = Pt(8)
    p_info.paragraph_format.space_after = Pt(14)
    
    r = p_info.add_run("Sinh viên thực hiện: ")
    r.bold = True
    p_info.add_run("[Điền Họ và tên sinh viên]\n")

    r = p_info.add_run("Mã số sinh viên (MSSV): ")
    r.bold = True
    p_info.add_run("[Điền Mã số sinh viên]\n")

    r = p_info.add_run("Môi trường thử nghiệm: ")
    r.bold = True
    p_info.add_run("C++17 (Compiler MSVC/GCC - O2), CPU Intel Core, 16GB RAM, Windows 11\n")

    # 3. MỤC I
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(4)
    r = h1.add_run("I. NỘI DUNG VÀ MỤC TIÊU THỰC NGHIỆM")
    r.font.size = Pt(13.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.line_spacing = 1.25
    p_intro.add_run("Thực nghiệm nhằm đo đạc và đánh giá thời gian thực thi của 4 giải thuật sắp xếp: ")
    p_intro.add_run("QuickSort, HeapSort, MergeSort").bold = True
    p_intro.add_run(" và hàm ")
    p_intro.add_run("sort của C++ (std::sort)").bold = True
    p_intro.add_run(" trên 10 bộ dữ liệu số thực, mỗi bộ gồm ")
    p_intro.add_run("1.000.000 phần tử").bold = True
    p_intro.add_run(" (kiểu double):\n")
    p_intro.add_run("• Dãy 1: Đã có thứ tự tăng dần.\n")
    p_intro.add_run("• Dãy 2: Đã có thứ tự giảm dần.\n")
    p_intro.add_run("• Dãy 3 đến Dãy 10: Dữ liệu có thứ tự ngẫu nhiên.\n")

    # 4. MỤC II
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(12)
    h2.paragraph_format.space_after = Pt(4)
    r = h2.add_run("II. KẾT QUẢ THỬ NGHIỆM")
    r.font.size = Pt(13.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    h2_1 = doc.add_paragraph()
    h2_1.paragraph_format.space_before = Pt(4)
    h2_1.paragraph_format.space_after = Pt(6)
    r = h2_1.add_run("1. Bảng thời gian thực hiện (đơn vị: ms)")
    r.bold = True
    r.font.size = Pt(12)

    # Bảng số liệu: 12 hàng x 5 cột
    table_data = [
        ["Bộ Dữ liệu", "QuickSort", "HeapSort", "MergeSort", "sort (C++)"],
        ["1 (Tăng dần)", "13.0", "112.0", "25.0", "16.0"],
        ["2 (Giảm dần)", "14.0", "111.0", "33.0", "14.0"],
        ["3 (Ngẫu nhiên)", "64.0", "280.0", "96.0", "68.0"],
        ["4 (Ngẫu nhiên)", "73.0", "300.0", "111.0", "63.0"],
        ["5 (Ngẫu nhiên)", "65.0", "312.0", "98.0", "64.0"],
        ["6 (Ngẫu nhiên)", "70.0", "305.0", "96.0", "64.0"],
        ["7 (Ngẫu nhiên)", "67.0", "309.0", "95.0", "61.0"],
        ["8 (Ngẫu nhiên)", "69.0", "304.0", "93.0", "63.0"],
        ["9 (Ngẫu nhiên)", "67.0", "335.0", "96.0", "70.0"],
        ["10 (Ngẫu nhiên)", "65.0", "299.0", "90.0", "64.0"],
        ["Trung bình", "56.7", "266.7", "83.3", "54.7"]
    ]

    table = doc.add_table(rows=len(table_data), cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Thiết lập đường viền cho bảng
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        '<w:top w:val="single" w:sz="6" w:space="0" w:color="888888"/>'
        '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="888888"/>'
        '<w:left w:val="single" w:sz="6" w:space="0" w:color="888888"/>'
        '<w:right w:val="single" w:sz="6" w:space="0" w:color="888888"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        '</w:tblBorders>'
    )
    tblPr.append(borders)

    col_widths = [Inches(1.8), Inches(1.2), Inches(1.2), Inches(1.2), Inches(1.2)]

    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.width = col_widths[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=120, bottom=120, left=150, right=150)

            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(val)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(11)

            if r_idx == 0:
                set_cell_background(cell, "2B4C7E") # Xanh đậm
                run.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) # Chữ trắng
            elif r_idx == len(table_data) - 1:
                set_cell_background(cell, "EAF1FB") # Xanh nhạt highlight
                run.bold = True
                run.font.color.rgb = RGBColor(0x0B, 0x3D, 0x91)
            else:
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F9FBFD")
                if c_idx == 0:
                    run.bold = True

    # 5. BIỂU ĐỒ
    h2_2 = doc.add_paragraph()
    h2_2.paragraph_format.space_before = Pt(16)
    h2_2.paragraph_format.space_after = Pt(6)
    r = h2_2.add_run("2. Biểu đồ cột thời gian thực hiện")
    r.bold = True
    r.font.size = Pt(12)

    chart_path = os.path.join(os.path.dirname(__file__), "..", "report", "chart.png")
    if os.path.exists(chart_path):
        p_chart = doc.add_paragraph()
        p_chart.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_chart.paragraph_format.space_before = Pt(4)
        p_chart.paragraph_format.space_after = Pt(4)
        doc.add_picture(chart_path, width=Inches(6.2))

        p_caption = doc.add_paragraph()
        p_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_caption.paragraph_format.space_before = Pt(2)
        p_caption.paragraph_format.space_after = Pt(14)
        r = p_caption.add_run("Hình 1: Biểu đồ cột thời gian thực hiện (ms) trên 10 bộ dữ liệu và giá trị trung bình")
        r.font.size = Pt(10.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # 6. MỤC III
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(12)
    h3.paragraph_format.space_after = Pt(6)
    r = h3.add_run("III. NHẬN XÉT VÀ GIẢI THÍCH KẾT QUẢ")
    r.font.size = Pt(13.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    p_body = doc.add_paragraph()
    p_body.paragraph_format.line_spacing = 1.25
    p_body.add_run("Dựa trên bảng số liệu và biểu đồ thu được từ thực nghiệm trên 1.000.000 số thực, em rút ra các nhận xét sau:\n\n")

    # QuickSort
    r = p_body.add_run("1. Thuật toán QuickSort:\n")
    r.bold = True
    p_body.add_run("• Độ phức tạp: Trung bình là O(N log N), trường hợp xấu nhất là O(N^2).\n")
    p_body.add_run("• Kết quả trên dãy 1 (Tăng dần - 13.0 ms) và dãy 2 (Giảm dần - 14.0 ms): Khi cài đặt QuickSort theo bài giảng, chọn pivot là phần tử chính giữa mảng pivot = a[(left + right) / 2], trên mảng đã có thứ tự tăng dần hoặc giảm dần, phần tử chính giữa này chính là giá trị trung vị của dãy. Nhờ đó mảng được chia đôi rất cân bằng, không bị rơi vào trường hợp xấu nhất O(N^2) và không bị tràn ngăn xếp (Stack Overflow). Do các phần tử đã gần đúng vị trí nên số lần hoán đổi ít, giúp QuickSort chạy cực nhanh.\n")
    p_body.add_run("• Trên 8 dãy ngẫu nhiên: Thời gian dao động từ 64 ms đến 73 ms (trung bình 56.7 ms). Thuật toán hoạt động rất hiệu quả, tốc độ tương đương với hàm sort của C++.\n\n")

    # HeapSort
    r = p_body.add_run("2. Thuật toán HeapSort:\n")
    r.bold = True
    p_body.add_run("• Độ phức tạp: Luôn là O(N log N) trong mọi trường hợp, không dùng bộ nhớ phụ (O(1)).\n")
    p_body.add_run("• Hiệu năng thực tế: Chạy chậm nhất trong cả 4 thuật toán, trung bình mất 266.7 ms.\n")
    p_body.add_run("• Giải thích nguyên nhân: Cấu trúc cây Heap lưu trên mảng khiến các bước truy cập phần tử cha - con bị nhảy cách quãng xa (i -> 2i+1, 2i+2). Với mảng lớn 1 triệu phần tử, việc này gây ra nhiều hiện tượng Cache Miss (bộ nhớ đệm CPU không chứa sẵn dữ liệu), CPU phải tốn thời gian lấy dữ liệu từ RAM nên tốc độ thực tế bị chậm hơn.\n\n")

    # MergeSort
    r = p_body.add_run("3. Thuật toán MergeSort:\n")
    r.bold = True
    p_body.add_run("• Độ phức tạp: Luôn là O(N log N) trong mọi trường hợp, có tính ổn định (Stable Sort).\n")
    p_body.add_run("• Hiệu năng thực tế: Thời gian trung bình là 83.3 ms, đứng thứ 3 sau sort C++ và QuickSort. Trên dãy tăng dần (25.0 ms) và giảm dần (33.0 ms), MergeSort chạy nhanh hơn mảng ngẫu nhiên (khoảng 90 - 111 ms).\n")
    p_body.add_run("• Đặc điểm: MergeSort cần mảng tạm kích thước O(N) để trộn hai nửa mảng lại với nhau.\n\n")

    # sort C++
    r = p_body.add_run("4. Hàm sort của C++ (std::sort):\n")
    r.bold = True
    p_body.add_run("• Hiệu năng thực tế: Chạy nhanh nhất tổng thể với thời gian trung bình 54.7 ms.\n")
    p_body.add_run("• Giải thích: Hàm sort trong thư viện <algorithm> của C++ sử dụng thuật toán Introsort (kết hợp thông minh giữa QuickSort, HeapSort khi đệ quy quá sâu để tránh O(N^2), và InsertionSort cho các đoạn mảng nhỏ). Ngoài ra, trình biên dịch C++ tối ưu hóa mã nguồn rất tốt nên đạt hiệu năng cao nhất.\n\n")

    # 7. MỤC IV
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(12)
    h4.paragraph_format.space_after = Pt(6)
    r = h4.add_run("IV. KẾT LUẬN")
    r.font.size = Pt(13.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    p_kl = doc.add_paragraph()
    p_kl.paragraph_format.line_spacing = 1.25
    p_kl.add_run("1. Hàm sort của C++ là lựa chọn tốt nhất và tiện lợi nhất khi làm việc thực tế nhờ được tối ưu toàn diện.\n")
    p_kl.add_run("2. QuickSort nếu chọn pivot hợp lý (ở giữa mảng) là thuật toán tự cài đặt nhanh nhất trong các thuật toán thông dụng.\n")
    p_kl.add_run("3. MergeSort chạy ổn định, phù hợp khi cần bảo toàn trật tự ban đầu của các phần tử bằng nhau.\n")
    p_kl.add_run("4. HeapSort đảm bảo O(N log N) lý thuyết và tiết kiệm bộ nhớ, nhưng thực tế chạy chậm hơn trên mảng lớn do hạn chế về truy xuất bộ nhớ.\n\n")

    # 8. MỤC V
    h5 = doc.add_paragraph()
    h5.paragraph_format.space_before = Pt(12)
    h5.paragraph_format.space_after = Pt(6)
    r = h5.add_run("V. THÔNG TIN CHI TIẾT – LIÊN KẾT GITHUB")
    r.font.size = Pt(13.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    p_git = doc.add_paragraph()
    p_git.paragraph_format.line_spacing = 1.25
    p_git.add_run("Toàn bộ mã nguồn, dữ liệu thử nghiệm và file báo cáo được lưu trữ công khai tại GitHub:\n")

    r_link = p_git.add_run("Link GitHub: https://github.com/username/IT003-Sorting-Benchmark\n")
    r_link.bold = True
    r_link.font.color.rgb = RGBColor(0x00, 0x66, 0xCC)
    r_link.underline = True

    r_note = p_git.add_run("(Sinh viên thay thế đường dẫn trên bằng link GitHub cá nhân sau khi tạo repo)\n\n")
    r_note.italic = True

    p_git.add_run("Cấu trúc repository trên GitHub:\n")
    p_git.add_run("• BaoCao_ThucNghiem_Sorting.pdf / .docx: Báo cáo kết quả thử nghiệm.\n")
    p_git.add_run("• src/: Chứa mã nguồn các thuật toán (quicksort.cpp, heapsort.cpp, mergesort.cpp, std_sort.cpp, benchmark_all.cpp).\n")
    p_git.add_run("• data/: Chứa mã nguồn sinh 10 bộ dữ liệu (generate_data.cpp).\n")
    p_git.add_run("• scripts/: Script Python vẽ biểu đồ (plot_chart.py).\n")
    p_git.add_run("• report/: File ảnh biểu đồ và bảng kết quả (chart.png, results.csv).\n")

    # Lưu file Word
    out_downloads = r"C:\Users\LENOVO\Downloads\BaoCao_ThucNghiem_Sorting.docx"
    out_project = os.path.join(os.path.dirname(__file__), "..", "report", "BaoCao_ThucNghiem_Sorting.docx")

    doc.save(out_downloads)
    doc.save(out_project)

    print("Da tao xong file Word tai:")
    print("1.", out_downloads)
    print("2.", out_project)

if __name__ == "__main__":
    create_report()
