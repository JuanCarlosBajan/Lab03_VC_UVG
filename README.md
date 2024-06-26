---
title: Image Filtering Project with U-Net and Perona-Malik Filter
author: Oscar Estrada, Sara Paguaga, Guillermo Santos & Juan Carlos Baján
date: 05/16/2024
output: Filtered images
---

# Image Filtering Project with U-Net and Perona-Malik Filter

This project implements a U-Net neural network for filtering grayscale images. We use the Perona-Malik anisotropic filter to create filtered images and train our neural network model.

## Description

The goal of this project is to build a U-Net to filter grayscale images. We use original images and their corresponding filtered images (using the Perona-Malik filter) to train the neural network.

## Project Structure

The project contains the following folders and files:

- `./Descargas_BSDS500/imgs`: Folder with the original images.
- `./Descargas_BSDS500/filtered`: Folder with the filtered images.
- `Anisotrópico.py`: Script to apply the Perona-Malik filter to the original images.
- `download_imgs.py`: Script to download the BSD500 database that was used in this proyect.
- `lab3.ipynb`: Jupyter notebook with the code to train the U-Net.
- `unet_model_2`: The model generated by the program. You can also try the first version atached in this repository.

## Requirements

To run this project, you need to have installed:

- Python 3.6+
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib
- scikit-image
- Jupyter Notebook

You can install the necessary packages using pip:

```bash
pip install tensorflow keras numpy matplotlib scikit-image jupyter
```

## Usage

1. **Download the image dataset**:
   Run `download_imgs.py` to download the image dataset used in this project.

2. **Apply the Perona-Malik filter to the original images**:
   Run `Anisotrópico.py` to convert the original images to filtered grayscale images and save them in the `filtered` folder.

3. **Train the U-Net**:
   Open and run the notebook `entrenamiento_unet.ipynb` in Jupyter. This notebook contains all the necessary code to:
   - Load the original and filtered images.
   - Create pairs of (x, y) windows from the images.
   - Build and train the U-Net model.
   - Visualize the results.

## Notes

- The results can significantly improve by increasing the number of windows and the window size k. In this project, we used a limited number of windows and a smaller k value due to available computational power limitations.
- Increasing these parameters in a higher-capacity computational environment can allow the model to capture more details and significantly improve performance.

## Results

Below is an example of the final result:

![Results](./final_output.png)
