CC=g++
SOURCE=main.cpp peks.cpp
DEPS=peks.h
EXECUTABLE=peks
CFLAG=-I /usr/local/include/pbc/
LDFLAGS=-Wl,-rpath /usr/include/ -lpbc -lssl -lcrypto -lgmp -lm


target:
	$(CC) $(SOURCE) -o $(EXECUTABLE) $(CFLAG) $(LDFLAGS)
