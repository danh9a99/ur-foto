from unidecode import unidecode
import re

def slugify(text):
    """Converts a given text into a URL-friendly slug"""
    text = unidecode(text).lower()
    text = re.sub(r'[\s]+', '-', text)
    return text