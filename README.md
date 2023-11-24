# Whiz-Wit-Sleuth
No need to worry about the examination analysis, Whiz-Wit-Sleuth is here! All it takes is previous year examination pdf file, then it will do the analysis based on frequently asked questions and generate the output🕵️‍♂️🦉

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Recommended](#recommended)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Whiz-Wit-Sleuth is a playful Python script designed to extract high probability (important) questions from a PDF file. It utilizes the PyPDF2 library for reading PDFs and regular expressions to identify and extract questions based on question numbers.

## Features

- Extracts imp questions from a PDF file.
- Saves extracted questions to a text file.

## Getting Started

Follow these instructions to get Whiz-Wit-Sleuth up and running on your local machine.

### Recommended 

- Whiz-Wit-Sleuth works well on rgpv paper formate.
- If language other than 'English' is present in the pdf then ready to face annoying symbol (but it won't affect the english text), it may be some frustrations from Whiz-Wit...

### Prerequisites

- Python 3.x
- PyPDF2 library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MUKHTAR-02/Whiz-Wit-Sleuth.git

2. Install the required dependencies:
      ```bash
   pip install PyPDF2

## Usage

1. To use Whiz Wit Sleuth, run the script with the path to your PDF file as an argument:
   ```bash
   python whiz_wit_sleuth.py path/to/your/file.pdf
- This will generate a text file with the extracted questions.

## Example

import PyPDF2 <br>
import re <br>
from datetime import datetime <br>

... (your code here)

pdf_path = "path/to/your/file.pdf" <br>
pdf_text = extract_text_from_pdf(pdf_path) <br>
analyze_questions(pdf_text) <br>


## Contributing

- If you would like to contribute to this project, feel free to open an issue or submit a pull request we need more coders like you. Welcome!

## License

- This project is licensed under the <a href = "LICENSE"> MIT License</a>
- Feel free to suggest about more features and improvements.
