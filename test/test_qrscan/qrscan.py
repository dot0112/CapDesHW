# import zxing

# reader = zxing.BarCodeReader()
# barcode = reader.decode("4.jpg")
# if barcode:
#     print(barcode.parsed)  # 인코딩된 문자열 출력

# import cv2

# detector = cv2.QRCodeDetector()

# image = cv2.imread("./3.jpg")
# retval, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(image)

# if retval:
#     # decoded_info는 리스트, 여러 QR코드 존재 가능
#     for i, qrData in enumerate(decoded_info):
#         if qrData:  # 빈 문자열이 있을 수도 있음
#             print(f"QR Code {i+1}: {qrData}")
# else:
#     print("QR 코드가 감지되지 않았습니다.")

from pyzbar.pyzbar import decode
import cv2

# 이미지 파일 경로
image_path = "4.jpg"

# 이미지 읽기 (OpenCV는 BGR 형식으로 불러옴)
image = cv2.imread(image_path)

# QR 코드 디코딩
decoded_objects = decode(image)

# 결과 출력
if decoded_objects:
    for obj in decoded_objects:
        print("QR Code Data:", obj.data.decode("utf-8"))
else:
    print("QR 코드가 감지되지 않았습니다.")
