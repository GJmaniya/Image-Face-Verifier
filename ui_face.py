import os
import shutil
from datetime import datetime
from deepface import DeepFace
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog
import threading


class FaceMatchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Matching Application")
        self.root.geometry("400x300")
        
        # Labels and Buttons
        self.label = tk.Label(self.root, text="Welcome to Face Matching Application", font=("Arial", 14))
        self.label.pack(pady=10)

        self.train_images_button = tk.Button(self.root, text="Select Training Images", command=self.select_train_images)
        self.train_images_button.pack(pady=5)

        self.test_folder_button = tk.Button(self.root, text="Select Test Folder", command=self.select_test_folder)
        self.test_folder_button.pack(pady=5)

        self.matched_folder_button = tk.Button(self.root, text="Select Matched Folder", command=self.select_matched_folder)
        self.matched_folder_button.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Face Comparison", command=self.start_face_comparison)
        self.start_button.pack(pady=20)

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.quit_button.pack(pady=5)

        # Variables to store the paths
        self.train_paths = []
        self.test_folder = ""
        self.matched_folder = ""

        # Date range check
        self.current_date = datetime.now().date()
        self.start_date = datetime(2024, 12, 6).date()
        self.end_date = datetime(2024, 12, 11).date()

        # Check date range on startup
        if not (self.start_date <= self.current_date <= self.end_date):
            messagebox.showerror("Error", "The application can only be run from December 6, 2024 to December 11, 2024.")
            self.root.quit()

    def select_train_images(self):
        file_paths = filedialog.askopenfilenames(title="Select Training Images", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.train_paths = list(file_paths)
        if file_paths:
            messagebox.showinfo("Selected Images", f"{len(file_paths)} training image(s) selected.")

    def select_test_folder(self):
        folder_path = filedialog.askdirectory(title="Select Test Folder")
        self.test_folder = folder_path
        if folder_path:
            messagebox.showinfo("Selected Folder", f"Test folder selected: {folder_path}")

    def select_matched_folder(self):
        folder_path = filedialog.askdirectory(title="Select Matched Folder")
        self.matched_folder = folder_path
        if folder_path:
            messagebox.showinfo("Selected Folder", f"Matched folder selected: {folder_path}")

    def compare_faces_with_multiple_train_images(self):
        try:
            if not self.train_paths or not self.test_folder or not self.matched_folder:
                messagebox.showerror("Error", "Please select all required paths before starting comparison.")
                return

            # Ensure the matched folder exists
            os.makedirs(self.matched_folder, exist_ok=True)

            match_count = 0
            for filename in os.listdir(self.test_folder):
                test_path = os.path.join(self.test_folder, filename)
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        # Check against all training images
                        for train_path in self.train_paths:
                            result = DeepFace.verify(img1_path=test_path, img2_path=train_path)
                            if result["verified"]:
                                match_count += 1
                                # Move matched file to the new folder
                                shutil.move(test_path, os.path.join(self.matched_folder, filename))
                                break  # Stop checking other train images for this test image
                    except Exception as e:
                        print(f"Error processing {test_path}: {e}")

            messagebox.showinfo("Comparison Complete", f"Number of matching photos: {match_count}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def start_face_comparison(self):
        # Check if current date is within the allowed period
        if not (self.start_date <= self.current_date <= self.end_date):
            messagebox.showerror("Error", "The application can only be run from December 6, 2024 to December 11, 2024.")
            return

        # Start comparison in a separate thread to avoid freezing the UI
        threading.Thread(target=self.compare_faces_with_multiple_train_images, daemon=True).start()


def run_app():
    root = tk.Tk()
    app = FaceMatchingApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
