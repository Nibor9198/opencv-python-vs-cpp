"""Filters a video stream.
"""
import cv2
import time

if __name__ == "__main__":
    print("Hello World")

    jaw_in, pitch_in, zoom_in = 0,0,4

    cap = cv2.VideoCapture('footage.mp4')
    cnt = 0  # Initialize frame counter

    # Some characteristics from the original video
    w_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    #frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # Croping values
    width = 640
    height = 480

    # The output, subject to change
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('result.avi', fourcc, fps, (width, height))

    if not cap.isOpened():
        print("Can't open input source")
        exit()

    while True:

        jaw_in += 0.1
        pitch_in += 0.1

        if pitch_in > 1:
            pitch_in = 0

        ret, frame = cap.read()  # Capture frame by frames
        cnt += 1  # Counting the frames

        # Avoid problems when video finish
        if not ret:
            break

        # Get rotation matrix
        matrix = cv2.getRotationMatrix2D((w_frame/2, h_frame/2), jaw_in, 1)
        # Aply rotation matrix
        rotated_frame = cv2.warpAffine(frame, matrix, (w_frame, h_frame))
        # Crop the frame
        crop_frame = cv2.getRectSubPix(rotated_frame, (int(width*zoom_in),
                                                        int(height*zoom_in)),
                                                        (w_frame/2, h_frame/2
                                                        - height*zoom_in/2
                                                        + pitch_in))
        # Resize the frame
        final_frame = cv2.resize(crop_frame, (width,height))

        #out.write(final_frame)
        #cv2.imshow('Cropped',final_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    #out.release()
    cv2.destroyAllWindows()
    print("Done")
