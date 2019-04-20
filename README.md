# `street-sign-classifier`

This project fulfills the requirements for the [UMSL CS5390 project](https://github.com/badriadhikari/2019-Spring-DL/tree/master/project_guidelines). It implements a street sign classifier using deep learning.

## Report

The report for this project can be viewed [here](https://github.com/Hopding/street-sign-classifier/blob/master/notebooks/street_sign_classifier_report.ipynb).

## Quick Start

> **Note:** This section only works for Mac and Linux machines. If you are on Windows, you can try using the [WSL](https://docs.microsoft.com/en-us/windows/wsl/faq). Otherwise, use the [Slow Start](#slow-start) section instead.

To download the data and run the Jupyter notebooks for this project, run the following commands:

```bash
# Download street sign image dataset
./download_data.py

# Install dependencies
conda env create -f environment.yml

# Start the Jupyter Notebook server
./start
```

This should open the Jupyter file explorer in a new browser tab. Navigate to the `notebooks/` directory. From here, you can open and run the EDA (`btsc_dataset_eda.ipynb`) or Keras model (`keras_model.ipynb`) notebooks.

## Slow Start

Stuff and thingz...

## Download Datasets to `./data`

```bash
./download_data.py
```

## Start Jupyter in Virtual Environment

```bash
./start
```

## Conda Virtual Environment Commands

```bash
# Create the environment
conda env create -f environment.yml

# Update the environment
conda env update -f environment.yml

# Activate the environment
conda activate street-sign-classifier

# Search for dependency and version
conda search [dependency]

# Add a package to the environment
<Manually open the environment.yml and add it>

# Deactivate the environment
conda deactivate
```

## Datasets

- https://btsd.ethz.ch/shareddata/
- http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html

## References

- https://medium.com/@waleedka/traffic-sign-recognition-with-tensorflow-629dffc391a6
- https://towardsdatascience.com/image-classification-python-keras-tutorial-kaggle-challenge-45a6332a58b8
- https://medium.com/nybles/create-your-first-image-recognition-classifier-using-cnn-keras-and-tensorflow-backend-6eaab98d14dd
