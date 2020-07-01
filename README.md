# arduino-raspberry-puzzles
Arduino and Raspberry Pi implementations for various puzzles.

Repository of basic old projects used for further inspiration in making anything with RaspberryPi or Arduino.

## Dir description

### vinculum (Arduino)

Very simple implementation of device, where if you press a button, it will trigger a loud alarm.

This was used in one of my psycho-hardcore game played on [Pražská Dvojka's](www.dvojka.cz) summer camp: the 3D-Game.
In short, the Vinculum was a center communication node of the [Borg Collective](https://en.wikipedia.org/wiki/Borg),
hidden from sight of other players.
When someone found this device, he or she could trigger alarm that signals the Borg Collective lost the game and
no longer shares its assimilated abilities.

### hanoi_puzzle (Raspberry Pi)

Implentation of the well known problem of the [Tower of Hanoi puzzle](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
for 4 rings and 3 rods.

Unfortunetaly I was too young to give proper names to components, so the code can be a little confusing.

### tank_puzzle (Arduino)

Logical puzzle similar to the [bucket puzzle](https://www.geeksforgeeks.org/puzzle-measure-4l-using-given-3-buckets/).

Imagine you want to pass a door, that is hydraulically sealed.
Your only option to open the door is to overload the hydro-tank with a criticall pressure.
The hydraulic locking mechanism consists of two components: the injector and the tank.
The Injector can have pressure of 0 - 3 Bars, the tank can have pressure 0 - 5 Bars.
However if you manage to set the pressure of tank to 4 Bars, the hydraulic system sets to criticall level and
the door opens.

In the control panel you can see something like this:
```
|         |    .   |    // o = LED is on 
|         |    o   |    // . = LED is off
|    .    |    o   |
|    .    |    o   |
|    o    |    o   |
|         |        |
|Injector |  Tank  |
```
This is one of the acceptable target state.

You can control the pressure of injector and tank with four buttons:
```
|   _      _    |    _      _    |
|  |_|    |_|   |   |_|    |_|   |
|  Pop   Empty  |   Pop   Empty  |
|               |                |
|   Injector    |      Tank      |
```

With these four buttons, you can perform six possible actions:
1. Pop Injector -> transforms all available pressure from the injector to the tank
2. Empty Injector -> sets pressure of the injector to 0
3. Pop Injector + Empty Injector -> sets pressure of the injector to 3
4. Pop Tank -> transforms all available pressure from tank to injector
5. Empty Tank -> sets pressure of the the tank to 0
6. Pop Tank + Empty Tank -> sets pressure of the tank to 5

### Matrix (Raspberry Pi 4)

The matrix composed of 4x4 LEDs represents a football match indicator (most likely) in
[Klabzubova Jedenácka](https://cs.wikipedia.org/wiki/Klapzubova_jeden%C3%A1ctka_(kniha)) long-term game made
for my beloved Sluníčkas Scout troop.
The matrix order is in 4 groups representing rows, where each element in the group represents columns; see the
following schema:
```
    1 2 3 4
    
a   B R Y G     B - blue
b   B R Y G     R - red
c   B R Y G     Y - yellow
d   B R Y G     G - green
```

#### Control

Control is done with SSH between a smartphone and the Raspberry Pi.
When the control program runs, the following 3 information must be inputted:
1. Command -- Turn on, Turn off, Turn everything off
2. Group (row)
3. Index (column)
