# Pruebas del Sistema de Gestión de Cafetería 
# Autor: Diego García de los Salmones Ajuria | A01736106

# coding=utf-8

import unittest

from bebidas import addBebida

class TestSum(unittest.TestCase):
    
    # Si el output es True: La información de la bebida es VÁLIDA
    # Si el output es False: La información de la bebida es INVÁLIDA
    
    # Test Case 1: El nombre de la bebida solo contiene letras (VÁLIDO)
    def test1_1(self):
        self.assertEqual(addBebida("Café,10"),True)
    def test1_2(self):
        self.assertEqual(addBebida("Espresso,10"),True)
    
    # Test Case 2: El nombre de la bebida contiene letras y otros símbolos (INVÁLIDO)
    def test2(self):
        self.assertEqual(addBebida("E5press0,2,8"),False)
    
    # Test Case 3: El nombre de la bebida no contiene letras (INVÁLIDO)
    def test3(self):
        self.assertEqual(addBebida("73,1"),False)
    
    # Test Case 4: No hay nombre de la bebida (INVÁLIDO)
    def test4(self):
        self.assertEqual(addBebida(",1,2,4,8,16"),False)
    
    # Test Case 5: El nombre de la bebida tiene menos de 2 caracteres de longitud (INVÁLIDO)
    def test5(self):
        self.assertEqual(addBebida("T,1,2,4,8,16"),False)
    
    # Test Case 6: El nombre de la bebida tiene entre 2 y 15 caracteres de longitud (VÁLIDO)
    def test6_1(self):
        self.assertEqual(addBebida("Té,1,2,4,8,16"),True)
    def test6_2(self):
        self.assertEqual(addBebida("Cappuccino,1,2,4,8,16"),True)
    def test6_3(self):
        self.assertEqual(addBebida("Café con Lechee,1,2,4,8,16"),True)
    
    # Test Case 7: El nombre de la bebida tiene más de 15 caracteres de longitud (INVÁLIDO)
    def test7_1(self):
        self.assertEqual(addBebida("Café con Lecheee,1,2,4,8,16"),False)
    def test7_2(self):
        self.assertEqual(addBebida("Agua de Jamaica que parece de Limón pero sabe a Tamarindo,1,2,4,8,16"),False)
    
    # Test Case 8: Hay valores de tamaños que están debajo del rango (1-48) (INVÁLIDO)
    def test8_1(self):
        self.assertEqual(addBebida("Café Americano,-1"),False)
    def test8_2(self):
        self.assertEqual(addBebida("Café Americano,0,10,20"),False)
        
    # Test Case 9: Todos los valores de tamaños están dentro del rango (1-48) (VÁLIDO)
    def test9_1(self):
        self.assertEqual(addBebida("Café Americano,1"),True)
    def test9_2(self):
        self.assertEqual(addBebida("Café Americano,48"),True)
    def test9_3(self):
        self.assertEqual(addBebida("Café Americano,1,2,4,8"),True)
    def test9_4(self):
        self.assertEqual(addBebida("Café Americano,8,16,24,48"),True)
    def test9_5(self):
        self.assertEqual(addBebida("Café Americano,1,12,24,36,48"),True)
        
    # Test Case 10: Hay valores de tamaños que están arriba del rango (1-48) (INVÁLIDO)
    def test10_1(self):
        self.assertEqual(addBebida("Café Americano,49"),False)
    def test10_2(self):
        self.assertEqual(addBebida("Café Americano,80"),False)
    def test10_3(self):
        self.assertEqual(addBebida("Café Americano,8,16,24,49"),False)
    def test10_4(self):
        self.assertEqual(addBebida("Café Americano,55,62,77,81"),False)
        
    # Test Case 11: Hay valores de tamaños que están abajo y arriba del rango (1-48) (INVÁLIDO)
    def test11(self):
        self.assertEqual(addBebida("Café Americano,0,1,48,49,88"),False)
        
    # Test Case 12: Todos los valores de tamaños son números enteros (VÁLIDO)
    def test12_1(self):
        self.assertEqual(addBebida("Latte,2"),True)
    def test12_2(self):
        self.assertEqual(addBebida("Latte,1,2,8"),True)
        
    # Test Case 13: Hay valores de tamaños que no son números enteros (INVÁLIDO)
    def test13_1(self):
        self.assertEqual(addBebida("Latte, 2.5"),False)
    def test13_2(self):
        self.assertEqual(addBebida("Latte, 1, 2, 4, 5.5"),False)
    def test13_3(self):
        self.assertEqual(addBebida("Latte, 1.1, 2.9, 4.33, 5.5"),False)
        
    # Test Case 14: Los valores de tamaños están en orden ascendente (VÁLIDO)
    def test14_1(self):
        self.assertEqual(addBebida("Té chai latte, 1,48"),True)
    def test14_2(self):
        self.assertEqual(addBebida("Té chai latte, 8,16,32"),True)
    def test14_3(self):
        self.assertEqual(addBebida("Té chai latte, 1,2,4,8"),True)
    def test14_4(self):
        self.assertEqual(addBebida("Té chai latte, 9,14,23,39,48"),True)
    
    # Test Case 15: Los valores de tamaños no están en orden ascendente (INVÁLIDO)
    def test15_1(self):
        self.assertEqual(addBebida("Té chai latte, 48,1"),False)
    def test15_2(self):
        self.assertEqual(addBebida("Té chai latte, 16,8,4,2,1"),False)
    def test15_3(self):
        self.assertEqual(addBebida("Té chai latte, 1,8,32,16"),False)
    def test15_4(self):
        self.assertEqual(addBebida("Té chai latte, 22,15,44,28"),False)
        
    # Test Case 16: No se ingresan valores de tamaños (INVÁLIDO)
    def test16_1(self):
        self.assertEqual(addBebida("Frappé"),False)
    def test16_2(self):
        self.assertEqual(addBebida("Frappé,"),False)
        
    # Test Case 17: Se ingresan de uno a cinco valores de tamaño (VÁLIDO)
    def test17_1(self):
        self.assertEqual(addBebida("Frappé,18"),True)
    def test17_2(self):
        self.assertEqual(addBebida("Frappé,16,32"),True)
    def test17_3(self):
        self.assertEqual(addBebida("Frappé,12,24,48"),True)
    def test17_4(self):
        self.assertEqual(addBebida("Frappé,4,8,16,32"),True)
    def test17_5(self):
        self.assertEqual(addBebida("Frappé,1,8,16,32,40"),True)
        
    # Test Case 18: Se ingresan más de 5 valores de tamaño (INVÁLIDO)
    def test18_1(self):
        self.assertEqual(addBebida("Frappé,1,2,4,8,16,32"),False)
    def test18_2(self):
        self.assertEqual(addBebida("Frappé,1,2,4,8,16,32,40"),False)
    def test18_3(self):
        self.assertEqual(addBebida("Frappé,1,2,4,8,16,32,40,48"),False)
        
    # Test Case 19: El nombre del artículo es el primero en la entrada (VÁLIDO)
    def test19_1(self):
        self.assertEqual(addBebida("Macchiato,21"),True)
    def test19_2(self):
        self.assertEqual(addBebida("Macchiato,21,22,28,29"),True)
        
    # Test Case 20: El nombre del artículo no es el primero en la entrada (INVÁLIDO)
    def test20_1(self):
        self.assertEqual(addBebida("21,Macchiato"),False)
    def test20_2(self):
        self.assertEqual(addBebida("22,Macchiato,29"),False)
    def test20_3(self):
        self.assertEqual(addBebida("21,22,28,29,Macchiato"),False)
        
    # Test Case 21: Una sola coma separa cada entrada en la lista (VÁLIDO)
    def test21_1(self):
        self.assertEqual(addBebida("Café,10"),True)
    def test21_2(self):
        self.assertEqual(addBebida("Frappé,16,32"),True)
    def test21_3(self):
        self.assertEqual(addBebida("Té chai latte, 8,16,32"),True)
    
    # Test Case 22: Más de una coma separa cada entrada en la lista (INVÁLIDO)
    def test22(self):
        self.assertEqual(addBebida("Café,,10,,,20,,30,,,40"),False)
    
    # Test Case 23: La entrada no contiene espacios en blanco (VÁLIDO)
    def test23(self):
        self.assertEqual(addBebida("Té,1,2,4,8,16"),True)
    
    # Test Case 24: La entrada contiene espacios en blanco (VÁLIDO)
    def test24_1(self):
        self.assertEqual(addBebida("Té, 1, 2, 4, 8, 16"),True)
    def test24_2(self):
        self.assertEqual(addBebida("Té ,1,2,4,8,16"),True)
    def test24_3(self):
        self.assertEqual(addBebida("Té , 1, 2, 4, 8, 16"),True)
    def test24_4(self):
        self.assertEqual(addBebida(" Té , 1 , 2 , 4 , 8 , 16 "),True)
    def test24_5(self):
        self.assertEqual(addBebida("Té         ,1,2,4,8,16     "),True)
    def test24_6(self):
        self.assertEqual(addBebida("     Té   ,  1  ,    2   , 4  , 8 ,     16 "),True)
        
if __name__=='__main__':
    unittest.main()
 