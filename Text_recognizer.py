# from paddleocr import PaddleOCR
# from PIL import Image
# import numpy as np
#
# # Step 1: Load the image using PIL
# image_path = r"C:\Users\Admin\Desktop\sample_omr.jpg"
# pil_image = Image.open(image_path).convert('RGB')
#
# # Step 2: Convert PIL image to numpy array
# image_np = np.array(pil_image)
#
# # Step 3: Initialize PaddleOCR
# ocr = PaddleOCR( lang='en')
#
# # Step 4: Perform OCR on the numpy image
# results = ocr.ocr(image_np)
# print(results)
#
# # Step 5: Collect numbers and letters with their positions
# questions = []
# options = []
#
# for block in results[0]:
#     text = block[1][0].strip()
#     coords = block[0][0]  # top-left corner (x, y)
#
#     if text.isdigit():
#         questions.append((int(text), coords))
#     elif text.upper() in ['A', 'B', 'C', 'D']:
#         options.append((text.upper(), coords))
#
# # Step 6: Match numbers to closest option using X-axis only
# answer_map = {}
#
# for q_num, q_pos in questions:
#     min_x_diff = float('inf')
#     matched_opt = None
#
#     for opt_letter, opt_pos in options:
#         x_diff = abs(q_pos[0] - opt_pos[0])
#         if x_diff < min_x_diff:
#             min_x_diff = x_diff
#             matched_opt = opt_letter
#
#     if matched_opt:
#         answer_map[q_num] = matched_opt
#
# # Step 7: Print result
# answer_map = dict(sorted(answer_map.items()))
# print("📘 Extracted Answer Dictionary (X-axis based):")
# print(answer_map)


from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

# Step 1: Load image using PIL
image_path = r"C:\Users\Admin\Desktop\sample_omr_2.jpg"


image = Image.open(image_path).convert("RGB")
image_np = np.array(image)

# Initialize OCR
ocr = PaddleOCR( lang='en')  # no cls as you said

# Run OCR
results = ocr.ocr(image_np)

print(results[0]["rec_texts"])