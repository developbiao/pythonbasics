### Using Concr package
from cnocr import CnOcr

def extract_text(result):
    lines = [''.join(line['text']) for line in result]
    text = '\n'.join(lines)
    return text

img_fg = '20230707115205.jpg'
ocr = CnOcr()
out = ocr.ocr(img_fg)
text = extract_text(out)
print(text)

