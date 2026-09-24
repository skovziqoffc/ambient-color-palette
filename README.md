<img width="1366" height="768" alt="Screenshot (287)" src="https://github.com/user-attachments/assets/50c306d4-0263-4b9f-860b-ff17cc624674" />
# Ambient Color Palette 🎨

A lightweight Python desktop application that extracts dominant color palettes from any chosen portion of your computer screen using K-Means clustering.

## Features
- **Global Hotkey:** Trigger the application anywhere using `Ctrl + Shift + Q`.
- **Custom Screen Snipping:** Draw a bounding region around any element on your desktop.
- **K-Means Core Engine:** Automatically processes and classifies image data down into 5 dominant HEX colors.
- **Instant Copy:** Single-click any color element to immediately copy the HEX value to your system clipboard.

## How It Works
The engine uses **Pillow** to take an instantaneous snapshot of the selected bounding box, scales the array via **NumPy**, runs a **Scikit-Learn K-Means Clustering Algorithm** to find dominant cluster centroids, and renders the result dynamically in a custom **Tkinter** overlay frame.

## 🚀 Download Standalone Executable
If you just want to use the application without looking at the code, navigate to the **Releases** tab on the right side of this GitHub repository page and download `main.exe`.

## 🛠️ Developer Setup & Installation
If you want to run the raw Python source code locally or modify it:

### Prerequisites
- Python installed on your machine.

### Setup Instructions
1. **Clone the repository**

2. **Install dependencies**

3. **Run the application**

> ⚠️ **Note:** Because this app hooks into low-level Windows API inputs to listen for global hotkeys, it requires administrator privileges. When you launch the `.exe`, Windows will automatically present a standard User Account Control (UAC) prompt.
>
> ## 📦 Requirements
The application relies on the following open-source libraries (listed in `requirements.txt`):
- `numpy` - Vectorized pixel data manipulation
- `pillow` - High-performance screen capture
- `scikit-learn` - K-Means clustering algorithm implementation
- `keyboard` - Global low-level OS hotkey hooks
