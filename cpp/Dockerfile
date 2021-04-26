FROM opencvcourses/opencv-docker:latest

RUN cd /usr/local/lib/
RUN ldconfig -v

RUN cd /home
RUN mkdir code
WORKDIR /home/code

COPY helloworld.cpp .
COPY footage.mp4 .

RUN g++ -o helloworld helloworld.cpp -I/usr/local/include/opencv4/ -lopencv_core -lopencv_videoio -lopencv_highgui

CMD [ "./helloworld" ]