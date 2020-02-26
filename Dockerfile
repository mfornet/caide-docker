FROM ubuntu
COPY caide /home/caide
COPY run.sh /home/run.sh
WORKDIR /home
RUN ./caide init
RUN ./caide problem basic
RUN mkdir io
RUN chmod +x run.sh
RUN echo "" > basic/basic.cpp
ENTRYPOINT ./run.sh
