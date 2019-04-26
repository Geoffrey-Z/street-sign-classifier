# `street-sign-classifier`

This project fulfills the requirements for [UMSL's CS5390 project](https://github.com/badriadhikari/2019-Spring-DL/tree/master/project_guidelines). It implements a street sign classifier using deep learning.

## Report

The original report for this project can be viewed [here](https://github.com/Hopding/street-sign-classifier/blob/master/notebooks/report.ipynb).

The update to the original report can be viewed [here](https://github.com/Hopding/street-sign-classifier/blob/master/notebooks/report_update.ipynb).

## Prerequisites

- This project uses [`conda`](https://conda.io/en/latest/) for package management. If you do not already have `conda` installed on your system, you can get it by installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/).
- This project is written in [Python 3.6](https://www.python.org/downloads/release/python-360/). Make sure you have this version of Python (or greater) installed on your system.

## Quick Start

> **Note:** This section only works for Mac and Linux machines. If you are on Windows, you can try using the [WSL](https://docs.microsoft.com/en-us/windows/wsl/faq). Otherwise, use the [Manual Start](#manual-start) section instead.

To automatically download the data and dependencies and run the Jupyter notebooks for this project, run the following command:

```bash
./start
```

This should open the Jupyter file explorer in a new browser tab. Navigate to the `notebooks/` directory. From here, you can open and run the EDA (`btsc_dataset_eda.ipynb`) or Keras model (`models/*.ipynb`) notebooks.

## Manual Start

1. Download image dataset:
   ```bash
   ./download_data.py
   ```
2. Create the virtual environment:
   ```bash
   conda env create -f environment.yml
   ```
3. Start the virtual environment:
   ```bash
   conda activate street-sign-classifier
   ```
4. Start the Jupyter notebook:
   ```bash
   jupyter notebook
   ```

## Command Reference

- **Download Data & Dependencies, and Start Jupyter**

  ```bash
  ./start # Only works on Mac and Linux machines
  ```

- **Download Datasets to `./data`**

  ```bash
  ./download_data.py
  ```

- **Start Jupyter**

  ```bash
  jupyter notebook
  ```

- **Conda Virtual Environment Commands**

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
- https://riptutorial.com/keras/example/32608/transfer-learning-using-keras-and-vgg
- https://stackoverflow.com/a/48286003
