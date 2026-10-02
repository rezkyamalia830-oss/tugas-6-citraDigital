import cv2

img = cv2.imread("images/absent/absent 01.jpeg")

x = 158
y = 630
w = 348
h = 122

crop = img[y:y+h, x:x+w]

cv2.imwrite("output/tes_absent_roi.jpg", crop)

print("ROI berhasil disimpan.")
print("Buka: output/tes_absent_roi.jpg")