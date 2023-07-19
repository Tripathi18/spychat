# spychat

## Table of Content
- [Introduction](#Itroduction)
- [Prerequisites](#Prerequisties)
- [Usage](#Usage)
- [Additional Information](#Additional_Information)


## Introduction


This is a Python program that allows users to send and receive secret messages using steganography techniques. 
It provides a simple user interface for selecting friends, encoding messages within images, decoding messages from images, adding friends, and setting status.

## Prerequisites
To run this program, you need to have the following dependencies installed:


- `steganography` library
- `spydetails` module
- `datetime` module


You can install the `steganography` library using the following command:

pip install steganography


## Usage

1. Run the program by executing the Python script.


python my_first_program.py


2. The program will prompt you with various options:

   - Add a status
   - Add a friend
   - Send a message
   - Read a message
   - Exit


3. Follow the instructions provided by the program to perform the desired actions.

## Additional Information

- The program uses steganography techniques to hide messages within images. It encodes the messages by modifying the least significant bit of each pixel in the image.
- The program stores friend details, such as name, salutation, age, and rating, in the `friends` list.
- The `spydetails` module contains classes and functions related to spy details, including `spy`, `Spy`, and `chatmessage`.
- The program allows users to select friends, encode messages within images, decode messages from images, add friends, and set status.
- The status messages available for selection are: Sleeping, Available, Busy, and At Work.

Feel free to explore and modify the code to suit your needs!

Note: Please ensure that you have the necessary permissions to use and modify the images used in the program.

Enjoy using the program!


This is a basic template for your README file. 
Feel free to enhance it with additional information, installation instructions, examples, or any other details you deem necessary based on your project requirements
