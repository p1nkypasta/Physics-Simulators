import pygame
import sys

# Initialize pygame
pygame.init()
pygame.font.init()

# Set up screen and constants
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Momentum of elastic collisions sim:")

# Set up the font
font = pygame.font.SysFont('Comic Sans MS', 20)


# Colors
WHITE = (255, 255, 255)
RED = (225, 0, 0)
CYAN = (100,120,225)

# Circle properties
circle_radius = 20
circleA_x = 2*WIDTH // 8
circleA_y = HEIGHT // 2
circleA_velocity_y = 0  # Initial downward velocity
circleA_velocity_x = 0 
massA = 5 #kg

circleB_x = WIDTH //2
circleB_y = HEIGHT // 2
circleB_velocity_x = 0
circleB_velocity_y = 0
massB = 2 #kg

initial_velocity = 0
fcoefficent = 0.15

# Create a text surface
Bmass = font.render(str(massB), True, (0, 0, 0))
Amass = font.render(str(massA), True, (0, 0, 0))
coefficient_of_friction= font.render(f'μ = {str(fcoefficent)}', True, (0, 0, 0))

# Gravity and bounce factor
gravity = 0.5
bounce_factor = -0.7

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input = pygame.key.get_pressed()
        if input[pygame.K_KP_ENTER]:
            initial_velocity = 3
            circleA_velocity_x = initial_velocity
            
    Ptot = round((massA*circleA_velocity_x) + (massB*circleB_velocity_x))
    initial_total_momentum = massA*initial_velocity
    momentum_loss = abs(Ptot - initial_total_momentum)

    A_p = massA*((circleA_velocity_x))
    B_p = massB*((circleB_velocity_x))
    A_velocity= font.render(f'Velocity A: {circleA_velocity_x:.1f} m/s', True, (0,0,0))
    B_velocity= font.render(f'Velocity B: {circleB_velocity_x:.1f} m/s', True, (0,0,0))
    A_momentum = font.render(f'Momentum A: {A_p:.1f} kgm/s', True, (0,0,0))
    B_momentum = font.render(f'Momentum B: {B_p:.1f} kgm/s', True, (0,0,0))
    Tot_momentumAB = font.render(f'Total Momentum of AB: {Ptot} kgm/s', True, (0,0,0))
    Tot_momentuminitial = font.render(f'Initial total momentum: {(initial_total_momentum)} kgm/s', True, (0,0,0))
    momentumlost = font.render(f'Momentum lost due to friction: {momentum_loss} kgm/s', True, (0,0,0))

    #movement
    circleA_x += circleA_velocity_x
    circleB_x += circleB_velocity_x


    acceleration = -1*(fcoefficent*9.8)

    #derived equation:
    #vB' = 2(mA)(mB)(vA)/((mB)**2) + (mA)(mB)

    if (circleA_x + circle_radius) >= (circleB_x - circle_radius):
        # circleB_velocity_x = (2*(massA)*(massB)*(circleA_velocity_x))/((massB**2)+ (massA)*(massB))
        # circleA_velocity_x = ((massA)*(circleA_velocity_x) - (massB)*(circleB_velocity_x))/massA
        circleB_velocity_x = (((2*massA)/(massA + massB))*(circleA_velocity_x))
        circleA_velocity_x = (((massA-massB)/(massA + massB))*(circleA_velocity_x))

    if fcoefficent > 0: 
        circleA_velocity_x += circleA_velocity_x/acceleration / 100
        circleB_velocity_x += circleB_velocity_x/acceleration / 100

  
    # Fill the background and draw the circle
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (circleA_x, int(circleA_y)), circle_radius)
    pygame.draw.circle(screen, CYAN, (circleB_x, circleB_y), circle_radius)
    screen.blit(Bmass, (circleB_x-5, circleB_y-15))
    screen.blit(Amass, (circleA_x-5, circleA_y-15))
    screen.blit(Tot_momentumAB, (20, 20))
    screen.blit(Tot_momentuminitial, (20, 45))
    screen.blit(A_momentum, (20, 70))
    screen.blit(B_momentum, (20, 95))
    screen.blit(A_velocity, (20, 120))
    screen.blit(B_velocity, (20, 145))
    screen.blit(coefficient_of_friction, (7*WIDTH//8, 20))
    screen.blit(momentumlost, (20, 170))

    # Update the display
    pygame.display.flip()
    
    clock.tick(60)  # Frame rate

#derived equation:
#vB' = 2(mA)(mB)(vA)/((mB)**2) + (mA)(mB)