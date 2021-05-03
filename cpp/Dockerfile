FROM opencvcourses/opencv-docker:latest

RUN cd /usr/local/lib/
RUN ldconfig -v

RUN cd /home
RUN mkdir code
WORKDIR /home/code

COPY main.cpp .
COPY footage.mp4 .

RUN g++ -o main main.cpp -I/usr/local/include/opencv4/ -lopencv_core -lopencv_imgproc -lopencv_videoio -lopencv_highgui

CMD [ "./main" ]