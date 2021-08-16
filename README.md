# anki-traditional

## About

A package to convert Anki decks (in `.anki2` format) to represent characters in
traditional Chinese characters.

## Setup

(assuming you're using Python 3.8.x)

First, create a virtual environment using `python3 -m venv venv`. Next, activate
it using `source venv/bin/activate`. Now, install the dependencies using
`pip install -r requirements.txt`. 

(you may use `python tradconv.py` as a sanity check
to see if things were installed correctly for the Hanzi converter.)

## Usage

Move your `.anki2` collection you want to bulk update into the root directory
of this project and run `python tradconv.py`.