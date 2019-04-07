https://github.com/Hopding/street-sign-classifier

- https://medium.com/@waleedka/traffic-sign-recognition-with-tensorflow-629dffc391a6
- https://github.com/waleedka/traffic-signs-tensorflow/blob/master/notebook1.ipynb
- https://btsd.ethz.ch/shareddata/
- http://cvrr.ucsd.edu/LISA/lisa-traffic-sign-dataset.html

## Evaluation Criteria

https://github.com/badriadhikari/2019-Spring-DL/tree/master/project_guidelines

## Project Schedule Outline

| Week  | Date         | Todo                              | Status |
| ----- | ------------ | --------------------------------- | ------ |
| 1     | March 3      | Read requirements                 | ✅     |
|       |              | Decide on project                 | ✅     |
|       |              | Setup GitHub repo                 | ✅     |
|       |              | Create Todo outline               | ✅     |
|       |              | Install dependencies              | ✅     |
| **2** | **March 10** | Find street sign image dataset    | ✅     |
|       |              | Create script to download dataset | ✅     |
|       |              | Create scripts to load dataset    | ✅     |
|       |              | Plot dataset in Jupyter notebook  | ✅     |
| **3** | **March 17** | --------------------------------- |        |
| **4** | **March 24** | --------------------------------- |        |
| **5** | **March 31** | --------------------------------- |        |
| **6** | **April 7**  | Normalize image sizes             | ✅     |
|       |              | Create basic Keras model          | ✅     |
| **7** | **April 14** |                                   |        |
| **8** | **April 21** |                                   |        |
| **9** | **April 28** |                                   |        |

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

## Start Jupyter in Virtual Environment

```bash
./start
```

## Download Datasets to `./data`

```bash
./download_data.py
```
