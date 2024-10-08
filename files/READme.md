How to Execute:
1. **Download the .py file**
2. **Make the Script Executable (Linux/macOS)**: If you are using Linux or macOS, you may need to make the script executable by running:
   ```sh
   chmod +x remove_clouds_keep_green.py
   ```
3. **Run the Script from the Command Line**: You can run the script from the command line using the following command:
   ```sh
   python remove_clouds_keep_green.py <image_path> <output_path> [--cloud_threshold CLOUD_THRESHOLD] [--lower_green L_G S_G V_G] [--upper_green U_G S_G V_G]
   ```
   - `<image_path>`: The path to your input image file (e.g., `input_image.jpg`).
   - `<output_path>`: The path where you want to save the processed output image (e.g., `output_image.jpg`).
   - `--cloud_threshold` (optional): Threshold value for cloud removal (default is 170).
   - `--lower_green` (optional): Lower HSV values for green segmentation (default is 35, 10, 40).
   - `--upper_green` (optional): Upper HSV values for green segmentation (default is 115, 255, 255).

   **Example Command**:
   ```sh
   python remove_clouds_keep_green.py example.jpg output.jpg --cloud_threshold 170 --lower_green 35 10 40 --upper_green 115 255 255
   ```

   This command processes the input image (`example.jpg`) and saves the output to `output.jpg`.
