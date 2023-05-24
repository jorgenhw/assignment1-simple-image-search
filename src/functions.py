#################### IMPORTS ####################
import os # For navigating directories
import cv2 # For image processing
import matplotlib.pyplot as plt # For plotting
import pandas as pd # For creating dataframes
from tqdm import tqdm # For progress bars


#################### FUNCTIONS ####################

# Function that loads an image and returns the image and the image path
def load_image(file_name):
    image_path = os.path.join("data", "flowers", file_name)
    flower_1 = cv2.imread(image_path)
    return flower_1, image_path

# Function that extracts the color histogram of an image and normalizes it using min-max normalization
def hist_and_normalize(image):
    """
    This function takes in an image and returns the normalized histogram of the image.
    : param image: image to be processed
    """
    # # First I'm extracing the histogram across all three channels of the image
    hist = cv2.calcHist([image], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])
    # # Then I'm normalizing the histogram
    min_max = cv2.normalize(hist, hist, 0, 1.0, cv2.NORM_MINMAX)
    return min_max

# Function that saves the histogram of an image to the out folder
def save_histogram(flower_1, flower_1_processed, image_path):
    # Extract the image name from the file path
    image_name = os.path.basename(image_path)
    # Split channels
    channels = cv2.split(flower_1)
    # Names of colors
    colors = ("b", "g", "r")
    # Create plot
    plt.figure()
    # Add title
    plt.title(f"Histogram of {image_name}")
    # Add xlabel
    plt.xlabel("Bins")
    # Add ylabel
    plt.ylabel("# of Pixels")

    # For every tuple of channel, color
    for (channel, color) in zip(channels, colors):
        # Create a histogram
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        # Plot histogram
        plt.plot(hist, color=color)
        # Set limits of x-axis
        plt.xlim([0, 256])
    
    # Save plot to the "output" folder
    output_path = os.path.join("out", f"{image_name}_histogram.png")
    plt.savefig(output_path)
    
    # Clear the plot
    plt.clf()
    plt.close()

# Function that returns a list of image paths in a folder
def get_image_paths(folder_path, image_extensions):
    """
    Get a list of all the image paths in the folder
    :param folder_path: The path to the folder containing the images
    :param image_extensions: A list of image extensions to include (e.g. ['.jpg', '.png', '.TIFF'])
    :return: A list of image paths
    """
    # Get a list of all the image paths in the folder
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                   if os.path.isfile(os.path.join(folder_path, f))
                   and os.path.splitext(f)[1].lower() in image_extensions]
    return image_paths

# Function that compares the histogram of an image to the histograms of all the images in a folder and returns a dataframe with the chi-squared distance between the histograms
def comparehistogram(image, image_list): # the input image_list should be a list of image paths
    """
    This function takes in an image and a list of images and returns a list of the chi-squared distance between the input image and the images in the list.
    : param image: image to be processed
    : param image_list: list of images to be compared to the input image
    """
    # Loading the reference image
    image_ref = cv2.imread(image)
    # First I'm extracting the histogram across all three channels of the image
    image_hist_ref = cv2.calcHist([image_ref], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])
    # Then I'm normalizing the histogram
    image_min_max_ref = cv2.normalize(image_hist_ref, image_hist_ref, 0, 1.0, cv2.NORM_MINMAX)
     # Create an empty list for the results
    result = []
    
    # Loop over the list of images
    for i in tqdm(image_list):
        if i == image:  # Skip the reference image
            continue
        # Load the current image
        image_cur = cv2.imread(i)
        # Extract the histogram across all three channels of the image
        image_hist = cv2.calcHist([image_cur], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
        # Normalize the histogram
        image_min_max = cv2.normalize(image_hist, image_hist, 0, 1.0, cv2.NORM_MINMAX)
        # Compute the chi-squared distance
        chi_squared_distance = round(cv2.compareHist(image_min_max_ref, image_min_max, cv2.HISTCMP_CHISQR), 2)
        # Append the image name and chi-squared distance to the results list
        result.append({'Image Name': os.path.basename(i), 'Chi-Squared Distance': chi_squared_distance})
    # Create a dataframe from the results list
    df = pd.DataFrame(result)

    # Sort the dataframe by the "Chi-Squared Distance" column in descending order
    df = df.sort_values(by='Chi-Squared Distance', ascending=True)
    
    # Save the dataframe as a CSV file in the "out" folder
    output_path = os.path.join("out", "chisquare_comparison.csv")
    df.to_csv(output_path, index=False)
    return df

# Function that outputs the top 5 images with the lowest chi-squared distance in a new pandas dataframe located in the out folder
def top5(df):
    """
    This function takes in a dataframe and returns a new dataframe with the top 5 images with the lowest chi-squared distance.
    : param df: dataframe to be processed
    """
    # Create a new dataframe with the top 5 images with the lowest chi-squared distance
    df_top5 = df.head(5)
    # Save the dataframe as a CSV file in the "out" folder
    output_path = os.path.join("out", "top5_most_similar_by_chisq.csv")
    df_top5.to_csv(output_path, index=False)
    return df_top5