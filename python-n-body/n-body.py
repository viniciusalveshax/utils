# Baseado em https://www.pygame.org/docs/

# Example file showing a circle moving on screen
import pygame

class Body:
	def __init__(self, name, x, mass, color):
		self.name = name
		self.x = x
		self.mass = mass
		self.v = 0
		self.color = color
		
	def calculate_f(self, other_body):
		G = 10
		#print(G, self.mass, other_body.get_mass())
		#print(self.name, self.x)
		num = (G * self.mass * other_body.get_mass())
		den = ((self.x - other_body.get_x()) * (self.x - other_body.get_x()))
		if abs(den) > 1:
			force = num / den
		else:
			# Simula que os planetas pararam de se atrair
			force = 0
		if abs(force) > 50:
			force = 0

		if other_body.get_x() < self.x:
			force = force * (-1)	
		
		return force

	
	def change(self, force):
		if abs(force) < 1:
			acel = 0
			new_v = 0
		else:
			acel = force / self.mass
			new_v = self.v + acel
		new_x = self.x + new_v + (acel/2)
		self.x = new_x
		self.v = new_v
		print(self.name, ", X: ", self.x, ", acel: ", acel, ", força: ", force)
		
	def draw(self):
		pos = pygame.Vector2(10 * self.x, screen.get_height() / 2)
		pygame.draw.circle(screen, self.color, pos, self.mass)
		
	def get_x(self):
		return self.x
		
	def get_mass(self):
		return self.mass
		
	def get_name(self):
		return self.name


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

b1 = Body("Marte", 10, 10, "red")
b2 = Body("Sol", 40, 40, "yellow")
b3 = Body("Terra", 100, 15, "blue")

paused = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #pygame.draw.circle(screen, "white", player_pos, 20)
    b1.draw()
    b3.draw()
    b2.draw()

    
    if paused == False:
        f_2_1 = b1.calculate_f(b2)
        f_3_1 = b1.calculate_f(b3)
        b1.change(f_2_1+f_3_1)
        
        f_1_2 = b2.calculate_f(b1)
        f_3_2 = b2.calculate_f(b3)
        b2.change(f_1_2+f_3_2)

        f_2_3 = b3.calculate_f(b2)
        f_1_3 = b3.calculate_f(b1)
        b3.change(f_1_3+f_2_3)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_p]:
        if paused:
        	paused = False
        else:
        	paused = True
    
    print(paused)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(10) / 1000

pygame.quit()
