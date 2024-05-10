import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 120

    def attack(self, target, damage):
        target.health -= damage
        energy_cost = damage * 0.35
        self.energy -= energy_cost
        self.energy += damage * 0.25
        self.energy = min(self.energy, 120)
        print(f"{self.name} menyerang {target.name} dengan damage sejumlah: {damage} ")

    def show_info(self):
        print(f"Informasi {self.name}:")
        print(f"Kesehatan: {self.health}")
        print(f"Energi: {self.energy}\n")

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 200

    def attack(self, player):
        damage = random.randint(15, 18)
        player.health -= damage
        print(f"{self.name} menyerang {player.name} dengan damage: {damage}\n")

    def show_info(self):
        print(f"Informasi {self.name}:")
        print(f"Kesehatan: {self.health}\n")

dragon = Monster("Dragon")
goblin = Monster("Goblin")

def ask_attack_choice(player):
    choice = input(f"{player.name}, ingin langsung menyerang monster? (ya/tidak): ")
    if choice.lower() == "ya":
        return True
    elif choice.lower() == "tidak":
        time.sleep(3)
        print("Waktu telah berlalu. Silakan pilih kembali.\n")
        return ask_attack_choice(player)
    else:
        print("Pilihan tidak valid. Silakan pilih ya atau tidak.\n")
        return ask_attack_choice(player)

def ask_attack_type(player):
    choice = input(f"{player.name}, ingin menggunakan\nSkill 1\nSkill 2\nSkill ultimate?\n(1/2/u): ")
    if choice == "1":
        return 25
    elif choice == "2":
        return 35
    elif choice.lower() == "u":
        return 100
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau u.\n")
        return ask_attack_type(player)

def ask_target_monster(player):
    while True:
        choice = input(f"{player.name}, ingin menyerang monster Dragon atau Goblin? (d/g): ")
        if choice.lower() == "d":
            return dragon
        elif choice.lower() == "g":
            return goblin
        else:
            print("Pilihan tidak valid. Silakan pilih Dragon (d) atau Goblin (g).\n")

def play_game():
    player1 = Player(input("Masukkan username player 1: "))
    player2 = Player(input("Masukkan username player 2: "))

    while True:
        print("=== Giliran Player 1 ===")
        if ask_attack_choice(player1):
            monster = ask_target_monster(player1)
            damage = ask_attack_type(player1)
            if monster.health > 0:
                player1.attack(monster, damage)
                if monster.health <= 0:
                    monster.health = 0
                    monster.show_info()
                    print(f"{monster.name} sudah kalah!")
                    if dragon.health <= 0 and goblin.health <= 0:
                        print("Selamat, game berhasil diselesaikan! Ini mahkotamu, King!")
                        break
                    else:
                        choice = input("Lanjutkan menyerang monster yang lain? (ya/tidak): ")
                        if choice.lower() == "tidak":
                            print("Terima kasih telah bermain!")
                            break
                else:
                    monster.attack(player1)
            else:
                print(f"{monster.name} sudah dikalahkan. Pilih monster lain.\n")

        print("=== Giliran Player 2 ===")
        if ask_attack_choice(player2):
            monster = ask_target_monster(player2)
            damage = ask_attack_type(player2)
            if monster.health > 0:
                player2.attack(monster, damage)
                if monster.health <= 0:
                    monster.health = 0
                    monster.show_info()
                    print(f"{monster.name} sudah kalah!")
                    if dragon.health <= 0 and goblin.health <= 0:
                        print("Selamat, game berhasil diselesaikan! Ini mahkotamu, King!")
                        break
                    else:
                        choice = input("Lanjutkan menyerang monster yang lain? (ya/tidak): ")
                        if choice.lower() == "tidak":
                            print("Terima kasih telah bermain!")
                            break
                else:
                    monster.attack(player2)
            else:
                print(f"{monster.name} sudah dikalahkan. Pilih monster lain.\n")

        player1.show_info()
        player2.show_info()
        if monster.health > 0:
            print("\n=== Giliran Player 1 ===\n")  # Baris ini ditambahkan untuk output setelah serangan player 2

play_game()