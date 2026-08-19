# Rotation-Aware UAV Object Detection and Thumbnail Extraction (SRT)

**Sha Rotation Thumbnail (SRT)** is a lightweight rotation-aware post-processing approach for generating consistently oriented object thumbnails from UAV imagery after object detection.

The project investigates whether evaluating detected regions across **0°, 90°, 180°, and 270° rotations** can improve the alignment and presentation of detected objects in automated AI output reports.

> **Research artifact:** This repository contains the implementation and experimental material associated with the SRT research work. Reported performance values should be interpreted in the context of the documented dataset, experimental protocol, and baseline comparison.

## Research Problem

Object detectors such as YOLOv5 can localize an object successfully while the extracted thumbnail remains poorly oriented or visually misaligned. This is particularly relevant to aerial imagery, where object orientation, camera viewpoint, and scene geometry can vary substantially.

SRT addresses the **thumbnail extraction and orientation problem after detection**, rather than modifying the underlying YOLOv5 detector architecture.

## Proposed Approach

The SRT workflow is conceptually:

```text
UAV Image
   │
   ▼
Object Detection (e.g., YOLOv5)
   │
   ▼
Detected Bounding Box
   │
   ├── 0° rotation
   ├── 90° rotation
   ├── 180° rotation
   └── 270° rotation
   │
   ▼
Candidate Object Thumbnails
   │
   ▼
Orientation / Alignment Selection
   │
   ▼
Final Thumbnail
```

The repository's current implementation provides the rotation-and-cropping prototype used for the experimental workflow. The selection criterion should be treated as an area for further engineering/reproducibility work because the prototype currently initializes a candidate and does not implement a quantitative alignment score.

## Dataset

The experimental work described in the accompanying research material uses **7,425 UAV aerial images** captured using a DH Q4 drone equipped with RGB and IR sensing.

Reported split:

| Split | Images |
|---|---:|
| Training | 5,197 |
| Validation | 1,114 |
| Testing | 1,114 |
| **Total** | **7,425** |

The dataset contains variation in lighting conditions and object orientations.

> **Dataset note:** Do not assume that the full source imagery is redistributed by this repository. Use the included dataset/file-list material to determine what is actually available for reproduction.

## Reported Results

The research material reports the following comparison with a YOLOv5 baseline:

| Metric | YOLOv5 | SRT | Improvement |
|---|---:|---:|---:|
| Precision | 0.844 | **0.919** | +0.075 |
| Recall | 0.793 | **0.875** | +0.082 |
| F1-score | 0.818 | **0.896** | +0.078 |

Reported variability:

- SRT Precision: **0.919 ± 0.012**
- SRT Recall: **0.875 ± 0.011**
- SRT F1-score: **0.896 ± 0.010**

The accompanying research analysis reports statistical tests with **p < 0.001** for the Precision, Recall, and F1-score comparisons.

### Interpretation

The reported results indicate that the SRT workflow improved the evaluated metrics relative to the stated YOLOv5 baseline under the experimental setup. These values are **reported experimental results**, not a claim that SRT universally improves every object-detection task.

## Key Contributions

1. **Rotation-aware thumbnail extraction** using four right-angle orientations.
2. **Detector-independent post-processing concept** that can be applied after object detection.
3. **Lightweight implementation** based on image transformation and cropping.
4. **UAV-focused evaluation** using a large aerial-image collection.
5. **Quantitative comparison** against a YOLOv5 baseline.

## Implementation

The main prototype is:

`Sha Rotation Thumbnail (SRT) algorithm.py`

It uses Python and Pillow to:

1. Read bounding-box coordinates.
2. Load the corresponding image.
3. Generate 0°, 90°, 180°, and 270° rotated views.
4. Crop the detected region.
5. Resize the crop to a thumbnail.
6. Encode the resulting thumbnail as JPEG/Base64 for report generation.

### Current prototype limitations

The current script contains experiment-specific configuration, including a local Windows image directory. It should therefore be treated as a **research prototype rather than a plug-and-play package**.

For a reproducible release, the next engineering version should:

- replace hard-coded paths with command-line/configuration arguments;
- implement an explicit quantitative alignment/quality score;
- select the best rotation based on that score rather than the first candidate;
- validate bounding-box coordinates after rotation;
- add automated tests;
- provide a requirements file and reproducible environment;
- separate dataset configuration from algorithm code.

## Example Workflow

```python
# Conceptual workflow
rotations = [0, 90, 180, 270]

for rotation in rotations:
    rotated_image = rotate(image, rotation)
    candidate = crop(rotated_image, bounding_box)
    score = alignment_score(candidate)

best_thumbnail = select_highest_scoring_candidate()
```

The code above illustrates the intended research workflow; the repository's existing Python script is the reference prototype.

## Repository Contents

Typical research artifacts include:

- SRT algorithm prototype
- UAV imagery / thumbnail examples
- Dataset file-list material
- Experimental dataset documentation
- Research visualizations
- Supporting spreadsheet material

## Research Context

This work sits at the intersection of:

- **UAV computer vision**
- **Object detection**
- **Aerial imagery analysis**
- **Rotation-aware image processing**
- **Edge/real-time AI**
- **Automated visual reporting**

## Reproducibility Checklist

Before reproducing the reported experiments, document:

- [ ] Dataset version and provenance
- [ ] Exact train/validation/test split
- [ ] YOLOv5 version and model variant
- [ ] Training hyperparameters
- [ ] Hardware and software environment
- [ ] Random seeds
- [ ] Evaluation procedure
- [ ] Statistical-test procedure
- [ ] SRT alignment-selection criterion

## Citation

If you use or discuss this implementation, please cite the associated research publication/patent where applicable.

```bibtex
@software{srt_uav_object_detection,
  author  = {Shahul Hameed C},
  title   = {Rotation-Aware UAV Object Detection and Thumbnail Extraction (SRT)},
  year    = {2026},
  url     = {https://github.com/educationsha/-large-dataset_Sha-Rotation-Thumbnail}
}
```

## Author

**Dr. Shahul Hameed C**  
AI Researcher & Engineer | Computer Vision | UAV Intelligence | Edge AI | Autonomous Systems

GitHub: https://github.com/educationsha

## License

No explicit open-source license is currently declared for this repository. If you intend external reuse, add an appropriate license and clarify the redistribution status of any datasets or third-party materials.
