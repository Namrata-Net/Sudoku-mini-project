def isValidSudoku(board):
	
	# Empty arrays to keep track of what numbers are already present in each row, col and box
    columns = []
    rows = []
    boxes = []
    
    # Add 9 empty hashmaps to each row, col and box
    # Row starts from top and goes down
    # Col starts from left and goes right
    # Box starts from top left and goes right
    # All of these are 0 indexed
    # Each hashmap will hold numbers that are already present in it as keys
    # We use hashmap because lookup time is O(1) ( Reference CS dojo@youtube)
    for i in range(9):
        columns.append({})
        rows.append({})
        boxes.append({})
        
    
    # For each row
    # Row index is represented by i
    # Every element should be unique in ith row
    for i in range(9):
    	
    	# For each col in that row
    	# Col index is represented by j
    	# Every element should be unique in jth col
        for j in range(9):
        	
        	# We will get number on board at that position
            element = board[i][j]
            
            # If the element is not empty (represented by . in the question. We don't care if the element is empty)
            if element != ".":
            	
            	# Return false if the element is repeated in ith row 
                if element in rows[i]:
                    return False
                    
            	# Return false if the element is repeated in jth col 
                if element in columns[j]:
                    return False
                    
                # Calculate the index of the box this element is present in
                # Element at 1st row and 2nd col will be in box 0 (All numbers are 0 indexed)
                # Element at 5th row and 8th col will be in box 5 (All numbers are 0 indexed)
                boxIndex = ((i // 3) * 3) + (j // 3)
                
                # Return false if the element is repeated in its corresponding box
                if element in boxes[boxIndex]:
                    return False
                
                # If we reach here it means element was not repeated in row, col or box
                # So we add it to ith row, jth col and its corresponding box
                rows[i][element] = True
                columns[j][element] = True
                boxes[boxIndex][element] = True
           
    # If we reach here it means no element was repeated anywhere on the board
    # Return true showing that the board is a valid sudoku
    return True
    
# generateSudoku() method will most likely give a invalid sudoku. Do not use this method if you want to show a positive case
# This method will always give a completed board. Partially completed board cannot be obtained from this method
board = generateSudoku()

# You can give your own board as input here and comment out the previous line
# This input should be a 9*9 array
# Each element of the array has to be a string
# Empty elements are represented by "."
# Give a valid 9*9 input or comment this line. Invalid inputs will throw errors. isValidSudoku() method will not validate the input
board = [[".", "9", .....]]

print (isValidSudoku(board))