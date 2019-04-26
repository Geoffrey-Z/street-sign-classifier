# Street Sign Classifier Report - Update

This notebook is an update to the [original project report](https://github.com/Hopding/street-sign-classifier/blob/master/notebooks/report.ipynb)

## Original Model

The model documented in the original report was a very simple one. It only had a single convolutional layer. This model achieved an accuracy of 95-96% with a ~0.15 loss on the test dataset.

## VGG19 Model

I was able to achieve an accuracy of 97-98% with a ~0.11 loss on the test dataset using an improved model. This model utilizes tranfer learning and early stopping to improve its accuracy.

The initial layers of the network are copied from the VGG19 network. The weights of the bottom seven layers are frozen. A single convolutional layer and a couple of dense layers are stacked on top of this. These layers are not frozen during training.

Shown below is a plot of the improved model's accuracy on the training and validation datasets per epoch during training.
<img src="assets/final-accuracy-per-epoch.png" width="400" style="margin: 15px">

Shown below is a plot of the improved model's loss on the training and validation datasets per epoch during training.
<img src="assets/final-loss-per-epoch.png" width="400" style="margin: 15px">

The improved model is available [here](https://github.com/Hopding/street-sign-classifier/blob/master/notebooks/final_model.ipynb)

## Image Augmentation

I also tried using image augmentation in the improved model. This, however, did not improve the accuracy. In fact, certain augmentation decreased the model's accuracy to as low as 90%. Listed below are the Keras [image transformations](https://keras.io/preprocessing/image/#imagedatagenerator-class) I tried, and their effects on the model's accuracy:

| Augmentation                         | Effect on Accuracy |
| ------------------------------------ | ------------------ |
| `featurewise_center=True`            | decreased          |
| `featurewise_std_normalization=True` | decreased          |
| `rotation_range=10`                  | decreased          |
| `width_shift_range=0.2`              | no effect          |
| `height_shift_range=0.2`             | no effect          |

The model I built using image augmentation is available [here](https://github.com/Hopding/street-sign-classifier/blob/master/notebooks/vgg19_augmentation_model.ipynb)
