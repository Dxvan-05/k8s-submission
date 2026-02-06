#!/usr/bin/env sh

# This script adds a TODO item to the TODO app for a random wiki page

RANDOM_WIKI_PAGE=$(curl -IL -o /dev/null -w "%{url_effective}\n" https://en.wikipedia.org/wiki/Special:Random)
TODO_ITEM="Read $RANDOM_WIKI_PAGE"
curl -X POST -H "Content-Type: text/plain" -d "$TODO_ITEM" "$TODO_BACKEND_URL/todos"