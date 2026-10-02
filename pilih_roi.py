import cv2

# BACA GAMBAR

img = cv2.imread("images/present/ijazah 01.jpg")

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

original_h, original_w = img.shape[:2]

print("Ukuran gambar asli:")
print(f"width  = {original_w}")
print(f"height = {original_h}")



max_width = 1200
max_height = 700

scale = min(
    max_width / original_w,
    max_height / original_h,
    1
)

preview_w = int(original_w * scale)
preview_h = int(original_h * scale)

preview = cv2.resize(
    img,
    (preview_w, preview_h)
)


roi = cv2.selectROI(
    "Pilih Area Tanda Tangan",
    preview,
    showCrosshair=True,
    fromCenter=False
)

x, y, w, h = roi


x_original = int(x / scale)
y_original = int(y / scale)
w_original = int(w / scale)
h_original = int(h / scale)


print()
print("===================================")
print("KOORDINAT GAMBAR ASLI")
print("===================================")

print(f"x      = {x_original}")
print(f"y      = {y_original}")
print(f"width  = {w_original}")
print(f"height = {h_original}")



crop = img[
    y_original:y_original + h_original,
    x_original:x_original + w_original
]


cv2.imwrite(
    "output/roi_tanda_tangan.jpg",
    crop
)

print()
print("Crop disimpan:")
print("output/roi_tanda_tangan.jpg")


cv2.destroyAllWindows()