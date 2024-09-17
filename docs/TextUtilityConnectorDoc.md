## About the connector
Utilities to process strings with features like sentences similarity and image to text OCR.
<p>This document provides information about the Text Utility Connector, which facilitates automated interactions, with a Text Utility server using FortiSOAR&trade; playbooks. Add the Text Utility Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Text Utility.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet CSE

Contributors: Naili.M

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-text-utility</pre>

## Prerequisites to configuring the connector
There are no prerequisites to configuring this connector.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
None.

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Sentences Similarity</td><td>Providing a sample sentence and a list of candidates sentences, the action returns the one most similar to the sample.</td><td>sentence_similarity <br/>Utility</td></tr>
<tr><td>Image to Text OCR</td><td>Extracts text from image file.</td><td>image_to_text <br/>Utility</td></tr>
</tbody></table>

### operation: Get Sentences Similarity
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Sentence</td><td>Specify the sentence you want to compare.
</td></tr><tr><td>Sentences To Compare</td><td>Specify the sentences to compare with. At least two are required in JSON format.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "sentence": "",
        "similarTo": "",
        "scores": ""
    }
]</pre>
### operation: Image to Text OCR
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Image IRI</td><td>Specify FortiSOAR IRI of the image file to perform OCR on.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "text": ""
    }
]</pre>
