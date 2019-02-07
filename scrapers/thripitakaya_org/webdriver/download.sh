#!/usr/bin/env bash

if [[ $# == 0 ]]; then
    echo "Usage:"
    echo "  $0 <Option>"
    echo "Option:"
    echo "  C: Chrome driver"
    echo "  F: Gecko driver (Firefox)"
    echo "  clean: remove all drivers"
    exit 1
fi

function download()
{
    url=${1}
    filename=${url##*/}
    echo "downloading ${filename}"
    wget ${url} &>/dev/null
    if [[ $? != 0 ]]; then
        echo "failed downloading webdriver: ${url}"
        exit 2
    fi
    if [[ ${filename##*.} == zip ]]; then
        unzip -o ${filename} &>/dev/null
    else
        tar xf ${filename} &>/dev/null
    fi
    if [[ $? != 0 ]]; then
        echo "failed extracting webdriver: ${filename}"
        exit 2
    fi
    rm ${filename}
}

if [[ $1 == 'C' ]]; then
    download https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip
elif [[ $1 == 'F' ]]; then
    download https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
else
    find . ! -iname ${0##*/} -delete
fi

