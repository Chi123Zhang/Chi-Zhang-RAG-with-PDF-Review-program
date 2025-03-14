# RAG with PDF Review

## Overview
The project implements a **search-enhanced generation (RAG) system** in a large PDF dataset for **intelligent document retrieval, query processing, and automatic text highlighting**.
It integrates **natural language processing (NLP), information retrieval (IR), and optimization techniques** to achieve **high-performance, scalable, and accurate document search**.

## Key Features
- **High-performance document indexing** – Uses **vector-based storage (FAISS)** and **TF-IDF + cosine similarity** for **fast and scalable search operations**.
- **Query matching optimization** – Implements **OpenAI Embedding** to reduce retrieval errors and ensure **highly relevant text selection**.
- **Computational efficiency** – suitable for large-scale applications through the use of **vectorized search methods and threshold-based similarity scoring** to reduce redundant calculations.
- **Automatic text highlighting** – ensures accurate content extraction by dynamically identifying and highlighting **the most relevant passages**.
- **Scalable and extensible design** – modular architecture supports **multi-document retrieval, real-time deployment and API integration**.

## Technologies Used
- **PDF Parsing**: PyMuPDF (`fitz`) for extracting and highlighting text.
- **Vector Database**: OpenAI’s vector store and FAISS.
- **Embedding Model**: OpenAI's embedding API for query processing.
- **Text Matching**: Uses **TF-IDF + Cosine Similarity** and **RapidFuzz** for best paragraph matching.

## Installation
Follow these steps to set up and run the project:

```sh
### 1. Install Dependencies
pip install openai pymupdf scikit-learn numpy rapidfuzz

### 2. Set Up OpenAI API Key & Run the Script

# For Linux/macOS:
export OPENAI_API_KEY="your-api-key"
python pdf_rag.py

# For Windows Command Prompt:
set OPENAI_API_KEY=your-api-key
python pdf_rag.py

# For Windows PowerShell:
$env:OPENAI_API_KEY="your-api-key"
python pdf_rag.py
```

## Usage
```
Upload a PDF.
Ask a question related to the PDF.
Retrieve and highlight the most relevant paragraph.
View the highlighted PDF (highlighted_output.pdf).
```
## Exampele
```
data/
│── final_report.pdf  # Input file
│── highlighted_output.pdf  # Output with highlighted text
To run it:
```sh
python src/rag.py --input data/final report.pdf
```
EX:
What's your question? (or type 'q' to quit)
-what is the summary of the report?

The report examines the impact of the North American Free Trade Agreement (NAFTA) on agricultural productivity and trade in the agricultural equipment sector between the United States and Mexico. Here’s a summary of the findings and conclusions:

- **Impact on Trade**: NAFTA significantly increased trade in agricultural equipment between the U.S. and Mexico. Following the implementation of NAFTA in 1994, the trade values generally trended upward, despite a temporary decline during the 2008 economic crisis.

- **Productivity Changes**: The analysis indicates a positive correlation between reduced tariff rates and increased agricultural productivity in Mexico. Lower tariffs, a direct result of NAFTA, allowed for better access to advanced machinery and technology.

- **Regression Analysis**: A regression model was used to analyze the effects of tariff rates, trade exposure, and employment growth on productivity. The findings show:
   - A significant positive impact of reduced tariff rates on productivity.
   - An unexpected negative correlation between trade exposure and productivity, suggesting that increases in trade might lead to competitive pressures that adversely affect productivity in some cases.
   - A strong negative correlation between employment growth and productivity, pointing to mechanization and efficiency improvements potentially leading to reduced labor demand.

-**Conclusions**: While NAFTA has facilitated productivity growth through lower tariffs and increased access to technology, it has also introduced complexities, such as reduced employment growth. The report emphasizes the need for further research to understand the long-term implications of NAFTA on labor markets and income inequality in Mexico.

- **Future Directions**: The report suggests that further analysis could include different control variables and explore the impacts of NAFTA on other sectors in both countries to provide a fuller picture of its economic effects【4:6†source】【4:1†source】【4:5†source】.

This summary encapsulates the major findings and implications of the study, highlighting both achievements and challenges posed by NAFTA in the agricultural sector.

![image](https://github.com/user-attachments/assets/dcd747fa-1abc-465d-b076-3b4468537fbd)


## File Structure
```
pdf-rag/
│── README.md               # Project documentation
│── example.pdf             # Sample PDF file
│── highlighted_output.pdf  # Output with highlights
│── highlight_data.json     # Stores highlight metadata
│── pdf_rag.py              # Main script for PDF processing and querying
```

## Future Improvements

-**Multi-page document search** – multiple PDF files can be searched simultaneously.
-**Accelerate large PDF indexing** – Optimize document parsing and retrieval efficiency.
-**Highlight different colors based on different queries**— differentiate highlighted sections based on query context to improve the user experience.


## License
This project is licensed under the MIT License.
