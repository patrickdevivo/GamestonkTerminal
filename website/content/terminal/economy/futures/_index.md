```
usage: futures [--export {csv,json,xlsx}] [-h]
```

Commodities futures overview. [Source: https://www.wsj.com/market-data/commodities]

```
optional arguments:
  --export {csv,json,xlsx}
                        Export dataframe data to csv,json,xlsx file (default: )
  -h, --help            show this help message (default: False)
```

Example:
```
2022 Feb 15, 04:54 (✨) /economy/ $ futures
                   Futures/Commodities
┌───────────────────────────┬─────────┬─────────┬───────┐
│                           │ Price   │ Chg     │ %Chg  │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Crude Oil Futures         │ 92.80   │ -2.66   │ -2.79 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Brent Crude Futures       │ 94.10   │ -2.38   │ -2.47 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Gold Futures              │ 1857.80 │ -11.60  │ -0.62 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Silver Futures            │ 23.460  │ -0.388  │ -1.63 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Natural Gas Futures       │ 4.422   │ 0.227   │ 5.41  │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Unleaded Gasoline Futures │ 2.7159  │ -0.0635 │ -2.28 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Copper Futures            │ 4.5300  │ 0.0225  │ 0.50  │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Corn Futures              │ 647.75  │ -8.00   │ -1.22 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Wheat Futures             │ 783.75  │ -15.50  │ -1.94 │
├───────────────────────────┼─────────┼─────────┼───────┤
│ Bloomberg Commodity Index │ 110.49  │ -0.61   │ -0.55 │
└───────────────────────────┴─────────┴─────────┴───────┘
```
