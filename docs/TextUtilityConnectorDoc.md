## About the connector
Utilities to process text with features like sentences similarity, OCR and macro extractions from MS Office documents
<p>This document provides information about the Text Utility Connector, which facilitates automated interactions, with a Text Utility server using FortiSOAR&trade; playbooks. Add the Text Utility Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Text Utility.</p>

### Version information

Connector Version: 1.1.0

Authored By: Fortinet CSE

Contributors: Naili.M

Certified: No
## Release Notes for version 1.1.0
Following enhancements have been made to the Text Utility Connector in version 1.1.0:
<ul>
<li>Added new action <code>Extract Macros</code>.</li>
<li></li>
<li><p>The following dependency is now removed:</p>

<ul>
<li>networkx</li>
<li>sentence-transformers</li>
</ul></li>

<li>A new dependency, <code>rapidfuzz</code> and <code>oletools</code> have been added.</li>
</ul>

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
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Sentences Similarity</td><td>Providing a sample sentence and a list of candidates sentences, the action returns the one most similar to the sample</td><td>sentence_similarity <br/>Utility</td></tr>
<tr><td>Image to Text OCR</td><td>Extract text from image file</td><td>image_to_text <br/>Utility</td></tr>
<tr><td>Extract Macros</td><td>Extract macros code from MS Office documents</td><td>extract_macros <br/>Utility</td></tr>
</tbody></table>

### operation: Get Sentences Similarity
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Sentence</td><td>Sentence/word you want to compare
</td></tr><tr><td>Sentences To Compare</td><td>One word/sentence or more to compare with (in JSON format)
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

The output contains a non-dictionary value.
### operation: Image to Text OCR
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Image IRI</td><td>FortiSOAR IRI of the image file to perform OCR on
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "text": ""
    }
]</pre>
### operation: Extract Macros
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the MS Offile file within FortiSOAR from where to extract macros code
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "text": ""
    }
]</pre>
## Included playbooks
The `Sample - text-utility - 1.1.0` playbook collection comes bundled with the Text Utility connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Text Utility connector.

- Extract Macros
- Get Sentence Similarity
- Image to Text OCR

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
