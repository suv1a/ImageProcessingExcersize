# 영상 이어 붙이기 Stitcher 활용
import cv2
import sys

# 3장의 영상을 리스트로 묶어서 반복문으로 하나하나 갖고옴
#img_names = ['images/restaurant1.jpg', 'images/restaurant2.jpg']
img_names = ['images/Blender_Suzanne1.jpg', 'images/Blender_Suzanne2.jpg']

# 불러온 영상을 imgs에 저장
imgs = []
for name in img_names:
    img = cv2.imread(name)
    
    if img is None:
        print('Image load failed!')
        sys.exit()
        
    imgs.append(img)
    
# 객체 생성
stitcher = cv2.Stitcher_create()

# 이미지 스티칭
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('Stitch failed!')
    sys.exit()
    
#cv2.imwrite('output.jpg', dst)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()