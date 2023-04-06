from glob import glob
import numpy as np
import pandas as pd
classes = {'h'': 0,' 'hq': 1, 'q': 2, 'qh': 3, 'qy': 4, 'qz': 5, 'y': 6, 'yz': 7, 'z': 8, 'zy': 9}
classes_label = ['h','hq', 'q', 'qh', 'qy', 'qz', 'y', 'yz', 'z', 'zy']


def vote_csv(glob_files_1, glob_files_2, loc_outfile):
    with open(loc_outfile, "w") as outfile:
        acc_1 = np.zeros([10,1])
        with open(glob_files_1, "r") as f_1:
            lines = f_1.readlines()
            length_right = np.zeros([10,1])
            length_total = np.zeros([10,1])
            #print(length_right)
            for i in range(0, 10):
                length_right[i] = 0
                length_total[i] = 0
                acc_1[i] = 0
                for line in lines:
                    if line.strip().split("_")[0] ==classes_label[i]:
                        length_total[i] += 1
                        label = line.strip().split(",")[-1]
                        if int(label) == i:
                            length_right[i] += 1
                acc_1[i] = float(length_right[i])/float(length_total[i])
                print(f"{i}acc1: {acc_1[i]}")

        print('#####################\n\n\n\n')
        acc_2 = np.zeros([10,1])
        with open(glob_files_2, "r") as f_2:
            lines = f_2.readlines()
            length_right = np.zeros([10, 1])
            length_total = np.zeros([10, 1])
            #print(length_right)
            for i in range(0, 10):
                length_right[i] = 0
                length_total[i] = 0
                acc_2[i] = 0
                for line in lines:
                    if line.strip().split("_")[0] ==classes_label[i]:
                        length_total[i] += 1
                        label = line.strip().split(",")[-1]
                        if int(label) == i:
                            length_right[i] += 1
                if length_total[i] !=0:
                    acc_2[i] = float(length_right[i])/float(length_total[i])
                else:
                    print('ohno!')
                print(f"{i}acc2: {acc_2[i]}")

        print('#####################\n\n\n\n')
        acc_3 = np.zeros([10,1])
        for i in range(len(acc_1)):
            if acc_1[i] > acc_2[i]:
                acc_3[i] = acc_1[i]
            else:
                acc_3[i] = acc_2[i]
            print(f"{i}acc3: {acc_3[i]}")
        print("*"*10)
        print(f"average:{np.sum(acc_3)/10}")
    # submission = pd.DataFrame({"ID": _id, "Label": pred_list})
    # submission.to_csv(loc_outfile, index=False, header=False)


if __name__ == "__main__":
    vote_csv(
        glob_files_1="resnext101_32x32d_submission_test_2_new.csv",
        glob_files_2="mzj.csv",
        loc_outfile="test.csv"
    )
