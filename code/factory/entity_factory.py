from re import match
from Player import Player
from Enemy import Enemy

from code.const import WIN_WIDTH
from code.entities.background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_Bg=[]
                for i in range(7):
                    list_Bg.append(Background(f'Level1Bg{i}',position(0,0)))
                    list_Bg.append(Background(f'Level1Bg{i}', position(WIN_WIDTH, 0)))
                return list_Bg