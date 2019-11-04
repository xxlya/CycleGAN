import glob
import random
import os

from torch.utils.data import Dataset
import h5py

class H5Dataset(Dataset):
    def __init__(self, root, transforms_=None, unaligned=False, mode='train'):
        self.unaligned = unaligned

        self.files_A = sorted(glob.glob(os.path.join(root, '%s/A' % mode) + '/*.*'))
        self.files_B = sorted(glob.glob(os.path.join(root, '%s/B' % mode) + '/*.*'))

    def __getitem__(self, index):
        f_A = h5py.File(self.files_A[index % len(self.files_A)],'r')
        item_A =f_A['in'].value.swapaxes(2,1).swapaxes(1,0)
        f_A.close()

        if self.unaligned:
            f_B = h5py.File(self.files_B[random.randint(0, len(self.files_B) - 1)],'r')
            item_B = f_B['ct'].value.swapaxes(2,1).swapaxes(1,0)
            f_B.close()
        else:
            f_B = h5py.File(self.files_B[index % len(self.files_B)],'r')
            item_B = f_B['ct'].value.swapaxes(2,1).swapaxes(1,0)
            f_B.close()

        return {'A': item_A, 'B': item_B}

    def __len__(self):
        return max(len(self.files_A), len(self.files_B))