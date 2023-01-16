import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.ttk
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

#window
root = tk.Tk()
root.title("Image Sequencer")

def browse(entry):
    # Open a file dialog and set the selected file/directory as the text in the entry widget
    file_path = tk.filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def generate_video():
    # Get the values from the Entry widgets
    image_folder = image_sequence_path.get()
    output_folder = output_directory_path.get()
    output_file_name_entry = output_file_name.get()
    output_file = os.path.join(output_folder, output_file_name_entry + ".mp4")
    fps = fps_entry.get()

    image_files = [os.path.join(image_folder, img)
                   for img in os.listdir(image_folder)
                   if img.endswith(".png")]

    if not image_folder:
        tk.messagebox.showerror("Error", "Please select an image sequence path")
        return
    if not output_folder:
        tk.messagebox.showerror("Error", "Please select an output directory")
        return
    if not output_file_name:
        tk.messagebox.showerror("Error", "Please enter an output file name")
        return
    if not fps:
        tk.messagebox.showerror("Error", "Please enter a value for FPS")
        return

    clip = ImageSequenceClip(image_files, fps=float(fps))
    total_frames = clip.fps * clip.duration

    def update_progress(current_frame):
        progress_bar["value"] = int(current_frame / total_frames * 100)
        root.update()

    for i, _ in enumerate(clip.iter_frames()):
        update_progress(i)

    clip.write_videofile(output_file, codec='libx264')


#widgets
image_sequence_path_label = tk.Label(root, text="Image Sequence Path:")
image_sequence_path = tk.Entry(root)
image_sequence_browse_button = tk.Button(root, text="Browse", command=lambda: browse(image_sequence_path))
output_directory_path_label = tk.Label(root, text="Output Directory:")
output_directory_path = tk.Entry(root)
output_directory_browse_button = tk.Button(root, text="Browse", command=lambda: browse(output_directory_path))
output_file_name_label = tk.Label(root, text="Output File Name:")
output_file_name = tk.Entry(root)
fps_label = tk.Label(root, text="FPS:")
fps_entry = tk.Entry(root)
progress_space = tk.Label(root, text="")
progress_label = tk.Label(root, text="Progress:")
progress_bar = tk.ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
generate_video_button_space = tk.Label(root, text="")
generate_video_button = tk.Button(root, text="Generate Video", command=generate_video)
bottom_space = tk.Label(root, text="")


#widget_layout
image_sequence_path_label.grid(row=0, column=0, sticky="W")
image_sequence_path.grid(row=0, column=1)
image_sequence_browse_button.grid(row=0, column=2)
output_directory_path_label.grid(row=1, column=0, sticky="W")
output_directory_path.grid(row=1, column=1)
output_directory_browse_button.grid(row=1, column=2)
output_file_name_label.grid(row=2, column=0, sticky="W")
output_file_name.grid(row=2, column=1)
fps_label.grid(row=3, column=0, sticky="W")
fps_entry.grid(row=3, column=1)
progress_space.grid(row=4, column=1)
progress_label.grid(row=5, column=0)
progress_bar.grid(row=5, column=1)
generate_video_button_space.grid(row=6, column=1)
generate_video_button.grid(row=7, column=1)
bottom_space.grid(row=8, column=1)

root.mainloop()