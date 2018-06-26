# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Hard coded data values and binary offsets.
"""

names = {
            0x03 : 'Agumon',
            0x04 : 'Betamon',
            0x11 : 'Gabumon',
            0x12 : 'Elecmon',
            0x1F : 'Patamon',
            0x20 : 'Kunemon',
            0x2D : 'Biyomon',
            0x2E : 'Palmon',
            0x39 : 'Penguinmon'
            }
            
items = {
            0x00 : 'sm.recovery',
            0x01 :'med.recovery',
            0x02 :'lrg.recovery',
            0x03 :'sup.recovery',
            0x04 :'MP Floppy',
            0x05 :'Medium MP',
            0x06 :'Large MP',
            0x07 :'Double flop',
            0x08 :'Various',
            0x09 :'Omnipotent',
            0x0A :'Protection',
            0x0B :'Restore',
            0x0C :'Sup.restore',
            0x0D :'Bandage',
            0x0E :'Medicine',
            0x0F :'Off. Disk',
            0x10 :'Def. Disk',
            0x11 :'Hispeed dsk',
            0x12 :'Omni Disk',
            0x13 :'S.Off.disk',
            0x14 :'S.Def.disk',
            0x15 :'S.speed.disk',
            0x16 :'Auto Pilot',
            0x17 :'Off. Chip',
            0x18 :'Def. Chip',
            0x19 :'Brain Chip',
            0x1A :'Quick Chip',
            0x1B :'HP Chip',
            0x1C :'MP Chip',
            0x1D :'DV Chip A',
            0x1E :'DV Chip D',
            0x1F :'DV Chip E',
            0x20 :'Port. potty',
            0x21 :'Trn. manual',
            0x22 :'Rest pillow',
            0x23 :'Enemy repel',
            0x24 :'Enemy bell',
            0x25 :'Health shoe',
            0x26 :'Meat',
            0x27 :'Giant Meat',
            0x28 :'Sirloin',
            0x29 :'Supercarrot',
            0x2A :'Hawk radish',
            0x2B :'Spiny green',
            0x2C :'Digimushrm',
            0x2D :'Ice mushrm',
            0x2E :'Deluxmushrm',
            0x2F :'Digipine',
            0x30 :'Blue apple',
            0x31 :'Red Berry',
            0x32 :'Gold Acorn',
            0x33 :'Big Berry',
            0x34 :'Sweet Nut',
            0x35 :'Super veggy',
            0x36 :'Pricklypear',
            0x37 :'Orange bana',
            0x38 :'Power fruit',
            0x39 :'Power Ice',
            0x3A :'Speed Leaf',
            0x3B :'Sage Fruit',
            0x3C :'Muscle Yam',
            0x3D :'Calm berry',
            0x3E :'Digianchovy',
            0x3F :'Digisnapper',
            0x40 :'DigiTrout',
            0x41 :'Black trout',
            0x42 :'Digicatfish',
            0x43 :'Digiseabass',
            0x44 :'Moldy Meat',
            0x45 :'Happymushrm',
            0x46 :'Chain melon',
            0x47 :'Grey Claws',
            0x48 :'Fireball',
            0x49 :'Flamingwing',
            0x4A :'Iron Hoof',
            0x4B :'Mono Stone',
            0x4C :'Steel drill',
            0x4D :'White Fang',
            0x4E :'Black Wing',
            0x4F :'Spike Club',
            0x50 :'Flamingmane',
            0x51 :'White Wing',
            0x52 :'Torn tatter',
            0x53 :'Electo ring',
            0x54 :'Rainbowhorn',
            0x55 :'Rooster',
            0x56 :'Unihorn',
            0x57 :'Horn helmet',
            0x58 :'Scissor jaw',
            0x59 :'Fertilizer',
            0x5A :'Koga laws',
            0x5B :'Waterbottle',
            0x5C :'North Star',
            0x5D :'Red Shell',
            0x5E :'Hard Scale',
            0x5F :'Bluecrystal',
            0x60 :'Ice crystal',
            0x61 :'Hair grower',
            0x62 :'Sunglasses',
            0x63 :'Metal part',
            0x64 :'Fatal Bone',
            0x65 :'Cyber part',
            0x66 :'Mega Hand',
            0x67 :'Silver ball',
            0x68 :'Metal armor',
            0x69 :'Chainsaw',
            0x6A :'Small spear',
            0x6B :'X Bandage',
            0x6C :'Ray Gun',
            0x6D :'Gold banana',
            0x6E :'Mysty Egg',
            0x6F :'Red Ruby',
            0x70 :'Beetlepearl',
            0x71 :'Coral charm',
            0x72 :'Moon mirror',
            0x73 :'Blue Flute',
            0x74 :'old fishrod',
            0x75 :'Amazing rod',
            0x76 :'Leomonstone',
            0x77 :'Mansion key',
            0x78 :'Gear',
            0x79 :'Rain Plant',
            0x7A :'Steak',
            0x7B :'Frig Key',
            0x7C :'AS Decoder',
            0x7D :'Giga Hand',
            0x7E :'Noble Mane',
            0x7F :'Metalbanana',
            }

rookies = (0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39)

starterTechs = {
            0x03 : 0x02,
            0x04 : 0X0C,
            0x11 : 0x2B,
            0x12 : 0X0C,
            0x1F : 0x2B,
            0x20 : 0x25,
            0x2D : 0x02,
            0x2E : 0X25,
            0x39 : 0x25
            }

starterTechSlots = {
            0x03 : 0x01,
            0x04 : 0x01,
            0x11 : 0x03,
            0x12 : 0X04,
            0x1F : 0x01,
            0x20 : 0x04,
            0x2D : 0x01,
            0x2E : 0X01,
            0x39 : 0x01
            }
            
chestItemOffsets = (
            0x13FE3118, #706
            0x13FE6844,
            0x13FEE01E,
            0x13FEE02A,
            0x13FEE036,
            0x13FF4DE8,
            0x13FF4DF4,
            0x13FF6978,
            0x13FF6984,
            0x13FFA098,
            0x13FFD7BC,
            0x13FFE0F0,
            0x13FFF35C,
            0x14000EDC,
            0x14000EE8,
            0x14000EF4,
            0x14003398,
            0x140033A4,
            0x14005868,
            0x140073E8,
            0x140073F4,
            0x14008F7C,
            0x14021168,
            0x14021174,
            0x14022D04,
            0x14023624,
            0x14023630,
            0x14023F54,
            0x14023F60,
            0x14030964, 
            0x140377A8,
            0x13FF58AA,
            0x13FF58B6,
            0x14038A04,
            0x13FFA508,
            0x14039338,
            0x140396CA,
            0x1403AEC4,
            0x1403AED0,
            0x1403AEDC,
            0x1403AEE8,
            0x14045424,
            0x1404A6DC,
            0x140539EC,
            0x140539F8,
            0x1405430C,
            0x14054318,
            0x14054324,
            0x1405836C,
            0x14058C9C,
            0x14067B7C,
            0x1406970C,
            0x14073334,
            0x14078F1C, #707
            0x14079848, #709
            0x14079854, #708
            0x14079860, #710
            0x1407986C, #711
            0x1407A178, #712
            0x1407A184, #713
            0x1407AA94, #700
            0x1407AAA0, #701
            0x1407AAAC, #702
            0x1407AAB8, #703
            0x1407BD46, #696
            0x1407BD52, #697
            0x1407BD5E, #698
            0x1407F430, #686
            0x1407FD54, #687
            0x14080688, #688
            0x14080FB4, #689
            0x140818F4, #690
            0x14081900, #691
            )

starter1SetDigimonOffset = 0x14D271C0       #set digimon id for agumon
starter1ChkDigimonOffset = 0x14CD1D24    #check digimon id to set agumon's tech
starter1LearnTechOffset  = 0x14CD1D40      #tech to learn for agumon
starter1EquipAnimOffset  = 0x14CD1D30      #animation to equip for agumon

starter2SetDigimonOffset = 0x14D271B8       #set digimon id for gabumon
starter2ChkDigimonOffset = 0x14CD1D44   #check digimon id to set gabumon's tech
starter2LearnTechOffset  = 0x14CD1D60       #tech to learn for gabuumon
starter2EquipAnimOffset  = 0x14CD1D50       #animation to equip for gabumon
