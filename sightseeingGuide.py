from mcpi.minecraft import Minecraft
mc = Minecraft.create()


places = {'Canada': (1, 1, 1), 'Mexico': (20, 20, 20), 'Japan': (50, 20, 1)}

choice = "1"
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        
        location = places[choice]

        x, y, z = location[0], location[1], location[2]
        
        mc.player.setTilePos(x, y, z)
