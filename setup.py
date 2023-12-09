import argparse
import os
import json
from pathlib import Path

prompt = '''
This is a crossword solver given a crossword puzzle in a JSON format.

The puzzle:
{"puzzle_id": 20818, "promo_id": null, "version": 0, "puzzle_meta": {"formatType": "Normal", "publishType": "Mini", "title": "", "printDate": "2023-01-01", "printDotw": 0, "editor": "", "copyright": "2022, The New York Times", "height": 5, "width": 6, "notes": [], "links": [], "layoutExtra": [], "author": "Joel Fagliano", "relatedContent": null}, "print_date": "2023-01-01", "enhanced_tier_date": null, "authors": ["Joel Fagliano"], "puzzle_data": {"clues": {"A": [{"clueNum": 1, "clueStart": 1, "value": "Like the number 23", "clueEnd": 5}, {"clueNum": 6, "clueStart": 7, "value": "Therefore", "clueEnd": 11}, {"clueNum": 7, "clueStart": 12, "value": "N.B.A. icon who famously wore 23", "clueEnd": 17}, {"clueNum": 8, "clueStart": 18, "value": "Indigenous people of the Arctic", "clueEnd": 22}, {"clueNum": 9, "clueStart": 24, "value": "23andMe analyzes them", "clueEnd": 28}], "D": [{"clueNum": 1, "clueStart": 1, "value": "Addictive thing in your pocket", "clueEnd": 25}, {"clueNum": 2, "clueStart": 2, "value": "Old TV episode", "clueEnd": 26}, {"clueNum": 3, "clueStart": 3, "value": "Like films from small studios", "clueEnd": 27}, {"clueNum": 4, "clueStart": 4, "value": "Exams for future docs", "clueEnd": 28}, {"clueNum": 5, "clueStart": 5, "value": "Dark time of day, in poetry", "clueEnd": 17}, {"clueNum": 7, "clueStart": 12, "value": "Happy dance", "clueEnd": 24}]}, "clueListOrder": ["Across", "Down"], "layout": [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], "answers": []}}

Answers: 
[
  null,
  "P",
  "R",
  "I",
  "M",
  "E",
  null,
  "H",
  "E",
  "N",
  "C",
  "E",
  "J",
  "O",
  "R",
  "D",
  "A",
  "N",
  "I",
  "N",
  "U",
  "I",
  "T",
  null,
  "G",
  "E",
  "N",
  "E",
  "S",
  null
]

Using this example, can you be a crossword solver? 
'''

months = ['03']

def format_message(puzzle):
  message = '''
  Here is the puzzle in the same JSON format:
  %s

  Format the solutions in the same way as the example above (i.e. an array of characters with empty spaces as "null") in the array of answers

  ''' % puzzle

  return message

all_messages = {}

for month in months:
  directory = 'crosswords_mini_empty/2023/'+month
  for file in os.scandir(directory):
    filename = file.path
    f = open(filename)
    data = json.load(f)
    puzzle = json.dumps(data)
    msg = format_message(puzzle)
    all_messages[data['print_date']] = msg



