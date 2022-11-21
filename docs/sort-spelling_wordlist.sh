#!/bin/sh

set -e

D="$(cd $(dirname "$0") ; pwd)"
sort -u -o "$D/spelling_wordlist.txt" "$D/spelling_wordlist.txt"
