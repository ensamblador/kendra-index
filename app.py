#!/usr/bin/env python3
import os

import aws_cdk as cdk

from kendra_index.kendra_index_stack import KendraIndexStack

TAGS = {"app": "generative ai business apps", "customer": "kendra-index-enterprise"}



app = cdk.App()
stk = KendraIndexStack(app, "kendra-index")

if TAGS.keys():
    for k in TAGS.keys():
        cdk.Tags.of(stk).add(k, TAGS[k])

app.synth()
