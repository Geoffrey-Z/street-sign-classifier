from skimage.data import imread
from os.path import join

from fs_utils import list_subdirs, list_files, PROJ_ROOT


def _load(data_dir):
    dataset = []
    for subdir in list_subdirs(data_dir):
        files = list_files(join(data_dir, subdir), ext='.ppm')
        for file_name in files:
            file_path = join(data_dir, subdir, file_name)
            dataset.append({
                'data': imread(file_path),
                'label': subdir
            })
    return dataset


def load_training():
    return _load(f'{PROJ_ROOT}/data/btsc/training/Training')


def load_testing():
    return _load(f'{PROJ_ROOT}/data/btsc/testing/Testing')


# dataset = load_training()
# print(dataset)
