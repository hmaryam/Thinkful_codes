Write a function to ask what style of drink a customer likes
import random
questions = {
    "strong": "Do ye like your drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"}


ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

user_favorate =[]

def find_user_favorate():
  for kind in range(len(questions.values())):
      user_input = raw_input(questions.values()[kind])
      if user_input in ('y','yes'):
        user_favorate.append(questions.keys()[kind])
        print ''
      else:
        print ''
  return user_favorate

def final_drink_ingridiants(user_favorate):
  print 'your final drink will be:'
  for b in range(len(user_favorate)):
    drink_ingredients = random.choice(ingredients[user_favorate[b]])
    print drink_ingredients
  
if __name__ == '__main__':  
  favorate_kinds = find_user_favorate()
  final_drink_ingridiants(user_favorate)         
