import pygame
import numpy as np

class Ball:
    def __init__ (self, radius, mass, pos_initial, color):
        self.radius = radius
        self.mass = mass
        self.color = color
        self.pos = np.array(pos_initial)
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))

        self.volume = 4/3 * np.pi * self.radius**3

    def set_new_position(self, new_position_y):
        self.pos[0] = self.pos[0]
        self.pos[1] = new_position_y; 
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))
    
    def detect_click(self, x, y):
        dist_x2 = (self.pos[0] - x) ** 2
        dist_y2 = (self.pos[1] - y) ** 2

        if (np.sqrt(dist_x2 + dist_y2) <= self.radius):
            return True
        else: 
            return False

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)
        
    def apply_gravity_force(self, gravity):     
        self.apply_force(self.mass * gravity)

    def apply_flotation_force(self, liquid, gravity, screen):
        #Altura submergida
        h = (self.pos[1] + self.radius) - (screen.get_height() - liquid.height)
        h = min(self.radius * 2, h)
        #Volum submergit
        Vs = np.pi * h**2 * (self.radius - h / 3)
        #Força de flotació
        B = (liquid.density * gravity * Vs)
        self.apply_force(-B)

    def update(self, dt, screen):
        #MOVIMENT LINEAL
        self.vel = self.vel + self.acc * dt
        self.pos = self.pos + self.vel * dt 
        self.acc = np.array([0, 0])
    
    def draw(self, screen):
        # Draw de la pilota
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def get_kinetic_energy(self): 
        energy = np.array([0, 0])
        energy = 0.5 * self.mass * np.pow(self.vel,2)
        return energy   

    def get_potential_energy(self, screen:pygame.Surface):
        energy = np.array([0, 0])
        energy = self.mass * self.gravity * (screen.get_height() - self.pos)
        return energy
        
    def collision_ball(self, other_ball):

        #Trobar els vectors unitaris de l'eix de xoc
        u = np.array(other_ball.pos - self.pos) / np.linalg.norm(other_ball.pos - self.pos)
        w = np.array([-u[1], u[0]])

        #Distància de seguretat
        if (np.abs(np.linalg.norm(other_ball.pos - self.pos)) <= (self.radius + other_ball.radius)):
            self.pos = self.pos + 1.1*(-u * ((self.radius + other_ball.radius) - np.linalg.norm(other_ball.pos - self.pos)))

        #Calcular velocitats finals amb nova base
        x_1 = ((self.mass - other_ball.mass) / (self.mass + other_ball.mass)) * self.vel + ((2 * other_ball.mass)/(self.mass + other_ball.mass)) * other_ball.vel
        x_2 =  ((2 * self.mass) / (self.mass + other_ball.mass)) * self.vel + ((other_ball.mass - self.mass) / (self.mass + other_ball.mass)) * other_ball.vel
        
        self.vel = x_1 * u +  self.vel * w
        other_ball.vel = x_2 * u + other_ball.vel * w


    def apply_ballistic(self, bullet_mass, bullet_vel):
        #Canvi en la velocitat lineal a causa de l'impacte
        self.vel = (bullet_mass * bullet_vel) / (self.mass + bullet_mass)
        self.angular_vel = self.vel / self.radius_rotation
        #Els dos objectes passen a ser un, ja que la bala queda enganxada
        self.mass = self.mass + bullet_mass

    def checkScreenEdges(self, screen:pygame.Surface):
        #Bottom edge
        if (self.pos[1] > screen.get_height() - self.radius):
            self.vel[1] = -self.vel[1]
            self.pos[1] = screen.get_height() - self.radius

        #Top edge
        if (self.pos[1] < 0 + self.radius):
            self.vel[1] = -self.vel[1]
            self.pos[1] = self.radius

        #Left edge
        if (self.pos[0] < 0 + self.radius):
            self.vel[0] = -self.vel[0]
            self.pos[0] = self.radius

        #Right edge
        if (self.pos[0] > screen.get_width() - self.radius):
            self.vel[0] = -self.vel[0]
            self.pos[0] = screen.get_width() - self.radius

    def apply_normal_and_friction_force(self, inclination, coef):
        N = -(self.gravity[1] * self.mass * np.cos(inclination))
        self.apply_force([-coef * N * -self.vel[0], -coef * N * -self.vel[1]])
        pass
    
