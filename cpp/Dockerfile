FROM gcc:4.9

WORKDIR /opencv-test

COPY helloworld.cpp .

RUN g++ -o helloworld helloworld.cpp

CMD [ "./helloworld" ]