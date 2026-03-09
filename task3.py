good = r"""
                              _ .--.
                             ( `    )
                          .-'      `--,
               _..----.. (             )`-.
             .'_|` _|` _|(  .__,           )
            /_|  _|  _|  _(        (_,  .-'
           ;|  _|  _|  _|  '-'__,--'`--'
           | _|  _|  _|  _| |
       _   ||  _|  _|  _|  _|
     _( `--.\_|  _|  _|  _|/
  .-'       )--,|  _|  _|.`
 (__, (_      ) )_|  _| /
jgs`-.__.\ _,--'\|__|__/
                 ;____;
                  \YT/
                   ||
                  |""|
                  '=='
"""

bad = r"""

         _.-.
       ,'/ //\
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  hh

"""

guard_awake = False

if not guard_awake:
    outcome = "Shadow: Beware of your shadow when crossing."
    print(good)

else:
    outcome = "Doom: Oh no! The guard saw you!"
    print(bad)

print(outcome)

