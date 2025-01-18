import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from game import Game
from player import Player
from room import Room

class PnjGUI(tk.Tk):  # Renommé de GameGUI à PnjGUI
    def __init__(self):
        super().__init__()
        
        self.game = Game()
        self.title("PNJ - La Maison Hantée")  # Titre modifié
        self.geometry("1024x768")
        
        self.setup_gui()
        self.bind_keys()
        
        
    def setup_gui(self):
        # Frame principale
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Zone de texte principale
        self.text_display = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            width=70,
            height=20
        )
        self.text_display.pack(padx=5, pady=5)
        
        # Frame inférieure pour les contrôles
        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Frame gauche pour les informations du joueur
        self.player_frame = ttk.LabelFrame(self.control_frame, text="Informations Joueur")
        self.player_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH)
        
        self.player_info = ttk.Label(self.player_frame, text="")
        self.player_info.pack(padx=5, pady=5)
        
        self.points_label = ttk.Label(self.player_frame, text="Points: 0")
        self.points_label.pack(padx=5, pady=5)
        
        # Frame centrale pour les commandes
        self.commands_frame = ttk.LabelFrame(self.control_frame, text="Actions")
        self.commands_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH)
        
        ttk.Button(self.commands_frame, text="Aide", command=self.show_help).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.commands_frame, text="Observer", command=self.look_around).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.commands_frame, text="Inventaire", command=self.show_inventory).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.commands_frame, text="Historique", command=self.show_history).pack(side=tk.LEFT, padx=2)
        
        # Frame droite pour les directions
        self.direction_frame = ttk.LabelFrame(self.control_frame, text="Directions")
        self.direction_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH)
        
        # Grille des directions
        directions = {
            'N': ('Nord', 0, 1), 'S': ('Sud', 2, 1),
            'E': ('Est', 1, 2), 'O': ('Ouest', 1, 0),
            'U': ('Haut', 0, 1), 'D': ('Bas', 2, 1)
        }
        
        for key, (name, row, col) in directions.items():
            ttk.Button(
                self.direction_frame,
                text=name,
                command=lambda d=key: self.move_direction(d)
            ).grid(row=row, column=col, padx=3, pady=3)
        
        # Frame pour la saisie de texte
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.input_entry = ttk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        ttk.Button(self.input_frame, text="Envoyer", command=self.process_input).pack(side=tk.RIGHT)
        
        # Démarrer le jeu
        self.start_game()
        
    def bind_keys(self):
        self.bind('<Return>', lambda e: self.process_input())
        
    def append_to_display(self, text):
        self.text_display.insert(tk.END, f"{text}\n")
        self.text_display.see(tk.END)
        
    def start_game(self):
        self.game.setup()
        self.append_to_display(f"Bienvenue dans la maison hantée!")
        self.append_to_display("Votre mission : explorez chaque pièce et résolvez les énigmes pour découvrir les secrets de la maison.")
        self.show_current_room()
        self.update_player_info()
        
    def move_direction(self, direction):
        result = self.game.player.move(direction)
        if result == "win":
            messagebox.showinfo("Félicitations!", "Vous avez gagné le jeu!")
            self.quit()
        elif result == "lose":
            messagebox.showinfo("Game Over", "Vous avez perdu!")
            self.quit()
        self.update_player_info()
        
    def show_current_room(self):
        room = self.game.player.current_room
        self.append_to_display(room.get_long_description())
        
    def update_player_info(self):
        player = self.game.player
        self.player_info.config(text=f"Joueur: {player.name}\nPièce: {player.current_room.name}")
        self.points_label.config(text=f"Points: {player.points}")
        
    def process_input(self):
        command = self.input_entry.get().strip()
        if command:
            self.append_to_display(f"\n> {command}")
            self.input_entry.delete(0, tk.END)
            
            command_parts = command.lower().split()
            if command_parts[0] in self.game.commands:
                result = self.game.commands[command_parts[0]].action(command_parts)
                if result == "quit":
                    self.quit()
            else:
                self.append_to_display("Commande non reconnue. Tapez 'help' pour voir les commandes disponibles.")
                
    def show_help(self):
        self.game.do_help([])
        
    def look_around(self):
        self.game.do_look([])
        
    def show_inventory(self):
        self.append_to_display(self.game.player.get_inventory())
        
    def show_history(self):
        self.game.player.print_history()

if __name__ == "__main__":
    game_gui = GameGUI()
    game_gui.mainloop()
