from count_cubes import *
import numpy as np
from glob import glob

datapath = 'data/'

ground_truth = np.genfromtxt(datapath + 'ground_truth.csv', delimiter=',', dtype='int')
answer = dict([(item[0],(item[1], item[2])) for item in ground_truth])

score = 0
score_y = np.array([0, 0, 0])
score_g = np.array([0, 0, 0])

imgs = [f for f in glob(datapath+'*') if '.jpg' in f]

for f in imgs:
    i = int(f[-6:-4])
    img = cv2.imread(f,-1)

    num_yellow, num_green = count_cubes(img)

    if num_yellow == answer[i][0] and num_green == answer[i][1]:
        score += 1
        print("good")
    else:
        print("bad")
        cv2.waitKey(0)
    if num_yellow == answer[i][0]:
        score_y[1] += 1
    if num_yellow < answer[i][0]:
        score_y[0] += 1
    if num_yellow > answer[i][0]:
        score_y[2] += 1
    if num_green == answer[i][1]:
        score_g[1] += 1
    if num_green < answer[i][1]:
        score_g[0] += 1
    if num_green > answer[i][1]:
        score_g[2] += 1

print("Score: {}/{}".format(score, len(imgs)))
print(score_y)
print(score_g)
