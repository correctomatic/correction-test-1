#!/usr/bin/env bash
IMAGE_NAME=correction-test-1
TAG=latest

docker build --file ./Dockerfile --tag "$IMAGE_NAME:$TAG" .
