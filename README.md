# makefun-awe

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/farhanqaz/makefun-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/farhanqaz/makefun-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

This is the entry for make.fun's bounty "Make the AI judge feel awe". The entry is a single short text about a millstone in a field. `main.py` writes it (1 to 280 Unicode code points, not only whitespace) to `/output/entry.txt`, creating the directory if needed. The program is deterministic and uses only the standard library.

Pass `--stdout` to print the text instead of writing the file.

`check_length.py` reads `/output/entry.txt` and reports its code-point count and whether it is valid.

## Run it

```
python3 main.py
```
