import cv2
import os

# Set the desired frame rate
desired_fps = 2

# Set the directory containing the videos
video_dir = 'trainingVideos/fight'

# Set the directory to save the frames
frames_dir = 'fightingFrames'

# Create the frames directory if it doesn't exist
os.makedirs(frames_dir, exist_ok=True)

# Keep track of the total number of frames
total_frames = 0

# Loop through the videos in the directory
for video_name in os.listdir(video_dir):
    if video_name.endswith('.mp4') or video_name.endswith('.avi'):
        video_path = os.path.join(video_dir, video_name)
        print(f"Processing video: {video_path}")

        # Open the video
        cap = cv2.VideoCapture(video_path)

        # Get the frame rate of the video
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(f"Frame rate of {video_path}: {fps} frames per second")

        # Calculate the delay between frames
        delay = int(1000 / desired_fps)  # Delay in milliseconds

        # Get the frame count
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Loop through the frames and save them
        for frame_idx in range(frame_count):
            ret, frame = cap.read()
            if ret:
                if frame_idx % (fps / desired_fps) == 0:  # Extract every (fps / desired_fps)-th frame
                    frame_path = os.path.join(frames_dir, f"frame_{total_frames}.jpg")
                    cv2.imwrite(frame_path, frame)
                    total_frames += 1
            else:
                break

            # Add a delay to control the frame rate
            cv2.waitKey(delay)

        # Release the video capture object
        cap.release()

print(f"Frame extraction completed. Total frames: {total_frames}")