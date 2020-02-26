#!/bin/bash
cp io/main.cpp basic/main.cpp
./caide make 2> io/output.err
cp submission.cpp io
