from iou import *

bb_with_8_point = np.load('bb_with_8_point.npy', allow_pickle='TRUE').item()

frame_1 = bb_with_8_point[0]
frame_2 = bb_with_8_point[1]

for i in range(len(frame_1)):
    for j in range(len(frame_2)):
        box1 = frame_1[i]
        box2 = frame_2[j]
        
        # print(f"frame1 bb{i}", frame_1[i])
        # print(f"frame2 bb{j}", frame_2[j])
        print(calculate_iou(box1, box2))
