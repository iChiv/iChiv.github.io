---
title: "Project Catch"
layout: project
category: Games
date: 2022-08-07
---

*Genre:*

First-Person Puzzle

*Tools:*

Unity & 3Ds MAX
& MS Powerpoint

*Platform:*

Win/Mac

*Team: *

Ziwei Niu – Program & Design

Baoze Wang – Art & Design

## Game Overview

Project Catch is a first-person puzzle game. In the game, the player cannot directly touch objects in the scene, but can catch objects in the scene with the camera and project them in the scene again to complete the puzzle.

![](https://redox.games/wp-content/uploads/2022/09/iShot_2022-08-15_15.00.32-1024x593.png)

[Click to Download]()

## Gameplay Flow

## Why I Made This Game

The game was a collaborative project in which **I was responsible for the game mechanics and level design, programming and project resource management**. The idea for the game came from a brainstorming session.

Initially we had different ideas about the game, but our goal was the same, to make a game with fun and substance. So we took this as a starting point and eventually we narrowed down the keywords to 5 to ensure the game was viable.

These five words covered the visuals, the core mechanics and the way we interacted with the game.

· **Cartoon rendering** – Project Catch will use this as the basis for building scenes.

· **Dimensional enhancement** – the logic of interaction between the core mechanism of taking pictures and projection.

· **Scene Mechanics** – the components that make up the levels of the game.

· **Outer Wilds** – we want Project Catch to have a world that is as dynamic and exploratory as it has.

· **Human Motion Interaction** – players can experience the game via VR/AR or Eye-tracking devices

![](https://redox.games/wp-content/uploads/2022/09/iShot_2022-08-20_00.15.28.png)

![](https://redox.games/wp-content/uploads/2022/09/iShot_2022-08-20_00.33.48.png)

## Gameplay

In Project Catch, players will play in the **first person**, using the mouse and keyboard. The only character in the game is the one played by the player and the player cannot see the character’s image.

The player controls the character’s actions with the mouse and keyboard.

There are two core ways for players to interact: **Catch** and **Project**.

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-09-14_13.15.10-1024x715.png)

## Gameplay Flow Chart

We consolidated the content of the game we produced into one scene, organising it into 6 levels.

We have placed three coins in this scene as points of interest and the player can choose whether to collect all of them. If the player collects all the coins, they will get a reward at the final screen.

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-09-14_13.16.32-1024x653.png)

[

![](https://redox.games/wp-content/uploads/2022/08/Project-Catch-第-3-页.png)

]()Click to see full flow

## Bonus

**The bonus scene can only be accessed when all 3 coins have been collected**.

This scene will show the base model we created when designing the level prototype and thank the player for playing.

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-08-15_15.15.34-1024x584.png)

## Feedback

We invited friends to test the game after we had created the full scenario in order to optimise the performance and experience.

We received some feedback, some of which has been modified in the game. ColorRoom will be redesigned in the future.

![](https://redox.games/wp-content/uploads/2022/08/ProjectCatch_pie-1024x880.png)

![](https://redox.games/wp-content/uploads/2022/08/PC_pie2-1024x880.png)

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-09-14_13.24.03-1024x774.png)

## Development Process

This is my first full independent unity 3D project that I have programmed alone, and there are parts of the desired functionality and mechanics that are not implemented in the playable DEMO.

In addition, because of the epidemic factor, **we used online meetings to keep our production progress in sync and used github to synchronise the game files**.

![](https://redox.games/wp-content/uploads/2022/08/IMG_2250-1024x552.jpg)

After identifying our game mechanics through keywords, we first extended the core mechanics of hand-drawn capture to build several GameObjects.

![](https://redox.games/wp-content/uploads/2022/08/IMG_2252-1024x429.jpg)

![](https://redox.games/wp-content/uploads/2022/08/IMG_2253-1024x429.png)

![](https://redox.games/wp-content/uploads/2022/08/IMG_2251-1024x429.png)

Based on these, we build the level by placing these interactable objects in a scene.

This white moulded scene remains in the game files to this day. Players can obtain the button to this hidden scene by collecting all the gold coins.

![](https://redox.games/wp-content/uploads/2022/08/IMG_2254-1024x429.png)

As the programming and art were being done at the same time, We use online Gantt charts to synchronise work progress and summarise iterative issues.

I planned the script arrangement according to the scenes and functions.

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-08-20_02.30.41-1024x356.png)

![](https://redox.games/wp-content/uploads/2022/08/Scripts-514x1024.png)

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-08-18_17.54.23-1024x542.png)

The camera UI was completely refined from a purely flat UI to a three-dimensional UI with hierarchical relationships, and button prompts were added to the camera functions.

To complete this upgrade, I needed to rewrite the script for the UI, add logical relationships to control the button prompts and the associated animations.

I used the DOTween Pro package to help with this, using the scripting API of this plugin.

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-09-14_13.35.09-1024x308.png)

![](https://redox.games/wp-content/uploads/2022/08/iShot_2022-08-18_18.58.50-1024x700.png)

## Future Plan

The game currently offers a full gaming experience. The following points could continue to be optimised if given the opportunity in the future:

· **Guidance Optimisation**: Currently, the game has a relatively well developed solution for interaction guidance through patterns and voice. However, due to the short progression, there are fewer parts of the level that test the player’s mastery of the video mechanics.**The guides and levels need to be redesigned and remapped in the future.**

· **More Levels**: Of the 6 levels available, only 2 involve a video recording mechanic, and this has been mentioned by players in feedback. The video recording mechanic does not form a complete intro-practice-master-twist cycle within the game. **This requires more levels to achieve**. In the feedback, the ColorRoom is the most boring level and we need to remake that part as well.

· **Human Motion Control**: The game is set up in such a way that the character cannot touch objects in the game other than the camera, which we hope will allow for a more immersive experience. Motion capture is a direction that could be tried in the future, **using OpenCV to recognise player movements through the camera** for gameplay.

## 发表回复 [取消回复]()

您的邮箱地址不会被公开。必填项已用 * 标注

评论 *

显示名称 *

邮箱 *

网站

在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。