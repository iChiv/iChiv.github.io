---
title: "Mortise Mirage"
layout: project
category: XR
date: 2024-03-06
---

*Genre:*

VR Puzzle

*Tools:*

Unity

*Platform:*

Meta Quest

*Team:*

Shuting Lei

Yijun Ma

[Yixuan Wang]()

Ziwei Niu

## Overview

**Mortise Mirage** is a VR immersive 3D puzzle game with **ancient ink wash painting** and **traditional mortise and tenon woodwork** as its main cultural themes. In this game, players will experience the assembly process of traditional mortise and tenon wooden objects in the artistic conception of landscape painting using their hands, feeling the craftsmanship and joy imbued with rich Eastern cultural imagery.

In the current demo release, players will be the first to experience the mortise and tenon assembly process of a **Chinese traditional sampan**. Based on the examination of traditional Chinese wooden boat structures and boat model examples, we designed handcrafted models, aiming to faithfully recreate the structural craftsmanship of traditional wooden boats. While players enjoy the immersive fun of 3D puzzle-solving, they can also explore the craftsmanship wisdom passed down through millennia embodied in a small boat.

## Gameplay Flow

## Highlights

- ***Puzzle assembly***: Mortise Mirage provides players with a unique immersive experience of being surrounded by puzzle pieces in three-dimensional space, enhancing the enjoyment and novelty of puzzle-solving.
- ***Educational Value***: Mortise Mirage faithfully reproduces the appearance and structural features of woodworking heritage, allowing players to experience the ingenuity of real mortise and tenon woodworking while playing.
- ***Aesthetic and immersive atmosphere***: The game masterfully combines dim light, creepy sound effects, scary monsters, lens and environment VFX. All these elements blend together to create a palpably dark world.

## Gameplay

“Mortise Mirage” is the first VR 3D puzzle game focused on traditional Chinese mortise-and-tenon joinery, offering a cultural, immersive assembly experience with high fidelity to the woodworking art form and expandable content. Set in an ink-wash “Ink Realm,” it blends music and interactive design for a tranquil exploration of Chinese culture while engaging in 3D puzzles. Leveraging Quest hand tracking, it delivers a novel puzzle-solving experience. The game authentically represents the woodworking craft, educating players on the cultural heritage. Its mechanics allow for future inclusion of various wooden cultural artifacts, showing significant expansion potential.

## Development Process

Firstly, we choose to use Meta All-in-one as the foundation of the project, which is more convenient for future direct packaging on Quest devices and native running. It comes with gesture tracking and related interfaces, making it easier to directly control through gestures and XR mode in the future, avoiding to some extent the disruption of immersion by controllers.

![](https://redox.games/wp-content/uploads/2024/03/iShot_2024-03-22_15.10.49-1024x780.png)

In the core assembly part of the game, scripts determine whether an object is correctly installed based on its distance and angle from the target position. If correctly installed, sound effects and visual effects will be played. When an entire section is assembled, level management scripts will traverse all required objects to check if each piece is in its correct position before deciding whether or not to proceed to the next stage.

![](https://redox.games/wp-content/uploads/2024/03/iShot_2024-03-22_15.12.00-1024x484.png)

When all stages are completed, a transparent model of the final product will appear. At this point players need to assemble each part onto their target positions; currently judgement logic still relies on angles and distances but may include assembly order requirements in future iterations so as to replicate traditional mortise-and-tenon assembly processes. Once complete, finished products move into display positions where interactive operations can be performed.

![](https://redox.games/wp-content/uploads/2024/03/MortiseMirageFinalLowVideoQuality.jpg)

## My Contributions

As the only interaction engineer for the project, I was responsible for the implementation of all player actions, level logic, and procedural animations. I was also responsible for communicating with the art team on how to place the assets, and ultimately adjusting the placement and fixing procedural issues that occurred when referencing other materials.

From configuring the VR interaction basics, stitching adsorption functions, model integrity judgement, UI interaction, and procedural animation, I independently completed almost all of the scripts for the gameplay sections.

![](https://redox.games/wp-content/uploads/2024/03/微信图片_20240418034639-1024x1024.png)

Firstly on the tiling attachments, I use distance and angle to determine if the player is moving the block to the target position at the correct angle.

![](https://redox.games/wp-content/uploads/2024/03/rider64_64SBC0WUU5-858x1024.png)

Then in the level logic, each block has a bool value to show if it’s finished splicing and determines if it’s finished by iterating through all the blocks in the current stage, and triggering a script to switch stages if it’s done.

![](https://redox.games/wp-content/uploads/2024/03/rider64_lA3QmZfNnV-422x1024.png)

The switching stage script contains sound and effect triggers and calls the method to go to the next stage.

![](https://redox.games/wp-content/uploads/2024/03/rider64_2gAPSmeT4M-640x1024.png)

When grabbing a block, the player is alerted to the current block being grabbed by the outer outline.

![](https://redox.games/wp-content/uploads/2024/03/rider64_Ue9yyvMI9s-640x1024.png)

Upon completion of the game, the player travels by boat to the next island for subsequent levels to be developed. To simulate the feeling of the boat floating, I used DOTween to animate the route as well as simulate the floating effect.

![](https://redox.games/wp-content/uploads/2024/03/rider64_SFnf6thFFL-699x1024.png)

I also created a lot of functional scripts, such as complete menus, random generation of floating decorations within the scene, etc., as well as scripts to control background music playback, adjusting volume, block floating, and block movement to a target location. Scripts that required additional art materials and sound effects were not implemented into the project due to project cycle issues, but can be viewed on the [GitHub]() page.

## Future Plan

Firstly, the assembly touch needs to be optimized. Try to use physical simulation for assembly and optimize the feedback effects of assembly. At present, only starting from sound effects and visual effects cannot bring enough immersive effect in virtual reality, which needs further optimization.

Secondly, more levels are needed for a richer interactive experience with various buildings and objects such as wooden umbrellas, pavilions, covered bridges. The scope of mortise and tenon is very wide. Due to our limited energy and time at this stage, we can’t provide a richer assembly experience but it leaves more room for the future of this project.

![](https://redox.games/wp-content/uploads/2024/03/8db86d19-060b-4267-b8e6-03a742a618df-1024x507.png)

Apart from assembling mortise-and-tenon joints also involve disassembling them like traditional tools such as Luban lock. Disassembling mortise-and-tenon structures can bring another angle of fun to the game.

As for the collection system currently due to limited level numbers and insufficient content it’s unable to give users enough sense of achievement. After adding more levels/items in the future they can be showcased collectively towards users.

## Refections

## How I met my aims?

My goal in this project was to assist in the design of VR-friendly puzzle game interactions and implement all tests in Unity and achieve the desired functionality. Achieving this utilised my knowledge of Virtual Reality, Game Design and Development, Meta ALL-IN-ONE SDK and Unity. After joining the group we had a very clear division of labour and I, as the more programmatically and Unity savvy member of the team, undertook almost all of the development and implemented all of the core functionality and achieved good results in procedural animation.

Firstly, for the basic mortise and tenon pickup, I used the Meta SDK’s own prefabs to implement it, and after initial testing and team discussion, we decided to use gesture recognition throughout, which can be adapted to new interaction methods very quickly.

Next, for the mortise-and-tenon splicing feature, I considered the performance limitations of the VR all-in-one machine. I referred to online tutorials and the guidance of the TA, but I didn’t find any ready-made solutions suitable for our project, so I first tried to implement the splice detection on the desktop platform, and then tested it in the VR all-in-one machine, and finally chose a solution with relatively low performance requirements.

In terms of the level detection function, I tried to use a traversal algorithm to check whether each square is in the right position, and gradually display the subsequent levels to ensure that the level flow is not wrong. For the level switching part, I created a fade-in/fade-out script to avoid the player’s feeling of vertigo due to sudden scene switching, but it could not be triggered stably when running standalone in a VR headset.

In terms of procedural animation, I used a plug-in to achieve the effect of decorations floating and fading, simulating the floating effect of a boat on the water, and achieved good results.

In terms of other interactions, the menu is the part I still haven’t solved, after making poke menus according to Meta’s official documentation, there are always cases where they are not detected, and in some cases, it can run normally on Windows platform using Oculus Runtime, but after installing it to the All-in-One PC it may need to be repeatedly operated to be triggered, which is still an unresolved issue at the moment.

Overall, I’ve gained a lot of development experience on this project, and it’s not the first time I’ve taken on the sole programming role on the team, but it’s by far the most complex programming project I’ve been responsible for. Since the Meta SDK has just been updated and the online tutorials are almost all outdated, I was able to solve a lot of problems independently by going through the documentation, which will help me a lot when I face more complex projects in the future. Due to time constraints, we tried to recreate as much as possible the framework of the game as we envisioned it at the beginning, providing a complete mortise-and-tenon joinery experience for the user, but there is still a lot of room for improvement in terms of details.

## What were my challenges? How did I face them?

First of all, Meta just updated its SDK at the beginning of the year, the APIs for getting user input and object status have changed, and the official documentation does not explain each excuse and the examples are relatively simple.

I first used the documentation to identify the required excuses, then isolated the required scripts from the sample scenarios to learn by imitation, then used ChatGPT to assist in explaining the inheritance relationship of the scripts and the function and effect of each line of code, and finally tested them with my own functional scripts.

The UI interaction of the Meta SDK is also a problem, although the toolkit provides the option to quickly mount scripts for Unity Canvas, it is not able to detect hand collisions correctly.

I used the official template as a base, first adding a working UnityCanvas prefab, then testing it level by level to find the part that implements the functionality, then replacing the display part with the image we created, adjusting the position to achieve our goal

This is not a permanent solution, and in the future it will be necessary to find parts of the UI code that interact correctly with the Quest SDK in order to adapt it to more functional menus that may appear in the future!

## 发表回复 [取消回复]()

您的邮箱地址不会被公开。必填项已用 * 标注

评论 *

显示名称 *

邮箱 *

网站

在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。