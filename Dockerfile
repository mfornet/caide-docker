FROM ubuntu
COPY cmd /home/cmd
COPY run.sh /home/run.sh
WORKDIR /home
RUN mkdir caide-tmp
RUN chmod +x run.sh
ENTRYPOINT ./run.sh
