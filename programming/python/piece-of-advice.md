# Piece of advise

- [Jake VanderPlas](https://twitter.com/jakevdp/status/1183241890289741825?s=20)
    ```
    # e.g. don't write methods like

    def load_data(filename):
      data = json.load(filename)
      # ...

    # This means *you* are responsible to support every imaginable
    # filetype/database/etc. Instead write methods like

    def load_data(data_dict):
      # ...

    # Let your users use the language.
    ```
- [![](https://pbs.twimg.com/media/D5GyQufUIAE4M5R?format=jpg&name=small)](https://twitter.com/jakevdp/status/1121873857973870592)

- Tricky Python bug I just hit due to an incorrect mental model of class & instance attributes:
  ```python
  class Foo:
    _num_instances = 0
    def __init__(self):
      self._num_instances += 1

  f1 = Foo()
  f2 = Foo()
  print(Foo._num_instances)
  ```
  Solution is to use `self.__class__._num_instances += 1`... you can see the real-world bug fix here: https://github.com/altair-viz/altair/pull/1454
  [source](https://twitter.com/jakevdp/status/1120898594519650304)
