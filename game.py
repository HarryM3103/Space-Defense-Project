import pygame
import os
import random

from store.enemies.enemy import Enemy
from store.ships.Ship import Ship
from store.players.PlayerAssault import PlayerAssault
from store.players.PlayerFighter import PlayerFighter
from store.players.PlayerHeavy import PlayerHeavy
from store.button.Button import Button
from store.lasers.Laser import Laser, collide
from store.power_ups.HealthPotion import HealthPotion
from store.musicPlayer.music import MusicPlayer
from store.scoreboard.score_storer import ScoreBoard
from store.enemies.boss import Boss
from store.healthbar.healthbar import HealthBar
pygame.mixer.init()


pygame.init()
WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255, 255, 255)

START_X = 450
START_Y = 600
player: Ship = None

MENU_BG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "images", "galaxy_bg.jpeg")), (WIDTH, HEIGHT))

GAME_BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "space.jpeg")), (WIDTH, HEIGHT))

BOSS_BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "space.jpeg")), (WIDTH, HEIGHT))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/ARCADECLASSIC.ttf", size)


class Menu:

    def menu(self):

        enemies = []
        wave_length = 5
        enemy_vel = 1
        clock = pygame.time.Clock()
        run = True
        MusicPlayer().menuMusic()

        def redraw_start_window():
            pygame.display.set_caption("Menu")

            WIN.blit(MENU_BG, (0, 0))
            MENU_TEXT = get_font(130).render("SPACE  DEFENSE", True, "#FFFFFF")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 90))

            for enemy in enemies:
                enemy.draw(WIN)

            WIN.blit(MENU_TEXT, MENU_RECT)

            CLASS_TEXT = get_font(90).render(
                "SELECT A  CLASS", True, "#FFFFFF")
            CLASS_RECT = CLASS_TEXT.get_rect(center=(500, 185))

            WIN.blit(CLASS_TEXT, CLASS_RECT)

            for button in [ATTACK_SHIP_BUTTON, FIGHTER_SHIP_BUTTON, HEAVY_SHIP_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)

            pygame.display.update()

        while run:

            if pygame.mixer.music.get_busy() is False:
                MusicPlayer().menuMusic()

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            ATTACK_SHIP_BUTTON = Button(image=pygame.image.load("assets/images/Play Rect.png"),
                                        pos=(500, 300), text_input="ATTACK", font=get_font(90), base_color="#FFA500", hovering_color="#FFFFFF")

            FIGHTER_SHIP_BUTTON = Button(image=pygame.image.load("assets/images/Quit Rect.png"),
                                         pos=(500, 450), text_input="FIGHTER", font=get_font(85), base_color="#FFA500", hovering_color="#FFFFFF")

            HEAVY_SHIP_BUTTON = Button(image=pygame.image.load("assets/images/Quit Rect.png"),
                                       pos=(500, 600), text_input="HEAVY", font=get_font(90), base_color="#FFA500", hovering_color="#FFFFFF")

            clock.tick(FPS)
            redraw_start_window()

            if len(enemies) == 0:
                for i in range(wave_length):
                    enemy = Enemy(random.randrange(50, WIDTH-50),
                                  random.randrange(-1500, -100), random.choice(["blue", "red", "grey"]))
                    enemies.append(enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ATTACK_SHIP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Game(level=0, wave_length=4).game(
                            PlayerAssault(START_X, START_Y))
                    if FIGHTER_SHIP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Game(level=24, wave_length=4).game(
                            PlayerFighter(START_X, START_Y))
                    if HEAVY_SHIP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Game(level=24, wave_length=4).game(
                            PlayerHeavy(START_X, START_Y-100))

            for enemy in enemies:
                enemy.move_down(enemy_vel)

                if enemy.y + enemy.get_height() > HEIGHT + 50:
                    enemies.remove(enemy)

        pygame.quit()


class Game:

    def __init__(self, level: int, wave_length: int) -> None:
        self.level = level
        self.wave_length = wave_length
        self.current_level = 0

    def game(self, player: Ship):

        MusicPlayer().gameMusic()

        pygame.mixer.music.stop()
        clock = pygame.time.Clock()
        run = True
        lives = 5
        enemies: list[Enemy] = []
        health_potions: list[HealthPotion] = []
        enemy_vel = 1
        laser_vel = 5
        farthests_spawn_distance = -1800

        def game_over():

            lostFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 140)
            wavesFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 75)
            MusicPlayer().gameOver()
            lost_label = lostFont.render(f"GAME OVER", True, "#FFFFFF")
            WIN.blit(lost_label, (160, 300))

            scoreboard = ScoreBoard("score.txt")

            def addToLeaderBoard():

                scoreboard = ScoreBoard("score.txt")
                scoreFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 80)
                wavesFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 75)

                if self.level > scoreboard.high_score()[0]:
                    scoreboard.addItem(self.level)
                    new_highScore = scoreFont.render(
                        f"NEW HIGHSCORE", True, "#FFFFFF")
                    score = wavesFont.render(
                        f"WAVES SURVIVED: {self.level}", True, "#FFFFFF")
                    WIN.blit(new_highScore, (230, 405))
                    WIN.blit(score, (200, 475))
                    pygame.display.update()

                else:
                    scoreboard.addItem(self.level)
                    score = wavesFont.render(
                        f"WAVES SURVIVED: {self.level}", True, "#FFFFFF")
                    WIN.blit(score, (180, 420))
                    pygame.display.update()

            if len(scoreboard.high_score()) != 0:
                addToLeaderBoard()

            else:
                scoreboard.addItem(self.level)
                score = wavesFont.render(
                    f"WAVES SURVIVED: {self.level}", True, "#FFFFFF")
                WIN.blit(score, (180, 420))
                pygame.display.update()

            pygame.display.update()
            pygame.time.delay(10000)

        def redraw_game_window():
            pygame.display.set_caption("Space Defense")

            WIN.blit(GAME_BG, (0, 0))

            myFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 50)
            currentLevel = myFont.render(
                f"Level: {self.level}", True, "#FFFFFF")
            playerHealth = myFont.render(
                f"Health: {player.health}", True, "#FFFFFF")
            playerLives = myFont.render(f"Lives: {lives}", True, "#FFFFFF")

            # GREY = (49, 49, 49)
            # YELLOW = (255, 197, 0)
            # BLUE = (0, 162, 255)

            # boss = Boss(100, 100)
            # healthBar = HealthBar(75, 660, boss, BLUE, GREY, YELLOW)
            # healthBar.draw_shieldBar(WIN)
            # healthBar.draw_healthBar(WIN)
            # boss.draw(WIN)

            for enemy in enemies:
                enemy.draw(WIN)

            for healhPot in health_potions:
                healhPot.draw(WIN)

            player.draw(WIN)

        # TODO FINISH SCORE SCREEN WHEN YOU DIE IN GAME

            WIN.blit(currentLevel, (25, 50))
            WIN.blit(playerHealth, (750, 50))
            WIN.blit(playerLives, (750, 90))

            pygame.display.update()

        while run:

            if pygame.mixer.music.get_busy() is False:
                MusicPlayer().gameMusic()

            clock.tick(FPS)
            redraw_game_window()

            if lives <= 0 or player.health <= 0:
                game_over()
                Menu().menu()

            if len(health_potions) == 0:
                if random.randrange(0, 5*60) == 1:
                    HealthPot = HealthPotion(random.randrange(50, WIDTH-70),
                                             random.randrange(-1800, -100))
                    health_potions.append(HealthPot)

            if len(enemies) == 0:
                self.level += 1
                self.wave_length += 2
                farthests_spawn_distance -= 45
                if player.health != player.maxHealth:
                    player.health += 25
                for i in range(self.wave_length):
                    enemy = Enemy(random.randrange(50, WIDTH-70),
                                  random.randrange(farthests_spawn_distance, -100), random.choice(["blue", "red", "grey"]))
                    enemies.append(enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    MusicPlayer().menuMusic()
                    run = False

            # MOVEMENT
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.checkBorder_LEFT() is True:
                player.move_left()
            if keys[pygame.K_d] and player.checkBorder_RIGHT() is True:
                player.move_right()
            if keys[pygame.K_w] and player.checkBorder_UP() is True:
                player.move_up()
            if keys[pygame.K_s] and player.checkBorder_DOWN() is True:
                player.move_down()
            if keys[pygame.K_SPACE]:
                player.shoot(WIN)

            for healthPot in health_potions[:]:
                healthPot.move_down(2)

                if collide(healthPot, player):
                    health_potions.remove(healthPot)
                    if player.health != player.maxHealth:
                        player.health += 25

                if healthPot.y + healthPot.get_height() > HEIGHT + 50:
                    health_potions.remove(healthPot)

            for enemy in enemies[:]:
                enemy.move_down(enemy_vel)
                enemy.move_lasers(laser_vel, player)

                if random.randrange(0, 2*60) == 1:
                    enemy.shoot(WIN)

                if collide(enemy, player):
                    player.health -= 25
                    enemies.remove(enemy)

                if enemy.y + enemy.get_height() > HEIGHT + 50:
                    enemies.remove(enemy)
                    lives -= 1

            player.move_lasers(-laser_vel, enemies)

        # TODO complete the check sequence
            if self.level == self.current_level + 25:
                BossFight(player, self).game(player)

        pygame.display.update()


class BossFight:  # TODO complete the BossFight class

    def __init__(self, player: Ship, game: Game) -> None:
        self.current_game = game
        self.player = player
        self.current_level = game.level

    def game(self, player: Ship):
        MusicPlayer().gameMusic()

        pygame.mixer.music.stop()
        clock = pygame.time.Clock()
        run = True
        lives = 5
        boss_list: list[Boss] = [Boss(25, -500)]
        health_potions: list[HealthPotion] = []
        boss_vel = 0.5
        laser_vel = 5

        def game_over():

            lostFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 140)
            wavesFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 75)
            MusicPlayer().gameOver()
            lost_label = lostFont.render(f"GAME OVER", True, "#FFFFFF")
            WIN.blit(lost_label, (160, 300))

            scoreboard = ScoreBoard("score.txt")

            def addToLeaderBoard():

                scoreboard = ScoreBoard("score.txt")
                scoreFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 80)
                wavesFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 75)

                if self.level > scoreboard.high_score()[0]:
                    scoreboard.addItem(self.level)
                    new_highScore = scoreFont.render(
                        f"NEW HIGHSCORE", True, "#FFFFFF")
                    score = wavesFont.render(
                        f"WAVES SURVIVED: {self.level}", True, "#FFFFFF")
                    WIN.blit(new_highScore, (230, 405))
                    WIN.blit(score, (200, 475))
                    pygame.display.update()

                else:
                    scoreboard.addItem(self.level)
                    score = wavesFont.render(
                        f"WAVES SURVIVED: {self.level}", True, "#FFFFFF")
                    WIN.blit(score, (180, 420))
                    pygame.display.update()

            if len(scoreboard.high_score()) != 0:
                addToLeaderBoard()

            else:
                scoreboard.addItem(self.level)
                score = wavesFont.render(
                    f"WAVES SURVIVED: {self.level}", True, "#FFFFFF")
                WIN.blit(score, (180, 420))
                pygame.display.update()

            pygame.display.update()
            pygame.time.delay(10000)

        def redraw_game_window():
            pygame.display.set_caption("Space Defense")

            WIN.blit(BOSS_BG, (0, 0))

            myFont = pygame.font.Font("assets/fonts/ARCADE.ttf", 50)
            currentLevel = myFont.render(
                f"Level: {self.current_level}", True, "#FFFFFF")
            playerHealth = myFont.render(
                f"Health: {self.player.health}", True, "#FFFFFF")
            playerLives = myFont.render(
                f"Lives: {lives}", True, "#FFFFFF")
            bossName = myFont.render(f"ROE V WADEdda", True, "#FFFFFF")

            for boss in boss_list:
                GREY = (49, 49, 49)
                YELLOW = (255, 197, 0)
                BLUE = (0, 162, 255)
                healthBar = HealthBar(75, 660, boss, BLUE, GREY, YELLOW)
                healthBar.draw_shieldBar(WIN)
                healthBar.draw_healthBar(WIN)
                boss.draw(WIN)

            for healthPot in health_potions:
                healthPot.draw(WIN)

            player.draw(WIN)

            WIN.blit(currentLevel, (25, 50))
            WIN.blit(playerHealth, (750, 50))
            WIN.blit(playerLives, (750, 90))
            WIN.blit(bossName, (500, 200))

            pygame.display.update()

        while run:

            if pygame.mixer.music.get_busy() is False:  # MUSIC PLAYER
                MusicPlayer().bossMusic()

            clock.tick(FPS)
            redraw_game_window()

            if lives <= 0 or player.health <= 0:
                game_over()
                Menu().menu()

            if len(health_potions) == 0:
                if random.randrange(0, 5*60) == 1:
                    HealthPot = HealthPotion(random.randrange(50, WIDTH-70),
                                             random.randrange(-1800, -100))
                    health_potions.append(HealthPot)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.checkBorder_LEFT() is True:
                player.move_left()
            if keys[pygame.K_d] and player.checkBorder_RIGHT() is True:
                player.move_right()
            if keys[pygame.K_w] and player.checkBorder_UP() is True:
                player.move_up()
            if keys[pygame.K_s] and player.checkBorder_DOWN() is True:
                player.move_down()
            if keys[pygame.K_SPACE]:
                player.shoot(WIN)

            for healthPot in health_potions[:]:
                healthPot.move_down(2)

                if collide(healthPot, player):
                    health_potions.remove(healthPot)
                    if player.health != player.maxHealth:
                        player.health += 25

                if healthPot.y + healthPot.get_height() > HEIGHT + 50:
                    health_potions.remove(healthPot)

            for boss in boss_list:
                if boss.y != -60:
                    player.damage = 0
                    boss.move_down()
                else:
                    player.damage = 6.25
                    boss.move_side_to_side()

                if boss.health == boss.currentHealth - 250:
                    player.damage = 0
                    boss.shield_regen()

            for boss in boss_list:
                boss.move_lasers(laser_vel, player)
                if random.randrange(0, 45) == 1:
                    i = random.randint(1, 4)
                    boss.rand_shoot(WIN, i)

            # TODO MAKE A SUPER SHOT FOR THE BOSS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    MusicPlayer().menuMusic()
                    run = False

            player.move_lasers_boss(-laser_vel, boss_list)

        Menu().menu()


Menu().menu()
