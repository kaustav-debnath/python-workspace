test = "Hello World!"
print(test[-9:])

"""
Date formatting table 

| Code | Meaning                     | Example Output (2025-06-27 15:45:30) |
| ---- | --------------------------- | ------------------------------------ |
| `%Y` | 4-digit year                | `2025`                               |
| `%y` | 2-digit year                | `25`                                 |
| `%m` | 2-digit month (01–12)       | `06`                                 |
| `%B` | Full month name             | `June`                               |
| `%b` | Abbreviated month name      | `Jun`                                |
| `%d` | 2-digit day (01–31)         | `27`                                 |
| `%A` | Full weekday name           | `Friday`                             |
| `%a` | Abbreviated weekday name    | `Fri`                                |
| `%H` | Hour (24-hour clock, 00–23) | `15`                                 |
| `%I` | Hour (12-hour clock, 01–12) | `03`                                 |
| `%p` | AM or PM                    | `PM`                                 |
| `%M` | Minute (00–59)              | `45`                                 |
| `%S` | Second (00–59)              | `30`                                 |
| `%f` | Microsecond (000000–999999) | `000000`                             |
| `%Z` | Time zone name              | (depends on tz info)                 |
| `%j` | Day of the year (001–366)   | `178`                                |
| `%U` | Week number (Sunday start)  | `25`                                 |
| `%W` | Week number (Monday start)  | `25`                                 |

"""