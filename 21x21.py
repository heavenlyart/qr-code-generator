from PIL import Image
L = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
a = "01100001 01100010 01100011 01100100 01100101 01100110 01100111"
b = a.split()
#L = []
'''for i in range(7):
    L.append([])
    for v in range(7):
        L[i].append(int(b[i][v]))
        
for i in L:
    print(i)'''
    
L2 = []
for i in range(21):
    L2.append([])
    for v in range(21):
        L2[i].append(0)
        
for i in L2:
    print(i)
    
print()
    
for i in range(7):
    for v in range(7):
        L2[i][v] = L[i][v]

for i in L2:
    print(i)
    
print()

# Horizontal Timing Pattern (Row 6)
for col in range(8, 13):
    if col % 2 == 0:
        L2[6][col] = 1
    else:
        L2[6][col] = 0

# Vertical Timing Pattern (Column 6)
for row in range(8, 13):
    if row % 2 == 0:
        L2[row][6] = 1
    else:
        L2[row][6] = 0
    
for i in range(7):
    for v in range(14,21):
        L2[i][v] = L[i][v-14]
    
for i in range(14,21):
    for v in range(7):
        L2[i][v] = L[i-14][v]
        
for i in L2:
    print(i)
    


scale = 20
grid_size = 21
img_size = grid_size * scale  # 21 * 20 = 420 pixels wide/tall

# Create a blank white canvas
# '1' means 1-bit (only Black and White)
# (img_size, img_size) is the dimensions
# color=1 means fill the whole thing with White first
canvas = Image.new('RGB', (img_size, img_size), color=(0,0,0))

# This "loads" the pixels so we can change their color
pixels = canvas.load()

# Now we loop through your L2 list (Rows and Columns)
for row in range(21):
    for col in range(21):
        
        # If your list has a 1 (Black module)...
        if L2[row][col] == 1:
            
            # ...we need to color a 20x20 block of pixels black
            for x in range(scale):
                for y in range(scale):
                    # We calculate the position on the canvas
                    # (0) means Black in this mode
                    pixels[col * scale + x, row * scale + y] = (0,255,0)

# Save it to your computer
canvas.save("my_first_qr.png")
canvas.show()
