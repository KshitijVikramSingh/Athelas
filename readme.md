## Athelas Lichess Assignment

### Task 1 - Usernames of the top 50 players in Classical Chess (Lichess)

`print_top_50_classical_players` function in main.py prints the top 50 players in Classical Chess (Lichess) to the console. The usernames are printed in the format `<rank>. <username>`.

##### Steps to run

1. Run `python3` in the root directory of this repository.
2. Run the following commands in the Python interpreter:

```
from main import print_top_50_classical_players
print_top_50_classical_players()
```

##### Output

```
1. HomabiorKro
2. Sharkfang
3. strategyforchess
4. OjaiJoao
5. igormezentsev
6. naytatel
7. ChessKeep
8. ChessTheory64
9. Thorwald5
10. lion2006-45
11. alp_arslan92
12. iCe_eNerGyTeaM
13. Tinea
14. LithargoelTheThrice
15. uzkuzk
16. TheGodOfChess10
17. asm2020
18. aXemble12
19. Kung_Fu_Panda3
20. morgadochess
21. AsacoPaco
22. ChesskingOriginal
23. marshal67
24. avcs
25. chessunable
26. chesspawnrookking
27. Truemasterme
28. Moussardraser
29. USSR77
30. Super_BrainPower
31. mohammed_taher
32. MarregZ
33. Compy133
34. repeat_42b
35. robscat
36. SILVERKNIGHT101
37. shaheus
38. Delebarre
39. PREDATOR624
40. Hematom87
41. Soundly
42. Matt2013
43. winmate
44. tiger2505
45. daaleksandrov
46. Chlorofluorocarbons
47. HandKnit
48. Sensei71
49. Avslugin80
50. Maksim1984
```

### Task 2 - Rating histories of the top player in Classical Chess (Lichess) over last 30 days

`print_last_30_day_rating_for_top_player` function in main.py prints the rating history of the top player in Classical Chess (Lichess) over last 30 days to the console. The rating history is printed in the format `<date>: <rating>`.

```This implementation assumes last 30 calendar days as 30 days from yesterday, including yesterday. The implementation can be easily modified to consider last 30 days as 30 days from today, including today.```

##### Steps to run

1. Run `python3` in the root directory of this repository.
2. Run the following commands in the Python interpreter:

```
from main import print_last_30_day_rating_for_top_player
print_last_30_day_rating_for_top_player()
```

##### Output

```
2024-01-01: 2500
2024-01-02: 2514
2024-01-03: 2530
2024-01-04: 2550
2024-01-05: 2544
2024-01-06: 2563
2024-01-07: 2545
2024-01-08: 2545
2024-01-09: 2545
2024-01-10: 2545
2024-01-11: 2545
2024-01-12: 2548
2024-01-13: 2551
2024-01-14: 2557
2024-01-15: 2561
2024-01-16: 2566
2024-01-17: 2566
2024-01-18: 2566
2024-01-19: 2562
2024-01-20: 2562
2024-01-21: 2562
2024-01-22: 2562
2024-01-23: 2562
2024-01-24: 2562
2024-01-25: 2562
2024-01-26: 2562
2024-01-27: 2578
2024-01-28: 2584
2024-01-29: 2584
2024-01-30: 2584
```

### Task 3 - Rating histories of all top 50 players in Classical Chess (Lichess) over last 30 days, exported to a CSV file

`generate_rating_csv_for_top_50_classical_players` function in main.py generates a CSV file containing the rating histories of all top 50 players in Classical Chess (Lichess) over last 30 days.

There is another function, `async_generate_rating_csv_for_top_50_classical_players` which does the same thing but asynchronously. This function is executed by default when the program is run. This function performs around 3.5 times faster than the synchronous version.

```This implementation assumes last 30 calendar days as 30 days from yesterday, including yesterday. The implementation can be easily modified to consider last 30 days as 30 days from today, including today.```

##### Steps to run

To run the async version of this task, i.e, the `async_generate_rating_csv_for_top_50_classical_players` function, follow these steps:

1. Run `python3 main.py` in the root directory of this repository.
2. Wait for the program to finish execution.
3. The CSV file will be generated in the root directory of this repository.

To run the sync version of this task, i.e, the `generate_rating_csv_for_top_50_classical_players` function, follow these steps:

1. Run `python3` in the root directory of this repository.
2. Run the following commands in the Python interpreter:

```
from main import generate_rating_csv_for_top_50_classical_players
generate_rating_csv_for_top_50_classical_players()
```

3. The CSV file will be generated in the root directory of this repository.
4. Exit the Python interpreter.

#### The Lichess API docs clearly mention that only one request should be made at any point. While there isn't a clearly mentioned rate limit, it is suggested that should a 429 error be encountered, the request should be retried after atleast 60 seconds.
#### The program has been written to retry after 2 seconds. This works but it is not recommended to do so. The program can be easily modified to retry after 60 seconds. This will increase the execution time of the program, but it will be more compliant with the Lichess API guidelines. 
#### For further details, please refer to the [Lichess API Tips](https://lichess.org/page/api-tips).

##### Output

```
Please refer to the `top_classical_players_ratings.csv` file in the root directory of this repository.
```

## Packages

### Networking

Exports the `HTTPRequests` class which is used to make HTTP requests. This class is a wrapper around the `requests` package. Currently, it only supports GET requests, but it can be extended to support other HTTP methods as well.

### Lichess

Exports the `LichessRequests` class which is used to fetch relevant data from the Lichess API. This class uses the `HTTPRequests` class to make HTTP requests, and then parses the response to extract the relevant data.

### BeautifulLogs

Exports the `log` function which is used to log data to the console. This function takes any number of arguments and prints them to the console in a formatted manner, depending on the type of the argument.

## References

### Lichess

- [Lichess API](https://lichess.org/api)