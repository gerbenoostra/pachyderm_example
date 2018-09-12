#!/usr/bin/env bash

source activate hackathon_ds_to_prod && \
    cd /opt/hackathon_ds_to_prod && \
    python3 -m dsprod.models.predict_model
