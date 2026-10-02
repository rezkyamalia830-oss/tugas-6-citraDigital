# Deteksi Tanda Tangan pada Ijazah

## Deskripsi

Miniproject ini digunakan untuk mendeteksi keberadaan tanda tangan pada area tanda tangan ijazah.

Program melakukan pengolahan citra dengan beberapa tahap, yaitu:

1. Crop area tanda tangan (ROI)
2. Konversi citra menjadi grayscale
3. Global thresholding
4. Otsu thresholding
5. Morphological opening
6. Morphological closing
7. Menghitung jumlah piksel foreground
8. Menghitung foreground ratio
9. Menentukan apakah tanda tangan PRESENT atau ABSENT

## Dataset

Dataset terdiri dari 18 citra ijazah:

- 9 citra dengan tanda tangan (PRESENT)
- 9 citra tanpa tanda tangan (ABSENT)

Data digunakan untuk menguji kemampuan sistem dalam membedakan citra yang memiliki tanda tangan dan yang tidak memiliki tanda tangan.

## Metode Pengolahan

### 1. Crop ROI

Program mengambil area yang menjadi lokasi tanda tangan pada ijazah.

ROI digunakan agar proses analisis hanya dilakukan pada area yang relevan.

### 2. Grayscale

Citra hasil crop dikonversi menjadi grayscale agar proses thresholding dapat dilakukan berdasarkan intensitas keabuan.

### 3. Global Threshold

Global threshold menggunakan nilai threshold 127.

Piksel citra dikonversi menjadi piksel foreground dan background menggunakan threshold tersebut.

### 4. Otsu Threshold

Otsu threshold digunakan untuk menentukan nilai threshold secara otomatis berdasarkan distribusi intensitas citra.

Nilai threshold Otsu berbeda pada setiap citra.

### 5. Morphological Opening

Opening digunakan untuk mengurangi noise kecil pada hasil thresholding.

### 6. Morphological Closing

Closing digunakan setelah opening untuk membantu memperbaiki bagian foreground yang terputus.

### 7. Foreground Pixel

Jumlah piksel foreground dihitung dari hasil morphological closing.

Program juga menghitung foreground ratio:

```text
Foreground Ratio =
Foreground Pixels / Total Pixels

