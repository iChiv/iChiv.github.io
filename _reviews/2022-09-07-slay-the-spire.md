---
title: "Slay the Spire"
layout: project
category: Reviews
date: 2022-09-07
description: "A design analysis of how Slay the Spire achieves near-perfect roguelike deck-building pacing and choice density"
thumbnail: /assets/images/reviews/slay-the-spire-cover.jpg
tags: [Analysis, Game Design, Roguelike, Deck-building]
lang: en
---

## 1. Introduction

Slay the Spire is a card-based Roguelike game created and published by Mega Crit Games. It combines deck building and Rogue gameplay, encouraging players to combine their decks based on randomly appearing cards and relics to defeat the enemies in the spire.

![Slay the Spire](/assets/images/reviews/slay-the-spire-img-1_9gbigsizimj21-1024x576.png)

The game is inherited from Dream Quest, developed by Peter Whalen, but optimized on its strong randomness to create a highly strategic gameplay experience for players using monster intent and clear card effects. In its wake, countless followers have flocked to this niche genre, and now the card-based Rogue has become an extremely large segment of the gaming community.

## 2. Making Random Strategic

At the 1989 GDC, game design master Sid Meier said:

> "A game is a series of interesting decisions"

Slay the Spire succeeds precisely because it offers players a predictable choice of strategies to crack difficult levels with calculation, no matter the difficulty. This kind of thinking is exactly what makes for interesting decisions.

I think there are often two types of randomness in strategy Rogue: **chance random** and **strategy random**.

### Chance Random

Random chance means that **the player makes a choice first and later sees a random result**.

For example, with mechanics such as character hit and critic rates in XCOM, the player has at least 3 outcomes after giving an attack command to a character.

- the attack hits, dealing normal damage.
- the attack hits, dealing bludgeoning damage.
- the attack missed.

The player is unable to accurately predict the outcome before the character acts, which can result in the entire course of the battle changing due to this one random circumstance.

Rogue games often have limited resources and the player consumes resources with every action, **creating what must be a poor gaming experience if the correct strategy may randomly travel as a result**.

### Strategy Random

Strategy random means that **the game generates random challenges or puzzles, and the player chooses his or her own determined expectations** based on these challenges.

![Into the Breach](/assets/images/reviews/slay-the-spire-img-2_Diesel2Fproductv22Finto-the-breach2Fhome2FEGS_SubsetGames_IntotheBreach_G2_02-1280x720-fbcadbedc3c2cab213b416060931efe05abed4b8-1024x576.jpg)

For example, in Into the Breach, the location of monster generation is random, but the player can clearly see the intent of each enemy, the location and type of new enemy that will appear on the next turn, and thus control the character to execute the optimal strategy of his or her choice.

This type of randomness is similar to gaming in a chess game, but instead of having to evolve the opponent's possible choices, the player simply uses the limited leverage his side has to solve the upcoming problem. However, it still **requires a great deal of calculation at each move, increasing the burden of thought on the player**.

![Slay the Spire gameplay](/assets/images/reviews/slay-the-spire-img-3_ss20-1024x576.webp)

Slay the Spire is a clever combination of two random mechanics, as players build decks from randomly appearing cards and then use them strategically to solve puzzles based on the battlefield.

This doesn't mean that the cards don't have random effects, but the presence of random luck means that it adds to the fun of the game. There are a handful of cards that cause random effects for each profession in the game, but they mostly affect situations where you are fighting more with less, and they don't randomise negative effects.

## 3. Core Mechanisms

### 3.1 Strategy

#### 3.1.1 Limited Resource Assignment

In traditional strategy games, players need to manage and administer the resources they collect in a limited amount of time to win, but one defeat does not mean the end of the game, as long as they can continue to collect resources, they will always have a chance to turn the game around.

In Strategy Rogue, the length of a single game is fixed, which means that the player's resources are fixed, and all of the player's strategic choices will revolve around the limited resources, i.e. the strategy is the solution to the allocation of those resources.

In Slay the Spire, players have 4 types of resources:

- **Card**: Cards are the strategies available to players when they engage in battle.
- **Gold**: Gold is a resource for players to buy items from merchants or to unlock higher level options in random events.
- **Potion**: Potions are one-time items that assist players in battle.
- **HP**: HP is a resource that players can choose to exchange in battle, and also affects some of the options for random events.

There are also **relics**, which are items that enhance the player's character's abilities, but it is almost impossible for the player to spend them in exchange for resources, so they are not classified as allocatable resources.

#### 3.1.2 Map

In Slay the Spire, players can choose different routes to the boss room at the bottom of the level.

At the start of each game, the player first obtains a complete map of the entire level, estimates the potential rewards based on the different types of rooms on the map, and selectively exchanges resources to defeat the final boss and win the game.

Six types of rooms are shown on the map:

- **Merchant**: Spend gold to acquire cards, relics or potions; spend gold to remove cards.
- **Random Events**: Random appearance of other types of rooms or special events.
- **Rest Site**: Restoring blood; strengthening cards (special relics will offer extra options)
- **Treasure**: Obtaining relics
- **Monsters**: Spend blood to gain cards, gold and potions
- **Elite Monsters**: Spend blood to gain cards, gold, relics and potions

#### 3.1.3 Combat

Combat is the part of Slay the Spire that players have to face as they move forward, and it's fair to say that everything players do to prepare for combat in the game is in service of it.

The victory condition is that all enemy lives are reduced to 0. The defeat condition is that the player's life is reduced to 0.

![Combat flow](/assets/images/reviews/slay-the-spire-img-4_STS_battle.drawio.png)

There are very few ways to restore life points in the game, so the player's strategic choices for balancing the character's attack and defence in each turn are in effect resource management of the character's life points.

The composition of the deck will directly affect the strategies available to the player in this section. At the same time, the enemy's intentions for the next turn are displayed in battle, encouraging players to choose the best strategy to break the situation.

### 3.2 Deck Building

#### 3.2.1 Strength dimensions

In battle, players need to spend a fixed amount of energy each turn to play cards to their effect. As a game with strategy at its core, it is extremely important that Slay the Spire is numerically balanced.

There are 367 cards in the game, with 75 exclusive cards for each of the four professions Silent, Defect, Ironclad and Watcher, 53 colourless cards common to all professions and 14 cursed cards.

Depending on the effect, the cards available to the player can be divided into four categories: **damage, defence, card draw and energy**.

After counting the effects of all the cards, it was calculated that the expected standard values for each type of card effect are directly linked to the energy consumption, and that the values of all the cards do not deviate too much from the standard values:

| Energy Cost | 0 | 1 | 2 | 3 |
|------------|---|---|---|---|
| Damage | 6 | 11 | 18 | 32 |
| Block | 4 | 9 | 16 | — |
| Card Draw | 1.5 | 3 | — | — |

In addition:

- Cards that are stronger than standard are often accompanied by negative effects/additional release conditions
- Cards that are weaker than standard often have other positive effects/can create more effects with other cards
- Colorless cards will be slightly higher than the Pro Deck standard value for their rarity

At the same time, the weak initial card strength of each character encourages players to use cards acquired during the game, and forces them to trigger more combinations between cards when facing enemies with several times stronger life values than their characters later on.

#### 3.2.2 Card System

Cards are the player's strategic options in battle, and the more strategic they are, the more complex the player will be able to deal with the situation.

For this reason, instead of including a large number of rare cards with extensive text descriptions, Slay the Spire simplifies card functions and then enriches them with linking effects. The player community refers to these effects as combos, and cards that can form combos are referred to as a card system.

![Gameplay screenshot](/assets/images/reviews/slay-the-spire-img-5_ss23-1024x576.webp)

Statistics on the popular systems for each profession reveal that the designers offer a wealth of strategic options for each profession.

There are four types of characters in the game, each with three basic card systems.

**Ironclad**

- Strength (emphasis on damage)
- Blocking (emphasis on defence)
- Depletion (emphasis on energy recovery)

**Silent**

- Poison (emphasis on attack)
- Knife (emphasis on attack)
- Discard (Energy Recovery & Card Draw)

**Defect**

- Lightning Ball (emphasis on attack)
- Frostball (emphasis on defence)
- Dark Ball (defence and card draw)

**Watcher**

- Reserved (emphasis on card draw)
- Stance (attack and energy recovery)
- Foresight (emphasis on card draw)

As you can see, each card system enhances 1-2 aspects of a character's ability, but winning battles requires a balance of players' abilities in four areas: damage, defence, card draw and energy, which requires players to match up and build different systems to win the ultimate victory.

The clear and easy-to-calculate card effects successfully create a unique experience that guides players in forming their own strategies in a random variety of ways.

## 4. Enhancing the Experience

Slay the Spire creates a random world rich in strategy and enhances the player's strategic choice experience with clear hints of monster intent and a card system that transforms functions to help players make sense of the battle and turn the tide.

### Visual cues for monster intent

Monster intent shows the enemy's next system in a straightforward manner, helping players to quickly understand the battle situation.

In the original beta version, this feature required players to click on each enemy to read text cues to understand their intent, which was improved to an iconic display as it was complex and difficult to understand.

There are 15 types of icons for monster intent, depending on the damage and effect, and the damage value is displayed directly on the icon. If the enemy's actions cause a compound effect, the icons will overlap and there are 12 types of compound icons. The monster itself animates differently depending on the intent.

![Monster intent icons](/assets/images/reviews/slay-the-spire-img-6_270.png)

| Damage/Effect Range | Icon |
|---------------------|------|
| 0-4 damage | ![](/assets/images/reviews/slay-the-spire-img-6_270.png) |
| 5-9 damage | — |
| 10-14 damage | — |
| 15-19 damage | — |
| 20-24 damage | — |
| 25-29 damage | — |
| 30+ damage | — |
| Block | — |
| Negative Effect | — |
| Powerful Negative Effect | — |
| Use a Buff | — |
| Escape | — |
| Asleep | — |
| Stunned | — |
| Not any of the above | — |

![More intent icons](/assets/images/reviews/slay-the-spire-img-7_216.png)

The following outcomes are possible when the enemy's intentions are unknown:

- Splitting
- Exploding
- Summoning Minion
- Changing form
- Reviving itself
- Doing nothing

![Intent unknown outcomes](/assets/images/reviews/slay-the-spire-img-8_224.png)

### Card design outside the system

When a player chooses a card system that is severely lacking in a certain function, they can choose a card that is severely over-valued in the missing function but has harsh conditions of use to complement the weaknesses of their library, giving players a wider range of strategic options.

Players can choose cards that convert an ability into another type of ability, such as Body Slam: Deal damage equal to your Block, which converts a defensive ability into a damage ability.

![Cross-system cards](/assets/images/reviews/slay-the-spire-img-9_290.png)

Colorless cards are difficult to form combinations with, but they are strong enough to complement a player's professional library, and can even have special combinations with other systems, providing players with more imaginative strategic options.

Special colorless cards can be drawn randomly in battle to enrich the player's deck, but they only have positive effects, enriching the player's strategic options.

## 5. Epilogue

At the time of the game's release, the production team called Slay the Spire a Rougelite game, giving players a degree of certainty amidst the overall randomness, which is reinforced as players gain experience and eventually leads to a practically realistic strategy.

The Rogue element provides players with the thrill of a close win, and the strategic gameplay allows players to win without doubting that luck is their winning formula, proving the appeal that thinking brings to the game.

It's hard to summarise what makes Slay the Spire work. The balance between random and strategic elements is just a symptom of what it is, but I think the core of it lies in the design philosophy of the team: **Continuous optimisation of the game mechanics with the player experience at the core**.

Slay the Spire opened in Early Access in 2017 and won't be released until 2019, during which time the team has been filling in content and adjusting values on a weekly basis, even though on the shop page they say "updated every fortnight". I believe that listening to players and constantly optimising and improving the game experience is the distance between Slay the Spire and a fun game.
