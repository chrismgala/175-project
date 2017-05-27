# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #3: Drawing

import MalmoPython
import os
import sys
import time
from subprocess import call
from tf_files import label_image as lI
from PIL import Image




itemsStr = "{{{iron_shovel}}}, {{{iron_pickaxe}}}, {{{iron_axe}}}, {{{flint_and_steel}}}, {{{apple}}}, {{{bow}}}, {{{arrow}}}, {{{coal}}}, {{{diamond}}}, {{{iron_ingot}}}, {{{gold_ingot}}}, {{{iron_sword}}}, {{{wooden_sword}}}, {{{wooden_shovel}}}, {{{wooden_pickaxe}}}, {{{wooden_axe}}}, {{{stone_sword}}}, {{{stone_shovel}}}, {{{stone_pickaxe}}}, {{{stone_axe}}}, {{{diamond_sword}}}, {{{diamond_shovel}}}, {{{diamond_pickaxe}}}, {{{diamond_axe}}}, {{{stick}}}, {{{bowl}}}, {{{mushroom_stew}}}, {{{golden_sword}}}, {{{golden_shovel}}}, {{{golden_pickaxe}}}, {{{golden_axe}}}, {{{string}}}, {{{feather}}}, {{{gunpowder}}}, {{{wooden_hoe}}}, {{{stone_hoe}}}, {{{iron_hoe}}}, {{{diamond_hoe}}}, {{{golden_hoe}}}, {{{wheat_seeds}}}, {{{wheat}}}, {{{bread}}}, {{{leather_helmet}}}, {{{leather_chestplate}}}, {{{leather_leggings}}}, {{{leather_boots}}}, {{{chainmail_helmet}}}, {{{chainmail_chestplate}}}, {{{chainmail_leggings}}}, {{{chainmail_boots}}}, {{{iron_helmet}}}, {{{iron_chestplate}}}, {{{iron_leggings}}}, {{{iron_boots}}}, {{{diamond_helmet}}}, {{{diamond_chestplate}}}, {{{diamond_leggings}}}, {{{diamond_boots}}}, {{{golden_helmet}}}, {{{golden_chestplate}}}, {{{golden_leggings}}}, {{{golden_boots}}}, {{{flint}}}, {{{porkchop}}}, {{{cooked_porkchop}}}, {{{painting}}}, {{{golden_apple}}}, {{{sign}}}, {{{wooden_door}}}, {{{bucket}}}, {{{bucket}}}, {{{water_bucket}}}, {{{lava_bucket}}}, {{{minecart}}}, {{{saddle}}}, {{{iron_door}}}, {{{redstone}}}, {{{snowball}}}, {{{boat}}}, {{{leather}}}, {{{milk_bucket}}}, {{{brick}}}, {{{clay_ball}}}, {{{reeds}}}, {{{paper}}}, {{{book}}}, {{{slime_ball}}}, {{{chest_minecart}}}, {{{furnace_minecart}}}, {{{egg}}}, {{{compass}}}, {{{fishing_rod}}}, {{{clock}}}, {{{glowstone_dust}}}, {{{fish}}}, {{{cooked_fish}}}, {{{dye}}}, {{{bone}}}, {{{sugar}}}, {{{cake}}}, {{{bed}}}, {{{repeater}}}, {{{cookie}}}, {{{filled_map}}}, {{{shears}}}, {{{melon}}}, {{{pumpkin_seeds}}}, {{{melon_seeds}}}, {{{beef}}}, {{{cooked_beef}}}, {{{chicken}}}, {{{cooked_chicken}}}, {{{rotten_flesh}}}, {{{ender_pearl}}}, {{{blaze_rod}}}, {{{ghast_tear}}}, {{{gold_nugget}}}, {{{nether_wart}}}, {{{potion}}}, {{{glass_bottle}}}, {{{spider_eye}}}, {{{fermented_spider_eye}}}, {{{blaze_powder}}}, {{{magma_cream}}}, {{{brewing_stand}}}, {{{cauldron}}}, {{{ender_eye}}}, {{{speckled_melon}}}, {{{spawn_egg}}}, {{{experience_bottle}}}, {{{fire_charge}}}, {{{writable_book}}}, {{{written_book}}}, {{{emerald}}}, {{{item_frame}}}, {{{flower_pot}}}, {{{carrot}}}, {{{potato}}}, {{{baked_potato}}}, {{{poisonous_potato}}}, {{{map}}}, {{{golden_carrot}}}, {{{skull}}}, {{{carrot_on_a_stick}}}, {{{nether_star}}}, {{{pumpkin_pie}}}, {{{fireworks}}}, {{{firework_charge}}}, {{{enchanted_book}}}, {{{comparator}}}, {{{netherbrick}}}, {{{quartz}}}, {{{tnt_minecart}}}, {{{hopper_minecart}}}, {{{prismarine_shard}}}, {{{prismarine_crystals}}}, {{{rabbit}}}, {{{cooked_rabbit}}}, {{{rabbit_stew}}}, {{{rabbit_foot}}}, {{{rabbit_hide}}}, {{{armor_stand}}}, {{{iron_horse_armor}}}, {{{golden_horse_armor}}}, {{{diamond_horse_armor}}}, {{{lead}}}, {{{name_tag}}}, {{{command_block_minecart}}}, {{{mutton}}}, {{{cooked_mutton}}}, {{{banner}}}, {{{spruce_door}}}, {{{birch_door}}}, {{{jungle_door}}}, {{{acacia_door}}}, {{{dark_oak_door}}}, {{{record_13}}}, {{{record_cat}}}, {{{record_blocks}}}, {{{record_chirp}}}, {{{record_far}}}, {{{record_mall}}}, {{{record_mellohi}}}, {{{record_stal}}}, {{{record_strad}}}, {{{record_ward}}}, {{{record_11}}}, {{{record_wait}}}"

itemsStr = itemsStr.replace("{", "")
itemsStr = itemsStr.replace("}", "")
items = itemsStr.split(",")


sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

def Menger(xorg, yorg, zorg, size, blocktype, holetype):
    #draw solid chunk
    genstring = GenCuboid(xorg,yorg,zorg,xorg+size-1,yorg+size-1,zorg+size-1,blocktype) + "\n"
    #now remove holes
    unit = size
    while (unit >= 3):
        w=unit/3
        for i in xrange(0, size, unit):
            for j in xrange(0, size, unit):
                x=xorg+i
                y=yorg+j
                genstring += GenCuboid(x+w,y+w,zorg,(x+2*w)-1,(y+2*w)-1,zorg+size-1,holetype) + "\n"
                y=yorg+i
                z=zorg+j
                genstring += GenCuboid(xorg,y+w,z+w,xorg+size-1, (y+2*w)-1,(z+2*w)-1,holetype) + "\n"
                genstring += GenCuboid(x+w,yorg,z+w,(x+2*w)-1,yorg+size-1,(z+2*w)-1,holetype) + "\n"
        unit/=3
    return genstring

def GenCuboid(x1, y1, z1, x2, y2, z2, blocktype):
    return '<DrawCuboid x1="' + str(x1) + '" y1="' + str(y1) + '" z1="' + str(z1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" z2="' + str(z2) + '" type="' + blocktype + '"/>'

def getItemDrawing(item, x, z):
    """Create the XML for the items."""
    return '<DrawItem x="' + str(x) + '" y="20" z="' + str(z) + '" type="' + item + '"/>'

def GetMissionXML(items, world):
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                  <About>
                    <Summary>Hello world!</Summary>
                  </About>

                <ServerSection>
                  <ServerInitialConditions>
                    <Time>
                        <StartTime>12000</StartTime>
                        <AllowPassageOfTime>false</AllowPassageOfTime>
                    </Time>
                    <Weather>rain</Weather>
                  </ServerInitialConditions>
                  <ServerHandlers>
                      <FlatWorldGenerator generatorString="''' + world + '''"/>
                      <DrawingDecorator>
                        <DrawSphere x="-27" y="70" z="0" radius="30" type="air"/>''' + Menger(-40, 40, -13, 27, "wool", "air") + '''
                        ''' + getItemDrawing('coal', 5, 3) + '''
                        ''' + getItemDrawing('apple', 5, 24) + '''
                        ''' + getItemDrawing('apple', 3, 44) + '''
                        ''' + getItemDrawing('coal', 7, 68) + '''
                        ''' + getItemDrawing('coal', 5, 88) + '''
                        ''' + getItemDrawing('apple', 5, 108) + '''
                        ''' + getItemDrawing('apple', 8, 120) + '''
                      </DrawingDecorator>
                      <ServerQuitFromTimeUp timeLimitMs="100000"/>
                      <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                  </ServerSection>

                  <AgentSection mode="Survival">
                    <Name>MalmoTutorialBot</Name>
                    <AgentStart>
                        <Placement x="5.5" y="6.0" z="0" yaw="0"/>
                    </AgentStart>
                    <AgentHandlers>
                      <ObservationFromFullStats/>
                      <ObservationFromChat />
                      <ContinuousMovementCommands turnSpeedDegs="180"/>
                      <ChatCommands />
                    </AgentHandlers>
                  </AgentSection>
                </Mission>'''

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)


worlds = [
    '3;7,2*3,2;1;village,decoration',
    '3;7,2*3,2;7;village,decoration',
    '3;7,2*3,2;6;village,decoration',
    '3;7,2*3,2;32;village,decoration',
    '3;7,2*3,2;33;village,decoration',
    '3;7,2*3,2;31;village,decoration',
    '3;7,2*3,2;32;village,decoration',
    '3;7,2*3,2;39;village,decoration',
    '3;7,2*3,2;140;village,decoration',
    '3;7,2*3,2;34;village,decoration',
    '3;7,2*3,2;11;biome_1(distance=11),village(distance=9),decoration',
    '3;7,2*3,2;13;biome_1(distance=11),village(distance=9),decoration',
    '3;7,2*3,2;131;biome_1(distance=11),village(distance=9),decoration',
    '3;7,2*3,2;167;biome_1(distance=11),village(distance=9),decoration',
    '3;7,2*3,2;5;stronghold(distance=3),biome_1(distance=9),village(distance=9),decoration,dungeon,mineshaft(chance=0.9)',
    '3;7,2*3,2;39;village,decoration',
    '3;7,2*3,2;140;stronghold(distance=3),biome_1(distance=9),village(distance=9),decoration,dungeon,mineshaft(chance=0.9)',
    '3;7,2*3,2;5;stronghold(distance=3),biome_1(distance=9),village(distance=9),decoration,dungeon,mineshaft(chance=0.9)',
    '3;7,2*3,2;0;stronghold(distance=3),biome_1(distance=11),village(distance=9),decoration',
    '3;7,2*3,2;16;stronghold(distance=3),biome_1(distance=11),village(distance=9),decoration'
]

# Attempt to start a mission:
for i in range(1, 20):
    items[i] = items[i].strip()

    missionXML = GetMissionXML(['coal','apple'], worlds[i])
    my_mission = MalmoPython.MissionSpec(missionXML, True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print "Error starting mission:",e
                exit(1)
            else:
                time.sleep(2)

    # Loop until mission starts:
    print "Waiting for the mission to start ",
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text

    print
    print "Mission running " + worlds[i]

    agent_host.sendCommand("pitch 0.1")
    time.sleep(1.5)
    agent_host.sendCommand("pitch 0")

    agent_host.sendCommand("move 0.2")

    while world_state.is_mission_running:
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        agent_host.sendCommand("move 0.0")
        #Getting a screenshot.
        call(["screencapture", "current_state" + ".png"])
        im = Image.open("current_state.png")
        rgb_im = im.convert('RGB')
        rgb_im.save('current_state.jpg')

        # Getting the item classification.
        top_k, label_lines, predictions = lI.classify()
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
            agent_host.sendCommand( "chat " + '%s (score = %.5f)' % (human_string, score))
        agent_host.sendCommand("move 0.7")
        time.sleep(7)

    for error in world_state.errors:
        print "Error:",error.text

    # Loop until mission ends:
    while world_state.is_mission_running:
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text

    print
    print "Mission ended"
    # Mission has ended.
