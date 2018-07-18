#!/usr/bin/env bash

rm -fr ./tosubmit/predictor ./tosubmit/predictor.zip
echo "clean submission"

MODEL_DIR=$1
cp -r $MODEL_DIR ./tosubmit/predictor
zip -r ./tosubmit/predictor.zip ./tosubmit/predictor
echo "the submission is ready at ./tosubmit/predictor.zip"