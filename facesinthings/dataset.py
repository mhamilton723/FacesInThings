import os
import zipfile
import pandas as pd
import requests
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import json
import torch


class FacesInThings(Dataset):
    def __init__(self, root_dir, transform=None, download=True):
        self.root_dir = root_dir
        self.transform = transform
        self.path_to_dataset = os.path.join(self.root_dir, "FacesInThings")
        self.images_dir = os.path.join(self.path_to_dataset, 'images')
        self.metadata_file = os.path.join(self.path_to_dataset, 'metadata.csv')

        if download and not os.path.exists(self.path_to_dataset):
            print(f"Could not find dataset at {self.path_to_dataset}, downloading...")
            self._download_dataset()

        self.metadata = pd.read_csv(self.metadata_file)
        self.metadata["boxes"] = self.metadata["boxes"].apply(lambda s: json.loads(s))

    def _download_dataset(self):
        os.makedirs(self.root_dir, exist_ok=True)
        url = "https://aka.ms/faces-dataset"
        response = requests.get(url)
        zip_path = os.path.join(self.root_dir, 'FacesInThings.zip')

        with open(zip_path, 'wb') as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.root_dir)

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        img_name = os.path.join(self.images_dir, self.metadata.iloc[idx]['file'])
        image = Image.open(img_name).convert("RGB")

        if self.transform:
            image = self.transform(image)

        metadata_row = self.metadata.iloc[idx].to_dict()
        return image, metadata_row

    @classmethod
    def custom_collate(cls, batch):
        images = torch.stack([item[0] for item in batch])  # Batch the images
        metadata = [item[1] for item in batch]  # Keep metadata as is (list of dictionaries)
        return images, metadata


if __name__ == '__main__':
    import torchvision.transforms as transforms

    # Example usage
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    root_dir = 'data'
    dataset = FacesInThings(root_dir=root_dir, transform=transform, download=True)
    loader = DataLoader(dataset, batch_size=5, shuffle=False, collate_fn=dataset.custom_collate)

    for images, metadata in loader:
        print(metadata)  # metadata will be a list of dictionaries
        break
