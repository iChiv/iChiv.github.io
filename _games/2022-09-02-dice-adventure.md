---
title: "Dice Adventure"
layout: project
category: Games
date: 2022-09-02
description: "An experimental puzzle game where dice mechanics drive spatial navigation through interconnected portal systems"
thumbnail: /assets/images/projects/dice-adventure-cover.jpg
tags: [Puzzle, Dice, Unity, Experimental]
lang: en
---

## Overview

**Dice Adventure** is an experimental puzzle game built around a simple but unusual premise: **what if movement itself is the puzzle?** Instead of directly controlling a character, the player rolls dice to determine movement outcomes, navigating through a system of interconnected portals.

The design challenge was not just making a dice-based game — it was making the dice *feel like a meaningful input,* not a source of randomness. The player should feel that their choices about which die to roll and when matter more than the outcome of the roll itself.

## Core Mechanics

The core loop follows: **assess the portal layout → choose a die → roll → navigate the result → solve the spatial puzzle.**

Three design principles guided the work:

- **Dice as decision, not chance** — The player chooses *which* die to roll in *which* context. The puzzle is about selecting the right tool for the right spatial configuration, not about hoping for a favorable outcome.

- **Portal interconnections** — Portals create a non-linear spatial network. The player solves puzzles not just by moving from A to B, but by understanding how the portal topology changes the relationship between spaces.

- **Progressive complexity** — Early levels teach one mechanic at a time. Later levels layer dice types, portal configurations, and spatial constraints to create compounding puzzle challenges.

## My Role

I was responsible for the full design and implementation of this experimental puzzle game, including:
- Core mechanic design and validation
- Level design and progression curve
- Programming and Unity implementation
- Visual feedback systems for dice outcomes

## Key Design Decisions

### Making randomness feel controllable

Dice-based mechanics risk feeling like the player is at the mercy of luck. I addressed this by making die *selection* the primary decision — the player always knows what each die type does, and the puzzle challenges their spatial reasoning around applying the right die in the right position, rather than reacting to random outcomes.

### Portals as spatial reconfiguration

Instead of treating portals as simple teleporters, I used them to reconfigure the spatial relationship between puzzle elements. The player has to think not just "where does this portal go," but "how does this portal change the topology of the space I'm solving."

## What I Learned

This project reinforced the value of **prototyping an unusual mechanic before over-investing in content.** The dice-and-portal combination was conceptually interesting, but only through building a playable version did I understand which types of puzzles were genuinely satisfying and which were merely complex without being engaging. That feedback loop — build, play, trim — is something I now apply even earlier in experimental projects.

![Dice Portal Diagram](/assets/images/projects/dice-adventure-diagram.png)

![Dice Adventure Screenshot](/assets/images/projects/dice-adventure-2.png)
