## Description of Files 

```
./chatgpt_ans = contains the ChatGPT response for each test case

./crosswords = contains a dataset of crossword puzzles from 01-01-2023 to 12-01-2023

./crosswords_empty = contains a dataset of crossword puzzles from 01-01-2023 to 12-01-2023 but with the answers removed

./crosswords_mini = contains a dataset of mini crossword puzzles from 01-01-2023 to 12-01-2023

./crosswords_mini_empty = contains a dataset of mini crossword puzzles from 01-01-2023 to 12-01-2023 but with the answers removed

experiment.py = code that access the API and gives ChatGPT all the puzzles

remove_ans.py = code that takes a crossword puzzle and removes the answers

setup.py = code that creates the messages given to ChatGPT
```

## Notes

- I have taken out the API Key due to that needing to stay private, so the script won't work if ran

- I will probably private this after a few days, since I don't know the copyright rules around the crossword data that I have in here

- crosswords and crosswords_empty aren't used since those puzzles turned out to be too big for the scope of this project 