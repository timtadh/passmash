#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#Author: Tim Henderson
#Email: tim.tadh@hackthology.com
#For licensing see the LICENSE file in the top level directory.

python -m passmash $@ | xclip -selection clipboard

