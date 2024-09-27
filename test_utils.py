from utils import convert_pdf_to_text

def test_convert_pdf_to_text():
    # for testing
    with open("sample.pdf", "rb") as f:
        text = convert_pdf_to_text(f)
        print(text)

if __name__ == "__main__":
    test_convert_pdf_to_text()
