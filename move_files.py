import shutil
import os

#MR
source1 = '/basket/junlin/CHAOS_CROPPED/MR'
dest1 = './datasets/MR2CT/train/A'
dest2 = './datasets/MR2CT/test/A'

subject = os.listdir(source1)

for s in subject[:16]:  #training
        files = os.listdir(os.path.join(source1,s))
        for f in files:
                if f.endswith(".h5") and f[:2] == 't1':
                        if not os.path.exists(os.path.join(dest1,f)):
                                shutil.move(os.path.join(source1,s,f), os.path.join(dest1,'sub'+s+'_'+f))

for s in subject[16:]:  #testing
        files = os.listdir(os.path.join(source1,s))
        for f in files:
                if f.endswith(".h5") and f[:2] == 't1':
                        if not os.path.exists(os.path.join(dest2, f)):
                                shutil.move(os.path.join(source1,s,f), os.path.join(dest2,'sub'+s+'_'+f))

#CT
source2 = '/basket/junlin/CHAOS_CROPPED/CT'
dest3 = './datasets/MR2CT/train/B'
dest4 = './datasets/MR2CT/test/B'

subject = os.listdir(source2)

for s in subject[:16]:  #training
        files = os.listdir(os.path.join(source2,s))
        for f in files:
                if f.endswith(".h5"):
                        if not os.path.exists(os.path.join(dest3, f)):
                                shutil.move(os.path.join(source2,s,f), os.path.join(dest3,'sub'+s+'_'+f))

for s in subject[16:]:  #testing
        files = os.listdir(os.path.join(source2,s))
        for f in files:
                if f.endswith(".h5"):
                        if not os.path.exists(os.path.join(dest4, f)):
                                shutil.move(os.path.join(source2,s,f), os.path.join(dest4,'sub'+s+'_'+f))