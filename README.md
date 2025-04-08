# The Sha Rotation Thumbnail (SRT) Algorithm for Thumbnail Extraction in AI Output Report Generation: A Real-Time Focus Rotational Algorithm Enhancing AI Detection in UAV Imagery


<p align="center">
<img width="1000px" alt="SRT Workflow" src="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/dron_bac_removed.png">
</p>
<p align="center"><a href="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail">[<img src="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/thumbnails.bmp" width="20px"> Dataset Summary]</a> | <a href="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/Sha%20Rotation%20Thumbnail%20(SRT)%20algorithm.py">[🛠️ SRT Algorithm Code]</a> | <a href="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/Dataset_Enhancing%20Drone%20Object%20Detection%20Accuracy%20in%20Surveillance%20Real-Time%20Evaluation%20of%20YOLOv5%20and%20the%20New%20Sha%20Rotation%20Thumbnail%20Algorithm.xlsx">[📊 Dataset Excel]</a></p>
<p align="center">
  <a href="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/Dataset%20filelist"><b>Explore Dataset Filelist</b> 📂</a>
</p>
<hr>

## Aim of the SRT Algorithm

Object detection and localization are critical in real-time image processing for applications like autonomous navigation, surveillance, and AI-driven content extraction. However, traditional models like YOLOv5 often fail to generate accurate thumbnails due to misaligned bounding boxes, even when objects are correctly identified. To address this, we present the Sha Rotation Thumbnail Algorithm (SRT), which enhances alignment and orientation by rotating detected objects at 0°, 90°, 180°, and 270°. This approach ensures precise thumbnail generation, even for skewed or rotated objects. 

Using the DH Q4 drone equipped with RGB and IR sensors, 7,425 aerial images were captured, with 5,197 used for training and 1,114 for validation and testing. Performance analysis revealed that SRT significantly outperformed YOLOv5. SRT achieved a mean Precision of 0.919 (SD = 0.012) versus YOLOv5's 0.844 (SD = 0.013), Recall of 0.875 (SD = 0.011) compared to YOLOv5's 0.793 (SD = 0.014), and an F1-Score of 0.896 (SD = 0.010) against YOLOv5's 0.818 (SD = 0.012). Statistical tests confirmed these improvements, with t-statistics of 19.433 for Precision, 21.135 for Recall, and 23.284 for F1-Score (all p < .001). Levene's test indicated equal variances, supporting the robustness of the findings.

---

## Overview of the Dataset

<p align="center">
<img src="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/thumbnails.bmp" alt="Dataset Overview" width="70%">
</p>

The dataset comprises 7,425 drone-captured images with varying lighting conditions and object orientations:

- **Training Images**: 5,197
- **Validation and Testing Images**: 1,114 each

[Dataset Summary](https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/Dataset%20filelist) | [Download Excel Dataset](https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/Dataset_Enhancing%20Drone%20Object%20Detection%20Accuracy%20in%20Surveillance%20Real-Time%20Evaluation%20of%20YOLOv5%20and%20the%20New%20Sha%20Rotation%20Thumbnail%20Algorithm.xlsx)

---

## Key Features of the SRT Algorithm

<p align="center">
<img src="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/dron_bac_removed.png" alt="SRT Process" width="70%">
</p>

1. **Rotation-Based Alignment**: Applies rotations at 0°, 90°, 180°, and 270° to optimize object orientation.
2. **Integration with YOLOv5**: Designed to enhance post-detection accuracy without modifying the YOLOv5 model.
3. **Lightweight and Efficient**: Minimal computational overhead, suitable for real-time applications.

---

## Results and Performance Metrics

- **Precision**: Improved from 0.844 (YOLOv5) to 0.919 (SRT)
- **Recall**: Increased from 0.793 (YOLOv5) to 0.875 (SRT)
- **F1-Score**: Enhanced from 0.818 (YOLOv5) to 0.896 (SRT)

Statistical tests confirmed the significance of these improvements (all p < .001). 

---

## How to Use the SRT Algorithm

### Code for the Sha Rotation Thumbnail Algorithm:
[GitHub Link](https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/Sha%20Rotation%20Thumbnail%20(SRT)%20algorithm.py)

```python
from srt_algorithm import SRT

# Example usage
srt = SRT()
thumbnails = srt.generate_thumbnails(image, bounding_boxes)
```

---

## Visualization of Outputs

<p align="center">
<img src="https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail/blob/main/thumbnails.bmp" alt="Output Example" width="70%">
</p>

The generated thumbnails demonstrate superior alignment and orientation, satisfying real-world application needs.

This Excel document contains folder,	name,	size,	URL, and 	type.

