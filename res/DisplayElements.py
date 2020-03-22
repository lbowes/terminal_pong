# describes a 7 segment representation of the digits 0 - 9

digits = [
    [
     1, 1, 1,       # # #
     1, 0, 1,       #   #
     1, 0, 1,       #   #
     1, 0, 1,       #   #
     1, 1, 1        # # #
    ],
    [
     0, 1, 0,         #   
     1, 1, 0,       # #  
     0, 1, 0,         #
     0, 1, 0,         #
     1, 1, 1        # # # 
    ],
    [
     1, 1, 1,       # # #
     0, 0, 1,           #
     1, 1, 1,       # # #
     1, 0, 0,       #
     1, 1, 1        # # #
    ],
    [
     1, 1, 1,       # # #
     0, 0, 1,           #
     1, 1, 1,       # # #
     0, 0, 1,           #
     1, 1, 1        # # #
    ],
    [
     1, 0, 1,       #   #
     1, 0, 1,       #   #
     1, 1, 1,       # # #
     0, 0, 1,           #
     0, 0, 1            #
    ],
    [
     1, 1, 1,       # # #
     1, 0, 0,       #
     1, 1, 1,       # # #
     0, 0, 1,           #
     1, 1, 1        # # #
    ],
    [
     1, 1, 1,       # # #
     1, 0, 0,       #
     1, 1, 1,       # # #
     1, 0, 1,       #   #
     1, 1, 1        # # #
    ],
    [
     1, 1, 1,       # # #
     0, 0, 1,           #
     0, 0, 1,           #
     0, 0, 1,           #
     0, 0, 1            #
    ],
    [
     1, 1, 1,       # # #
     1, 0, 1,       #   #
     1, 1, 1,       # # #
     1, 0, 1,       #   #
     1, 1, 1        # # #
    ],
    [
     1, 1, 1,       # # #
     1, 0, 1,       #   #
     1, 1, 1,       # # #
     0, 0, 1,           #
     0, 0, 1            #
    ]
]

# The message displayed on the winning screen, compressed
winTextWidth = 35
winTextHeight = 17

winText_RLE = [
    4, 2, 1, 6, 3, 2, 1, 3, 1, 1, 5, 1, 4, 1, 1, 3, 1, 1, 1, 5, 1, 3, 1, 
    1, 1, 3, 1, 1, 1, 5, 1, 3, 5, 2, 1, 5, 5, 2, 1, 1, 1, 2, 4, 2, 4, 1, 
    1, 5, 1, 5, 1, 3, 1, 3, 1, 3, 1, 5, 1, 3, 2, 5, 5, 1, 1, 3, 1, 3, 1, 
    3, 5, 1, 1, 3, 1, 251, 1, 3, 1, 2, 3, 2, 2, 2, 1, 2, 4, 12, 1, 3, 1, 
    3, 1, 3, 2, 2, 1, 1, 1, 16, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 2, 
    3, 14, 1, 1, 1, 4, 1, 3, 1, 2, 2, 5, 1, 13, 1, 1, 1, 3, 3, 2, 1, 2, 
    2, 1, 4
]

####  #      ###  #   # ##### #### 
#   # #     #   # #   # #     #   #
####  #     #####  # #  ####  #### 
#     #     #   #   #   #     #   #
#     ##### #   #   #   ##### #   #
                                   
                                   
                                   
                                   
                                   
                                   
                                   
      #   #  ###  ##  #  ####      
      #   #   #   ##  # #          
      # # #   #   # # #  ###       
       # #    #   #  ##     #      
       # #   ###  #  ## ####        