---
title: "Repair Below From Above"
layout: project
category: XR
date: 2022-09-01
---

*Genre：*

VR Puzzle

*Tools: *

Unreal Engine5 & Blender & PS

*Platform: *

Oculus Mobile

*Team:*

Ziwei Niu – Program

Qiantao Zhang – Program

Min Pan – Art

Ziyi Hua – Art

Enwei Jin – Art

## Overview

![](https://redox.games/wp-content/uploads/2022/09/20220907-001639-1024x537.png)

Repair Below From Above is a VR game where players have to complete puzzles in a closed box based on information from the monitor above.

The game is the work of a few friends and I for Epic Games MegaJam 2022, **the theme of the GameJam is “As Above So Below”**.

I was responsible for **concept design, programming, sound, animation, visual effects , testing, **and** optimisation for this project**. This was also my first time working on a VR game in Unreal Engine5.

## Gameplay Flow

[Click to Download]()

## Brainstorming

After knowing that the theme of the activity was ‘As Above So Below’, we conceived the idea in terms of both the literal meaning and the meaning of the phrase.

**Literal meaning:**

A game with mechanisms linking two different dimensions such as up and down, positive and negative, inside and outside.

**Meaning of the Phrase:**

The phrase is derived from the Jade Book.

In the Isaac Newton version, the phrases appear written like: “that which is below is like that which is above and that which is above is like that which is below”.

![](https://redox.games/wp-content/uploads/2022/09/As-Above-So-below-2-1-1024x587.png)

A double sided Pool idea
An upside down idea
An up and down idea****

In the end we opted for a top-down concept that was more in tune with the theme and refined it into a more logical magnetic mechanism.

![](https://redox.games/wp-content/uploads/2022/09/iShot_2022-09-06_23.49.12-300x278.png)

![](https://redox.games/wp-content/uploads/2022/09/iShot_2022-09-06_23.41.47-1024x819.png)

## Gameplay

In Repair Below From Above, players need to **pick up the magnetic spanner**and **place the magnetic ball into the level box**, changing the position of the spanner according to the information on the display above to **attract the ball through the maze** and reach the target location.

The magnetic spanner has a **power limit** and is fully charged at the start of the level. Each time the magnetic force is activated, the power will be consumed and the level will fail if the power is depleted but the target is not reached.

The magnetic ball has **inertia** and will continue to move in the direction of the magnetic force when attracted by the spanner until it hits an obstacle.

## Gameplay Flow Chart

![](https://redox.games/wp-content/uploads/2022/09/AASB-1-1.png)

![](https://redox.games/wp-content/uploads/2022/09/image-20220906230959919-1024x514.png)

There are 3 levels in the game and after completing each level, the ball is transported to its initial position and the level container is changed.

The three levels are structured as follows:****

## Development Process

![](https://redox.games/wp-content/uploads/2022/09/屏幕截图-2022-09-05-231740-1024x575.png)

After deciding on the content of the game, I first built the game environment on top of VRTemplate and configured the player character **VRPawn** for subsequent testing.

![](https://redox.games/wp-content/uploads/2022/09/屏幕截图-2022-09-05-231648-1024x576.png)

I then started to create the **character’s hand animations**. There are six hand movements depending on the player’s buttons and the type of object they are holding.

![](https://redox.games/wp-content/uploads/2022/09/屏幕截图-2022-09-05-231459-1024x576.png)

Once the spanner was finished, I animated **the grip position** to ensure that the player could keep the correct orientation when picking up the handle with either hand.

![](https://redox.games/wp-content/uploads/2022/09/屏幕截图-2022-09-05-231931-1024x576.png)

While the rest of the team worked on the models and functions, I collected some of the **game’s sound effects** and **background music** and added additional effects through Audition to match the style of the game.

In the engine, I used both **Cue and Metasounds** to add sound effects to the game.****

Once the scenes and features were mostly complete, I used both the **traditional Particle System and Niagara** to create **the rolling effects for the magnetic ball** and the **electromagnetic effects for the magnetic spanner**, which vibrate when the player activates the magnetic effects.

![](https://redox.games/wp-content/uploads/2022/09/屏幕截图-2022-09-08-044645-1024x869.png)

In the end I was responsible for **packaging** the whole game into Oculus Mobile format.

![](https://redox.games/wp-content/uploads/2022/09/屏幕截图-2022-09-08-044125-1024x845.png)

Final Built

## Future Plan

This six and a half day production cycle included a lot of firsts for me:

My first GameJam; My first VR game in Unreal; and My first Visual Effects.

Our project has been submitted to MegaJam 2022, but in the final test I think there is still a lot of room for improvement in the game.

**1. Lack of depth in mechanics **

The game tends to have a good amount of mechanics, but the number of levels is short and the levels are of a single composition.

The game experience is poor if the playthrough is short, but the existing mechanics are too easy if there is an opportunity to make more levels. The biggest challenge of the game is the control of the direction of magnetic suction of the ball and the power consumption of the spanner.

**There is still a lot of room to explore the mechanism of magnetism itself**, such as using magnetism to push the ball, strong magnetism to control the ball to jump, and speeding up the ball to hit the scene that can destroy it.

**2. The visual effects are just normal **

The trailing path of the ball using the traditional particle effects is fair, but the spanner electromagnetic effects are a bit abrupt and large due to my first experience with Niagara, which may affect the player’s normal gameplay.

**I will continue to learn about effects in the future**. Ideally, the electromagnetic effect should be located between the two sides of the spanner, with the light effect slightly larger than the size of the top of the spanner.

**3. Inadequate testing **

The time taken to understand the theme, define the concept of the game and create a program that could be run for testing was too long, ending up with only two and a half days for us to make further changes to the mechanics.

This also resulted in the levels and mechanics being presented to the player in a more rushed experience at the end. We wanted to be able to **build the test content as quickly as possible once the base gameplay was finalised, shortening the test time so that we had more time** to optimise the gameplay and graphics.

## 发表回复 [取消回复]()

您的邮箱地址不会被公开。必填项已用 * 标注

评论 *

显示名称 *

邮箱 *

网站

在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。