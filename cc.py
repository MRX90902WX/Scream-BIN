import random
from randomtimestamp import randomtimestamp
from datetime import datetime


class CC():
  '''Individual card info and methods.
  '''


  CCDATA = {
    'American': {
      'len_num': 15,
      'len_cvv': 4,
      'pre': [34, 37],
      'remaining': 13
    },
    'Discover': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [6001],
      'remaining': 12
    },
    'Mastercard': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [51, 55],
      'remaining': 14
    },
    'Visa': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [4],
      'remaining': 15
    },    
  }

  def __init__(self):
    self.cc_type = None
    self.cc_len = None
    self.cc_num = None
    self.cc_cvv = None
    self.cc_exp = None
    self.cc_prefill = []

  def generate_cc_exp(self):
    '''Generates a card expiration date that is 
    between 1 and 3 years from today. Sets `cc_exp`.
    '''
    self.cc_exp = randomtimestamp(
        start_year = datetime.now().year + 1,
        text = True,
        end_year = datetime.now().year + 3,
        start = None,
        end = None,
        pattern = "%m-%Y")
    
  def generate_cc_cvv(self):
    '''Generates a type-specific CVV number.
    Sets `cc_cvv`. 
    '''
    this = []
    length = self.CCDATA[self.cc_type]['len_cvv']

    for x_ in range(length):
      this.append(random.randint(0, 9))

    self.cc_cvv = ''.join(map(str,this))

  def generate_cc_prefill(self):
    '''Generates the card's starting numbers
    and sets `cc_prefill`.
    '''
    this = self.CCDATA[self.cc_type]['pre']
    self.cc_prefill = random.choices(this)

  def generate_cc_num(self):
    '''Uses Luhn algorithm to generate a theoretically 
    valid credit card number. Sets `cc_num`. 
    ''' 
    remaining = self.CCDATA[self.cc_type]['remaining']
    working = self.cc_prefill + [random.randint(1,9) for x in range(remaining - 1)] 

    check_offset = (len(working) + 1) % 2
    check_sum = 0

    for i, n in enumerate(working):
      if (i + check_offset) % 2 == 0:
        n_ = n*2
        check_sum += n_ -9 if n_ > 9 else n_
      else:
        check_sum += n

    temp = working + [10 - (check_sum % 10)]
    self.cc_num = "".join(map(str,temp)) 

  def return_new_card(self):
    '''Returns a dictionary of card details.
    '''
    return {'cc_type': self.cc_type,
            'cc_num': self.cc_num, 
            'cc_cvv': self.cc_cvv,
            'cc_exp': self.cc_exp}

  def print_new_card(self):
    '''Prints a single card to console.
    '''
    hr = '\033[1;31m--------------------------------'

    print(f'%s' % hr)
    print(f'\033[1;34mType: \033[1;37m%s' % self.cc_type)
    print(f'\033[1;34mNumber: \033[1;37m%s' % self.cc_num)
    print(f'\033[1;34mCVV: \033[1;37m%s' % self.cc_cvv)
    print(f'\033[1;34mExp: \033[1;37m%s' % self.cc_exp)


class CCNumGen(): 
  '''Generates theoretically valid credit card numbers
  with CVV and expiration date. Prints a list of dictionaries. 
  '''
  hr = '\033[1;31m--------------------------------'

  card_types = ['American','Discover','Mastercard','Visa']

  def __init__(self, type='Visa', number=1):

    self.type = type
    self.num = number
    self.card_list = []

    if self.type not in self.card_types:
      print('Card type not recognized. Task ended.')
      return
    if not isinstance(self.num, int):
      print('Number of cards must be a whole number. Task ended.')
      return

    print(self.hr)
    print(f'\033[1;32mGeneradas %s Tarjetas de %s' % (self.num, self.type))

    for x_ in range(0, self.num):
      new = CC()
      new.cc_type = self.type
      new.generate_cc_exp()
      new.generate_cc_cvv()
      new.generate_cc_prefill()
      new.generate_cc_num()
      self.card_list.append(new.return_new_card())
      new.print_new_card()

    print(self.hr)
    print('Completado.')
    print(self.hr)

  def print_card_list(self):
    '''Prints the list of cards to console.
    '''
    for d in self.card_list:
      print('\033[1;36m------------------------------')
      for k in d:
        print(f'%s: %s' % (k, d[k]))

#Banner
print("\033[1;32m  ____ ____    __  _______")
print("\033[1;32m / ___/ ___|   \ \/ /_   _|")
print("\033[1;33m| |  | |   _____\  /  | |")
print("\033[1;33m| |__| |__|_____/  \  | |")
print("\033[1;31m \____\____|   /_/\_\ |_|")

#Menu
print("")
print(" \033[1;31m1. \033[1;36mAmerican Express")
print(" \033[1;31m2. \033[1;36mDiscover")
print(" \033[1;31m3. \033[1;36mMastercard")
print(" \033[1;31m4. \033[1;36mVisa")
print("")

card_type = input(" \033[1;34mOpcion: \033[1;37m")
print("")

if card_type == "1":
   American = CCNumGen('American', 10)
elif card_type == "2":
   Discover = CCNumGen('Discover', 10)
elif card_type == "3":
   Mastercard = CCNumGen('Mastercard', 10)
elif card_type == "4":
   Visa = CCNumGen('Visa', 10)
else:
    print(" \033[1;31m[x]Opcion invalida")
    exit()
