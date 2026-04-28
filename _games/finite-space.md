---
title: "Finite Space"
layout: project
category: Games
date: 2024-01-02
description: "A space survival action game about resource collection, building construction, and constrained decision-making"
thumbnail: /assets/images/projects/finite-space-1.png
lang: en
tags: [Action, WebGL, Unity, Prototype]
links:
  - title: "Watch Gameplay"
    url: "https://www.youtube.com/watch?v=Db5xqYW9-GQ"
---

## Overview

**Finite Space** is an action game about resource gathering, building construction, and survival decision-making within a confined area.

For me, the most interesting design question wasn't "how do we make a tense game" — it was **how do you give the player clear goals, reasonable pressure, and a reason to replay when space, resources, and time are all limited.**

This project was also where I first confronted the problem of **design completeness** head-on. Resources could be combined directly into buildings, but the building system didn't have enough strategic depth to sustain interesting choices beyond a few rounds. That lesson stayed with me: I now ask much earlier whether a single-layer mechanic can support enough variation to keep the player engaged.

## Core Mechanics

The player moves within a restricted area, collects resources, and builds structures directly from harvested materials — all while responding to an approaching threat.

Three design axes drove the project:

- **Pressure through constrained space**  
  The player can't hide. Every move involves a tradeoff between position, resource distribution, and threat pacing. Compared to open-level designs, this approach forces more frequent decisions — there is almost never a "safe" moment.

- **Resource-to-building directness**  
  Resources are converted directly into buildings without an equipment intermediary. This works well for early momentum but revealed a problem: the buildings didn't differentiate enough in function, making the tradeoffs between choices feel shallow.

- **Short-session pacing**  
  The game is built around short rounds. I focused on density: is the opening clear? Is there a decision pivot mid-round? Does the ending provide a sense of payoff? Bad pacing in a short-session game kills replayability faster than anything.

## My Role

In this project, I was responsible for:

- Building the **survival and resource loop within constrained space**
- Using **resource and building combinations to create strategic variety**
- Balancing **moment-to-moment decision pressure** with **repeat-play pacing**

## Key Design Decisions

### Constraint as framework, not limitation

Many action games treat limited space as a restriction to be overcome. In this project, limited space is the primary source of decision-making. The player can't be safe everywhere at once, so they have to actively prioritize. My focus was on making the "limited" nature of the space an informative constraint — one the player can read and act on — rather than a frustrating one.

### Building system completeness

After the project wrapped, the biggest gap I identified was in the building system itself. Resource-to-building was too direct, and the building options didn't branch enough. After a few rounds, the player could exhaust the strategic space.

This led me to a more rigorous approach in later projects:
- Does the system still offer new choices after five, ten, or twenty rounds?
- Does the resource conversion chain have enough branches and tradeoffs?
- Is the player choosing between *doing it or not*, or between *different directions that each have meaningful costs and benefits*?

### Each round as a self-contained design unit

Because the game follows a short-session structure, I treated each round as an independent design unit — not as a small piece of a long progression system. The goal was for the player to enter a decision state quickly and complete a satisfying experience loop within a short time.

## What I Learned

This project gave me two lasting takeaways:

First, **designing through constraints** is powerful. When space, resources, and time are all limited, the designer's job is not to remove those limits — it's to make them readable and actionable for the player.

Second, **design completeness matters more than first impressions**. A mechanic that seems solid on paper can reveal shallow depth after just a few playthroughs. Catching that too late means the cost of fixing it is disproportionately high. **Finite Space** was the project where this lesson really landed for me.

I now ask a question much earlier in every project: *In the fifth, tenth, and twentieth round, will the player still be making interesting choices?*

## Gameplay Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/Db5xqYW9-GQ" frameborder="0" allowfullscreen></iframe>
