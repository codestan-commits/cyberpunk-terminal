# Random Number Generator Screen
# Developed by: stancodes
# Date: 18/7/25

import tkinter as tk
import random
from tkinter import font as tkfont

class CyberpunkScreen:
    """
    A cyberpunk-style "hacking" screen with rapidly scrolling random numbers.
    Inspired by movie-style terminal interfaces (green text on black background).
    """
    
    def __init__(self, master):
        """
        Initialize the cyberpunk terminal screen.
        
        Args:
            master (tk.Tk): The root window for the application.
        """
        self.master = master
        master.title("CYBERPUNK TERMINAL")
        master.geometry("800x600")
        master.configure(bg="black")
        
        # Configure cyberpunk aesthetics
        self.text_color = "#00FF00"  # Classic green
        self.bg_color = "black"
        self.font_size = 12
        self.font = tkfont.Font(family="Courier", size=self.font_size)
        
        # Create a scrolling text widget (like a terminal)
        self.terminal = tk.Text(
            master,
            bg=self.bg_color,
            fg=self.text_color,
            insertbackground=self.text_color,
            font=self.font,
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=0
        )
        self.terminal.pack(expand=True, fill="both")
        
        # Start the random number stream
        self.running = False
        self.start_stream()
        
        # Close on Escape key
        master.bind("<Escape>", lambda e: master.destroy())
        
    def generate_random_line(self):
        """Generate a line of random numbers/symbols for the cyberpunk effect."""
        chars = "0123456789ABCDEF!@#$%^&*()_+-=[]{}|;:,.<>?"
        line_length = random.randint(40, 80)
        return ''.join(random.choice(chars) for _ in range(line_length))
    
    def update_terminal(self):
        """Continuously add random lines to simulate a hacking screen."""
        if not self.running:
            return
            
        # Insert a new random line
        self.terminal.insert(tk.END, self.generate_random_line() + "\n")
        
        # Auto-scroll and limit buffer size (for performance)
        self.terminal.see(tk.END)
        if int(self.terminal.index('end-1c').split('.')[0]) > 100:
            self.terminal.delete(1.0, 2.0)  # Delete oldest line
            
        # Schedule next update (random speed for a more dynamic feel)
        delay = random.randint(50, 200)
        self.master.after(delay, self.update_terminal)
    
    def start_stream(self):
        """Start the random number stream."""
        self.running = True
        self.update_terminal()
    
    def stop_stream(self):
        """Stop the random number stream."""
        self.running = False

def main():
    """Run the cyberpunk terminal."""
    root = tk.Tk()
    app = CyberpunkScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
