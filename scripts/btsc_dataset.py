from skimage.transform import resize as skimage_resize  # pylint: disable=import-error
from skimage.data import imread as skimage_read  # pylint: disable=import-error
from os.path import join

from fs_utils import list_subdirs, list_files, PROJ_ROOT


def _load(data_dir):
    dataset = []
    for subdir in list_subdirs(data_dir):
        files = list_files(join(data_dir, subdir), ext='.ppm')
        for file_name in files:
            file_path = join(data_dir, subdir, file_name)
            dataset.append({
                'data': skimage_read(file_path),
                'label': subdir
            })
    return dataset


def load_training():
    return _load(f'{PROJ_ROOT}/data/btsc/training/Training')


def load_testing():
    return _load(f'{PROJ_ROOT}/data/btsc/testing/Testing')


def resize_image(image, size):
    return skimage_resize(image, (size, size), mode='constant', anti_aliasing=True)
