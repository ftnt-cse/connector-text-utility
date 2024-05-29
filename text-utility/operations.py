"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import logging
from .constants import *
from connectors.core.connector import get_logger, ConnectorError
from sentence_transformers import SentenceTransformer, util
from connectors.cyops_utilities.builtins import download_file_from_cyops
from PIL import Image
import pytesseract
import os


logger = get_logger('text-utility')
logger.setLevel(logging.DEBUG)


def sentence_similarity(config, params):
    scores = {}
    report = {}
    sentences = [ params.get("sentence") ]
    
    sentences_to_compare_with = params.get("sentences_to_compare_with").replace(" ","").split(",") if "," in params.get("sentences_to_compare_with") else params.get("sentences_to_compare_with")

    if not isinstance(sentences_to_compare_with,list) and len(sentences_to_compare_with) < 2:
        ConnectorError(A1PARAM2_ERROR)
        raise Exception(A1PARAM2_ERROR)
    
    sentences.extend(sentences_to_compare_with)

    model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    sentence_embeddings = model.encode(sentences)

    for sentence, embedding in zip(sentences[1:], sentence_embeddings[1:]):
        score = util.pytorch_cos_sim(sentence_embeddings[0], embedding)
        logger.debug(f"[{sentences[0]}] compared to [{sentence}], scores [{score.item()}]")
        scores.update({sentence:score.item()})
        report.update({sentence:score.item()})
        
    sorted_scores = sorted(scores, key=scores.get, reverse=True)
    if len(sorted_scores) > 0:
        logger.info(f"[{sentences[0]}] and [{sorted_scores[0]}] are similar")
        return {
            "sentence":sentences[0],
            "similarTo":sorted_scores[0],
            "scores":report
        }
    else:
        ConnectorError(GENERIC_ERROR)
        raise Exception(GENERIC_ERROR)
        
        
        
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
  