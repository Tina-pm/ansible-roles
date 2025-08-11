# vim:ts=2:sw=2:et:ai:sts=2

# Inspired on
# https://eengstrom.github.io/musings/add-bitwise-operations-to-ansible-jinja2


class FilterModule:
  def filters(self):
    return {
      'bw_and': self.bw_and,
      'bw_or': self.bw_or,
      'bw_xor': self.bw_xor,
      'bw_not': self.bw_not,
      'bw_shl': self.bw_shl,
      'bw_shr': self.bw_shr,
    }

  def bw_and(self, x, y):
    return x & y

  def bw_or(self, x, y):
    return x | y

  def bw_xor(self, y, x):
    return x ^ y

  def bw_not(self, x):
    return ~ x

  def bw_shl(self, x, b):
    return x << b

  def bw_shr(self, x, b):
    return x >> b
