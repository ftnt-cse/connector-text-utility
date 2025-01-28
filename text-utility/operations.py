"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .constants import *
from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.builtins import download_file_from_cyops
from PIL import Image
from rapidfuzz import fuzz
from oletools.olevba import VBA_Parser
import pytesseract
import os
import logging


logger = get_logger('text-utility')
logger.setLevel(logging.INFO)


def sentence_similarity(config, params):

    scores = {}
    sentence = params.get("sentence")
    sentences_to_compare_with = params.get("sentences_to_compare_with")
    if not isinstance(sentences_to_compare_with,list):
        ConnectorError(A1PARAM2_ERROR)
        raise Exception(A1PARAM2_ERROR)
    for s in sentences_to_compare_with:
        # Similarity in %
        similarity = fuzz.ratio(sentence, s)
        scores.update({s: similarity})
    return scores
        

def image_to_text(config, params):
    
    image_iri = params.get("image_iri")
    res = download_file_from_cyops(image_iri)
    file_path = "{0}/{1}".format('/tmp', res['cyops_file_path'])
    logger.info("File temporarily saved at: {}".format(file_path))  
    if not os.path.isfile(TESSERACT_BIN):
        ConnectorError("Tesseract binary not found please yum install -y tesseract")
        raise Exception("Tesseract binary not found please yum install -y tesseract")
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_BIN
    ocr_text = pytesseract.image_to_string(Image.open(file_path))
    os.remove(file_path)
    return ocr_text
  

def extract_macros(config, params):

    macros = []
    file_iri = params.get("file_iri")
    res = download_file_from_cyops(file_iri)
    file_path = "{0}/{1}".format('/tmp', res['cyops_file_path'])
    vba_parser = VBA_Parser(file_path)
    logger.info(f"File temporarily saved at: {file_path}")     

    if vba_parser.detect_vba_macros():
        # Loop through all the macros
        for (filename, stream_path, vba_filename, vba_code) in vba_parser.extract_macros():
            macros.append({
            "filename": filename,
            "stream_path": stream_path,
            "file_name": vba_filename,
            "macro":vba_code
            })
    else:
        macros.append({"result":"No macros found."})
    vba_parser.close()
    os.remove(file_path)
    return macros  