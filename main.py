import os
import warnings
from typing import Dict

from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass
from qamodel import ScienceChatBot


############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []
    chatbot = ScienceChatBot()
    answers = chatbot.predict_answer(request.text)
    for question, answer in zip(request.text, answers):
        if answer == "Please enter a valid question!":
            output.append(answer)
            continue
        output.append(" : ".join([question, answer]))
    return SchemaUtil.create(SimpleText(), dict(text=output))
