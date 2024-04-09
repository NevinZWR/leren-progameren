import time
import math
from termcolor import colored
from data import *

##################### O03 #####################
def copper2silver(amount: int) -> float:
    return amount / 10

def silver2gold(amount: int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:  
    return silver2gold(copper2silver(amount))

def platinum2gold(amount: int) -> float:
    return amount * 25

def getPersonCashInGold(mainCharacter: dict) -> float:
    totalGold = 0
    totalGold += mainCharacter['gold']
    totalGold += copper2gold(mainCharacter['copper'])
    totalGold += silver2gold(mainCharacter['silver']) 
    totalGold += platinum2gold(mainCharacter['platinum'])
    return totalGold


##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    costPeople = people *  JOURNEY_IN_DAYS * COST_FOOD_HUMAN_COPPER_PER_DAY
    costHorses = horses * JOURNEY_IN_DAYS * COST_FOOD_HORSE_COPPER_PER_DAY
    return round(copper2gold(costPeople + costHorses),2)


##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    filterlist = []
    for friend in list:
        try:
            if friend[key] == value:
                filterlist.append(friend)
        except KeyError:
            print('de key is niet gevonden')
            
    return filterlist


def getAdventuringPeople(people:list) -> list:
    filteredfriend = getFromListByKeyIs(people, 'adventuring', True)
    return filteredfriend

def getShareWithFriends(friends:list) -> list:
    filteredfriend = getFromListByKeyIs(friends, 'shareWith', True)
    return filteredfriend
def getAdventuringFriends(friends:list) -> list:
    advfriend = getAdventuringPeople(friends)
    ultfriend = getShareWithFriends(advfriend)
    return ultfriend
    

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    horseNeeded = math.ceil(people / 2)
    return horseNeeded

def getNumberOfTentsNeeded(people:int) -> int:
    tentNeeded = math.ceil(people / 3)
    return tentNeeded


def getTotalRentalCost(horses:int, tents:int) -> float:
    silverHorse_cost = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    goldTent_cost = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
    goldHorse_cost = silver2gold(silverHorse_cost)
    totalCost = goldTent_cost + goldHorse_cost
    return totalCost

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    item_texts = []
    for item in items:
        item_text = f"{item['amount']}{item['unit']} {item['name']}"
        item_texts.append(item_text)
    
    if len(item_texts) == 1:
        return item_texts[0] # als het maar 1 is dan doet ie zonder komma
    elif len(item_texts) == 2:
        return ' & '.join(item_texts)
    else:
        last_item = item_texts.pop()  #pakt de laatste item uit de lijst
        return ', '.join(item_texts) + " & " + last_item
        



def getItemsValueInGold(items: list) -> float:
    total_gold = 0.0
    for item in items:
        price_amount = item['price']['amount']
        price_type = item['price']['type']
        if price_type == 'copper':
            total_gold += copper2gold(price_amount * item['amount'])
        elif price_type == 'silver':
            total_gold += silver2gold(price_amount * item['amount'])
        elif price_type == 'gold':
            total_gold += price_amount * item['amount']
        elif price_type == 'platinum':
            total_gold += platinum2gold(price_amount * item['amount'])
    
    return round(total_gold, 2)

##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total_gold = 0.0
    for person in people:
        cash = person['cash']
        total_gold  += getPersonCashInGold(cash)
    return round(total_gold,2)


##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    interestedinvestors = []
    for investor in investors:
        percentageinvestor = investor['profitReturn']
        if percentageinvestor <= 10:
             interestedinvestors.append(investor)
    return interestedinvestors

 

def getAdventuringInvestors(investors:list) -> list:
    interestinvestor = getInterestingInvestors(investors)
    adventinvestor = getAdventuringPeople(interestinvestor)
    return adventinvestor
  
 
def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    total_cost = 0.0
    adventinvestors = getAdventuringInvestors(investors)
    if len(adventinvestors) == 0:
        return 0.0
    else:
        aantalHorse = len(adventinvestors)
        aantalTent = len(adventinvestors)
        rentCost = getTotalRentalCost(aantalHorse, aantalTent)
        gearCost = getItemsValueInGold(gear) * len(adventinvestors)
        foodCost = getJourneyFoodCostsInGold(len(adventinvestors), aantalHorse)
        total_cost += gearCost
        total_cost += rentCost
        total_cost += foodCost
        return round(total_cost, 2)



##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    max_nights = leftoverGold / getJourneyInnCostsInGold(1, people, horses)
    return int(max_nights)

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    human_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horse_cost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    oneNigth_Cost = human_cost + horse_cost
    costs = nightsInInn * oneNigth_Cost
    return round(costs,2)


##################### O13 #####################

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    adventinvestersprofit = []
    adventinvesters = getInterestingInvestors(investors)
    for advantinvester in adventinvesters:
        profit = advantinvester['profitReturn']
        profitpercentage = profit / 100
        investcut = profitpercentage * profitGold
        adventinvestersprofit.append(round(investcut, 2))
    return adventinvestersprofit



def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    if profitGold == 0:
        return 0.0
    investGold = sum(investorsCuts)
    remainingGold = profitGold - investGold
    adventurer_cut = round(remainingGold / fellowship, 2)
    return adventurer_cut


##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(people))

    # verdeel de uitkomsten
    for person in people:
        name = person['name'] # pakt de naam van de persoon uit de dict
        start = getPersonCashInGold(person['cash']) # pakt de gold van de persoon uit de dict
        end = start + goldCut 
        if person in adventuringFriends: # als de persoon in de adventuringFriends lijst zit end += goldcut
            end += goldCut
        if person in interestingInvestors:
            index = interestingInvestors.index(person) # pakt de index van de persoon in de interestingInvestors lijst
            end += investorsCuts[index]
            
        earnings.append({
            'name'   : name,
            'start'  : start,
            'end'    : end
        })

    return earnings

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()