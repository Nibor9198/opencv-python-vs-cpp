
//#include "usr/local/include/opencv4/opencv2/core.hpp"

#include "opencv2/opencv.hpp"
#include "opencv2/core.hpp"
#include "opencv2/videoio.hpp"
#include "opencv2/highgui.hpp"
#include <opencv2/imgproc.hpp>

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;

int main(int, char**){
    std::cout << "Hello World!";

    Mat frame;
    VideoCapture cap;

    string deviceID = "footage.mp4";

    int apiID = cv::CAP_ANY;

    cap.open(deviceID, apiID);
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    cout << "Start grabbing" << endl;

    float camera_jaw = 0;
    float camera_pitch = 0;
    float camera_zoom = 4;

    double frame_width = cap.get(CAP_PROP_FRAME_WIDTH);
    double frame_height = cap.get(CAP_PROP_FRAME_HEIGHT);


    double output_height = 640;
    double output_width = 480;

    for (;;)
    {

        camera_jaw += 0.1;
        camera_pitch += 0.1;

        if(camera_pitch > 1){
            camera_pitch = 0;
        }

        cap.read(frame);

        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }

        Point center = Point(frame_width/2, frame_height/2);

        Mat matrix = getRotationMatrix2D(center, camera_jaw, 1.0);
        Mat rotated_frame = Mat::zeros( frame.rows, frame.cols, frame.type() );

        warpAffine(frame, rotated_frame, matrix, rotated_frame.size());

        Mat cropped_frame = Mat::zeros( frame.rows, frame.cols, frame.type() );
        Size zoom_size = Size(output_height * camera_zoom, output_width * camera_zoom);
        Point2f crop_position = Point2f(output_width * camera_zoom, output_height * camera_zoom);

        getRectSubPix(cropped_frame, zoom_size, crop_position, cropped_frame);

        Mat final_frame = Mat::zeros( output_height, output_width, frame.type() );

        resize(cropped_frame, final_frame, Size(output_height, output_width));
        if (waitKey(1) >= 0)
            break;
    }
    return 0;
}


