# eht2025_difx_templating

# Correlation Environment

Use DiFX-2.9.1/2.9.x - tbd

Use CALC 11 rather than the old default CALC 9.1 model by, e.g.,
```
$ calcifMixed --calc=difxcalc *.calc
$ startdifx --dont-calc *.input
```

Channel definitions are sorted in numerically increasing order in the DiFX v2d file to keep CASA data reduction happy.


# Notes on Stations

The SMT 345G receiver is not sideband reparating; LSB folds onto USB (b2+b3, b1+b4).


# TODO


# Tracks

```
Track   Freq  HOPS  Stations
e25c04  230G  tbd   ...
...
```
