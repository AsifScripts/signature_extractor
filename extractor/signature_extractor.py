# extractor/signature_extraction.py
import cv2
from skimage import measure
import numpy as np
import os
from django.conf import settings  # <-- Add this

def extract_signatures(image_path):
    image = cv2.imread(image_path, 0)  # Read as grayscale
    _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)

    # Label connected components 
    labels = measure.label(binary, connectivity=2)
    mask = np.zeros(binary.shape, dtype="uint8")

    for label in np.unique(labels):
        if label == 0:
            continue
        
        labelMask = np.zeros(binary.shape, dtype="uint8")
        labelMask[labels == label] = 255
        
        numPixels = cv2.countNonZero(labelMask)
        if 500 < numPixels < 5000:  # Thresholds to tune
            mask = cv2.add(mask, labelMask)

    # Save extracted signature to media folder
    output_path = os.path.join(settings.MEDIA_ROOT, 'output_signature.png')
    cv2.imwrite(output_path, mask)

    # Return relative URL path for rendering in template
    return 'media/output_signature.png'
