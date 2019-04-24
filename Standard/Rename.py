import os
path = 'D:\\MyFiles\\Downloads\\Pictures\\'
filenames = os.listdir(path)
print(filenames)
for file in filenames:
    i = 0
    images = os.listdir(format(path+str(file)))
    for image in images:
        src = os.path.join(os.path.abspath(path), format(str(file)), image)
        dst = os.path.join(os.path.abspath(path), format(
            str(file)) + '_' + format(str(i), '0>2s') + '.jpg')
        os.rename(src, dst)
        print('Converting %s to %s ...' % (src, dst))
        i = i + 1
