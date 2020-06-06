import sys,time
def jalan (kata):
    for e in kata:
       sys.stdout.write(e)
       sys.stdout.flush()
       time.sleep(0.1)
jalan("Goblok lu beraninya keroyokan dan dibelakang".center(44))
jalan("nih buat lu bansat".center(44))
jalan("   -----
          |   |
          |   |
          |   |
        ---   ---
    ----|       |----
  --                --
|--  Sialan lu goblok --|
|-- iya lu yang goblok--|
|______________________|".center(44))
