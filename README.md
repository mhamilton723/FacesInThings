# Seeing Faces in Things: A Model and Dataset for Pareidolia

This repository contains a PyTorch DataLoader for the FacesInThings dataset, a collection of pareidolic face images (faces perceived in objects) annotated with bounding boxes and various attributes.

The dataset was introduced in the paper "Seeing Faces in Things: A Model and Dataset for Pareidolia", which studies the 
phenomenon of pareidolia from both human and computer vision perspectives. 
The dataset consists of ~5,000 images, each annotated with bounding boxes, 
perceived emotions, face types, and other characteristics.


## Installation

Clone the repository:

```bash
git clone https://github.com/your-repo/FacesInThingsLoader.git
```

Install the required Python dependencies:

```
pip install -r requirements.txt
```

## Usage
The dataset is downloaded automatically if not available locally.

See our [Demo Usage Notebook](Demo%20Usage.ipynb) for some quick examples of working with the dataset


## Dataset Structure

```
FacesInThings.zip
│
├── images/
│   ├── 000000009.jpg
│   ├── 000000027.jpg
│   ├── ...
│
└── metadata.csv
```

The `metadata.csv` file contains the following fields:

- `file`: Name of the image file.
- `url`: Direct URL to the image.
- `boxes`: Bounding boxes for the detected pareidolic faces. Stored in `[x1, y1, w, h]` format
- `is_primary`: Whether the bounding box is the primary face.
- `Is there a face?`: Yes/No/Several.
- `Hard to spot?`: Difficulty in spotting the face (Easy/Medium/Hard).
- `Accident or design?`: Whether the face appears accidental or by design.
- `Emotion?`: Perceived emotion (Neutral, Happy, Sad, etc.).
- `Person or creature?`: Type of face (Human, Animal, Alien, etc.).
- `Gender?`: Perceived gender (Neutral, Female, Male).
- `Amusing?`: Whether the face is amusing (Yes/No/Somewhat).
- `Common?:` How common this type of pareidolia is.
- `Flags`: Any additional flags (e.g., ‘Interesting’, ‘NSFW’).
- `num_boxes`: Number of bounding boxes.
- `train`: Whether the image is part of the training split.


## Citation
```
@inproceedings{hamilton2024faces,
  title={Seeing Faces in Things: A Model and Dataset for Pareidolia},
  author={Hamilton, Mark and Stent, Simon and others},
  booktitle={ECCV},
  year={2024}
}
```

