from skimage.transform import resize as skimage_resize  # pylint: disable=import-error
from sklearn.model_selection import train_test_split  # pylint: disable=import-error


def resize_image(image, size):
    return skimage_resize(image, (size, size), mode='constant', anti_aliasing=True)


def train_validation_test_split(X, y, random_state):
    X_train, X_rest, y_train, y_rest = train_test_split(
        X, y, test_size=0.4, random_state=random_state)

    X_validation, X_test, y_validation, y_test = train_test_split(
        X_rest, y_rest, test_size=0.5, random_state=random_state)

    return (X_train, X_validation, X_test, y_train, y_validation, y_test)
