import os
import shutil
from deepface import DeepFace
from PIL import Image

def get_multiple_paths(prompt):
    print(prompt)
    paths = []
    while True:
        path = input().strip()
        if not path:  # Break on empty input
            break
        paths.append(path)
    return paths

def compare_faces_with_multiple_train_images(train_paths, test_folder, matched_folder):
    try:
        # Validate the training images
        for train_path in train_paths:
            if not os.path.exists(train_path):
                print(f"Error: Training image not found: {train_path}")
                return
            try:
                img = Image.open(train_path)
                img.verify()
            except Exception as e:
                print(f"Error: Invalid training image: {train_path}. Error: {e}")
                return

        # Ensure the matched folder exists
        os.makedirs(matched_folder, exist_ok=True)

        # Count matching photos
        match_count = 0
        for filename in os.listdir(test_folder):
            test_path = os.path.join(test_folder, filename)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Check against all training images
                    for train_path in train_paths:
                        result = DeepFace.verify(img1_path=test_path, img2_path=train_path)
                        if result["verified"]:
                            match_count += 1
                            # Move matched file to the new folder
                            shutil.move(test_path, os.path.join(matched_folder, filename))
                            break  # Stop checking other train images for this test image
                except Exception as e:
                    print(f"Error processing {test_path}: {e}")

        print(f"Number of matching photos: {match_count}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    print("Welcome to the Face Matching Application!")
    print("This app is only testing Purpose and use only 7 days")
    # Collect training image paths from the user
    train_images = get_multiple_paths("Enter paths to images (one per line). Press Enter on an empty line when done:")

    # Collect test folder path
    print("Enter the path to the images Targeted folder:")
    test_folder = input().strip()

    # Collect matched folder path
    print("Enter the path to save matched images:")
    matched_folder = input().strip()

    # Run the comparison
    print("Starting face comparison...")
    compare_faces_with_multiple_train_images(train_images, test_folder, matched_folder)

if __name__ == "__main__":
    main()

