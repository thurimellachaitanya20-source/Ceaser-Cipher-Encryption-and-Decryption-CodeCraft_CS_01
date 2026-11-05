# CodeCraft_CS_01
It's an encryption and decryption of text or sentences.

About: Caesar Cipher Implementation
This repository contains a complete implementation of the Caesar Cipher, one of the oldest and simplest encryption techniques. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions (the key) in the alphabet. The technique is famously named after Julius Caesar, who reportedly used it for his private correspondence.

Objective
The main objective of this project was to create a program capable of both encrypting and decrypting text using the Caesar Cipher algorithm.

Features
The program is designed to be user-friendly and fully functional:
Allows the user to input any message.
Accepts a shift value (key) from the user.
Performs either encryption or decryption based on the user's choice.
Handles a defined alphabet set that includes uppercase letters (A-Z) and various symbols (!@#$%^&*).

Algorithm Summary
The core logic follows these steps:

Input: The user provides the Mode (Encrypt/Decrypt), the Key (shift value), and the Message.

Processing: For every character in the message, the program finds its position in the defined alphabet.

Shifting:
For Encryption, the position is shifted a fixed number of positions to the right (forward) by the key.
For Decryption, the position is shifted a fixed number of positions to the left (backward) by the key.

Wrap-around: Modulo arithmetic is used to handle wrap-around, ensuring the shift loops back to the start of the alphabet when the shift exceeds the alphabet length.

Output: The final encrypted or decrypted message is returned to the user.

This project successfully demonstrates the fundamental principles of substitution ciphers and meets the requirements of implementing a fully functional Caesar Cipher.
