# NetNoise
This is code associated with the "Butterfly Effects in Perceptual Development" UROP Project.

## Download Cifar-10-C ##
Cifar10c is called in the file test.py. You need to ensure that Cifar10C is a folder that contains two files (the images and the labels, separately) and that folder is in the same directory as test.py. The dataset can be downloaded here: https://zenodo.org/record/2535967#.YoUYrhPMJ0s

It is 3 gB so can be worked with locally depending on storage.

## Setting up experiment ID ##

Run following command to create experiment ID files:

main.py --run=config --experiment_type=training

main.py --run=config --experiment_type=testing

main.py --run=config --experiment_type=activations

## Running Training ##

Then, run in shell:

sbatch train.sh

The models will be saved to the NetNoise/models directory. There will be 7 regimens for both the AlexNet implementation and the ResNet implementation.

## Run Testing ##

Then, run in shell:

sbatch test.sh

The experiment will run on both Cifar10 and Cifar10C. For Cifar10 testing, the result plot will automatically be saved to the results directory. For Cifar10C analysis, a CSV file will be saved for each architecture. 

## Run Analysis ##
Then, run in python:

cifar10c_analysis.py

Different features and statistical relationships can be examined in this script.

## Run Activations ##
If activations are desired for the experiment, run:

sbatch activate.sh

A partially working implementation of the code to establish invariance coefficients across regimens can be found here:
https://colab.research.google.com/drive/1rK33Z4K6zZA-oi7nglhx5cdV9k8l6Jen?pli=1&authuser=1#scrollTo=BgaoHTu1K9k2
This analysis was not included in the final report of this experiment.
