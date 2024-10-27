import pygame


pygame.init()

WIDTH = 820
HEIGHT = 750
pygame.display.set_caption('Two Player Chess')
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 40)
timer = pygame.time.Clock()
fps = 60

# init game variable and image
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_pieces_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_pieces_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

white_pieces_captures = []
black_pieces_captures = []

# 0 - whites turn no selection, 1 - whites turn selected, 2 - blacks turn no selection, 3 - blacks turn selected
turn_step = 0
selection = 100
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (70, 70))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (70, 70))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (70, 70))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (70, 70))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (70, 70))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (60, 60))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (70, 70))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (70, 70))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (70, 70))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (70, 70))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (70, 70))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (60, 60))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
#check variables/ flashing counter
counter = 0
winner = ""
game_over = False

# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [480 - (column * 160), row * 80, 80, 80])
        else:
            pygame.draw.rect(screen, 'light gray', [560 - (column * 160), row * 80, 80, 80])
            
        pygame.draw.rect(screen, 'gray', [0, 640, WIDTH, 110])
        pygame.draw.rect(screen, 'gold', [0, 640, WIDTH, 110], 5)
        pygame.draw.rect(screen, 'gold', [640, 0, 180, HEIGHT], 5)
        status_text = ['White: select a Piece to move!', 'White: select a Destination!', 'Black: select a Piece to move!', 'Black: select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (15, 675))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 80 * i), (640, 80 * i), 2)
            pygame.draw.line(screen, 'black', (80 * i, 0), (80 * i, 640), 2)

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_pieces_locations[i][0] * 80 + 11, white_pieces_locations[i][1] * 80 + 11))
        else:
            screen.blit(white_images[index], (white_pieces_locations[i][0] * 80 + 7, white_pieces_locations[i][1] * 80 + 7))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_pieces_locations[i][0] * 80 + 1, white_pieces_locations[i][1] * 80 + 1, 80, 80], 2)
            
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_pieces_locations[i][0] * 80 + 11, black_pieces_locations[i][1] * 80 + 11))
        else:
            screen.blit(black_images[index], (black_pieces_locations[i][0] * 80 + 7, black_pieces_locations[i][1] * 80 + 7))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'green', [black_pieces_locations[i][0] * 80 + 1, black_pieces_locations[i][1] * 80 + 1, 80, 80], 2)

    
# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        all_moves_list.append(moves_list)
    
    return all_moves_list

def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_pieces_locations
        friend_list = white_pieces_locations
    else:
        enemies_list = white_pieces_locations
        friend_list = black_pieces_locations
        
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friend_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_pieces_locations and \
            (position[0], position[1] + 1) not in black_pieces_locations and position[1] < 7:
                moves_list.append((position[0], position[1] + 1))
        # initial state of pawn piece
        if (position[0], position[1] + 2) not in white_pieces_locations and \
            (position[0], position[1] + 2) not in black_pieces_locations and position[1] == 1:
                moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_pieces_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_pieces_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
            
    if color == 'black':
        if (position[0], position[1] - 1) not in black_pieces_locations and \
            (position[0], position[1] - 1) not in white_pieces_locations and position[1] > 0:
                moves_list.append((position[0], position[1] - 1))
        # initial state of pawn piece
        if (position[0], position[1] - 2) not in black_pieces_locations and \
            (position[0], position[1] - 2) not in white_pieces_locations and position[1] == 6:
                moves_list.append((position[0], position[1] - 2))
        if (position[0] - 1, position[1] - 1) in white_pieces_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
        if (position[0] + 1, position[1] - 1) in white_pieces_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
    return moves_list

def check_rook(position, color):
    moves_list =[]
    if color == 'white':
        enemies_list = black_pieces_locations
        friend_list = white_pieces_locations
    else:
        enemies_list = white_pieces_locations
        friend_list = black_pieces_locations
    for i in range(4): # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friend_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                    if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list and \
                         0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                             path = False
                    chain += 1
            else: path = False
        
    
    return moves_list
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])  
    return moves_list

# def check_king(position, color):
def check_bishop(position, color):
    moves_list =[]
    if color == 'white':
        enemies_list = black_pieces_locations
        friend_list = white_pieces_locations
    else:
        enemies_list = white_pieces_locations
        friend_list = black_pieces_locations
        
    for i in range(4): # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friend_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                    moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                    if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list and \
                         0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                             path = False
                    chain += 1
            else: path = False
    
    return moves_list
    
def check_knight(position, color):
    moves_list =[]
    if color == 'white':
        enemies_list = black_pieces_locations
        friend_list = white_pieces_locations
    else:
        enemies_list = white_pieces_locations
        friend_list = black_pieces_locations
        
    # 8 squares to check
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friend_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
        
    return moves_list

# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options
    

# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 80 + 40, moves[i][1] * 80 + 40), 5)

def draw_captured():
    for i in range(len(white_pieces_captures)):
        captured_piece = white_pieces_captures[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (670, 5 + 50 * i))
    for i in range(len(black_pieces_captures)):
        captured_piece = black_pieces_captures[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (750, 5 + 50 * i))

# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_pieces_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_pieces_locations[king_index][0] * 80 + 1, white_pieces_locations[king_index][1] * 80 + 1, 80, 80], 5)
        
    if turn_step < 2:
        if 'king'in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_pieces_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_pieces_locations[king_index][0] * 80 + 1, black_pieces_locations[king_index][1] * 80 + 1, 80, 80], 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 300, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))
    
       
black_options = check_options(black_pieces, black_pieces_locations, 'black')
white_options = check_options(white_pieces, white_pieces_locations, 'white')
    
# main game loop
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
        
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 80
            y_coord = event.pos[1] // 80
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_pieces_locations:
                    selection = white_pieces_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_pieces_locations[selection] = click_coords
                    if click_coords in black_pieces_locations:
                        black_piece = black_pieces_locations.index(click_coords)
                        white_pieces_captures.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_pieces_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_pieces_locations, 'black')
                    white_options = check_options(white_pieces, white_pieces_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                    
            if turn_step > 1:
                if click_coords in black_pieces_locations:
                    selection = black_pieces_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_pieces_locations[selection] = click_coords
                    if click_coords in white_pieces_locations:
                        white_piece = white_pieces_locations.index(click_coords)
                        black_pieces_captures.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'    
                        white_pieces.pop(white_piece)
                        white_pieces_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_pieces_locations, 'black')
                    white_options = check_options(white_pieces, white_pieces_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                # init game variable and image
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                white_pieces_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                black_pieces_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

                white_pieces_captures = []
                black_pieces_captures = []
                
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_pieces_locations, 'black')
                white_options = check_options(white_pieces, white_pieces_locations, 'white')
                
    if winner != '':
        game_over = True
        draw_game_over()
                    
    pygame.display.flip()
    
pygame.quit()