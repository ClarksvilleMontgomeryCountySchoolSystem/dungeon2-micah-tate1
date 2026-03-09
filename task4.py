good = r"""

  ,;;.
,'  '''-,-. __
 \,, > / _ '  \
  `./-'    `. '
    (_._  ,(--)
     `| '  /` }
     `----' ( |
     |    )  ||
     |`.  | '_I
     |_|__| '
      c'c'
      |)|)
      |'|'
   ,_'_'_\  jv               
"""

bad = r"""
     ________
  __(_____  <|
 (____ / <| <|
 (___ /  <| L`-------.
 (__ /   L`--------.  \
 /  `.    ^^^^^ |   \  |
|     \---------'    |/
|______|____________/]
[_____|`-.__________]
"""

drawbridge_raised = True
if  drawbridge_raised:
    outcome = "Doom: Find a way to cross."
    print(bad)
else:
    outcome = "Thunder: You may cross."
    print(good)

print(outcome)
