import cv2
import os

def split_video_to_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the base filename without extension
    file_name = os.path.splitext(os.path.basename(video_path))[0]

    # Read the video frames and save them as images
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        frame_filename = os.path.join(output_folder, f"{file_name}_frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    # Input video file path
    video_path = "path/to/your/video.mp4"

    # Output folder path (will be created if doesn't exist)
    output_folder = "path/to/output/folder"

    # Split video to frames
    split_video_to_frames(video_path, output_folder)
