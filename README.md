# nlp_toolbox
nlp_toolbox is an open-source GitHub repository that provides a collection of tools for natural language processing tasks. The repository provides functions for loading text from multiple sources such as the web and ebooks. Additionally, it includes functions for summarizing text, OCR, interacting with the OpenAI GPT API, and generating word clouds.

<div>
  <img src="https://img.shields.io/pypi/pyversions/nlp_toolbox?logoColor=brown&style=plastic" alt= "Version"/>
  <img src="https://img.shields.io/pypi/dm/nlp_toolbox" alt="Download Badge"/>
  <img src="https://img.shields.io/github/last-commit/thinh-vu/nlp_toolbox" alt="Commit Badge"/>
  <img src="https://img.shields.io/github/license/thinh-vu/nlp_toolbox?color=red" alt="License Badge"/>
</div>

# II. REFERENCES
## 2.1. How to use this package?
- Install the stable version: `pip install nlp_toolbox`
- You can install the latest `nlp_toolbox` version from source with the following command:
`pip install git+https://github.com/thinh-vu/nlp_toolbox.git@main`

_(*) You might need to insert a `!` before your command when running terminal commands on Google Colab._

- To start using functions, you need to import them: `from nlp_toolbox import *`

# III. DEPENDENCIES
## ChatGPT API
ChatGPT API simplifies NLP tasks by allowing you to send a request in a prompt format and receive a response without the need for dependent packages.

To send a request to ChatGPT API endpoint, you will need an OpenAI API key that can be obtained from [OpenAI](https://platform.openai.com/account/api-keys).

## spacy

Download pre-trained files using terminal.
```
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_sm
```

## pytesseract

<details>
  <summary> Quick installation guide </summary>

  **On Linux**

  ```
  sudo apt-get update
  sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
  ```
  **On Mac**
  `brew install tesseract`

  **On Windows**
  - Download binary from https://github.com/UB-Mannheim/tesseract/wiki. 
  - Add `pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'` to your script.
  - Install python package using pip:
  ```
  pip install tesseract
  pip install tesseract-ocr
  ```
</details>

Reference: [Installation guide](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- For Windows: Specific the location of the pytesseract by adding this code to your python project `pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mrthi\AppData\Local\Tesseract-OCR\tesseract.exe'`

- Add pre-trained languages data: 
  - Visit github and download the data file: [tessdata](https://github.com/tesseract-ocr/tessdata), eg: `vie.traineddata` for Vietnamese
  - Copy the downloaded file to the `tessdata` folder, Eg `C:\Users\YOUR-USER-NAME\AppData\Local\Tesseract-OCR\tessdata`

# IV. 🙋‍♂️ CONTACT INFORMATION
You can contact me at one of my social network profiles:

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/thinh-vu">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.messenger.com/t/mr.thinh.ueh">
    <img src="https://img.shields.io/badge/Messenger-00B2FF?style=for-the-badge&logo=messenger&logoColor=white" alt="Messenger Badge"/>
  <a href="https://www.youtube.com/channel/UCYgG-bmk92OhYsP20TS0MbQ">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  </a>
    <a href="https://github.com/thinh-vu">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github Badge"/>
  </a>
</div>

---

If you find value in my open-source projects and would like to support their development, you can donate via [Paypal](https://paypal.me/thinhvuphoto?country.x=VN&locale.x=en_US) or Momo e-wallet (VN). Your contribution will help me maintain my blog hosting fee and continue to create high-quality content. Thank you for your support!

![momo-qr](https://github.com/thinh-vu/vnstock/blob/main/src/momo-qr-thinhvu.jpeg?raw=true)
