'''Adds aliases into your rc file

Sets aliases in `.zshrc` files.

### Usage

Alias the `cat` command to c:

    $ al c cat

'''

import os
import sys


PATH = os.path.abspath('/Users/mvanveen/.zshrc')

class WrongNumberArgsError(Exception):
  def __init__(self, num_args, *args, **kw):
    self._args = num_args
    super(WrongNumberArgsError, self).__init__(*args, **kw)

  def __str__(self, *args, **kw):
    return (
      'Wrong number of args! Got %s, expected 3. \n  Please try escaping'
      'your output with double quotes.' % (self._args, )
    )

def main():

  if not len(sys.argv) is 3:
    raise WrongNumberArgsError(len(sys.argv))
  shortcut = sys.argv[1]
  full     = ' '.join(sys.argv[2:])

  alias = '%s="%s"' % (shortcut, full)

  with open(PATH, 'r') as file_obj:
   inp = file_obj.read()

  user_inp = raw_input('setting alias: %s\n OK? [Yy/Nn]' % alias)
  if not user_inp.lower() == 'y':
    sys.exit()

  print 'Setting alias... ',
  with open(PATH, 'w') as file_obj:
    file_obj.write('\n'.join(
      inp.split('\n') + ['alias ' + alias])
    )
  print 'OK'

if __name__ == '__main__':
  main()
