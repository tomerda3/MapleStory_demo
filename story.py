from enemy import *
from set_up import *

class Player(pygame.sprite.Sprite):

    walkRight = pygame.image.load(os.path.join("Assets", "PLAYER_IMAGE_left.png")).convert_alpha()
    walkLeft = pygame.image.load(os.path.join("Assets", "PLAYER_IMAGE_right.png")).convert_alpha()

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.player_level = 1
        self.width = width
        self.height = height
        self.color = color
        self.image = self.walkRight
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.current_health = 500
        self.target_health = 500
        self.max_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change = 5

        self.current_mana  = 500
        self.target_mana  = 500
        self.max_mana  = 1000
        self.mana_bar_length = 400
        self.mana_ratio = self.max_mana / self.mana_bar_length
        self.mana_change = 5

        self.current_exp = 0
        self.target_exp  = 0
        self.max_exp = 1000
        self.exp_bar_length = 400
        self.exp_ratio = self.max_mana / self.mana_bar_length
        self.exp_change = 50

    def hit(self, damage):
        if self.target_health - damage <= 0:
            self.target_health = 0
        else:
            self.target_health -= damage

    def get_exp(self, exp):
        if self.current_exp + exp >= (self.player_level*150):
            self.current_exp = (self.current_exp + exp) - (self.player_level*150)
            self.target_exp = (self.current_exp + exp) - (self.player_level*150)
            self.player_level += 1
            self.current_health = self.max_health/2
            self.current_mana = self.max_mana/21
        else:
            self.target_exp += exp
            self.current_exp += exp

    def handle_movement(self,keys_pressed, player_rect):
        global IS_JUMPING, Y_VELOCITY, Y_GRAVITY, JUMP_HEIGHT

        if keys_pressed[pygame.K_a] and COUNT_UNIVERSE != 1 :  # pladyer_move.x - VELOCITY > BORDER.x //and player_rect.x - VELOCITY > BORDER.x
            self.image = self.walkLeft
            player_rect.x -= VELOCITY

        if keys_pressed[pygame.K_a] and COUNT_UNIVERSE == 1 and player_rect.x - VELOCITY > 0:  # pladyer_move.x - VELOCITY > BORDER.x
            self.image = self.walkLeft
            player_rect.x -= VELOCITY

        if keys_pressed[pygame.K_d] and COUNT_UNIVERSE != 5:  # pladyer_move.x - VELOCITY > BORDER.x
            self.image = self.walkRight
            player_rect.x += VELOCITY

        if keys_pressed[
            pygame.K_d] and COUNT_UNIVERSE == 5 and player_rect.x + player_rect.width < WIDTH:  # pladyer_move.x - VELOCITY > BORDER.x
            player_rect.x += VELOCITY

        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_SPACE] and player_rect.y - VELOCITY > 0:
            IS_JUMPING = True

        if IS_JUMPING:
            player_rect.y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                IS_JUMPING = False
                Y_VELOCITY = JUMP_HEIGHT
        # if keys_pressed[pygame.K_s] and player_rect.y + player_rect.height < SURFACE_HEIGHT:
        #     player_rect.y += VELOCITY

    def get_damage(self, damage):
        if self.target_health - damage <= 0:
            self.target_health = 0
        else:
            self.target_health -= damage

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def basic_health(self):
        BAR_POSITION = 280
        pygame.draw.rect(WIN, RED, (BAR_POSITION, HEIGHT-25, self.target_health/self.health_ratio-30, 20))
        pygame.draw.rect(WIN, WHITE, (BAR_POSITION, HEIGHT-25, self.health_bar_length/2-30 ,20), 2)

        red_health_text = HEALTH_FONT.render(
            "HP: " + str(self.current_health), True, WHITE)
        WIN.blit(red_health_text, (BAR_POSITION, HEIGHT - 55))

    def basic_level(self):
        red_level_text = HEALTH_FONT.render(
            "Level: " + str(self.player_level), True, WHITE)
        WIN.blit(red_level_text, (5, HEIGHT - 50))

    def lost_mana(self, mana_lost):
        if self.target_mana - mana_lost <= 0:
            self.target_mana = 0
        else:
            self.target_mana -= mana_lost

    def get_mana(self,amount):
        if self.target_mana < 500:
            self.target_mana += amount
        if self.target_mana > self.max_mana:
            self.target_mana = 500

    def basic_mana(self):
        BAR_POSITION = 465
        pygame.draw.rect(WIN, BLUE, (BAR_POSITION, HEIGHT-25, self.target_mana/self.mana_ratio-30, 20))
        pygame.draw.rect(WIN, WHITE, (BAR_POSITION, HEIGHT-25, self.mana_bar_length/2-30 ,20), 2)

        red_mana_text = HEALTH_FONT.render(
            "MP: " + str(self.current_health), True, WHITE)
        WIN.blit(red_mana_text, (BAR_POSITION, HEIGHT - 55))

    def basic_exp(self):
        BAR_POSITION = 100
        pygame.draw.rect(WIN, GREEN, (BAR_POSITION, HEIGHT-25, self.target_exp/self.exp_ratio-30, 20))
        pygame.draw.rect(WIN, WHITE, (BAR_POSITION, HEIGHT-25, self.exp_bar_length/2-30 ,20), 2)

        red_exp_text = HEALTH_FONT.render(
            "EXP: " + str(self.current_exp) + " / " +str(self.player_level*150), True, WHITE)
        WIN.blit(red_exp_text, (BAR_POSITION, HEIGHT - 55))

    def draw(self, rect):
        pygame.draw.rect(WIN, BLUE_NAVY, (0, HEIGHT-50, WIDTH/1.4, 50), 30)
        self.basic_health()
        self.basic_mana()
        self.basic_level()
        self.basic_exp()
        WIN.blit(self.image, (rect.x, rect.y))

def draw_window(rect,player,enemies,right_bullets,left_bullets):
    WIN.blit(BACKGROUND, (0, 0))
    # pygame.draw.rect(WIN, (255,255,255), BORDER)
    if enemies.__sizeof__() != 0:
        for enemy in enemies:
            enemy.basic_health()
            enemy.draw(WIN)
    player.draw(rect)

    for bullet in right_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in left_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    # WIN.blit(player.image, (red.x, red.y))
    pygame.display.update()

def handle_bullets(right_bullets, left_bullets, player_rect, enemies):

    for bullet in right_bullets:
        bullet.x += BULLET_VEL
        for enemy in enemies:
            if int(bullet.x) in range(int(enemy.x-enemy.width/15), int(enemy.x+enemy.width/15)):
                enemy.get_damage(player.player_level*30)
                if bullet in right_bullets:
                    right_bullets.remove(bullet)
            # if player_rect.colliderect(enemy.sprite.rect):
            #     player.get_damage(10)
            if enemy.target_health <= 0 or enemy.current_health <= 0:
                enemies.remove(enemy)
                player.get_exp(50*COUNT_UNIVERSE)
        if bullet.x > WIDTH:
            right_bullets.remove(bullet)

    for bullet in left_bullets:
        bullet.x -= BULLET_VEL
        for enemy in enemies:
            if int(bullet.x) in range(int(enemy.x-enemy.width/15), int(enemy.x+enemy.width/15)):
                enemy.get_damage(player.player_level*30)
                if bullet in left_bullets:
                    left_bullets.remove(bullet)
            if enemy.target_health <= 0 or enemy.current_health <= 0:
                enemies.remove(enemy)
                player.get_exp(50*COUNT_UNIVERSE)
        if bullet.x < 0:
            left_bullets.remove(bullet)

def switch_background(message,player_rect):
    global COUNT_UNIVERSE, BACKGROUND

    if message == "right":
        COUNT_UNIVERSE += 1
        string_image = 'story_image' + str(COUNT_UNIVERSE) + '.png'
        BACKGROUND = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', string_image)), (WIDTH, HEIGHT))
        player_rect.x = 0
    else:
        COUNT_UNIVERSE -= 1
        string_image = 'story_image' + str(COUNT_UNIVERSE) + '.png'
        BACKGROUND = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', string_image)), (WIDTH, HEIGHT))
        player_rect.x = WIDTH - 10

def enemy_setup():
    ENEMY_HEIGHT = 285
    enemy_1_left = pygame.image.load(os.path.join("Assets", "Blood_Pirate_left.png")).convert_alpha()
    enemy_1_right = pygame.image.load(os.path.join("Assets", "Blood_Pirate_right.png")).convert_alpha()
    enemy_2_left = pygame.image.load(os.path.join("Assets", "Monster_Prison_Guard_Rhino_LEFT.png")).convert_alpha()
    enemy_2_right = pygame.image.load(os.path.join("Assets", "Monster_Prison_Guard_Rhino_RIGHT.png")).convert_alpha()
    enemy_3_left = pygame.image.load(os.path.join("Assets", "Prison_Guard_Rhino_left.png")).convert_alpha()
    enemy_3_right = pygame.image.load(os.path.join("Assets", "Prison_Guard_Rhino_right.png")).convert_alpha()
    enemy_4_left = pygame.image.load(os.path.join("Assets", "Balrog_left.png")).convert_alpha()
    enemy_4_right = pygame.image.load(os.path.join("Assets", "Balrog_right.png")).convert_alpha()
    enemy_5_left = pygame.image.load(os.path.join("Assets", "Blood_Pirate_left.png")).convert_alpha()
    enemy_5_right = pygame.image.load(os.path.join("Assets", "Blood_Pirate_right.png")).convert_alpha()

    dict_enemy_left = {"1": enemy_1_left, "2": enemy_2_left, "3": enemy_3_left, "4": enemy_4_left, "5": enemy_5_left}
    dict_enemy_right = {"1": enemy_1_right, "2": enemy_2_right, "3": enemy_3_right, "4": enemy_4_right, "5": enemy_5_right}

    enemies = [[]]

    for i in range(1, 6):
        enemies.append([Enemy(random.randint(0, HEIGHT), ENEMY_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, 700,dict_enemy_right[str(i)], dict_enemy_left[str(i)],i*100 ),
                        Enemy(random.randint(0, HEIGHT), ENEMY_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, 700,dict_enemy_right[str(i)], dict_enemy_left[str(i)],i*100),
                        Enemy(random.randint(0, HEIGHT), ENEMY_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, 700,dict_enemy_right[str(i)], dict_enemy_left[str(i)],i*100),])
    return enemies

player_sprite = pygame.sprite.GroupSingle(Player(700, 285, PLAYER_WIDTH, PLAYER_HEIGHT, RED))
player = player_sprite.sprites()[0]

def main():
    # Basic setup
    player_rect =player.rect
    clock = pygame.time.Clock()
    run = True
    # random_enemy = random.randint(0, 1)
    enemies = enemy_setup()
    right_bullets = []
    left_bullets = []

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1 and player.target_mana >= 150:
                    player.lost_mana(150)
                    bullet = pygame.Rect(
                        player_rect.x, player_rect.y + player_rect.height // 2 - 2, 10, 5)
                    if player.image == player.walkRight:  #  walkRight walkLeft
                        bullet.x += player_rect.width
                        right_bullets.append(bullet)
                    else:
                        bullet.x -= player_rect.width
                        left_bullets.append(bullet)
                    # BULLET_FIRE_SOUND.play()

                if event.type == RED_HIT:
                    player.hit(COUNT_UNIVERSE*10)
                    # HEALTH_SOUND.play()

        # player.get_mana(1 / 1.5)
        player.get_mana(2)

        for enemy in enemies[COUNT_UNIVERSE]:
            if event.type == ENEMY_HIT:
                enemy.move(player_rect)
            if enemy.target_health <= 0:
                enemies[COUNT_UNIVERSE].remove(enemy)
                player.add_score(10*COUNT_UNIVERSE)

        if (player_rect.x%WIDTH) >= WIDTH-10 and COUNT_UNIVERSE <= MAX_UNIVERSE:
            switch_background("right",player_rect)
        elif (player_rect.x%WIDTH) <= 0 and COUNT_UNIVERSE != 1:
            switch_background("left",player_rect)

        keys_pressed = pygame.key.get_pressed()
        player.handle_movement(keys_pressed,player_rect)
        handle_bullets(right_bullets, left_bullets,player_rect, enemies[COUNT_UNIVERSE])

        # list_enemy = []
        # for enemy in enemies[COUNT_UNIVERSE]:
        #     list_enemy.append(enemy.sprites()[0])

        draw_window(player_rect, player, enemies[COUNT_UNIVERSE], right_bullets, left_bullets)

    main()

if __name__ == "__main__":
    main()