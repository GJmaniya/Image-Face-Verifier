# Image-Face-Verifier
This Face Matching Application uses DeepFace to compare faces from a folder of test images against multiple training images. Matched images are moved to a specified folder. It validates inputs, restricts use to a set date range, and allows users to decide whether to continue or exit after each run.
# Overview
*FaceMatchTool* is a Python-based utility for face comparison using the DeepFace library. It allows users to compare images in a test folder against multiple training images to identify matches. Matched images are then moved to a specified folder for further use or organization. The application is designed for batch processing and is intuitive to use, offering features like validation of input images, error handling, and an interactive workflow.

*Features*
-->Multi-Image Training: Compare multiple training images against a folder of test images.
-->File Management: Automatically moves matched images to a designated folder.
-->Interactive User Workflow: Supports real-time user decisions to continue or exit the program.
-->Input Validation: Ensures training images are valid and accessible before proceeding.
-->Customizable Date Restriction: Configured to run within a specific date range (e.g., December 6–11, 2024 it is optional).
-->User-Friendly Prompts: Guides the user through providing paths for training images, test folders, and matched folders.

*How It Works*
1.Collect Input Paths: The user provides paths to training images, the test folder containing images to be checked, and a destination folder for matched images.
2.Validate Training Images: Ensures all training images are valid and readable.
3.Compare Faces: Uses DeepFace to compare faces in the test folder against the training images.
4.Match Handling: If a match is found, the matched image is moved to the specified folder, avoiding redundant checks.
5.Interactive Control: After processing, the user can choose to continue or exit using keyboard inputs (Enter to proceed, Esc to quit).

*Requirements*
Python 3.7+
Libraries:
os
shutil
datetime
DeepFace
PIL (Pillow)
keyboard
*Error Handling*
-->Invalid Image Paths: Alerts the user if training images are missing or unreadable.
-->Face Matching Errors: Logs specific errors during the face verification process.
-->Interactive Workflow: Allows the user to exit gracefully at any point.

*Future Enhancements*
-->Support for real-time logging of matched files.
-->Expanded date validation or removal for unrestricted usage.
-->Integration with cloud storage for input/output paths.
-->Support for additional face recognition backends
