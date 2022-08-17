import argparse
from genericpath import isdir
import matplotlib.pyplot as plt
import nibabel as nib
import os


def main(path):
    sub_dirs = os.listdir(path)
    for sub_dir in sub_dirs:
        if not os.path.isdir(f"{path}/{sub_dir}"):
            continue
        target = nib.load(f"{path}/{sub_dir}/fixed_image.nii.gz").dataobj
        source = nib.load(f"{path}/{sub_dir}/moving_image.nii.gz").dataobj
        pred = nib.load(f"{path}/{sub_dir}/pred_fixed_image.nii.gz").dataobj
        ddf = nib.load(f"{path}/{sub_dir}/ddf.nii.gz").dataobj
        mid_vol = target.shape[2] // 2

        plt.subplot(2, 2, 1)
        plt.imshow(target[:, :, mid_vol], cmap="gray")
        plt.subplot(2, 2, 2)
        plt.imshow(source[:, :, mid_vol], cmap="gray")
        plt.subplot(2, 2, 3)
        plt.imshow(pred[:, :, mid_vol], cmap="gray")
        plt.subplot(2, 2, 4)
        plt.imshow(ddf[:, :, mid_vol], cmap="gray")
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", help="Path", type=str)
    args = parser.parse_args()

    main(args.path)