import cv2
import os

def capture_screenshots(video_path, output_folder, num_screenshots=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = cv2.VideoCapture(video_path)

    # Get total number of frames
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the frames per second (fps) of the video
    fps = video.get(cv2.CAP_PROP_FPS)

    interval = total_frames // num_screenshots

    for i in range(num_screenshots):
        frame_number = i * interval
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        # Read the frame
        ret, frame = video.read()

        if ret:
            output_path = os.path.join(output_folder, f"screenshot_{i+1}.jpg")
            cv2.imwrite(output_path, frame)
        else:
            print(f"Failed to capture frame at {frame_number}")

    video.release()
    print(f"{num_screenshots} screenshots saved to {output_folder}")

