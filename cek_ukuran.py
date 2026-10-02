import cv2
from pathlib import Path

folder = Path("images/present")

for file in sorted(folder.glob("*")):
    img = cv2.imread(str(file))

    if img is not None:
        height, width = img.shape[:2]
        print(f"{file.name}: {width} x {height}")