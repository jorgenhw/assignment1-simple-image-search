<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Datascience 2023</h1> 
  <h2 align="center">Assignment 1: Building a simple image search algorithm</h2> 
  <h3 align="center">Visual Analytics</h3> 


  <p align="center">
    Jørgen Højlund Wibe<br>
    Student number: 201807750
  </p>
</p>
<br><br>

<!-- ABOUT THE PROJECT -->
## About the project
In this this assignment, we'll be using ```OpenCV``` to design a simple image search algorithm.

It involves loading an image, processing it by extracting the histogram and normalizing it, saving the histogram plot, comparing the histogram of the image to other images in a folder, and finding the top 5 most similar images.

## Assignment objectives
For this exercise, you should write some code which does the following:

- Define a particular image that you want to work with
- For that image
  - Extract the colour histogram using ```OpenCV```
- Extract colour histograms for all of the **other* images in the data
- Compare the histogram of our chosen image to all of the other histograms 
  - For this, use the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
- Find the five images which are most simlar to the target image
  - Save a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:


<!-- USAGE -->
## Usage

To use or reproduce the results you need to adopt the following steps.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.77.3 (Universal). The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment, install libraries and run the project.

1. Clone repository
2. Run setup.sh
   

### Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/AU-CDS/assignment3-pretrained-cnns-jorgenhw.git
cd assignment1-simple-image-search-jorgenhw
```

### Run ```setup.sh```

To replicate the results, I have included a bash script that automatically 

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
4. Runs the script
5. Deactivates the virtual environment

Run the code below in your bash terminal:

```bash
bash setup.sh
```

## Inspecting results

The results are saved in the ```out``` folder. The results are 1) a plot of the histogram of the chosen image (```image_0001.jpg_histogram.png```), 2) a .csv file containing the chi-squared distances from the reference image to all other images in the data folder (```chisquare_comparison.csv```) and 3) the top five most similar images to the reference image (```top5_most_similar_by_chisq.csv```).

<!-- REPOSITORY STRUCTURE -->
## Repository structure

This repository has the following structure:
```
│   main.py
│   README.md
│   requirements.txt
│   setup.sh
│
├───data
│       all images in .jpg
│
├───out
│       image_0001.jpg_histogram.png
│       chisquare_comparison.csv
│       top5_most_similar_by_chisq.csv
│
└──src
        functions.py
```

<!-- ABOUT THE DATA -->
## Data
The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).

## Final remarks / conclusion
In conclusion, this project successfully implemented a simple image search algorithm using OpenCV. The algorithm extracts color histograms from images, compares them using the chi-squared distance metric, and identifies the top 5 most similar images to a reference image.

The project demonstrates the application of image processing techniques for visual analytics, enabling users to analyze and compare images based on their color distributions. It can be used as a starting point for more complex image search algorithms or as a foundation for building image similarity systems in various domains.