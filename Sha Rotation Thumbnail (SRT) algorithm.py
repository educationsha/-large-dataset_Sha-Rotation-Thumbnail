# Sha Rotation Thumbnail (SRT) algorithm
# Pseudocode for proposed Sha Rotation Thumbnail (SRT) algorithm
# Input: Detected object bounding box (x, y, width, height), image I
# Initialize: Rotations = [0°, 90°, 180°, 270°]
# For each rotation R in Rotations
# Rotate image I by R degrees      
# Extract bounding box (x, y, width, height)
# Generate thumbnail T_R for rotated image
# Select thumbnail T with best bounding box alignment
# Return T
# Output: Correctly oriented thumbnail view
from PIL import Image
import os
import base64
from io import BytesIO
def generate_thumbnail(row):
    try:
       
        xmin, ymin, xmax, ymax = map(float, row[:4])
        image_path = row[7].strip()
        image_filename = os.path.basename(image_path)
        new_directory = 'C:\\Users\\dhaksha\\Downloads\\Sha_AL\\Desktop\\Found'
        new_path = os.path.join(new_directory, image_filename)
        best_thumbnail = None
        rotations = [0, 90, 180, 270]
        with Image.open(new_path) as image:
            for rotation in rotations:
                rotated_image = image.transpose(getattr(Image.Transpose, f"ROTATE_{rotation}"))
                cropped_image = rotated_image.crop((xmin, ymin, xmax, ymax))
                thumbnail = cropped_image.resize((100, 100))
                buffered = BytesIO()
                thumbnail.save(buffered, format='JPEG')
                base64_thumbnail = base64.b64encode(buffered.getvalue()).decode('utf-8')
                if best_thumbnail is None:
                    best_thumbnail = base64_thumbnail
        return f'<img src="data:image/jpeg;base64,{best_thumbnail}" />'
    except (ValueError, FileNotFoundError, OSError) as e:
        print(f"Error processing image for row: {row}\nError: {e}")
        return None
