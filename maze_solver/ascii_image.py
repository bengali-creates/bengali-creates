from PIL import Image
import numpy as np
from tkinter import filedialog


# Function to map pixel intensity to maze characters
def pixel_to_maze_char(pixel, threshold):
    """
    Maps a pixel intensity to '|' for walls and ' ' for paths based on the dynamic threshold.
    """
    return '|' if pixel < threshold else ' '

# Function to resize the image while maintaining its aspect ratio
def resize_image(image, new_width=50):
    """
    Resizes the image to a new width while preserving the aspect ratio.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to process the image and generate ASCII maze
def image_to_maze(image, new_width=50):
    """
    Converts a grayscale maze image into an ASCII maze using a dynamically calculated threshold.
    """
    # Convert image to grayscale
    grayscale_image = image.convert("L")
    
    # Resize the image
    resized_image = resize_image(grayscale_image, new_width)
    
    # Convert to numpy array for efficient processing
    pixel_array = np.array(resized_image)
    
    # Dynamically calculate the threshold (median intensity)
    threshold = np.median(pixel_array)
    print(f"Dynamic Threshold: {threshold}")  # Debugging threshold value
    
    # Map pixels to ASCII maze characters
    maze_data = ''.join(
        pixel_to_maze_char(pixel, threshold) for pixel in pixel_array.flatten()
    )
    
    # Format ASCII maze into rows
    maze_width = resized_image.width
    maze_text = '\n'.join(
        maze_data[i:i + maze_width] for i in range(0, len(maze_data), maze_width)
    )
    
    return maze_text

# Main function to run the program
def main():
    """
    Main function to load the maze image, convert it to ASCII, and save the output.
    """
    path = filedialog.askopenfilename(title="Select an image", filetypes=(("Image File", "*.png"),("all files", "*.*")))  # Path to the uploaded maze image
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Error opening the image: {e}")
        return

    # Generate ASCII maze
    new_width = 50  # Resize the maze to this width
    maze_text = image_to_maze(image, new_width=new_width)

    # Print and save the ASCII maze
    print(maze_text)
    with open("maze_ascii.txt", "w") as file:
        file.write(maze_text)

# Run the program
main()
