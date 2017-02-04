1. Rework configurations
 - find all constants
 - implement SafeConfigParser

2. Abstract-ify utils and modules
 - this means to make each command its own function
 - map groups of commands into objects

3. Better cmd parsing
 - currently treating return carriages and spaces as different chars but python parses them equally

4. Multiprocess dis bish
 - requires implementing true objects and possible interprocess memory
