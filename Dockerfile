FROM continuumio/miniconda3
ARG ENVIRONMENT_FILE=environment.yml
ARG ENVIRONMENT_NAME=hackathon_ds_to_prod

# replace dockers shell used by run to bash such that 'source activate' works
RUN ln -fs /bin/bash /bin/sh

# setup conda environment
ARG INSTALL_DIR=/opt/$ENVIRONMENT_NAME
RUN mkdir -p $INSTALL_DIR
COPY $ENVIRONMENT_FILE $INSTALL_DIR/

# create build environments, based on run env and build tools
RUN conda env create -f $INSTALL_DIR/environment.yml

ARG PACKAGE_NAME=dsprod
COPY $PACKAGE_NAME $INSTALL_DIR/$PACKAGE_NAME

COPY models $INSTALL_DIR/models
COPY runit.sh $INSTALL_DIR/


