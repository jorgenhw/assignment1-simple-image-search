import src.functions as func
import os

def main():
    # Loading image that I want to process
    print("Loading desired image...")
    flower_1, image_path = func.load_image("image_0001.jpg")
    print(f"SUCCESS: Image loaded from {image_path}")

    # Processing the image (extracting histogram and normalizing it)
    print("Processing the desired image...")
    flower_1_processed = func.hist_and_normalize(flower_1)
    print("SUCCESS: Image processed")

    # Saving the histogram plot of image_0001.jpg to the "out" folder
    print("Saving histogram plot of desired image to 'out' folder...")
    func.save_histogram(flower_1, flower_1_processed, image_path)
    print("SUCCESS: Histogram plot saved to 'out' folder")

    # Loading all images from the "data/flowers" folder
    print("Loading all images from the 'data/flowers' folder...")
    image_paths = func.get_image_paths(os.path.join("data","flowers"), [".jpg"])
    print("SUCCESS: All images loaded")

    # Comparing the histogram of image_0001.jpg to all the other images in the folder and saving these results in the 'out' folder
    print("Comparing the histogram of image_0001.jpg to all the other images in the folder and saving the results in the out folder...")
    df = func.comparehistogram(image_paths[0], image_paths)
    print("SUCCESS: Comparison complete")

    # Finding the top 5 most similar images to image_0001.jpg and saving this as a .csv file in output folder 
    print("Saving the top 5 most similar images to image_0001.jpg as a .csv file in out folder...")
    func.top5(df)
    print("SUCCESS: Top 5 most similar images saved as a .csv file in out folder")

    print("All done! :-)")

if __name__ == "__main__":
    main()