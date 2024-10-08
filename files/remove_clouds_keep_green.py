#!/usr/bin/env python3
import cv2
import numpy as np
from PIL import Image
import argparse
import os

def remove_cloud_reflectance_and_keep_green(image_path, output_path, cloud_threshold=170, lower_green=(35, 10, 40), upper_green=(115, 255, 255)):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to HSV color space to segment green areas
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Create a mask to keep only green areas
    green_mask = cv2.inRange(hsv_image, np.array(lower_green), np.array(upper_green))

    # Convert to grayscale for cloud detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Create a mask based on the cloud threshold
    _, cloud_mask = cv2.threshold(gray_image, cloud_threshold, 255, cv2.THRESH_BINARY)
    # Invert the cloud mask to target clouds
    cloud_mask = cv2.bitwise_not(cloud_mask)

    # Combine the green mask and the inverted cloud mask
    combined_mask = cv2.bitwise_or(green_mask, cloud_mask)

    # Apply the combined mask to the original image to keep non-cloud areas and green regions
    result = cv2.bitwise_and(image, image, mask=green_mask)

    # Convert the result to a PIL image
    result_pil = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    # Save the result image
    result_pil.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Remove cloud reflectance and retain green areas from drone images of water surfaces.")
    parser.add_argument('image_path', type=str, help="Path to the input image file.")
    parser.add_argument('output_path', type=str, help="Path to save the output image file.")
    parser.add_argument('--cloud_threshold', type=int, default=170, help="Threshold value for cloud removal (default: 170).")
    parser.add_argument('--lower_green', type=int, nargs=3, default=[35, 10, 40], help="Lower HSV values for green segmentation (default: 35 10 40).")
    parser.add_argument('--upper_green', type=int, nargs=3, default=[115, 255, 255], help="Upper HSV values for green segmentation (default: 115 255 255).")
    
    args = parser.parse_args()

    # Run the cloud removal and green retention process
    remove_cloud_reflectance_and_keep_green(
        args.image_path,
        args.output_path,
        cloud_threshold=args.cloud_threshold,
        lower_green=tuple(args.lower_green),
        upper_green=tuple(args.upper_green)
    )

    print(f"Processed image saved at: {args.output_path}")

if __name__ == "__main__":
    main()