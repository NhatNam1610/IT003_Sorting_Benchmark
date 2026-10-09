$htmlPath = "C:\Users\LENOVO\.gemini\antigravity\scratch\IT003_Sorting_Benchmark\report\report.html"
$docxPath1 = "C:\Users\LENOVO\Downloads\BaoCao_ThucNghiem_Sorting.docx"
$docxPath2 = "C:\Users\LENOVO\.gemini\antigravity\scratch\IT003_Sorting_Benchmark\report\BaoCao_ThucNghiem_Sorting.docx"

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open($htmlPath)
    $doc.SaveAs2($docxPath1, 16) # 16 = wdFormatXMLDocument (.docx)
    $doc.SaveAs2($docxPath2, 16)
    $doc.Close()
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    Write-Host "Xuat file Word (.docx) thanh cong!"
} catch {
    Write-Host "Loi Word COM: " $_.Exception.Message
}
