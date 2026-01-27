import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

box_id = 0
vertical_gap = 0.2  # Gap between blocks in each tower

# Grid of towers: rows x columns x height
for row in range(5):
    for col in range(5):
        # Starting position for this tower - no horizontal gaps
        x = row * 1
        y = col * 1
        z = 0.5

        # Reset size for each tower
        length = 1
        width = 1
        height = 1

        # Build tower of 10 blocks
        for level in range(10):
            pyrosim.Send_Cube(name=f"Box{box_id}", pos=[x, y, z], size=[length, width, height])
            box_id += 1

            z += height/2  # Move up by half of current block's height
            z += vertical_gap  # Add gap between blocks

            # Shrink size for next block
            length *= 0.9
            width *= 0.9
            height *= 0.9

            z += height/2  # Move up by half of next block's height

pyrosim.End()
