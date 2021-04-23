#!/bin/bash
cp io/main.cpp .
./cmd -I /home/lib -- main.cpp 2> io/output.err
cp caide-tmp/result.cpp io
