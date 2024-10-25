#!/usr/bin/env python
import os
import argparse
from PIL import Image

def resize_image(input_path, output_dir):
    # Open the original image
    original = Image.open(input_path)
    
    # Get the original size
    original_width, original_height = original.size

    # Get the base filename without the extension
    base_filename = os.path.splitext(os.path.basename(input_path))[0]

    # Define the scaling factors and corresponding output filenames
    scales = {
        '1x': (1/3, f"{base_filename}.png"),
        '2x': (2/3, f"{base_filename}@2x.png"),
        '3x': (1, f"{base_filename}@3x.png")
    }

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Resize and save the images
    for scale_name, (scale, output_filename) in scales.items():
        new_size = (int(original_width * scale), int(original_height * scale))
        resized_image = original.resize(new_size, Image.LANCZOS)
        resized_image.save(os.path.join(output_dir, output_filename))

    print(f"Images saved in {output_dir} directory.")

def main(args):
    input_file = os.path.realpath(args.input)
    output_directory = os.path.realpath(args.output)

    if not os.path.exists(input_file) or not input_file.lower().endswith('.png'):
        print(f"[Error] Invalid input file: {input_file}")
        return

    print(f"Processing image: {input_file}")
    resize_image(input_file, output_directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize a PNG image into 1x, 2x, and 3x versions.")
    parser.add_argument('input', help="Path to the input PNG image")
    parser.add_argument('output', help="Directory to save the resized images")
    
    args = parser.parse_args()
    main(args)
