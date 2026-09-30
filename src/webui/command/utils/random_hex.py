import random


def random_hex(prefix):
    """
  隨機產生一位數的 16 進位制字串並加上指定前綴。

  Args:
    prefix: 字串前綴。

  Returns:
    隨機產生的 16 進位制字串。
  """

    hex_digits = "0123456789ABCDEF"
    prefix
    return prefix + random.choice(hex_digits)
