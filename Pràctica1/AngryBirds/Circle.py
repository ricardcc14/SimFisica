import pygame
import Box2D as b2
import utils

class Circle:
    def __init__(self, world:b2.b2World, x:float, y:float, radius:float, images:list[pygame.Surface]):
        self.radius = radius
        self.images = images

        self.isRemoved = False

        #Preprocessat de les textures
        for img in images:
            texture = pygame.image.load(img) if isinstance(img, str) else img
            texture_size = int(radius * 2)
            texture = pygame.transform.scale(texture, (texture_size, texture_size))
            
            # Crear mascara circular
            mask = pygame.Surface((texture_size, texture_size), pygame.SRCALPHA)
            pygame.draw.circle(mask, (255, 255, 255, 255), 
                            (texture_size//2, texture_size//2), int(radius))
            
            # Aplicar mascara
            texture = texture.convert_alpha()
            texture.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.images.append(texture)
    
        self.currentStatus = 0 #0 is alive, 1 is collided 2 is toDestroy
        


        bodydf = b2.b2BodyDef()
        bodydf.position = utils.pixelToWorld(x, y)
        bodydf.type = b2.b2_dynamicBody
        bodydf.userData = self
        self.body:b2.b2Body = world.CreateBody(bodydf)

        circleshape = b2.b2CircleShape(radius=utils.pixelToWorld(radius))
        fd = b2.b2FixtureDef()
        fd.shape=circleshape
        fd.density = 1
        fd.restitution = 0
        fd.friction = 1
        self.body.CreateFixture(fd)
        pass

    def draw(self, screen:pygame.Surface):
        position:b2.b2Vec2 = utils.worldToPixel(self.body.position.copy())
        position.y = screen.get_height()-position.y


        #pygame.draw.circle(screen, 'lightgray', position, self.radius)
        #pygame.draw.circle(screen, 'black', position, self.radius, 1)
        current_texture = self.images[self.currentStatus]
    
        if current_texture.get_size() != (self.w, self.h):
            current_texture = pygame.transform.scale(current_texture, (int(self.w), int(self.h)))
            
        screen.blit(current_texture, (position.x - self.w/2, position.y - self.h/2))
        pass

    def update(self):
        pass

    def destroy(self, world:b2.b2World):
        world.DestroyBody(self.body)
        self.isRemoved = True